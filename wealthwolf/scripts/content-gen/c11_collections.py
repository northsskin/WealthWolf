from lib import *

S = 'credit-debt'
terms = {
    'charge-off': term('Charge-off', 'When a lender gives up on collecting and writes the debt off, often after about 180 days late. You still owe it, and it can still go to a collector.',
                       'A card charged off at $900 is not forgiven. The $900 can be sold to a collector.'),
    'debt-validation': term('Debt validation', 'Your written request that a collector prove you owe the debt, and say who the original lender was, before you pay.',
                            'You do not recognize a $740 letter. You write back and ask for validation. You do not send money first.'),
    'bankruptcy': term('Bankruptcy', 'A court process for debts you cannot pay. Chapter 7 can wipe many unsecured debts and stays on a credit report for up to 10 years. Chapter 13 is a payment plan, often 3 to 5 years, and stays for about 7 years.',
                       'Chapter 7 is not free, and most student loans usually are not wiped. It is a last resort, not a first call.'),
}

charge = lesson('cb-chargeoff', 'Charge-Offs', 'Written off is not the same as forgiven.', [
    mc('What is a charge-off?',
       ['The lender writes the debt off as a loss, often around 180 days late', 'The debt is forgiven', 'The balance becomes a reward'], 0,
       'They stopped hoping. You did not stop owing.',
       context='A [[charge-off]] usually happens after many months late, often about 180 days. The lender may sell the debt. It can sit on your [[credit report]] for about seven years. Paying it later does not erase that clock.'),
    tf('A charged-off debt is forgiven and you can ignore letters about it.', False,
       'You still owe it. A collector may own it now.'),
    num('The card charged off at $900. A collector says you owe $900 plus $40 of fees they added. If the $40 is allowed, what is the ask?', 940,
        '$900 + $40 = $940. Ask them to prove both numbers before you pay.'),
    mc('Does paying a charge-off delete it from the report the same week?',
       ['No. The mark can remain for about seven years, though the status can update to paid', 'Yes. Payment rewinds the clock to zero', 'Yes, if you pay in cash'], 0,
       'Paid is better than unpaid. It is not the same as gone.'),
    mc('About how many days late is a common charge-off point?', ['About 180', 'About 3', 'About 3,000'], 0, 'Around six months past due.'),
    fill('A charge-off means the lender wrote the debt off. You ___ still owe it.', ['do', 'do not', 'might never'], 0, 'Wrote off is an accounting step. The debt remains.'),
])

rights = lesson('cb-rights', 'What Collectors Cannot Do', 'They can ask for the money. They cannot threaten jail over a credit card.', [
    sort('Allowed, or not allowed?', ['Allowed', 'Not allowed'], [
        ('Send a letter about a debt you owe', 0),
        ('Call you at a reasonable hour', 0),
        ('Sue you, if the law and the facts allow it', 0),
        ('Threaten you with arrest over a credit-card bill', 1),
        ('Call you at 3 a.m.', 1),
        ('Lie about how much you owe', 1),
    ], context='Under the Fair Debt Collection Practices Act, collectors cannot harass you, call before 8 a.m. or after 9 p.m., or threaten jail for an ordinary consumer debt. They can still contact you, and they can still sue.'),
    tf('A collector can have you arrested for an unpaid credit-card bill.', False,
       'Ordinary consumer debt is not a crime. A threat of arrest is a tactic.'),
    mc('What time of day is off limits for collector calls?',
       ['Before 8 a.m. and after 9 p.m.', 'Only Sundays', 'There is no limit'], 0,
       'Those are the federal edges.'),
    mc('They keep calling after you ask them, in writing, to stop calling. What can you do?',
       ['Tell them in writing to stop, and report the harassment', 'Pay so they will be nice', 'Ignore the law. They are allowed to harass'], 0,
       'A written request to stop calls is a real tool. It does not erase the debt.'),
    tf('“We will sue” is always a lie.', False,
       'Sometimes they can sue. Sometimes it is a bluff. Validation and the dates tell you more than the tone.'),
    mc('Who enforces these rules?',
       ['The Consumer Financial Protection Bureau and the FTC, among others', 'The card’s rewards program', 'Nobody'], 0,
       'Report abuse. Do not debate it on the phone at 3 a.m.'),
], fmt='sort')

