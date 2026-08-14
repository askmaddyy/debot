#!/usr/bin/env python3
"""debot lint — deterministic detector for AI-writing tells.

Usage:
    python3 lint.py FILE [FILE...]
    python3 lint.py --json FILE
    cat text.txt | python3 lint.py -

Exit codes: 0 = below --max-score (default 3.0, matching the "clean" verdict
cutoff), 1 = at or above it, 2 = usage error.
No dependencies. Python 3.8+.
"""

import argparse
import json
import math
import re
import sys
import unicodedata

# ---------------------------------------------------------------- word lists

STOCK_VOCAB = [
    "delve", "delves", "delving", "tapestry", "testament", "landscape",
    "robust", "seamless", "seamlessly", "pivotal", "crucial", "foster",
    "fostering", "underscore", "underscores", "leverage", "leveraging",
    "realm", "vibrant", "boast", "boasts", "embark", "embarking",
    "multifaceted", "holistic", "streamline", "streamlining", "elevate",
    "empower", "empowering", "harness", "harnessing", "unlock", "unlocking",
    "supercharge", "transformative", "revolutionize", "groundbreaking",
    "cutting-edge", "game-changer", "game-changing", "ever-evolving",
    "fast-paced", "meticulously", "intricate", "myriad", "plethora",
    "synergy", "paradigm", "beacon", "unwavering", "unparalleled",
]

STOCK_PHRASES = [
    r"in today'?s [\w-]+ (?:world|era|environment|landscape|age)",
    r"it(?:'s| is) (?:important|worth) (?:to note|noting)",
    r"navigate the (?:complexities|challenges|landscape)",
    r"plays? a (?:crucial|vital|key|pivotal) role",
    r"at its core",
    r"in the realm of",
    r"a testament to",
    r"when it comes to",
    r"look no further",
    r"the world of",
    r"whether you(?:'re| are) a [\w\s]{1,30} or a",
    r"take (?:your|the) [\w\s]{1,20} to the next level",
    r"stand(?:s)? the test of time",
    r"rich (?:history|tapestry|heritage)",
    r"treasure trove",
    r"dive (?:deep|deeper) into",
    r"a deep dive",
    r"shed(?:s|ding)? light on",
    r"food for thought",
    r"double-edged sword",
]

COPULA_DODGES = [
    r"serves? as",
    r"functions? as",
    r"acts? as a",
    r"stands? as",
    r"represents? a (?:significant|major|key|crucial|fundamental)",
]

SIGNIFICANCE = [
    r"marks? a (?:pivotal|significant|major|new|crucial)",
    r"pivotal (?:moment|step|role|point)",
    r"(?:major|significant|important) milestone",
    r"highlights? the (?:importance|significance|need)",
    r"underscores? the",
    r"broader (?:journey|effort|trend|shift) toward",
    r"paves? the way",
    r"ushers? in",
]

TRANSITION_CRUTCHES = ["moreover", "furthermore", "additionally",
                       "consequently", "in addition,"]

PHILOSOPHICAL_OPENERS = [
    r"since the dawn of",
    r"in an increasingly [\w-]+ world",
    r"in an era (?:of|where|defined)",
    r"throughout (?:human )?history",
    r"few (?:things|topics|questions) (?:are|have been) (?:as|more)",
]

LISTICLE = [
    r"(?:a few |some |\d+ )?(?:things|lessons) i(?:'ve)? learned",
    r"here(?:'s| are) what i learned",
    r"key takeaways",
]

SIGNPOSTING = [
    r"let'?s (?:dive|delve|jump|dig) (?:in|into)",
    r"let'?s (?:explore|unpack|break (?:it|this) down)",
    r"in this (?:post|article|guide|blog|section|essay), (?:we|i|you)",
    r"without further ado",
    r"now that we'?ve (?:covered|discussed|explored)",
    r"buckle up",
    r"read on to",
    r"stay tuned",
    r"in the (?:following|next) sections?",
]

CHATBOT = [
    r"great question",
    r"i hope this (?:helps|email finds you well|message finds you well)",
    r"^certainly[,!]",
    r"^absolutely[,!]",
    r"feel free to (?:reach out|ask|contact)",
    r"(?:don'?t|do not) hesitate to",
    r"i(?:'m| am) (?:just )?an ai",
    r"as an ai(?: language model)?",
    r"as of my (?:last |knowledge )?(?:update|cutoff)",
    r"i wanted to (?:reach out|touch base|follow up)",
    r"happy to (?:help|assist) (?:further|with anything else)",
    r"is there anything else",
]

