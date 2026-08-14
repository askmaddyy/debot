# The tell catalog

Same 21 items as SKILL.md's checklist, same numbers, in the same order — this file just gives each one a bad→good pair and more room to explain. The linter (`scripts/lint.py`) catches the mechanical ones automatically; the content tells (1–5) need a human, though the linter's low-concreteness check gives a rough signal for the zero-concreteness variant noted at the end of this section.

**How to use this file:** don't hunt for patterns one at a time. Read the flagged text once with all of these loaded, fix everything in one rewrite pass, then verify.

## A. Content tells — the text says less than it appears to

### 1. Significance inflation
Everything is a milestone, a pivotal moment, a testament to something. Real writers state what happened and let the reader decide if it matters.

- ✗ "The migration marked a pivotal step in the team's broader journey toward operational excellence."
- ✓ "The migration cut deploy time from 40 minutes to 6."

### 2. Vague attribution
Claims hung on nobody: "experts agree", "studies show", "it is widely recognized". Either name the source or own the claim yourself.

- ✗ "Many industry observers consider caching one of the hardest problems in computing."
- ✓ "Cache invalidation is hard. It broke our pricing page in March, and nobody noticed for two days."

### 3. The empty "why it matters" paragraph
A paragraph that restates the previous paragraph at a higher altitude, adding words but no information. Usually starts with "This is important because", "In essence", or "At its core". Delete it entirely; if something genuinely matters, say the specific consequence.

- ✗ "This approach is significant because it fundamentally changes how teams think about deployment."
- ✓ (deleted, or:) "Now nobody waits for Friday to ship."

### 4. Both-sides mush
Reflexively balancing every claim ("While X has advantages, it also presents challenges") until the text commits to nothing. Humans writing for real audiences take positions.

- ✗ "While microservices offer flexibility, they also introduce complexity, so the right choice depends on your context."
- ✓ "For a five-person team, microservices are a mistake. Split the monolith when the team splits, not before."

### 5. Padding the obvious
Explaining things the audience already knows, defining common terms, adding "as you may know" context — and the grand philosophical opening ("Since the dawn of computing...", "In an increasingly connected world..."). Respect the reader's floor and start inside the actual topic.

- ✗ "Email, a widely used form of digital communication, remains important for business."
- ✓ (just start with the actual point)

**Also watch for: zero concreteness.** Long stretches of pure abstraction — no number, date, name, or event anywhere. Individually clean sentences can't save a piece with nothing to point at; sustained abstraction is one of the strongest generated-text signals. If the source offers a concrete, use it; if not, keep the abstraction brief rather than elaborating it. This isn't a separate checklist item so much as what padding the obvious and both-sides mush add up to when they run through an entire piece.

## B. Vocabulary tells — words models love and people don't

### 6. Stock AI vocabulary
Certain words are radioactive because models overuse them at 10–100x human rates: *delve, tapestry, testament, landscape, robust, seamless, pivotal, crucial, foster, underscore, leverage, realm, vibrant, boast, embark, journey, navigate, elevate, unlock, harness, empower, streamline, holistic, multifaceted, ever-evolving, game-changer, cutting-edge, transformative, meticulous, myriad, plethora, in today's fast-paced world*. None is banned in isolation; three in one paragraph is a signature. `scripts/lint.py` checks a shorter, more conservative version of this list — it deliberately leaves out words like "journey" and "navigate" that are too common in ordinary writing to flag automatically without false-positiving on normal text.

- ✗ "This robust framework empowers teams to seamlessly navigate the evolving landscape of cloud infrastructure."
- ✓ "The framework handles most cloud setups without custom work."

### 7. Copula avoidance
Dodging "is" with dressier verbs: *serves as, functions as, acts as, stands as, represents, constitutes*. "Is" is fine. "Is" is good.

- ✗ "The config file serves as the single source of truth."
- ✓ "The config file is the single source of truth."

### 8. Synonym and structure cycling
Rotating through synonyms to avoid repeating a word (the app → the application → the platform → the solution → the tool). Humans repeat the natural word. Repetition is clarity, not weakness.

The structural variant: one sentence scaffold recycled with the slots refilled — "doesn't automatically make it right... doesn't automatically make every practice right... doesn't automatically make you a better person." Repeat words freely; vary structures.

### 9. False ranges
"From X to Y" spans that don't describe an actual continuum: "from startups to enterprises, from healthcare to finance". It's a decorative way of saying "various", which is itself a way of saying nothing.

- ✗ "Used by everyone from solo developers to Fortune 500 companies."
- ✓ "About 4,000 teams use it; the biggest processes 2 million orders a day."

### 10. Transition crutches
Moreover, Furthermore, Additionally, Consequently stitching every paragraph together. Humans mostly just start the next sentence; the logical connection is usually obvious from the content.

## C. Rhythm and structure tells — the shape gives it away