letter_lines = [('bal', 'Amount the letter says you owe', 740)]
LETTER = doc('bill', 'Collection letter', letter_lines, subtitle='You do not recognize this account',
             meta=[['They say it is from', 'Harbor Card']],
             totals=[('They want', 740, True)],
             note='Do not pay until they validate the debt in writing.')
valid = lesson('cb-validation', 'Make Them Prove It', 'A letter is a claim. Proof is separate.', [
    mc('What is debt validation?',
       ['A written demand that the collector prove you owe the debt', 'Paying the letter the day it arrives', 'A credit freeze'], 0,
       'Proof first. Money second.',
       context='[[Debt validation]] means you write to the collector and ask them to prove the debt: the amount, and the original creditor. Do it in writing. Keep a copy. This is different from a [[dispute]] with your bank about a charge on your statement.'),
    num('The letter asks for $740. You recognize $500 of an old card and not the other $240. How much is unexplained?', 240,
        '$740 − $500 = $240.', doc=LETTER),
    mc('What do you send before any money?',
       ['A written validation request', 'The full $740 in cash', 'Your card number by text'], 0,
       'Pay what you owe after you know the number is real.'),
    tf('You should give a collector your bank login so they can “look it up.”', False,
       'Never. They can send proof on paper.'),
    order('Put a strange collection letter in order.',
          ['Read the amount and the original creditor', 'Check your own records', 'Write for validation if it is unclear', 'Pay only what the proof supports'],
          'Read, check, ask, then pay what is real.'),
    mc('They never send proof. What do you not do?',
       ['Pay the full letter just to make it stop', 'Keep your copy of the request', 'Watch your credit reports'], 0,
       'An unproven demand is not a bill you have confirmed.'),
], fmt='document')

sol = lesson('cb-time-limit', 'Time Limits', 'The right to sue is not the same in every state. The report has its own clock.', [
    info('Two different clocks',
         'A statute of limitations is the time a collector has to sue you. It depends on your state and the kind of debt. Nobody on the phone gets to invent it.\n\n'
         'Separately, most negative marks stay on a [[credit report]] for about seven years. A debt can be too old to sue over and still be on the report. Paying, or even promising to pay, can restart the lawsuit clock in some states. Get advice before you send money on a very old debt.'),
    mc('What does a statute of limitations limit?',
       ['How long they can sue you, under your state’s rules', 'How long the debt can appear on a credit report, nationwide, in every case', 'How long a charge-off takes to happen'], 0,
       'Lawsuit clock and report clock are different.'),
    tf('After the lawsuit time limit passes, the debt always vanishes from your credit report the same day.', False,
       'The report can keep a negative mark for about seven years even when a lawsuit is no longer available.'),
    mc('A caller says “your state limit is 90 days, so pay today.” What is wrong with trusting that?',
       ['They are not your lawyer, and the limit depends on the state and the debt', 'Nothing. Callers know your statute', 'Time limits are the same everywhere: 90 days'], 0,
       'Look it up, or ask a legal-aid office. Do not take the collector’s word for the clock.'),
    mc('Why be careful about sending a small “good faith” payment on a very old debt?',
       ['In some states it can restart the time they have to sue', 'It deletes the report', 'It is required by federal law'], 0,
       'A friendly payment can have a legal side effect.'),
    fill('The time they have to sue is set by your ___, not by the collector’s script.', ['state', 'mood', 'credit score'], 0, 'State law. Confirm it.'),
])

settle_a = [
    ('pay', 'Pay in full', 1200),
]
settle_b = [
    ('pay', 'Settle for', 700),
]
assert 1200 - 700 == 500
FULL = doc('statement', 'Pay in full', settle_a, totals=[('You pay', 1200, True)])
SETTLE = doc('statement', 'Settlement offer', settle_b, subtitle='Get the deal in writing before you pay',
             totals=[('You pay', 700, True)],
             note='The unpaid $500 can count as taxable income. Ask a tax preparer or check irs.gov for the current year.')
