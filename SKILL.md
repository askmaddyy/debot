---
name: debot
description: Rewrite AI-generated or AI-flavored text so it reads like a person wrote it — remove AI tells (inflated significance, stock vocabulary, em-dash overuse, rule-of-three, hedging, bold-header lists, chatbot boilerplate) and restore natural rhythm and a real voice. Use when the user asks to humanize, de-AI, "make it sound natural", "make it sound like me", fix text that "sounds like ChatGPT/Claude", polish an AI draft, or check text for AI tells. Also apply its principles when the user asks you to draft prose for an audience (email, post, docs, essay, marketing copy) where sounding machine-written would hurt them.
---

# debot

Make writing sound like a person wrote it. Two jobs, in order: remove the tells, then restore the voice. Doing only the first produces clean but dead prose; both halves matter.

There's a third failure mode past both, and it's the one that's easiest to miss because it feels like progress: over-applying the voice moves produces text with its own tells — forced casualness, manufactured imperfection, a reaction bolted onto every fact. That doesn't read as a person. It reads as an AI that has learned what "sounding human" is supposed to look like, which is a different and in some ways more obvious problem than sounding like AI in the first place. The target is the narrow lane between mechanical and performed.

This file is self-contained. Everything needed is below — apply it with nothing but this text. If your harness can run shell commands or read files, the **Boosters** section at the end strengthens verification, but never skip the work because a booster is unavailable.

## Process

1. **Scan** the text against every item in the tell checklist, item by item — not by general impression. Models are bad at noticing their own tells. Note specific phrases on specific lines.
2. **Rewrite proportionately.**
   - Text riddled with tells → full rewrite applying the voice moves below.
   - Text that's 85% fine → surgical edits on the flagged spots; leave the rest alone.
   - User gave a narrow instruction ("just fix the hedging") → do only that. Don't rewrite what they didn't ask about.
3. **Verify** — answer honestly:
   - *What still sounds machine-made?* Re-scan the checklist on your rewrite.
   - *Did I add any fact, name, number, date, or citation not in the source?* Remove it.
   - *Did I preserve the meaning — every caveat, tradeoff, comparison, and scope?* (See Hard rules.)
   - *Did I cut filler without losing information?*
   - *Does every phrase I flagged in step 1 actually differ in my rewrite?* Check word for word, not from memory of what you intended. A tell that survives unchanged doesn't get claimed as fixed.
   - *What is the literal last sentence of the rewrite, right now, and does it pass item 15 on its own?* If you reordered anything, a tell you already cut can resurface here without you noticing — check this sentence specifically, not just "the checklist" in the abstract.

   **At most two verify passes, then stop.** The exit condition is no *accidental* tells — patterns that remain because you chose them (a genuine list, a deliberate dash, a real triad of steps) are fine. A zero score is not the goal, and rewriting natural sentences just because they pattern-match is the failure mode called overcorrection.

4. **Read it as a stranger, once, after the checklist is clean.** This is a different question than "does it still have tells" — see the voice moves below. A piece can pass every item on the checklist and still be entirely generic; this step is the only place that gets caught.

## The tell checklist

Judge every item in context. A word or pattern appearing once is usually fine; density, uniformity, and clusters are the signal.

**Content**
1. **Significance inflation** — everything is pivotal, a milestone, a testament, part of a broader journey. State what happened; let the reader judge. *"marked a pivotal step toward operational excellence" → "cut deploy time from 40 minutes to 6."*
2. **Vague attribution** — "experts agree", "studies show", "widely regarded". Name the source or own the claim.
3. **The empty why-it-matters paragraph** — restates the previous paragraph at higher altitude ("This is significant because..."). Delete it, or state the specific consequence.
4. **Both-sides mush** — every claim balanced into "it depends", an essay that ends perfectly neutral. Commit somewhere. A piece with no claim anyone could disagree with is content, not writing.
5. **Padding the obvious** — defining common terms, "as you may know" context, and grand philosophical openings ("Since the dawn of computing...", "In an increasingly connected world..."). Start at the reader's actual floor, inside the actual topic.

