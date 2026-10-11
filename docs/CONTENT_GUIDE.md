# Wealthwolf content guide

How to add a section of the course. Each section prompt in [`docs/prompts/`](prompts) assumes you've read this first. Sections 1 (Everyday Money) and 2 (Earning) are finished examples. When in doubt, copy what they do.

All paths below are inside `wealthwolf/`.

## Shape of a section

- **A section** is an entry in `src/data/sections.json` plus a folder `src/data/<section-id>/`. The entry has `id`, `order`, `title`, `description` and a `trial`: `{ id, title, summary, xp: 50, draw: 12 }`. The trial is a 12-question test drawn from every unit in the section.
- **A unit** is one JSON file in that folder: `NN-<unit-id>.json`. Its `order` field sets its place in the section.
- **Every unit has exactly 8 lessons**, then:
  - a review (`type: "review"`, "Sharpen Up", `draw: 8`)
  - a unit trial (`type: "boss"`, 4 questions of its own plus `draw: 4` from the unit)

  The `review()` and `trial()` helpers build both.
- **Every lesson has 5 to 8 steps.**

## Write units with the generator, not by hand

Each unit is produced by one Python script in `scripts/content-gen/`, named with the section's letter, for example `c01_borrowing.py`. Run it from that folder:

```bash
cd scripts/content-gen && python3 c01_borrowing.py
```

Copy an existing script as your template. [`e01_paycheck.py`](../wealthwolf/scripts/content-gen/e01_paycheck.py) and [`u05_fees.py`](../wealthwolf/scripts/content-gen/u05_fees.py) show every step type and document kind. The helpers in `lib.py`:

| Helper | Makes |
|---|---|
| `info(title, body)` | A card that teaches, no question |
| `mc(prompt, choices, answer, explain, context=, doc=, docs=, why=)` | Multiple choice. `why` gives one line per choice, shown when that wrong choice is picked |
| `tf(prompt, answer, explain)` | True or false |
| `fill(prompt_with____, choices, answer, explain)` | Fill the gap. The prompt has exactly one `___` |
| `num(prompt, answer, explain, unit='$')` | Type a number. Cents work automatically. Use `unit='%'`, `'months'` and so on for non-money |
| `order(prompt, items, explain)` | Put items in order. Give the items in the correct order |
| `match(prompt, pairs)` | Match pairs |
| `sort(prompt, buckets, items)` | Sort items into 2 or 3 buckets. Items are `(text, bucketIndex)` |
| `spot(prompt, doc, answer_line_id, explain)` | Tap the wrong or suspicious line on a document |
| `alloc(prompt, total, step, categories, explain)` | Budget builder. Categories take `fixed`, `min` or `max`, and `min`/`fixed` must be multiples of `step` |
| `doc(kind, title, lines, subtitle=, meta=, totals=, note=)` | A document: `paystub`, `bill`, `receipt` or `statement`. Lines are `(id, label, amount)` plus an optional `{'date':…}`. Money out is negative on statements. **Assert every total in Python** (`assert total(...) == ...`) |
| `lesson(id, title, summary, steps, fmt=, story=)` | Numbers the steps `<id>-q1…` |
| `write_unit(file, id, order, title, description, wolfLine, terms, lessons, section='<section-id>')` | Writes the unit JSON |

**Lesson formats** (`fmt`) show as an icon on the path. Mix them in every unit:
- `concept`: the default
- `document`: read a pay stub, bill, statement or receipt
- `story`: a short story about a person, read first, with questions about it. Pass `story={'title','character','body'}`
- `spot`: find the problem on a document
- `sort`: sort or build
- `call`: make the call, comparing two options with `docs=[A, B]`

A good unit has at least one story, one document or spot lesson, and one call or sort lesson.

**IDs.** Lesson ids start with the unit's two-letter prefix (given in your section prompt), for example `cs-what-is-a-score`. Never reuse an id. Never rename or delete an existing lesson id: saved progress is keyed by it. To move a lesson to another unit, cut it from one file and paste it into the other with its id unchanged.

## Words (the glossary)

- **Define each word once,** in the `terms` map of the unit that teaches it: `{'id': term('Name', 'definition', 'example')}`. Write definitions in plain language, and make the example concrete with a number where possible.
- **Introduce a word inside a step,** in its `context`, `prompt`, info `body` or story `body`, by wrapping it: `[[credit score]]`, or `[[scores|credit-score]]` when the display text differs from the id.
- **Never use a word before it's taught.** A word can appear in `explain`, `choices` or sort/order `items` only after an earlier step on the path has taught it. The checker enforces this.
- **Reuse words that already exist.** Find them with `grep -o '"[a-z0-9-]*": {' src/data/*/*.json`, or look at `/glossary` in the app. Link them with `[[...]]`, don't redefine them, and never give a new word an id that's already used.

## Writing rules

- **Assume the learner knows nothing.** One idea per step. Teach the word, then ask about it straight away.
- **The Wolf's voice:** short, dry, encouraging. `explain` is one or two short sentences that show the working, for example `$2,000 × 0.04 = $80.`
- **Real-world documents and numbers.** Keep figures realistic and the math clean. For money use `$1,234.56`, and `−` for minus in explanations.
- **US rules.** Any figure that changes yearly (tax brackets, contribution limits, the standard deduction, Social Security amounts) must be checked on the official source and labelled with its year, for example "(2026 limit)". Sources: irs.gov, ssa.gov, medicare.gov, healthcare.gov, consumerfinance.gov, studentaid.gov, fdic.gov. If you can't confirm a number, write the lesson so it doesn't depend on it.
- **Education, not advice.** "A common rule of thumb is…", not "You should buy…".
- **Punctuation:**
  - No em dashes. Use a colon, a full stop or a comma.
  - Use curly apostrophes (’), as the existing files do.
  - No emoji.
- **Multiple choice:**
  - Usually 3 choices. Wrong choices must be believable, not silly.
  - Add `why=[...]` when the wrong answers teach something.
- **Unit trials:** their 4 own questions must not repeat a lesson prompt word for word (the checker flags this). Write fresh questions on the same ideas.
- **Stories:** a named person with an age and a job, two or three short paragraphs, every number in **bold**, and questions that walk through the math. Vary the names and backgrounds.

## Check your work

1. `python3 <your script>.py` for each unit. The asserts in the script catch broken document totals.
2. `npm run check`. It must end with **No problems found.** and show the section with every unit at 8 lessons.
3. `npm run build`.
4. `npm run dev:unlocked`, open http://localhost:5190, go to your section with **All sections**, and play every new lesson. Check:
   - Every answer marked correct really is correct.
   - The explanations add up.
   - Nothing is cut off or scrolls sideways at phone width (DevTools → 375px wide).
5. Play the Section Trial once.

## Hand-off

- Work on a branch named for the section, for example `section-3-credit-debt`.
- Commit the scripts and the generated JSON together, then open a pull request.
- Don't edit other sections' files, the app code, or `src/styles/` unless your section prompt says so. If something in the app needs changing, note it in the pull request.