CONCLUSION_BOILERPLATE = [
    r"^in conclusion",
    r"^in summary",
    r"^to sum(?:marize| up)",
    r"^overall,",
    r"^ultimately,",
    r"^all in all",
    r"the future of [\w\s]{1,30} (?:is|looks|remains)",
    r"only time will tell",
    r"exciting (?:times|future) (?:lie|lies|ahead)",
]

HEDGES = [
    "arguably", "typically", "generally", "essentially", "potentially",
    "presumably", "seemingly", "relatively", "somewhat", "fairly",
    "in many cases", "in some cases", "more often than not",
    "importantly", "notably", "interestingly", "significantly",
]

WORDY_IDIOMS = [
    (r"in order to", "to"),
    (r"due to the fact that", "because"),
    (r"despite the fact that", "although"),
    (r"has the ability to", "can"),
    (r"have the ability to", "can"),
    (r"a wide (?:variety|range|array) of", "many"),
    (r"a (?:significant|substantial) (?:number|amount) of", "many/much"),
    (r"at this point in time", "now"),
    (r"in the event that", "if"),
    (r"prior to", "before"),
    (r"subsequent to", "after"),
    (r"utilize", "use"),
    (r"in close proximity to", "near"),
    (r"first and foremost", "first"),
]

NEGATIVE_PARALLELISM = [
    r"\bnot (?:just|only|merely|simply) [^.!?\n]{2,80}[,;—–-] ?(?:but|it)",
    r"\bisn'?t (?:just|only|merely|simply|about)\b",
    r"it'?s not (?:about )?[^.!?\n]{2,60}[.;—–-] ?it'?s",
    r"\bnot because [^.!?\n]{2,60}[,;] ?but because",
    r"this is(?:n'?t| not) [^.!?\n]{2,60}[.;] ?(?:this|it) is",
]

# ------------------------------------------------------------------ helpers

SEVERITY_WEIGHT = {"high": 3, "medium": 2, "low": 1}


def strip_nonprose(text):
    """Blank out code fences, inline code, and URLs so they don't trigger flags.

    Replaces with spaces/newlines of equal shape so line numbers stay valid.
    """
    def blank(match):
        return "".join("\n" if c == "\n" else " " for c in match.group(0))

    text = re.sub(r"```.*?(?:```|\Z)", blank, text, flags=re.S)
    text = re.sub(r"`[^`\n]+`", blank, text)
    text = re.sub(r"https?://\S+", blank, text)
    return text


def word_count(text):
    return max(1, len(re.findall(r"[A-Za-z0-9'-]+", text)))


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def sentences(text):
    """Rough sentence split over prose (headings, list markers, and
    blockquoted lines dropped — same definition of "prose" the broetry
    check below uses, so the two checks don't disagree on what counts)."""
    prose = re.sub(r"^\s*(?:#{1,6} .*|[-*•] .*|\d+\. .*|>.*)$", "", text,
                   flags=re.M)
    parts = re.split(r"(?<=[.!?])\s+", prose)
    return [p for p in (s.strip() for s in parts) if len(p.split()) >= 3]


def is_emoji(ch):
    if ch in "✅❌➡✨⭐❗❤":
        return True
    cp = ord(ch)
    return (0x1F300 <= cp <= 0x1FAFF) or (0x1F000 <= cp <= 0x1F2FF) or \
        (0x2600 <= cp <= 0x27BF and unicodedata.category(ch) == "So")


# ------------------------------------------------------------------ checks