settle = lesson('cb-settle', 'Settling', 'Less than the full balance, in writing, with the tax question asked.', [
    num('They will take $700 on a $1,200 debt. How much less is that than paying in full?', 500, '$1,200 − $700 = $500.',
        context='Settling means the collector accepts less than the full [[balance]] and closes the account. Get the agreement in writing before you pay. The forgiven part can be taxable. Check irs.gov or a tax preparer for the year you settle.',
        docs=[FULL, SETTLE]),
    mc('What do you need before you send the $700?',
       ['A written agreement that $700 settles the debt', 'A verbal “sure” on the phone', 'A new loan to pay the settlement'], 0,
       'If it is not in writing, you may still owe the rest.'),
    tf('The $500 they forgive can sometimes count as taxable income.', True,
       'Canceled debt often shows up at tax time. Confirm the current rule.'),
    mc('Settling versus paying $1,200 in full. What is the trade?',
       ['You save $500 and you may owe tax on the forgiven part, and the report may say “settled” rather than “paid in full”', 'Settling deletes the history', 'They are identical on your report'], 0,
       'Cheaper cash now, a different mark, and a possible tax form.'),
    num('If you settle five debts the same way, each $500 below the balance, how much was forgiven in total?', 2500,
        '$500 × 5 = $2,500. That is the figure to ask a tax preparer about.'),
    mc('You do not have the $700. What is a settlement not?',
       ['A reason to take a payday loan', 'Something you can postpone until you have the money', 'A deal that must be in writing'], 0,
       'Borrowing at 390% to settle a debt recreates the problem.'),
], fmt='call')

bank = lesson('cb-bankruptcy', 'Bankruptcy, at a High Level', 'A court, a cost, and a mark that lasts years. Not a coupon.', [
    mc('What is Chapter 7, in plain terms?',
       ['A court process that can wipe many unsecured debts, and can stay on your report for up to 10 years', 'A payment plan of 3 to 5 years', 'A way to raise your credit score next month'], 0,
       'Wipe, with rules, and a long mark.',
       context='[[Bankruptcy]] is a court process. Chapter 7 can discharge many unsecured debts and can stay on a [[credit report]] for up to 10 years. Chapter 13 is a court payment plan, often 3 to 5 years, and the mark is about 7 years. Most student loans are usually not wiped. There are court costs and, often, a lawyer.'),
    mc('What is Chapter 13?',
       ['A court-supervised payment plan, often 3 to 5 years', 'A one-day erasure of every debt including student loans', 'The same thing as a credit freeze'], 0,
       'You pay into a plan. The mark is about 7 years.'),
    tf('Bankruptcy is free and wipes student loans in a typical case.', False,
       'It costs money to file, and most student loans usually stay.'),
    mc('How long can a Chapter 7 bankruptcy stay on a credit report?', ['Up to 10 years', '10 weeks', 'Until you ask nicely'], 0,
       'Up to 10 years.'),
    mc('How long is a Chapter 13 mark, in the usual case?', ['About 7 years', 'About 7 weeks', 'Forever'], 0,
       'About 7 years from filing.'),
    mc('When is it worth a serious look?',
       ['When you cannot pay, the calls and lawsuits are real, and a nonprofit credit counselor or legal aid has walked through the options with you', 'The first month you carry a card balance', 'To get a higher credit-card limit'], 0,
       'Last resort. Real advice, not a TikTok.'),
])

