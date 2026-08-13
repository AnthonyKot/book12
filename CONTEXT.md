# Book 12 — CONTEXT (authority document)

Comparative reading of official citizenship-test study materials: the same questions
— who are we, what did we do, what must you believe — answered by ~15 states to the
people they are about to admit. Working title (user decision open): **The Entrance
Exam** / "Welcome to the Nation" / "Same Oath, Different Pasts". Tagline candidate:
"Eleven states introduce themselves to the people they're about to admit."

Precedence (inherited from book8/book6): this file → AGENT.md (audience, priority
stack, personal hook, pitch gate) → chapter contract → TEMPLATE.md → chapter prose.

## Thesis (v1)

A citizenship guide is the state's shortest authorized self-portrait, and the only
history book whose reader is graded on believing it. Because space is minimal and
every line is testable, omission signals are stronger than in schoolbooks — and what
a state makes an applicant *affirm* (values, oaths, revocability clauses) is data
schoolbooks don't carry. Coding categories per passage (from book8): **space · agency
· vocabulary · causes · numbers · people**, plus two native to this corpus:
**distractors** (the wrong answers a state writes are a self-portrait) and
**testability** (what is narrated vs what is examined — the two anti-correlate:
EE narrates 10pp of occupation history and tests none of it; DE tests ~70 history
items and narrates nothing, publishing no answer key; RU narrates nothing at all).

The engine (from the 2026-08-13 corpus recon): **the grammar of atonement scales** —
date+agent (CA "In 2008, Ottawa formally apologized") → fraction (FR "une part de
responsabilité") → nameless event (AT's Waldheim paragraph without Waldheim) → URL in
an appendix (AU's National Apology as a link) → agent deleted from the sentence (US
"What group of people was taken to America and sold as slaves?") → filed under art
criticism (ES memoria histórica as film studies) → legislated remedy for an unnamed
wrong (ES 2-year fast track for Sephardic Jews, expulsion never mentioned).

## Corpus

15 positions — see `CORPUS.md` (editions, agencies, genres, provenance caveats).
**10 core columns**: UK · CA · AU · US · DE · AT · DK · FR · ES · EE.
**Special voices, never peer columns** (book8's KZ rule):
- **RU** — 18-page demo exam only; the finding is assent-not-knowledge (the Crimea
  question where all three options presuppose the annexation) and the missing
  Great Patriotic War. Never in a ladder as a full narrator.
- **NL · LV** — states that publish exam outcomes/tools but no book; the
  state/commercial split is the exhibit.
- **Zero column: JP · IL · BY** — no published test corpus (verified with sources,
  manifest-east.md). Ministerial discretion instead of a self-portrait.

Provenance caveats (gating for quotes):
- **UK** = third-party re-typeset of the Crown-copyright text
  (uk-2013-lifeintheuk-retypeset.pdf). Discovery and drafting OK; **final quotes
  eye-checked against the TSO original before shipping** (book8's SD rule).
- **FR** = scanned, no text layer; tesseract here has only `eng` traineddata.
  **FR quotes are transcribed from page images and eye-checked**; never grep-verified.
- **CA** file is the 2012 text in its 2021 reprint; **AU** file is the 2020 trimmed
  "testable section" edition — the trimming is itself a finding (the p.1 trigger
  warning survives the removal of the content it warned about).

## Spine (~12 chapters + epilogue) — chapter unit = the SLOT, not the event

| Part | Chapters |
|---|---|
| I The machinery | 0 Intro: the gradient (DK 243pp → DE 460 questions → RU 18pp → JP/IL/BY nothing) · 1 Meet the documents (cards) |
| II The past | 2 The founding story · 3 Empire & slavery (UK lead) · 4 The war (DE/AT/DK/FR/EE) · 5 First peoples (CA/AU/US/DK-Greenland) · 6 The missing history (RU without 1941–45 · US without Jim Crow · ES Franco-as-isolation) |
| III The present tense | 7 The values you must affirm · 8 The wrong answers (distractors) · 9 Narrate vs test · 10 The invisible applicant |
| IV The silence | 11 The states that won't write (NL · LV · zero column) |
| — | Epilogue: Could you pass? |

Two axes (book8): slot chapters = rows; document profiles = columns (cards in ch. 1,
full profiles as closing synthesis). Credit precedes critique.

## Chapter form

Nine beats in `TEMPLATE.md`, adapted to slots — a rhythm, not a form. The ladder is
ordered by **rhetorical posture** (e.g. atonement grammar: named-and-dated → qualified
→ agentless → absent), never alphabetical; empty cells meaningful; zero-mention badges
("Stolen Generations: 0 mentions in the testable section"). Exhibit vs essay modes per
AGENT.md. Fixed coda every chapter: **"Now take your own country's test."**

## Voice (inherited from book8, unchanged)

- **Quotes or nothing** — no claim about a document without the passage, original +
  translation.
- **Banned blame register**: *propaganda, brainwashing, regime* (as sneer), *sheep*.
- **Banned guide register**: *just, simply, obviously, of course*.
- Funny by accuracy; provocations may open, never close; no title claims more than
  its quotes support; jargon defined once, never apologised for.
- Extra rule for this corpus: the applicant is never the joke. The books are
  addressed to people passing a harder test than the reader ever took — mockery of
  the *test-taker* (as opposed to the test-writer) is banned.

## Checks (deliberately light — inherited)

`verify.sh`: anti-leak (GATING: no PDF/corpus file ever tracked; repo publishes to
GitHub Pages) · internal links · chapter-count sync computed · HTML nesting · coda
refrain. Quote audit rule: grep against corpus-orig/ **with newlines normalized**
(`tr '\n' ' '` — pdftotext hard-wraps mid-phrase); FR + UK additionally eye-checked
(see provenance caveats).

## Status log

- 2026-08-13: corpus collected (agy + 2× codex; grok dead — 402, retired). 11 official
  PDFs + UK re-typeset supplied by user; manifests in resources/. Zero column verified
  (JP/IL/BY). Two-agent content recon of all 10 text documents, quote-verified.
  Plan approved: cut (10 core + RU/NL/LV/zero), slot-spine, pilot = ch. 3 Empire &
  slavery. Repo scaffolded; corpus-orig extracted; recon quotes grep-verified.
- Open (user): title/tagline pick · US 2025 128q manual browser download (for ch. 8's
  test-mutation diff) · optional TSO purchase for UK quote verification before ship.
