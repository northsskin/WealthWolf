# Prompt: build Section 3, Credit & Debt

Paste everything below the line into Cursor (Agent mode).

---

Build **Section 3: Credit & Debt** of the Wealthwolf course in this repo. First read `docs/CONTENT_GUIDE.md` and follow it exactly. Then study `wealthwolf/scripts/content-gen/e01_paycheck.py`, `u05_fees.py` and the JSON they produce, and match their structure, tone and quality.

**This section already exists in a small form.** `wealthwolf/src/data/credit-debt/01-debt-credit.json` holds one early unit with 4 lessons (`dc-good-bad-debt`, `dc-apr`, `dc-avalanche-snowball`, `dc-credit-score`), plus `dc-review` and `dc-trial`. It also defines the words debt, loan, credit-card, good-debt, bad-debt, mortgage, apr, balance, minimum-payment, avalanche-method, snowball-method, credit-score, credit-limit and credit-utilization.
- Keep every existing lesson id.
- Move `dc-apr`, `dc-credit-score` and `dc-avalanche-snowball` into the units listed below. Move their word definitions along with them if you like, as long as each word is defined exactly once.
- `mortgage` is taught in Section 5 later. Leave its definition where it is and don't use it here.

**Section entry.** In `src/data/sections.json`, the `credit-debt` entry already exists with order 3. Give it:
- the description "Borrowing, credit scores and getting out of debt, without getting eaten alive."
- a trial: `{ "id": "cd-section-trial", "title": "Section Trial: Credit & Debt", "summary": "Twelve questions from the whole section. Three strikes and you’re out.", "xp": 50, "draw": 12 }`

**What learners already know.** Section 1 taught budgeting, banking, overdrafts, and debit vs. credit cards (the word `credit-card` is first taught there). Section 2 taught paychecks and the word `inflation`. Build on these, don't re-teach them.

**Units.** Scripts are named `c01_….py` to `c11_….py`. Each unit has 8 lessons, plus a review and a unit trial.

| # | File and unit id | Prefix | Title | Lesson ideas (mix the formats) |
|---|---|---|---|---|
| 1 | `01-debt-credit.json`, id `debt-credit` | `dc` | Borrowing Basics | Keep `dc-good-bad-debt`. Add: what borrowing costs, principal vs. interest, secured vs. unsecured, a loan agreement (document), "can I afford this payment?" (call), co-signing risks, Leo’s first loan (story) |
| 2 | `02-interest-apr.json` | `ia` | Interest & APR | Move `dc-apr` in. Add: simple interest math, how interest builds month to month, APR vs. APY, comparing two loan offers (call, two docs), total cost of a loan, fees hidden in APR, Maya’s phone financing (story) |
| 3 | `03-credit-scores.json` | `cs` | Credit Scores | Move `dc-credit-score` in. Add: the five factors and their weights, payment history, utilization math, length of history, new credit and hard inquiries, building credit from zero (secured card, credit-builder loan), myths (sort) |
| 4 | `04-credit-reports.json` | `cr` | Credit Reports | Report vs. score, the three bureaus, free reports at AnnualCreditReport.com, reading a report (document), spot an account that isn’t yours (spot), disputing an error, freezing your credit, how long negative marks stay |
| 5 | `05-credit-cards.json` | `cc` | Credit Cards | Reading a card statement (document): statement balance, minimum payment, due date. Grace period, paying in full vs. minimum (math), how the minimum traps you, credit limit and utilization, cash advances, picking a first card (call) |
| 6 | `06-card-traps.json` | `ct` | Card Rewards & Traps | Cashback math, points vs. cash, rewards that cost more than they earn, annual fees (call), 0% intro APR and what happens after, balance transfers and their fees, store cards, Jay’s rewards chase (story) |
| 7 | `07-student-loans.json` | `sl` | Student Loans | Federal vs. private, subsidized vs. unsubsidized, interest while in school, grace period, repayment plans (standard vs. income-driven), reading a loan summary (document), forgiveness basics (verify current programs on studentaid.gov), choosing a school with cost in mind (call) |
| 8 | `08-car-loans.json` | `cl` | Car Loans & Leases | Total cost of a car, loan length vs. total interest (call), down payment, buy vs. lease, dealer add-ons (spot on a buyer’s order), being upside down (owing more than the car is worth), refinancing, Sofia buys a used car (story) |
| 9 | `09-debt-payoff.json` | `dp` | Getting Out of Debt | Move `dc-avalanche-snowball` in. Add: listing every debt (document), the minimum-payment trap, consolidation loans, negotiating a lower rate, a debt payoff plan (allocate), staying motivated, Ray’s $9,000 climb (story) |
| 10 | `10-lending-traps.json` | `lt` | Payday Loans, BNPL & Other Traps | Payday loan math (a $15 fee on $100 for two weeks as an APR), rent-to-own, title loans, buy now pay later and missed payments, “no credit check” offers, spot the trap in an ad (spot), better options when you’re short, Dev’s BNPL pile-up (story) |
| 11 | `11-collections.json` | `cb` | Collections & Bankruptcy | Charge-offs and collections, your rights (debt collectors can’t harass you), validation letters, statute of limitations basics, settling a debt (call), bankruptcy at a high level (Chapter 7 vs. 13) and its costs, rebuilding afterwards |

**Facts to confirm before using:** how long late payments and bankruptcies stay on a report, current federal student loan repayment plans, and that free weekly credit reports are still offered. Label anything time-sensitive with its year.

**Done when:**
- `npm run check` shows Section 3 with 11 units, each with 8 lessons, and reports no problems.
- `npm run build` passes.
- Every new lesson plays correctly in `npm run dev:unlocked`, including the Section Trial.
