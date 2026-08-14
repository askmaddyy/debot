# Adding the human back

Removing tells produces neutral text. Neutral text is still recognizably machine-made, because no person is neutral — a checklist can only subtract, and subtraction has a floor. This file is the positive half: what actually makes writing read like one specific person made it, not just like nobody obviously broke any rules.

There's a third failure past both of those, and it's the one that's hardest to notice because it can feel like success: over-applying the moves below produces its own signature — forced casualness, a fragment that isn't earning its place, a reaction bolted onto a plain fact. That doesn't read as a person. It reads as an AI that has learned what "sounding human" is supposed to look like, which is arguably a more obvious tell than sounding like AI in the first place. Every move below has a matching failure mode where pushing it too hard produces exactly this — it's called out where it applies.

## The moves

### 1. Let rhythm follow the idea, not a pattern
After the rewrite, check the shape of your sentences. If four in a row are 15–25 words, break the pattern: fuse two into one long sentence, or drop a three-word one after it. The linter measures this (sentence-length standard deviation); a human page usually scores above 8, machine text often sits below 6.

Watch the failure mode on the other side: fixing this by alternating length on a schedule — long, short, long, short, or question-then-answer-then-explanation — just swaps one mechanical pattern for another that's equally recognizable once you've seen a few pieces "humanized" this way. Real rhythm tracks the weight of the idea, not a rule. Two long sentences in a row are fine if the explanation genuinely needed both. A short sentence lands because the point is sharp, not because the schedule called for one.

### 2. Commit, unevenly
Pick the claim you actually believe and state it without a parachute. But don't stop there — the tell isn't just hedging, it's *uniform* hedging or *uniform* confidence across an entire paragraph. Real people are sure about some things and genuinely not sure about others in the same breath, and the difference shows. A paragraph where every claim carries the same "probably" is as synthetic as a paragraph where nothing does.

- Uniform hedge: "This will probably work for most teams in many situations, though results may vary depending on setup."
- Uneven, real: "This works. I genuinely don't know what happens above 1GB — we never tested it."

### 3. Trade abstraction for one concrete detail
One number, one name, one date, one sensory fact beats a paragraph of qualities — but only if it's **already in the source or known to you for certain**. Never invent specifics to seem human; if the source has no concrete detail, the honest move is plain abstraction, stated briefly.

- Abstract: "The deployment process was slow and frustrating for the team."
- Concrete (if true): "Deploys took 40 minutes, so people batched changes and Fridays were a graveyard."

### 4. Write like you'd say it — don't perform casualness
Not slang — directness. Contractions where natural. Sentences that could survive being read aloud to a colleague without embarrassment. If a sentence would sound pompous spoken across a desk ("this serves as a testament to our commitment"), it's pompous on the page.

The failure mode here is specific and common: reaching for "so, here's the thing," "honestly," "the cool part is," or "basically" as connective tissue between ideas. That isn't how the person you're rewriting for talks — it's an AI's idea of how casual people talk, and it's just as identifiable a pattern as the formal tells it's replacing. These words earn a place only when a voice sample actually shows the person using them. Without one, directness beats performed casualness every time.

### 5. Don't manufacture imperfection
Polished writing is not itself a tell. Plenty of real human writing — a good technical explainer, a tight email, a well-edited essay — is extremely clean, with no fragments, no stray "and" openers, no rough edges at all. What actually reads as machine-made is *predictability*, not smoothness, and those are different things. Never add a typo, a fragment, a slang word, or forced casualness whose only job is to make the text look human; if the content doesn't earn a fragment, write the full sentence.

The exception is texture the content already implies, not texture you're inserting: Humans start sentences with "And" and "But" when the logic genuinely wants it. They use a fragment for real emphasis. Sometimes. They ask a question and answer it themselves, when the question is one they actually had. A slightly lopsided paragraph is human because the ideas were lopsided, not because lopsidedness itself reads as human — don't inject imperfection as a costume.

### 6. Have a reaction only when the source earns one, and default to withholding it
AI writing tends to report a mundane fact and a startling one in exactly the same tone, because it isn't actually reacting to either — it's listing. A person registers surprise, annoyance, relief, doubt. But this move is easy to overuse, and overused it becomes its own tell: a plain, technical, or factual claim usually needs no reaction at all. "The cache loses data when the server fails" doesn't need ", which is obviously a problem" tacked on — the reader can tell. Reserve a reaction for where the stakes or the surprise are genuinely large enough that stating them adds real information, and when you're not sure, leave it out.