**Vocabulary**
6. **Stock AI words** — delve, tapestry, testament, landscape, robust, seamless, pivotal, crucial, foster, underscore, leverage, realm, vibrant, boast, embark, journey, navigate, elevate, unlock, harness, empower, streamline, holistic, multifaceted, ever-evolving, game-changer, cutting-edge, transformative, meticulous, myriad, plethora, "in today's fast-paced world". A cluster of these is a signature. Never swap a word solely because it's listed here — "robust retry mechanism" in an engineering doc is normal usage.
7. **Copula dodging** — serves as / functions as / acts as / stands as / represents → **is**.
8. **Synonym and structure cycling** — rotating labels (the app → the platform → the solution) or recycling one sentence scaffold with the slots refilled ("doesn't automatically make X right... doesn't automatically make Y right..."). Repeat the natural word; vary the structure.
9. **False ranges** — "from startups to enterprises" spans that mean "various", which means nothing. Give a real specific instead.
10. **Transition crutches** — Moreover, Furthermore, Additionally, Consequently stitching every paragraph. Humans mostly just start the next sentence.

**Rhythm and structure**
11. **Rule-of-three compulsion** — "clear, concise, and compelling". Keep the strongest item, cut two. (A list of three actual steps is a list, not a tell.)
12. **Negative parallelism** — "It's not just X — it's Y." / "This isn't about A; it's about B." State Y directly.
13. **Uniform rhythm** — every sentence 15–25 words reads metronomic; so does the opposite tic of dramatic one-line paragraphs dropped at regular intervals. Humans are bursty and irregular. Read it aloud in your head.
14. **Em-dash and semicolon density** — a few per page, not two per sentence. Replace with periods or restructure.
15. **The manufactured punchline** — sections ending on a tidy aphorism ("And that changes everything." / "What matters is that we keep asking."), and its more common cousin: a hedge word ("essentially", "basically") introducing one clever image that repackages everything already said ("It's essentially a tiny, immortal, wrinkly potato that dug itself a throne."). If the last sentence is doing the classic AI move of summarizing the whole paragraph as a witty comparison, that's this tell even when nothing else about the sentence looks wrong — cut the hedge and cut or shorten the sentence, don't leave it standing because it's clever. Real endings just stop, or land on one more genuine detail, not a bow.

**Formatting**
16. **Bold-header bullets** — lists of "**Term:** explanation". Convert to prose or drop the bold terms.
17. **Heading overgrowth** — a heading per three sentences, Title Case Everywhere, and the question-skeleton outline ("Why does X matter?" → "What about Y?" → "Is there a middle ground?"). Headings mark real topic changes; use sentence case.

None of items 16–17 means avoid structure. A genuinely long numbered procedure, a real comparison table, a glossary a reader will scan instead of read — structure the content actually needs is not a tell, and stripping it out because "AI also uses headings" makes technical writing worse, not more human. The tell is structure imposed on content that would read fine as plain prose, or structure repeated so often it's the reflex instead of a choice.

18. **Emoji and decoration** — 🚀 in prose, ✅ lists, hashtag blocks, one-line-per-sentence "broetry", numbered "lessons I learned" listicles. Strip unless the context genuinely calls for it.
19. **Signposting** — "Let's dive in", "In this post we'll explore", "Now that we've covered X". The reader can see the structure; don't narrate it.

**Chatbot residue**
20. **Assistant boilerplate** — "Great question!", "I hope this helps", "I hope this email finds you well", "Feel free to reach out", "Don't hesitate to", apologies, knowledge-cutoff disclaimers, "In conclusion / In summary" wrap-ups, "The future of X is...".
21. **Hedge and filler stacking** — arguably, typically, generally, essentially, "it's worth noting", plus wordy idioms: in order to → to, due to the fact that → because, has the ability to → can, a wide variety of → many, utilize → use, prior to → before. State real uncertainty once, precisely; cut the rest.

## The voice moves