### 11. Rule-of-three compulsion
Triads everywhere: "clear, concise, and compelling", "plan, execute, and iterate". One strong item beats three weak ones. When you catch a triad, keep the best item and cut the other two.

- ✗ "The rewrite made the codebase cleaner, faster, and more maintainable."
- ✓ "The rewrite made the codebase faster: build time dropped from 12 minutes to 4."

### 12. Negative parallelism
"It's not just X — it's Y." "This isn't about A; it's about B." A manufactured drumbeat that models reach for constantly. State Y directly.

- ✗ "This isn't just a linter — it's a whole new way of thinking about writing."
- ✓ "The linter checks for AI tells and gives you line numbers."

### 13. Uniform sentence rhythm
AI sentences cluster around the same length, producing an eerie evenness. Human writing is bursty: a long winding sentence that takes its time getting somewhere, then a short one. Like that. Read the text aloud in your head; if it sounds like a metronome, split some sentences and fuse others.

The mirror-image tic: dramatic one-line paragraphs dropped at regular intervals ("Yes." / "That shouldn't be dismissed."). One per piece can land; a rhythm of them is a tell — merge most into real paragraphs.

### 14. Em-dash and semicolon density
Em dashes are legal — but models deploy them at several times the human rate, often two per sentence. Keep at most a few per page. Replace the rest with periods, commas, or restructuring. Same for semicolon chains.

### 15. The manufactured punchline
Ending sections with a tidy aphorism or mic-drop line ("And that changes everything." / "The future is already here."). Real endings just stop when the content is done.

The more common variant: a hedge word ("essentially", "basically") introducing one clever image that repackages the whole paragraph into a punchline. This is easy to miss because the sentence itself can read as good writing — the tell is the *placement and function*, not the words. If the last sentence is quietly doing "and in summary, it's like X", that's the same move as the aphorism, just dressed as a joke instead of a moral.

- ✗ "It's essentially a tiny, immortal, wrinkly potato that dug itself a throne."
- ✓ (cut the hedge and the summarizing frame — either end one detail earlier, or state the last fact plainly: "They can even walk backward as fast as forward.")

## D. Formatting tells — layout as camouflage

### 16. Bold-header bullet lists
Lists where every item is "**Term:** explanation". One is fine; a document built from them reads like a slide deck that lost its slides. Convert to prose when the items connect logically, or drop the bold terms.

### 17. Heading overgrowth
A heading for every three sentences, Title Case Everywhere, and "fragmented header syndrome" (H2 → one line → H3 → one line). Headings should mark real topic changes. Use sentence case.

**None of 16–17 means avoid structure.** A genuinely long numbered procedure, a real comparison table, a glossary a reader will scan instead of read start to finish — structure the content actually needs is not a tell, and stripping it because "AI also uses headings" makes technical and documentation writing worse, not more human. The tell is structure imposed on content that would read fine as plain prose, or structure so habitual it's the reflex instead of a choice made for this piece.

### 18. Emoji and decorative symbols
🚀 in professional prose, ✅/❌ lists, arrows in running text, hashtag blocks (#OpenSource #BuildInPublic), one-line-per-sentence "broetry", and numbered "lessons I learned" listicles. Unless the register genuinely calls for it (some chat, some social), strip them.

### 19. Signposting and throat-clearing
"Let's dive in." "In this post, we'll explore..." "Now that we've covered X, let's turn to Y." The reader can see the structure; don't narrate it. Start where the content starts.

- ✗ "In this guide, we'll walk through everything you need to know about connection pooling."
- ✓ "Connection pooling breaks in three ways. Here's the first."

## E. Chatbot residue — the assistant leaking into the document

### 20. Assistant boilerplate
"Great question!", "Certainly!", "I hope this helps!", "Feel free to reach out", offers to elaborate, apologies for limitations, knowledge-cutoff disclaimers. None of this survives into a document a human publishes.

### 21. Hedging and filler density
*arguably, generally, typically, essentially, in many cases, it's worth noting that, it's important to remember* — each one defensible, but models stack them until every sentence has an escape hatch. Also wordy idioms: "in order to" (→ to), "due to the fact that" (→ because), "has the ability to" (→ can), "a wide variety of" (→ many). Cut hedges unless the uncertainty is real and load-bearing; then state it once, precisely ("this failed in 2 of 30 runs"), not as fog.

## What NOT to flag (false positives)

- **Technical terms** that happen to be on the stock list ("robust standard errors" in statistics, "pivot" in dataframes, "leverage" in finance, "harness" in "test harness").
- **Genuine transitions.** One "however" per page is writing, not a tell.
- **Actual lists of parallel items.** Three steps that really are three steps may be a list.
- **The user's own voice.** If their writing samples use em dashes heavily, that's their style — keep it. The goal is *their* human, not *a* human.
- **Quoted or cited material.** Never rewrite what someone else said.