def run_checks(raw):
    text = strip_nonprose(raw)
    words = word_count(text)
    per_k = 1000.0 / words
    flags = []  # dicts: check, severity, line, excerpt, note

    def find_all(pattern):
        return [(m.start(), m.group(0)) for m in
                re.finditer(pattern, text, flags=re.I | re.M)]

    def add(check, severity, pos, excerpt, note=""):
        flags.append({
            "check": check, "severity": severity,
            "line": line_of(text, pos) if pos is not None else None,
            "excerpt": excerpt.strip()[:80] if excerpt else "",
            "note": note,
        })

    # 1. stock vocabulary — only flag words that cluster (2+ hits in the
    # same paragraph). A single instance anywhere, even a real technical
    # term like "test harness", is normal usage per this skill's own
    # "one is fine, a cluster is the signature" rule.
    para_spans, last = [], 0
    for m in re.finditer(r"\n\s*\n", text):
        para_spans.append((last, m.start()))
        last = m.end()
    para_spans.append((last, len(text)))

    for start, end in para_spans:
        para = text[start:end]
        para_hits = [(start + m.start(), m.group(0)) for w in STOCK_VOCAB
                     for m in re.finditer(r"\b" + re.escape(w) + r"\b",
                                          para, re.I)]
        if len(para_hits) >= 2:
            for pos, hit in para_hits:
                add("stock-vocab", "medium", pos, hit,
                    "word models overuse; fine once, a tell in clusters")

    # 2. stock phrases / significance / signposting / chatbot / conclusions
    for patterns, check, sev in [
        (STOCK_PHRASES, "stock-phrase", "high"),
        (COPULA_DODGES, "copula-dodge", "low"),
        (SIGNIFICANCE, "significance-inflation", "high"),
        (SIGNPOSTING, "signposting", "high"),
        (CHATBOT, "chatbot-residue", "high"),
        (CONCLUSION_BOILERPLATE, "boilerplate-conclusion", "medium"),
        (NEGATIVE_PARALLELISM, "negative-parallelism", "high"),
        (PHILOSOPHICAL_OPENERS, "philosophical-opener", "high"),
        (LISTICLE, "lessons-listicle", "medium"),
    ]:
        for pat in patterns:
            for pos, hit in find_all(pat):
                add(check, sev, pos, hit)

    # 3. hedging density
    hedge_hits = []
    for h in HEDGES:
        hedge_hits += [(m.start(), m.group(0)) for m in
                       re.finditer(r"\b" + re.escape(h) + r"\b", text, re.I)]
    if len(hedge_hits) * per_k > 8:
        for pos, hit in hedge_hits:
            add("hedging", "low", pos, hit,
                f"{len(hedge_hits)} hedges in {words} words")

    # 4. wordy idioms
    for pat, fix in WORDY_IDIOMS:
        for pos, hit in find_all(r"\b" + pat + r"\b"):
            add("wordy-idiom", "low", pos, hit, f"try: {fix}")

    # 5. em dash density
    dashes = [(m.start(), "—") for m in re.finditer("—|--", text)]
    if len(dashes) * per_k > 4 and len(dashes) >= 3:
        for pos, hit in dashes:
            add("em-dash-density", "medium", pos, hit,
                f"{len(dashes)} dashes / {words} words (human rate is far lower)")

    # 6. rule of three (adjective/noun triads)
    triads = find_all(r"\b[\w-]+, [\w-]+,? (?:and|or) [\w-]+\b")
    if len(triads) * per_k > 5 and len(triads) >= 3:
        for pos, hit in triads:
            add("rule-of-three", "low", pos, hit,
                "triad density high; keep the strongest item")

    # 7. bold-header bullets
    bold_bullets = find_all(r"^[ \t]*[-*•][ \t]*\*\*[^*\n]+\*\*[:.]?")
    if len(bold_bullets) >= 3:
        for pos, hit in bold_bullets:
            add("bold-bullet-list", "medium", pos, hit,
                "'**Term:** text' list; convert to prose or drop bold")

    # 8. title-case headings
    for pos, hit in find_all(r"^#{1,6} .+$"):
        content_words = [w for w in re.findall(r"[A-Za-z][\w'-]*", hit)
                         if len(w) > 3]
        if len(content_words) >= 3 and \
                all(w[0].isupper() for w in content_words):
            add("title-case-heading", "low", pos, hit, "use sentence case")

    # 9. emoji
    for i, ch in enumerate(text):
        if is_emoji(ch):
            add("emoji", "medium", i, ch)

    # 9b. transition-crutch density
    trans_hits = []
    for t in TRANSITION_CRUTCHES:
        trans_hits += [(m.start(), m.group(0)) for m in
                       re.finditer(r"\b" + re.escape(t), text, re.I)]
    if len(trans_hits) >= 3 and len(trans_hits) * per_k > 4:
        for pos, hit in trans_hits:
            add("transition-crutch", "medium", pos, hit,
                f"{len(trans_hits)} stitching transitions; just start the "
                "next sentence")

    # 9c. hashtag blocks (#Tag with no space after #, 2+ on one line)
    for pos, hit in find_all(r"^(?:\s*#[A-Za-z]\w+){2,}\s*$"):
        add("hashtag-block", "high", pos, hit)

    # 9d. broetry: many one-sentence dramatic paragraphs
    # A label intro to a code block/list ("With the CLI:") or a short
    # sign-off ("MIT.") is doc structure, not the AI one-line-punch tic —
    # only flag paragraphs that read as a standalone dramatic beat.
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    prose_paras = [p for p in paras
                   if not re.match(r"^(#{1,6} |[-*•] |\d+\. |>)", p)]
    short_paras = [p for p in prose_paras
                   if len(p.split()) <= 10 and "\n" not in p
                   and not p.endswith(":")
                   and not re.match(r"^\*\*[^*]+\*\*[:.]?$", p)
                   and len(p.split()) >= 3]
    if len(short_paras) >= 4 and len(short_paras) > 0.3 * max(1, len(prose_paras)):
        for p in short_paras[:8]:
            add("broetry", "medium", text.find(p), p,
                f"{len(short_paras)}/{len(prose_paras)} paragraphs are "
                "one-line punches; merge into real paragraphs")

    # 9e. low concreteness: long prose with zero digits reads generated
    if words >= 250 and not re.search(r"\d", text):
        add("low-concreteness", "medium", None, "",
            f"{words} words with no number, date, or quantity anywhere; "
            "human essays almost always anchor on at least one concrete — "
            "review for both-sides mush and missing specifics")

    # 9f. phrase echo: the same content trigram recycled as a scaffold
    toks = re.findall(r"[a-z']+", text.lower())
    tri_count = {}
    for i in range(len(toks) - 2):
        tri = " ".join(toks[i:i + 3])
        tri_count[tri] = tri_count.get(tri, 0) + 1
    for tri, n in tri_count.items():
        if n >= 4 and words < 3000:
            m = re.search(re.escape(tri.split()[0]) + r"\W+" +
                          re.escape(tri.split()[1]) + r"\W+" +
                          re.escape(tri.split()[2]), text, re.I)
            add("phrase-echo", "low", m.start() if m else None, tri,
                f"same 3-word scaffold used {n}x; vary the structure")

    # 10. sentence rhythm uniformity
    lens = [len(s.split()) for s in sentences(text)]
    if len(lens) >= 8:
        mean = sum(lens) / len(lens)
        sd = math.sqrt(sum((x - mean) ** 2 for x in lens) / len(lens))
        if sd < 6.0:
            add("uniform-rhythm", "medium", None, "",
                f"sentence-length stddev {sd:.1f} over {len(lens)} sentences "
                "(<6 reads metronomic; vary lengths)")

    return flags, words


