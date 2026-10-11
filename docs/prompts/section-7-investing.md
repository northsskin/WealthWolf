# Prompt: build Section 7, Investing

Paste everything below the line into Cursor (Agent mode).

---

Build **Section 7: Investing** of the Wealthwolf course in this repo. First read `docs/CONTENT_GUIDE.md` and follow it exactly. Then study `wealthwolf/scripts/content-gen/e01_paycheck.py`, `u05_fees.py` and the JSON they produce, and match their structure, tone and quality.

**This section already exists in a small form.** `wealthwolf/src/data/investing/01-investing.json` holds one early unit with:
- 4 lessons: `iv-compound`, `iv-stocks-bonds`, `iv-index-funds`, `iv-diversification`
- the Portfolio Simulator placeholder `iv-sim` (`type: "sim"`, not built yet)
- `iv-review` and `iv-trial`

It also defines the words investing, return, compound-growth, rule-of-72, stock, bond, risk, dividend, portfolio, fund, index, index-fund, expense-ratio, diversification and concentration-risk.
- Keep every existing lesson id.
- Move `iv-index-funds`, `iv-diversification` and `iv-sim` into the units listed below. `iv-sim` must stay `type: "sim"` with no steps; copy its dict as it is.
- Each word is defined exactly once. Move a definition with its lesson if you like.

**Section entry.** The `investing` entry in `src/data/sections.json` already exists with order 7. Give it:
- the description "Make your money work while you sleep: stocks, funds, retirement accounts and keeping your nerve."
- a trial: `{ "id": "inv-section-trial", "title": "Section Trial: Investing", "summary": "Twelve questions from the whole section. Three strikes and you’re out.", "xp": 50, "draw": 12 }`

**What learners already know.** Don't redefine these words; link them with `[[...]]` and go deeper:
- Section 1: saving and APY.
- Section 2: the words `401k`, `employer-match`, `vesting`, `rollover`, `inflation`.
- Section 6: capital gains and tax-advantaged accounts.

**Units.** Scripts are named `i01_….py` to `i12_….py`. Each unit has 8 lessons, plus a review and a unit trial.

| # | File and unit id | Prefix | Title | Lesson ideas (mix the formats) |
|---|---|---|---|---|
| 1 | `01-investing.json`, id `investing` | `iv` | Investing Basics | Keep `iv-compound` and `iv-stocks-bonds`. Add: saving vs. investing (call), risk and return, time in the market, the cost of waiting 10 years (math), emergency fund first, Lily starts with $50 a month (story) |
| 2 | `02-stock-market.json` | `sk` | The Stock Market | What a share is, exchanges and tickers, why prices move, market cap, P/E at a beginner level, reading a stock quote (document), dividends and dividend yield (math), individual stocks vs. the whole market (call) |
| 3 | `03-bonds-rates.json` | `bd` | Bonds & Interest Rates | How a bond works (coupon, maturity), Treasuries vs. corporate bonds, why bond prices fall when rates rise, CDs and I bonds (confirm current I bond rules on TreasuryDirect), yield (math), the role of bonds in a portfolio, comparing a CD and a Treasury (call) |
| 4 | `04-funds-etfs.json` | `fe` | Funds, ETFs & Index Investing | Move `iv-index-funds` in. Add: mutual fund vs. ETF (sort), active vs. passive, expense ratios over 30 years (math), reading a fund fact sheet (document), target-date funds, spot the high-fee fund (spot), Omar picks his first fund (story) |
| 5 | `05-allocation.json` | `aa` | Diversification & Asset Allocation | Move `iv-diversification` in. Add: asset allocation by time horizon, stocks/bonds mixes and their swings, rebalancing (math), international diversification, risk tolerance (a quiz-style sort), choosing a mix for a goal (call), Ben’s lopsided portfolio (spot) |
| 6 | `06-workplace-retirement.json` | `wr` | 401(k)s & the Employer Match | Choosing a contribution rate, traditional vs. Roth 401(k) (call), picking funds from a plan menu (document), auto-escalation, this year’s limits and catch-up contributions (confirm on irs.gov), loans from a 401(k) and their risks, Jamie raises their rate 1% a year (story; Jamie is from Section 2) |
| 7 | `07-iras.json` | `ir` | IRAs: Roth vs. Traditional | What an IRA is, Roth vs. traditional (call), income limits and contribution limits (confirm), opening one (order), 401(k) + IRA together, the backdoor Roth at a high level only, early withdrawal rules for Roth contributions, Maya opens a Roth at 22 (story) |
| 8 | `08-brokerage.json` | `br` | Brokerage Accounts & Placing Trades | Opening a brokerage account, cash vs. margin (avoid margin), market vs. limit orders (call), fractional shares, reading a trade confirmation (document), SIPC protection, fees to watch (spot), automatic investing (dollar-cost averaging, math) |
| 9 | `09-investor-psychology.json` | `ip` | Investor Psychology | Panic selling in a crash (with a real historical drop and recovery), timing the market, FOMO and hype, recency bias, survivorship bias, checking your account too often, writing your own rules (order), Ray sells at the bottom (story) |
| 10 | `10-real-estate-investing.json` | `re` | Real Estate Investing | REITs vs. owning a rental (call), rental math: rent − costs = cash flow, cap rate (math), vacancy and repairs, being a landlord (the work involved), house hacking, leverage cuts both ways, Sofia runs the numbers on a duplex (story) |
| 11 | `11-crypto.json` | `cy` | Crypto & Speculation | What crypto is, volatility (math on a 60% drop), scams and rug pulls (spot), exchanges and custody, speculation vs. investing (sort), how much is too much (a small slice you can afford to lose), meme stocks and options as gambling, Kai’s crypto lesson (story) |
| 12 | `12-portfolio.json` | `pf` | Building Your Portfolio | Move `iv-sim` in (it stays a placeholder). Add: a three-fund portfolio, putting it all together by age and goal (allocate), costs check (spot), automating it (order), when to change your plan (call), staying the course, Morgan builds a plan (story; Morgan is from Section 1) |

**Facts to confirm before using:** this year’s 401(k) and IRA limits, Roth income limits, and I bond rules. Use real historical market events correctly. Never suggest specific stocks or promise returns: use “historically, on average” language.

**Done when:**
- `npm run check` shows the section with 12 units, each with 8 lessons, and reports no problems.
- `npm run build` passes.
- Every new lesson plays correctly in `npm run dev:unlocked`, including the Section Trial.