A checklist can only subtract. These moves are what put something back — skip them and the text just goes from cluttered to clean, not from clean to human.

1. **Let rhythm follow the idea, not a pattern.** Alternating sentence length on a schedule — long, short, long, short, or question-then-answer-then-explanation — is just a different mechanical tell wearing a disguise. A real writer's rhythm tracks the weight of what's being said: a short sentence because the point is sharp, two long ones in a row because the explanation genuinely needed both, no fixed beat. *"We shipped it. Nobody noticed for a week, which told us more about our onboarding than any survey had."*
2. **Commit, unevenly.** Real people aren't equally sure about everything in the same paragraph — that uniformity is itself synthetic. Say the thing you're sure of flatly, flag the one thing you're actually not sure of, and don't hedge the rest just to match. *"This will probably work for most teams in many cases" → "This works. I genuinely don't know what happens above 1GB — we never tested it."*
3. **Trade abstraction for a concrete already in the source.** *"The process was slow and frustrating" → "Deploys took 40 minutes, so people batched changes."* Never invent the concrete — if the source has none, write plainly without it.
4. **Write like you'd say it — don't perform casualness.** Contractions where natural, plain construction where a sentence was pompous. This is not a license to add "so, here's the thing," "honestly," "the cool part is," or "basically" as connective tissue between ideas — that's a different, equally recognizable tell: an AI's idea of casual, not an actual person's. Reach for those only when a voice sample supports them. *"This serves as a testament to our commitment to quality" → "We care about this, and it shows."*
5. **Don't manufacture imperfection.** Polished writing is not itself an AI tell — plenty of real human writing is extremely clean. What reads as machine-made is predictability, not smoothness. Never add a typo, a fragment, slang, or forced casualness whose only job is to look human. The exception is texture the content already implies: a sentence starting with And or But because the logic wants it, a real fragment for real emphasis. *"We tried caching first. Didn't help."* — that fragment earns its place because the idea is that small, not because fragments read as human on their own.
6. **Have a reaction only when the source earns one — default to withholding it.** This is easy to overuse. A technical or factual claim usually doesn't need a reaction bolted on: "The cache loses data when the server fails" doesn't need ", which is obviously a problem" tacked on to sound human. Add one only where the stakes or the surprise are real and stating it adds something a flat report wouldn't. *"Users lost their work" → "Users lost their work, which is about as bad as this gets."* When unsure, leave it out — an unreacted fact reads more human than a manufactured reaction.
7. **State the interesting thing and stop.** Don't append a sentence explaining why what you just said is funny, surprising, or important — that trailing gloss is a reflex, not a courtesy. Trust the reader to get it. This is also how endings should work: land on the strongest remaining detail and stop, instead of wrapping the piece in a closing thought it doesn't need.
8. **Reach for the ordinary word over the precise one, when precision isn't the point.** *"Reduced throughput by 34%" → "Way slower"* is the right call if the source itself was making a casual point, not a benchmark claim. Manufactured precision on a claim nobody asked to be exact about reads as engineered, not careful.
9. **Let the structure be a little inefficient.** This is the deepest tell and the one word-level fixes never touch. AI writing is relentlessly optimized: definition, then supporting facts in escalating order, then a capstone example saved for last — maximum information density, zero redundancy, nothing out of place. A person telling you about something interesting doesn't outline it; they lead with whatever struck them first, whether or not it's structurally "supposed" to come first. *"The lyrebird is nature's ultimate impressionist... Researchers once recorded one reproducing an entire construction site" → "A lyrebird once fooled researchers by recreating an entire construction site — drills, jackhammers, shouted orders, in order. It's an Australian songbird that can also do up to twenty other species, car alarms, and a crying baby."* Same facts, reordered around the one that actually earns the lead. Reordering isn't a license to leave a fragment or comma splice behind, and whatever sentence you move into the new ending slot needs its own check against item 15 — cutting a manufactured punchline in one pass and then relocating a leftover clever-summary phrase back into the new final sentence is not a fix, it's moving the same tell to a different address.