- Flat: "The migration caused data loss for a subset of users."
- Reacting, earned: "The migration lost data for some users, which is about as bad as this gets."
- Reacting, not earned (don't do this): "The cache loses data when the server fails, which is obviously a problem." — the reaction adds nothing the reader didn't already know from the fact itself.

### 7. State the interesting thing and stop
One of the most reliable AI tells is the trailing gloss: say something surprising, then immediately explain why it's surprising, as if the reader needs the joke unpacked. A person trusts the reader. This applies to endings too — you don't owe the piece a summary or a closing thought. Land on the strongest detail you have left and stop; see checklist item 15 for what happens when you don't.

### 8. Reach for the ordinary word, when precision isn't the point
Manufactured precision on a claim nobody asked to be exact about reads as engineered, not careful. If the source is making a casual point, a casual word carries it better than a number that implies more rigor than the claim actually has.

- Over-precise: "This reduced throughput by approximately 34%."
- Right register, if that's all the source meant: "This is way slower."

Don't confuse this with move 3 — when the source *does* give you a real number and the claim is precision-worthy, use it. This move is about not adding false rigor to a claim that was never rigorous to begin with.

### 9. Let the structure be a little inefficient
This is the deepest tell, and the one every move above misses, because it isn't about words at all. AI writing is relentlessly optimized: a definitional opener, supporting facts in escalating order, a capstone example held back for the end — maximum information density, nothing redundant, nothing out of place. That shape is itself a signature. A person telling you something interesting doesn't outline it. They lead with whatever struck them, and the context that "should" come first structurally shows up second, or not at all.

- Optimized order: "The lyrebird is nature's ultimate impressionist. [background, then escalating examples] ...Researchers once recorded one reproducing an entire construction site."
- Human order, same facts: "A lyrebird once fooled researchers by recreating an entire construction site — drills, jackhammers, shouted orders, in sequence. It's an Australian songbird that can also do up to twenty other species, car alarms, and a crying baby."

Nothing was added or cut, only reordered around the fact that actually earns the lead. This is genuinely harder than the word-level moves, because reordering a paragraph risks breaking it grammatically — a rewrite that reorders sentences but leaves a dangling fragment or a comma splice behind has traded one tell for a worse problem. The result still has to read like something a careful person wrote, not a shuffled draft.

## Final check: read it as a stranger

This is not another item to scan for — it's two different kinds of question, asked once, after the checklist comes back clean.

First: could this exact paragraph have been written by literally anyone, about any topic, on any day? If every sentence in it would sit just as comfortably in a different piece about something else, the mechanical pass succeeded and the writing still isn't done.

Second, and easy to miss even after the first check passes: does the order of ideas read like an outline, or like someone remembering something interesting? A piece can use plain words, vary its rhythm, and still march through its facts in the most logical possible sequence — which is its own kind of tell, per move 9 above. If the best fact is sitting at the end because that's where a structural outline puts a capstone, not because that's where a person would naturally land it, move it.

Third: does this sound like a specific person, or like an AI that has learned what sounding human is supposed to look like? This is the check for the failure mode named at the top of this file. Forced casual connectives, a fragment that isn't earning its place, a reaction bolted onto a plain fact — these are all technically "voice moves," applied, and still add up to something a real person wouldn't have written. If the answer here is closer to the second description than the first, something was pushed too hard rather than not hard enough.

The fix for any of the three failures isn't to add personality as garnish. It's to find the one place in the piece — often just one sentence, sometimes just its position — that only this piece, about this thing, needed.

## "Humanize" vs. "sound like me"

These requests need different behavior. "Humanize / make it natural" means apply this file's defaults: plain, direct, confident prose — impersonate nobody. "Make it sound like me" requires voice evidence; without samples, use the user's own wording from the current conversation, and never substitute an invented persona ("blunt and quirky" is just another costume).

## Calibrating to a specific person

When the user gives you writing samples (or you can see things they actually wrote — their messages in this conversation are samples too), extract a profile before rewriting:

1. **Sentence habits** — average length, how often they go long, fragment tolerance.
2. **Formality floor** — do they write "can't" or "cannot"? "thanks" or "thank you"? Greetings and sign-offs?
3. **Punctuation fingerprint** — em dashes? parentheses? exclamation points? ellipses?
4. **Pet constructions** — phrases they reuse, how they open emails, how they hedge when they genuinely hedge.
5. **Bluntness level** — do they soften asks ("would it maybe be possible") or state them ("can you send X by Friday")?

Then match it — including the parts that contradict this skill's defaults. A user who loves em dashes gets em dashes. The target is "sounds like them", not "sounds like debot".

Match what you find; don't improve it. A user whose real writing runs long and looping doesn't get tightened up "for their own good" — that's substituting your judgment of good writing for their actual voice, and it's the opposite of what this mode exists to do. Only step in where something is a genuine error (a typo, a broken sentence), not where it's just not how you'd have written it.

Keep the profile to 5–8 observed facts. Don't psychoanalyze; describe mechanics you can point to in the sample.

## The ceiling

Say this part honestly, because overclaiming it is worse than admitting it: the single most human thing writing can carry is a specific, unprovable personal detail — a real memory, a name, an opinion nobody could have predicted. Manufacturing one to close the gap breaks the rule that outranks sounding human. Never invent.

On source material that already has real texture, this process gets very close to indistinguishable — there's something true and specific for every move above to work with. On thin or purely abstract source material, the honest output is well-made and still a little generic in that one particular way, and that is the correct result, not a failure of the process. A good rewrite of flat material is not the same thing as a good rewrite of material that had a real story in it, and no checklist should pretend otherwise.

## The lines you don't cross

Voice is presentation. Facts are not. Every technique here reshapes how true things are said. The moment a rewrite would be improved by a detail you don't have, the answer is to write well without it, not to make it up.

Meaning is not presentation either. Preserve every caveat, tradeoff, comparison, causal claim, and scope limit from the source. "Reduced latency but increased memory usage" must not become "dramatically improved performance" — nothing was invented, but the tradeoff vanished, and that is just as much a corruption as a fabricated fact.
