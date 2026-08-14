# debot

A skill that stops LLMs from writing like LLMs.

## What it does

Paste [SKILL.md](SKILL.md) into ChatGPT, Claude, or whatever you're using, and ask it to humanize a piece of text. It has a list of about twenty specific habits that give AI writing away — bold-header bullet lists, "it's not just X, it's Y," hedging every sentence into mush — and works through them one at a time. The whole list, plus what to write instead, is in SKILL.md.

## How it works

Scan the text, flag those habits, rewrite around them, then check the rewrite for the same problems before sending it back. Along the way it puts some rhythm back into the sentences and swaps hedged claims for plain ones. Nothing gets added or dropped factually. Same facts in, same facts out.

No tools needed for any of this. Copy-paste works fine.

If you can run Python 3.8 or newer, `scripts/lint.py` does the same scan as a script and gives you a score, so you don't need a model to check a file:

```bash
python3 scripts/lint.py yourfile.md
```

## How this compares

Asked deepseek-v4-flash (via opencode, not Claude) to write a short paragraph about a fun topic, no other instructions. It picked naked mole rats. That's the "before" text below, unedited, not cherry-picked for how bad it sounds:

> The naked mole rat is nature's strangest overachiever. This pink, nearly hairless rodent lives in underground colonies where a single queen does all the breeding, like a bee hive — except it's a mammal. They're famously cancer-resistant, can survive without oxygen for nearly 20 minutes, and don't even seem to feel certain types of pain. They also outlive other rodents by a huge margin, some reaching 30 years, and — bizarrely — they barely age at all. To top it off, they communicate in "chirps" that are unique to each colony, and they can even walk backward as fast as they walk forward. It's essentially a tiny, immortal, wrinkly potato that dug itself a throne.

Same model, same paragraph, three treatments.

**Just told to "humanize this text," no method:**

> The naked mole rat is basically nature's strangest overachiever. It's this pink, almost hairless little rodent that lives underground in colonies where a single queen does all the breeding — like a bee hive, except, you know, it's a mammal... Basically, it's a tiny, practically immortal, wrinkly potato that managed to dig itself a throne.

Reads looser. There's a "you know" in there, a real human tic. But look at what didn't change: "nature's strangest overachiever" survives untouched, and the pass picked up more hedge words than it removed ("basically" twice, "practically" once). A vague instruction makes text sound casual without making it say anything different.

**Given [blader/humanizer](https://github.com/blader/humanizer)'s real SKILL.md**, fetched live from their repo:

> The naked mole rat is nature's strangest overachiever. This pink, nearly hairless rodent lives in underground colonies where a single queen does all the breeding, like a bee hive, except it's a mammal... It's essentially a tiny, immortal, wrinkly potato that dug itself a throne.

Mostly the original with the em dashes taken out. "Nature's strangest overachiever" and the entire closing line survive word for word, hedge included. Our own linter still catches it: one flag, "lightly seasoned."

**Given this repo's real SKILL.md:**

> The naked mole rat doesn't look like much: a pink, nearly hairless rodent that digs in the dark. But the underground colony is organized like a bee hive, with one queen doing all the breeding, except it's a mammal. The rest is even stranger. The animals resist cancer, last about twenty minutes without oxygen, and seem immune to some kinds of pain. They outlive other rodents by a wide margin, with some hitting thirty years old, and they barely age at all. Their colony has its own dialect of chirps, and they can scurry backward as fast as they scurry forward. It's a peculiar animal, but it earns its reputation.

The opener changes, and this time so does the closer. Earlier drafts of this section ran the same test and got a version that fixed the opener but left the exact same "essentially a tiny, immortal, wrinkly potato that dug itself a throne" punchline standing, unchanged from the original, while claiming in its own summary line that it had been trimmed. That was a real gap: the checklist's punchline examples were all inspirational aphorisms ("The future is already here"), and a hedge-word-plus-clever-metaphor closer like the potato line didn't obviously match, so the model never flagged it. Fixed the checklist to name that pattern explicitly, added a verify step that checks a flagged phrase actually changed before it gets called fixed, and reran the exact same test above. No potato, no hedge, no aphorism. Rerun it yourself if you want to check.

None of the actual rewrites above came from Claude, the model that wrote this skill. Run it yourself and see what you get:

```bash
opencode run "Apply the skill in this file to the text at the end of it. Reply with only the rewritten text." -f your_prompt.txt -m opencode/deepseek-v4-flash
```

where `your_prompt.txt` is SKILL.md (ours or humanizer's) followed by whatever text you're testing.

## Install

With the skills CLI:

```
npx skills add askmaddyy/debot
```

As a Claude Code plugin:

```
/plugin marketplace add askmaddyy/debot
/plugin install debot@debot
```

With zero tooling: copy the contents of SKILL.md into the system prompt or the chat.

## Sound like you

By default debot writes plain, direct prose. Want your own voice instead? Paste a few things you've actually written into [voice/samples.md](voice/samples.md). After that, every rewrite matches your sentence habits and punctuation without you asking. No samples yet? Just say "make it sound like me" and it'll go off your messages in the conversation.

## Layout

```
SKILL.md                 the skill: scan, rewrite, verify
references/              expanded tell catalog, voice guide
scripts/lint.py          deterministic tell detector
voice/samples.md         your writing samples, for automatic voice matching
```

## License

MIT.