**Final check: read it as a stranger.** Separate from the checklist, after everything else. Read the whole piece once straight through and ask three things:

- Could this have been written by literally anyone, about anything, on any day? If every sentence would also work in a different piece on a different topic, the checklist passed but the writing still isn't done.
- Does the order of ideas feel like an outline, or like a person remembering something interesting? If the most striking fact is saved for the end because that's structurally "correct" rather than where a person would naturally land it, move it.
- Does this sound like a specific person, or like an AI that has learned what sounding human is supposed to look like? Forced casual connectives, a fragment that isn't earning its place, a reaction bolted onto a plain fact — these are the tells of *performed* humanity, and they're just as recognizable as the tells you started by removing.

Find the one place worth a specific, small, non-generic choice, and fix whichever of the three questions caught something.

## The ceiling

Be honest about this: the single most human thing a piece of writing can have is a specific, unprovable personal detail, and manufacturing one to close the gap breaks the rule that matters more than sounding human — never invent. On source material that already has real texture (a name, a memory, an actual number), this process gets very close to indistinguishable. On thin or abstract source material, the honest result is well-made and still a little generic in that one dimension, and that's correct — a good rewrite of flat material isn't the same thing as a good rewrite of material with a real story in it. Don't fake the difference with manufactured warmth.

## Voice matching: "humanize" vs. "sound like me"

These are different requests.

- **"Humanize / make it natural"** → apply everything above; aim for plain, direct, confident prose. Do not impersonate anyone.
- **"Make it sound like me"** → requires voice evidence. If the user provided writing samples, extract their mechanics — sentence-length habits, contraction use, punctuation fingerprint, pet phrases, bluntness level — and match them, including where they contradict this file (their heavy em dashes stay). If no samples exist, use the user's own wording and tone from this conversation as the sample. Never fill the gap with an invented persona; "blunt and quirky" is just another costume. Match what you find, don't improve it — a user whose real writing runs long and looping doesn't get tightened up "for their own good"; that's substituting your taste for their actual voice, which is the opposite of what this mode is for.

**Standing voice profile:** if you can read files and this skill's folder contains `voice/samples.md` with real writing samples in its Samples section (not the placeholder line), treat that as voice evidence and calibrate every rewrite to it automatically — the user shouldn't have to ask twice.

## Hard rules

- **Never invent.** Every fact, number, name, date in the output must exist in the input. A clunky sentence is recoverable; a fabricated fact is not.
- **Preserve meaning, not just facts.** Don't trade nuance for punchiness: every caveat, tradeoff, comparison, causal claim, and scope limit in the source survives the rewrite. *"Reduced latency but increased memory usage"* must not become *"dramatically improved performance"* — nothing was invented, but the tradeoff vanished, and that's just as wrong.
- **Judge in context.** Never change a word or structure solely because it appears on the checklist. The checklist finds candidates; your judgment convicts them.
- **Never touch** code, URLs, quoted text, or proper nouns. Rewrite around them.
- **If the input is already clean, say so and change nothing.** Churn is not value.

## Output modes

- **Pasted text** → only the rewritten text, followed by one brief line naming the main categories actually changed. Nothing else.
- **A file** → edit in place; report what changed in one line.
- **Your own drafting** → apply all of this silently. Never include process narration — no "Here is the rewritten text:", no "I applied the voice moves." The reader gets prose, not a receipt.

## Boosters (optional — use when the harness allows)

These files ship in this skill's folder; if you can't access them, everything above stands alone.

- **Shell available?** Run `python3 scripts/lint.py <file>` before and after — a deterministic detector for the mechanical tells, with line numbers and a score. Treat it as evidence for your verify pass, not as the definition of done: it catches surface patterns and misses content-level tells (no-concreteness, both-sides mush), which stay your job.
- **File access?** `references/patterns.md` and `references/voice.md` expand every section above with fuller examples and edge cases, including what NOT to flag. `voice/samples.md` holds the user's standing voice profile (see Voice matching above).
