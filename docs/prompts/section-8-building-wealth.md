# Prompt: build Section 8, Building Wealth

Paste everything below the line into Cursor (Agent mode).

---

Build **Section 8: Building Wealth**, the final section of the Wealthwolf course, in this repo. First read `docs/CONTENT_GUIDE.md` and follow it exactly. Then study `wealthwolf/scripts/content-gen/e01_paycheck.py`, `u05_fees.py` and the JSON they produce, and match their structure, tone and quality.

**Section entry.** Add this to `src/data/sections.json` (keep the array sorted by `order`):
```json
{ "id": "building-wealth", "order": 8, "title": "Building Wealth",
  "description": "The long game: the economy, financial independence, retirement and leaving something behind.",
  "trial": { "id": "bw-section-trial", "title": "Section Trial: Building Wealth",
             "summary": "Twelve questions from the whole section. Three strikes and you’re out.", "xp": 50, "draw": 12 } }
```
Put the units in `src/data/building-wealth/`. Scripts are named `w01_….py` to `w10_….py`.

**What learners already know.** Most of the course: budgeting, earning, credit, insurance, home, taxes and investing. The word `inflation` is already defined; link it with `[[inflation]]`. This section ties everything together, so the last unit should feel like a graduation.

**Units.** Each unit has 8 lessons, plus a review and a unit trial.

| # | File and unit id | Prefix | Title | Lesson ideas (mix the formats) |
|---|---|---|---|---|
| 1 | `01-economy.json`, id `economy` | `ec` | Inflation & the Economy | How inflation is measured (CPI), what $100 buys over time (math), wages vs. prices, recessions and what they mean for jobs, unemployment rate, protecting your plan in a downturn (call), reading a simple economic headline (document), Grandpa’s $1 movie ticket (story) |
| 2 | `02-the-fed.json` | `fd` | Interest Rates & the Fed | What the Federal Reserve does, the federal funds rate in plain words, how rate changes reach your savings, loans and mortgages (sort), rates and stock and bond prices, locking a rate vs. waiting (call), a rate-change news story worked through (story) |
| 3 | `03-financial-independence.json` | `fn` | Financial Independence | Savings rate as the big lever (math), the 4% rule of thumb and its limits, your FI number (25× yearly spending), Lean vs. regular FI, Coast FI, what FI looks like for an ordinary income, two paths compared (call), Dana’s 15-year plan (story) |
| 4 | `04-retirement-planning.json` | `rt` | Planning for Retirement | How much you might need, replacing 70–80% of income as a rule of thumb, starting at 25 vs. 35 (math), retirement calculators, account order, catching up later in life, a retirement plan checklist (order), Marcus at 45 (story) |
| 5 | `05-social-security.json` | `so` | Social Security & Medicare | How Social Security is earned (work credits), claiming at 62 vs. full retirement age vs. 70 (math; confirm on ssa.gov), reading a Social Security statement (document), spousal benefits basics, Medicare Parts A, B, D and Advantage (sort; confirm on medicare.gov), enrollment windows, Rita decides when to claim (story) |
| 6 | `06-retirement-income.json` | `ri` | Turning Savings into Income | Withdrawal rates, which accounts to draw from first (a common order), required minimum distributions (confirm the current starting age on irs.gov), sequence-of-returns risk, annuities at a high level, a retirement paycheck plan (allocate), Joe and Ann’s first retired year (story) |
| 7 | `07-estate-planning.json` | `ep` | Estate Planning | Why everyone needs a will, beneficiaries trump wills (true/false), power of attorney and health care directives, trusts at a high level, what probate is, a “where everything is” document (order), estate tax at a high level (confirm this year’s exemption), the Lees update everything after a baby (story) |
| 8 | `08-giving.json` | `gv` | Giving & Philanthropy | Giving within a budget (allocate), choosing charities (checking a charity), tax deductions for giving (confirm current rules), donor-advised funds at a high level, giving time vs. money, giving to family (call), Priya’s giving plan (story) |
| 9 | `09-advisors.json` | `ad` | Working with Advisors | Do you need an advisor? (call), fiduciary vs. salesperson, fee-only vs. commission (math on a 1% fee over 30 years), robo-advisors, checking an advisor (FINRA BrokerCheck), red flags (spot on a pitch), questions to ask (order), Omar interviews two advisors (story) |
| 10 | `10-money-plan.json` | `mp` | Your Money Plan | A capstone that puts the whole course on one page: income, budget, safety net, debt plan, insurance, investing, goals (allocate and order), a yearly money checkup, adjusting for life changes, “you’re the Alpha now” (story), a final mixed review |

**Also:** once the course is complete, retune the rank thresholds in `wealthwolf/src/lib/ranks.js` so that Alpha lands near the end of the course. Each section pays roughly 1,200–1,500 XP. Update the rank descriptions in `RANK_SKILLS` in `src/screens/Landing.jsx` if they no longer match.

**Facts to confirm before using:** Social Security claiming ages and rules, Medicare enrollment periods, the age required minimum distributions start, and this year’s estate tax exemption. Label each with its year.

**Done when:**
- `npm run check` shows the section with 10 units, each with 8 lessons, and reports no problems.
- `npm run build` passes.
- Every new lesson plays correctly in `npm run dev:unlocked`, including the Section Trial.