chris_story = {
    'title': 'The letter',
    'character': 'Chris, 41, home health aide',
    'body': 'Chris gets a letter demanding **$860**. He recognizes an old medical bill of about **$640**. He does not recognize the other **$220**, and he does not remember a card called Northline.\n\n'
            'The letter says he will be sued on Friday. It arrived on Wednesday. He has **$200** in savings.',
}
assert 860 - 640 == 220
chris = lesson('cb-chris', 'Chris Gets a Letter', 'Prove the strange part. Do not empty the savings on a two-day threat.', [
    num('How much of the $860 does Chris not recognize?', 220, '$860 − $640 = $220.'),
    mc('What does he do before paying anything?',
       ['Write for validation of the whole $860, and check his records on the $640', 'Pay $860 from a payday loan', 'Ignore a real $640 he knows about forever'], 0,
       'The known bill and the mystery $220 are not the same decision.'),
    tf('“We will sue on Friday” on a Wednesday letter is a reason to skip validation and pay in a panic.', False,
       'A two-day threat is pressure. Proof still comes first.'),
    mc('His $200 in savings is also his emergency buffer. What should it not become?',
       ['A payday-loan down payment', 'Money he keeps while he asks for proof', 'Untouched until he knows the debt'], 0,
       'Do not turn a letter into a worse debt.'),
    num('If validation shows he owes only the $640, how much was the letter overstating?', 220, '$860 − $640 = $220.'),
    mc('After the real amount is proven, what is a sane way to handle the $640?',
       ['A payment plan he can afford, in writing', 'A title loan', 'No response, ever, including to a lawsuit'], 0,
       'A real debt gets a real plan. A lawsuit, if one actually arrives, needs a response.'),
], fmt='story', story=chris_story)

rebuild = lesson('cb-rebuild', 'Afterward', 'The mark ages. New on-time payments are the record you can still write.', [
    mc('A charge-off or a bankruptcy is on the report. What still helps?',
       ['On-time payments on the accounts you have now', 'Opening five cards this week', 'Never looking at the report again'], 0,
       'The old mark ages. The new history is what you add.',
       context='Rebuilding is slow on purpose. Pay the bills you have, keep utilization low, and a [[secured card]] can start a fresh on-time record. The old mark falls off on its own clock. You do not pay a company that promises to delete accurate negative marks.'),
    tf('A company that promises to erase accurate late payments from your report is offering a normal, legal service.', False,
       'Accurate marks come off when the clock runs out. Pay for a lie and you often pay twice.'),
    mc('Which new account fits a rebuild?',
       ['A secured card, used little and paid in full', 'A payday loan', 'Three store cards on the same day'], 0,
       'Small, secured, and boring.'),
    num('A Chapter 7 was filed in 2020. The 10-year mark runs to about what year?', 2030, '2020 + 10 = 2030.', unit=None),
    mc('While you wait, what do you check?',
       ['All three credit reports, for errors and for accounts that are not yours', 'Nothing', 'Only the ads'], 0,
       'The file can still be wrong. Wrong is worth a dispute.'),
    fill('Accurate negative marks come off when the ___ runs out, not when a stranger promises.', ['clock', 'sale', 'reward'], 0,
         'Seven years for most marks. Up to ten for Chapter 7.'),
])

trial_steps = [
    tf('A charge-off means the debt is forgiven.', False, 'It was written off. You can still owe it.'),
    mc('A collector threatens jail over a credit-card bill. That threat is…',
       ['Not allowed', 'Required by law', 'A sign you should pay in cash tonight'], 0,
       'Ordinary consumer debt is not a reason to threaten arrest.'),
    mc('Chapter 7 can stay on a credit report for up to how long?', ['10 years', '10 days', 'One billing cycle'], 0,
       'Up to 10 years.'),
    num('A collector will settle $2,000 for $1,250. How much less is that than the full balance?', 750,
        '$2,000 − $1,250 = $750.'),
]

lessons = [charge, rights, valid, sol, settle, bank, chris, rebuild,
           review('cb'), trial('cb', 'Collections & Bankruptcy', trial_steps)]
write_unit('11-collections.json', 'collections', 11, 'Collections & Bankruptcy',
           'Charge-offs, your rights, settlements, and what bankruptcy actually is.',
           'A letter is not a verdict. Make them prove the debt.', terms, lessons, section=S)