def score(flags, words):
    pts = sum(SEVERITY_WEIGHT[f["severity"]] for f in flags)
    return pts * 1000.0 / words


def verdict(s):
    if s < 3:
        return "clean — reads human"
    if s < 10:
        return "lightly seasoned — a careful reader would wonder"
    if s < 25:
        return "flagged — recognizably AI-flavored"
    return "heavy bot — unmistakably machine-written"


# -------------------------------------------------------------------- main

def report(name, flags, words, as_json, max_score):
    s = score(flags, words)
    if as_json:
        print(json.dumps({
            "file": name, "words": words, "score": round(s, 1),
            "verdict": verdict(s), "flag_count": len(flags), "flags": flags,
        }, indent=2))
    else:
        print(f"\n{name}: {len(flags)} flag(s), {words} words, "
              f"score {s:.1f}/1000w — {verdict(s)}")
        by_check = {}
        for f in flags:
            by_check.setdefault(f["check"], []).append(f)
        for check, items in sorted(by_check.items(),
                                   key=lambda kv: -len(kv[1])):
            print(f"  {check} ×{len(items)}")
            for f in items[:6]:
                loc = f"L{f['line']}" if f["line"] else "--"
                note = f"  ({f['note']})" if f["note"] else ""
                excerpt = f" \"{f['excerpt']}\"" if f["excerpt"] else ""
                print(f"    {loc:>5}{excerpt}{note}")
            if len(items) > 6:
                print(f"    ... and {len(items) - 6} more")
    return s < max_score


def main():
    ap = argparse.ArgumentParser(description="Detect AI-writing tells.")
    ap.add_argument("files", nargs="+", help="files to lint, or - for stdin")
    ap.add_argument("--json", action="store_true", dest="as_json")
    ap.add_argument("--max-score", type=float, default=3.0,
                    help="exit 0 if score is below this (default 3)")
    args = ap.parse_args()

    ok = True
    for path in args.files:
        try:
            raw = sys.stdin.read() if path == "-" else \
                open(path, encoding="utf-8", errors="replace").read()
        except OSError as e:
            print(f"error: {e}", file=sys.stderr)
            return 2
        flags, words = run_checks(raw)
        if not report(path, flags, words, args.as_json, args.max_score):
            ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
