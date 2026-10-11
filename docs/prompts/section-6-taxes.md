# Prompt: build Section 6, Taxes

Paste everything below the line into Cursor (Agent mode).

---

Build **Section 6: Taxes** of the Wealthwolf course in this repo. First read `docs/CONTENT_GUIDE.md` and follow it exactly. Then study `wealthwolf/scripts/content-gen/e01_paycheck.py`, `u05_fees.py` and the JSON they produce, and match their structure, tone and quality.

**Section entry.** Add this to `src/data/sections.json` (keep the array sorted by `order`):
```json
{ "id": "taxes", "order": 6, "title": "Taxes",
  "description": "How income tax really works, how to file, and how to legally keep more of your money.",
  "trial": { "id": "tx-section-trial", "title": "Section Trial: Taxes",
             "summary": "Twelve questions from the whole section. Three strikes and you’re out.", "xp": 50, "draw": 12 } }
```
Put the units in `src/data/taxes/`. Scripts are named `t01_….py` to `t08_….py`.

**What learners already know.** Don't redefine these words; link them with `[[...]]`:
- From Section 2: `fica`, `w-2`, `pre-tax-deduction`, `form-1099`, `estimated-taxes`, `business-expense`, `401k`, the gig-tax rule of thumb, and quarterly due dates.
- From Section 1: `sales-tax`.

Go deeper, don't repeat.

**Accuracy matters most in this section.** Use the IRS figures for the tax year you’re writing about (tax year 2026, filed in 2027, unless those aren’t published yet; then use the latest published year). Look every number up on irs.gov: brackets, standard deduction, credit amounts, contribution limits. Label each one with its year, for example “(2026 standard deduction, single)”. Keep worked examples simple: a single filer, W-2 income, the standard deduction. Where a rule has many exceptions, say “usually” and keep to the common case. This is education, not tax advice: add one line in the first unit saying that, and pointing to IRS Free File and VITA for free help.

**Units.** Each unit has 8 lessons, plus a review and a unit trial.

| # | File and unit id | Prefix | Title | Lesson ideas (mix the formats) |
|---|---|---|---|---|
| 1 | `01-income-tax.json`, id `income-tax` | `tx` | How Income Tax Works | Gross income → adjusted gross income → taxable income (order), the standard deduction, tax brackets as buckets, marginal vs. effective rate (math), “a raise can’t make you take home less” (true/false myth), federal vs. state vs. FICA (sort), Ana’s first tax bill worked out step by step (story) |
| 2 | `02-withholding.json` | `wh` | Withholding & the W-4 | What withholding is, the W-4 form and when to update it, refund vs. owing (it’s your money either way), the IRS withholding estimator, two jobs and withholding, reading a W-4 (document), a too-big refund as a 0% loan to the government (call), Chris has two jobs (story) |
| 3 | `03-filing.json` | `fi` | Filing Your Return | Who must file, filing deadlines and extensions (an extension to file isn’t an extension to pay), the documents you need (sort), filing status, IRS Free File and VITA vs. paid software vs. a preparer (call), reading a simplified Form 1040 (document), e-file and direct deposit, fixing a mistake (amended return) |
| 4 | `04-deductions-credits.json` | `dd` | Deductions & Credits | Deduction vs. credit (worth comparing with math), standard vs. itemized (call), common credits: Earned Income Tax Credit, Child Tax Credit, education credits (confirm amounts), refundable vs. nonrefundable, deductions you can take without itemizing, Jamal checks if he qualifies for the EITC (story) |
| 5 | `05-self-employment-tax.json` | `se` | Self-Employment Taxes | Self-employment tax (both halves of FICA, 15.3% on 92.35% of net), Schedule C at a high level (document), business expenses and the home office basics, mileage (confirm the current IRS rate), quarterly estimates and safe harbor basics, keeping records (sort), Rosa’s second freelance year (story) |
| 6 | `06-investment-taxes.json` | `vt` | Taxes on Investments | Capital gains, short- vs. long-term (math), dividends, cost basis, tax-loss harvesting basics, why holding over a year matters (call), interest income from savings (1099-INT), reading a brokerage 1099 summary (document) |
| 7 | `07-tax-advantaged.json` | `ta` | Tax-Advantaged Accounts | Traditional vs. Roth: pay tax now or later (call), 401(k) and IRA limits (confirm), HSA triple tax advantage, 529 plans, which account first (a common priority order), early withdrawal penalties, Kim splits $6,000 across accounts (allocate) |
| 8 | `08-state-local-tax.json` | `st` | State & Local Taxes | States with no income tax, flat vs. graduated state tax, local and city income taxes, property tax at a high level, sales tax differences, moving states mid-year, comparing take-home pay in two states (call), Leo’s job offer in another state (story) |

**Done when:**
- `npm run check` shows the section with 8 units, each with 8 lessons, and reports no problems.
- `npm run build` passes.
- Every new lesson plays correctly in `npm run dev:unlocked`, including the Section Trial.
- Every yearly figure carries its year.
