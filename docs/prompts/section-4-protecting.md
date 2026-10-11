# Prompt: build Section 4, Protecting What You Have

Paste everything below the line into Cursor (Agent mode).

---

Build **Section 4: Protecting What You Have** of the Wealthwolf course in this repo. First read `docs/CONTENT_GUIDE.md` and follow it exactly. Then study `wealthwolf/scripts/content-gen/e01_paycheck.py`, `u05_fees.py` and the JSON they produce, and match their structure, tone and quality.

**Section entry.** Add this to `src/data/sections.json` (keep the array sorted by `order`):
```json
{ "id": "protecting", "order": 4, "title": "Protecting What You Have",
  "description": "Scams, identity theft and insurance: keep one bad day from undoing years of work.",
  "trial": { "id": "pr-section-trial", "title": "Section Trial: Protecting What You Have",
             "summary": "Twelve questions from the whole section. Three strikes and you’re out.", "xp": 50, "draw": 12 } }
```
Put the units in `src/data/protecting/`. Scripts are named `p01_….py` to `p09_….py`.

**What learners already know.** Don't re-teach these; link the existing words with `[[...]]`:
- Section 1 covered account safety (passwords, two-factor authentication, alerts) and payment-app scams.
- Section 2 covered job scams, the word `premium`, COBRA and Medicaid.
- Section 3 covered credit reports and credit freezes.

**Units.** Each unit has 8 lessons, plus a review and a unit trial.

| # | File and unit id | Prefix | Title | Lesson ideas (mix the formats) |
|---|---|---|---|---|
| 1 | `01-scams.json`, id `scams` | `sc` | Scams & Fraud | How scams work (urgency, authority, secrecy), phishing emails and texts, spot the fake in a message (spot), impostor calls (“IRS”, “your bank”, “grandchild in trouble”), romance and investment scams, gift-card and wire red flags (sort), what to do in the first hour, Rosa’s fake delivery text (story) |
| 2 | `02-identity-theft.json` | `it` | Identity Theft | What thieves want (Social Security number, logins), how it happens, warning signs (spot on a statement), freezing your credit at all three bureaus, IdentityTheft.gov recovery steps (order), protecting mail and documents, tax identity theft, Marcus finds an account he never opened (story) |
| 3 | `03-insurance-basics.json` | `ib` | Insurance Basics | What insurance is (pooling risk), premium vs. deductible vs. coverage limit, reading a policy summary (document), higher deductible vs. lower premium (call), what to insure (big losses you couldn’t cover) vs. skip (sort), exclusions, filing a claim (order), claims and your rates |
| 4 | `04-auto-insurance.json` | `ai` | Auto Insurance | Liability vs. collision vs. comprehensive (sort), state minimums vs. enough coverage, uninsured motorist coverage, what changes your price, comparing two quotes (call), after an accident (order), reading a declarations page (document), Theo’s fender-bender (story) |
| 5 | `05-home-insurance.json` | `hi` | Renters & Home Insurance | Why renters need it (the landlord’s policy doesn’t cover your stuff), what it covers: belongings, liability, hotel costs. Actual cash value vs. replacement cost (math), home insurance basics, floods and earthquakes aren’t included, a home inventory, Priya’s apartment fire (story) |
| 6 | `06-health-insurance.json` | `hl` | Health Insurance | Premium, deductible, copay, coinsurance, out-of-pocket maximum (each taught, then the math of one ER visit), in- vs. out-of-network, HMO vs. PPO (sort), choosing between two plans for your situation (call), open enrollment and special enrollment, Marketplace plans and income-based discounts |
| 7 | `07-medical-bills.json` | `mb` | Medical Bills, HSAs & FSAs | Reading an Explanation of Benefits (document), checking a bill against it (spot a double charge), asking for an itemized bill, negotiating and payment plans, financial assistance at hospitals, HSA vs. FSA (sort; confirm this year’s limits on irs.gov), HSA tax advantages, Jordan’s $3,200 surprise bill (story) |
| 8 | `08-life-insurance.json` | `li` | Life Insurance | Who needs it (people who depend on your income), term vs. whole life (call), how much (a simple income-replacement estimate), beneficiaries, coverage through work and its limits, why most people choose term, Aisha and her new baby (story) |
| 9 | `09-disability-umbrella.json` | `du` | Disability & Umbrella Coverage | Disability insurance as income insurance, short- vs. long-term, coverage through work, how much it pays (math), umbrella liability coverage and who needs it, building an insurance checklist (sort), reviewing coverage each year, putting it together (call) |

**Facts to confirm before using:** this year’s HSA and FSA contribution limits (irs.gov), and current health insurance enrollment rules (healthcare.gov). Label them with the year.

**Done when:**
- `npm run check` shows the section with 9 units, each with 8 lessons, and reports no problems.
- `npm run build` passes.
- Every new lesson plays correctly in `npm run dev:unlocked`, including the Section Trial.

It appears as Section 4 once Section 3 is in place. Until then the app numbers it by position.
