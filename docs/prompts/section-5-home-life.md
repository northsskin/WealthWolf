# Prompt: build Section 5, Home & Life

Paste everything below the line into Cursor (Agent mode).

---

Build **Section 5: Home & Life** of the Wealthwolf course in this repo. First read `docs/CONTENT_GUIDE.md` and follow it exactly. Then study `wealthwolf/scripts/content-gen/e01_paycheck.py`, `u05_fees.py` and the JSON they produce, and match their structure, tone and quality.

**Section entry.** Add this to `src/data/sections.json` (keep the array sorted by `order`):
```json
{ "id": "home-life", "order": 5, "title": "Home & Life",
  "description": "Renting, buying, sharing money and the big moments that cost the most.",
  "trial": { "id": "home-section-trial", "title": "Section Trial: Home & Life",
             "summary": "Twelve questions from the whole section. Three strikes and you’re out.", "xp": 50, "draw": 12 } }
```
Put the units in `src/data/home-life/`. Scripts are named `h01_….py` to `h10_….py`.

**What learners already know.** Budgeting, saving, emergency funds and goals (Section 1). Paychecks and job changes (Section 2). Credit scores, loans and interest (Section 3). Insurance, including renters and home insurance (Section 4).
- The word `mortgage` is already defined in `src/data/credit-debt/01-debt-credit.json` but not yet taught. Teach it here with `[[mortgage]]`. Don't define it again.

**Units.** Each unit has 8 lessons, plus a review and a unit trial.

| # | File and unit id | Prefix | Title | Lesson ideas (mix the formats) |
|---|---|---|---|---|
| 1 | `01-renting.json`, id `renting` | `rn` | Renting | How much rent you can afford (rent-to-income math), reading a listing, application fees and screening, reading a lease (document), security deposits and getting yours back, renters’ rights basics, spot the bad clause (spot), Kayla’s first lease (story) |
| 2 | `02-moving-roommates.json` | `mv` | Moving & Roommates | The real cost of moving (document), splitting rent fairly by room size (math), shared bills and a roommate agreement, what happens if a roommate leaves, utilities setup, comparing two apartments (call), Ben and Ola split a place (story), the moving checklist (order) |
| 3 | `03-rent-vs-buy.json` | `rb` | Rent vs. Buy | What owning really costs beyond the mortgage (taxes, insurance, repairs), the 5-year rule of thumb, opportunity cost of a down payment, flexibility vs. equity (sort), a rent vs. buy comparison (call, two docs), when renting is the smart move, myths (“rent is throwing money away”), Sam’s decision (story) |
| 4 | `04-buying-a-home.json` | `bh` | Buying a Home | How much house you can afford, down payment and PMI, saving for closing costs, pre-approval, the steps from offer to keys (order), inspections and appraisals, reading a Closing Disclosure (document), first-time buyer programs (verify current programs) |
| 5 | `05-mortgages.json` | `mg` | Mortgages | What a mortgage is, fixed vs. adjustable rate (call), 15- vs. 30-year total interest (math), how amortization works (early payments are mostly interest), points, a Loan Estimate (document), refinancing basics, extra payments and what they save |
| 6 | `06-owning-a-home.json` | `oh` | Owning a Home | Property tax, homeowners insurance and escrow, the 1% maintenance rule of thumb, HOA fees (spot one on a statement), home equity, HELOCs and their risks, a homeowner’s yearly budget (allocate), Nia’s first-year surprises (story) |
| 7 | `07-relationships.json` | `rl` | Money & Relationships | Talking about money early, joint vs. separate vs. both accounts (sort), splitting costs fairly with different incomes (math), shared goals, financial infidelity and red flags, lending money to friends, prenups at a high level, Alex and Jordan merge finances (story) |
| 8 | `08-family-costs.json` | `fc` | Kids & Family Costs | The cost of a baby’s first year (document), childcare costs and options (call), Dependent Care FSA and the child tax credit (confirm current amounts on irs.gov), 529 college savings plans, teaching kids about money, life insurance once you have dependents, a family budget (allocate), Maria plans for twins (story) |
| 9 | `09-life-events.json` | `le` | Big Life Events | A money checklist for each event (order): moving cities, getting married, divorce, a new baby, job loss, a death in the family. A wedding budget (allocate), updating beneficiaries and insurance, planning for a big expense, Tom’s whirlwind year (story) |
| 10 | `10-helping-family.json` | `hf` | Helping Family | Supporting parents or siblings without sinking yourself, gifts vs. loans (call), co-signing for family (risks), setting boundaries, caring for aging parents (costs and options), sending money abroad (fees and exchange rates), putting your own oxygen mask on first, Lina helps her mom (story) |

**Facts to confirm before using:** typical PMI rules, current first-time buyer programs, child tax credit and Dependent Care FSA limits (irs.gov). Label them with the year.

**Done when:**
- `npm run check` shows the section with 10 units, each with 8 lessons, and reports no problems.
- `npm run build` passes.
- Every new lesson plays correctly in `npm run dev:unlocked`, including the Section Trial.
