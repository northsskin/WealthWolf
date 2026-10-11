from lib import *

S = 'taxes'
terms = {
    'traditional-ira': term('Traditional IRA',
                            'An individual retirement account. A contribution can be deductible now, and withdrawals in retirement are usually taxed.',
                            'A $2,000 deductible contribution in the 12% bracket saves $240 this year.'),
    'roth-ira': term('Roth IRA',
                     'An individual retirement account you fund with money that has already been taxed. Qualified withdrawals later are tax-free.',
                     'A $2,000 Roth contribution saves $0 of tax this year. The qualified withdrawals are the point.'),
}

trad = doc('statement', 'Traditional IRA', [
    ('put', 'Contribution', 2000),
    ('save', 'Tax saved this year at 12%', 240),
], subtitle='Deductible in this example')
roth = doc('statement', 'Roth IRA', [
    ('put', 'Contribution', 2000),
    ('now', 'Tax already paid on that money, at 12%', 240),
], subtitle='No deduction this year')
assert 2000 * 0.12 == 240

which = lesson('ta-which', 'Now or Later', 'Same $2,000. The tax moves to a different year.', [
    num('A $2,000 deductible traditional contribution is in the 12% bracket. How much tax does it save this year?', 240,
        '$2,000 × 0.12 = $240.',
        context='A [[traditional IRA]] can be a deduction now. A [[Roth IRA]] is funded after tax. Qualified Roth withdrawals later are tax-free. This is the trade, not a personal plan.',
        docs=[trad, roth]),
    mc('Which page buys a deduction this year?',
       ['The traditional IRA', 'The Roth IRA', 'Both'], 0,
       'The traditional page saves $240 now. The Roth page already paid that $240.',
       why=['The $240 is tax saved this year.', 'The Roth contribution is not deductible.', 'Only the traditional page is a deduction.'],
       docs=[trad, roth]),
    mc('Which page is built so a qualified withdrawal later is tax-free?',
       ['The Roth IRA', 'The traditional IRA', 'Neither. Both are taxed again later'], 0,
       'That is the Roth bargain. Traditional withdrawals are usually taxed later.'),
    tf('The Roth contribution in this pair saves $240 of tax this year.', False,
       'The $240 on the Roth page is tax already paid. The traditional page is the one that saves it.'),
    fill('Qualified Roth withdrawals are ___.',
         ['tax-free', 'taxed again', 'a capital loss'], 0,
         'Tax-free, when they are qualified. That is why you paid tax on the way in.'),
], fmt='call')

limits = lesson('ta-limits', '2026 Limits', 'The employee deferral and the IRA cap are different numbers.', [
    info('Label the year',
         'For 2026, the employee [[401(k)|401k]] deferral limit is **$24,500**. The catch-up at age 50 is **$8,000**, so **$32,500**. At ages 60, 61, 62, and 63 the catch-up is **$11,250**, so **$35,750**.\n\nThe IRA limit, traditional and Roth combined, is **$7,500**, plus **$1,100** at age 50, so **$8,600**. The employer match is not part of the $24,500.'),
    num('What is the 2026 employee 401(k) deferral limit, before any catch-up?', 24500,
        '$24,500 for 2026.'),
    num('At age 50, the 401(k) catch-up is $8,000. What is the total you can defer?', 32500,
        '$24,500 + $8,000 = $32,500.'),
    num('What is the 2026 IRA limit before the age-50 catch-up?', 7500,
        '$7,500, shared by traditional and Roth contributions.'),
    num('At age 50, the IRA catch-up is $1,100. What is the total IRA limit?', 8600,
        '$7,500 + $1,100 = $8,600.'),
])

hsa = lesson('ta-hsa', 'The HSA’s Three Tax Breaks', 'In, growth, and qualified money out.', [
    info('Already on the path',
         'An [[HSA|health-savings-account]] can be pre-tax or deductible on the way in, can grow without a yearly tax, and can come out tax-free for qualified medical costs.\n\nFor 2026 the contribution limit is **$4,400** with self-only coverage and **$8,750** with family coverage, plus **$1,000** at age 55. You need a qualifying health plan. This is the same HSA you already met.'),
    num('What is the 2026 HSA limit for self-only coverage, before the age-55 catch-up?', 4400,
        '$4,400.'),
    num('What is the 2026 family HSA limit, before that catch-up?', 8750,
        '$8,750.'),
    num('Age 55 adds $1,000. What is the self-only total then?', 5400,
        '$4,400 + $1,000 = $5,400.'),
    tf('An HSA is the same account as a 529 plan.', False,
       'An HSA is for qualified medical costs. A 529 is for education.'),
])

college = lesson('ta-529', 'A 529, Again', 'Education money. Not a promised return.', [
    info('The tax piece',
         'A [[529 plan]] is still the education account from the family unit. Qualified withdrawals are tax-free at the federal level. The investments inside can fall.\n\n**$150** a month is **$1,800** a year of contributions. That is the part you choose. The balance later is not a rate this course will invent.'),
    num('What is $150 a month for a year?', 1800, '$150 × 12 = $1,800.'),
    mc('What is the federal tax rule this lesson will stand behind?',
       ['Qualified education withdrawals are tax-free', 'The balance rises by a set percent', 'Contributions are always deductible on the federal return'], 0,
       'The qualified withdrawal is the rule. A federal deduction for the contribution is not the promise.'),
    tf('A 529 contribution and an HSA contribution share one 2026 limit.', False,
       'They are different accounts with different limits.'),
    fill('A qualified 529 withdrawal for education is federally ___.',
         ['tax-free', 'taxed as wages', 'a payroll tax'], 0,
         'Tax-free when it is qualified. The investment result is separate.'),
])

order = lesson('ta-order', 'Which Account First', 'A common sketch. Not an order the IRS requires.', [
    info('Match, then the expensive debt, then the HSA',
         'A common order: take the full employer match, pay high-interest debt, fund an [[HSA|health-savings-account]] if you qualify, then an IRA or more of the [[401(k)|401k]].\n\nThe match is a 100% return on the dollars it matches. Skipping it to buy a taxable fund first gives away that match. This is a sketch, not a rule for every household.'),
    order('Put this common sketch in order.',
          ['Take the full employer match',
           'Pay high-interest debt',
           'Fund an HSA if you qualify',
           'Add an IRA or more of the 401(k)'],
          'The match is first because it is extra pay. High-interest debt and a qualifying HSA come before the extra retirement dollars.'),
    mc('The employer matches dollar for dollar up to a cap. What is the cost of not contributing enough to get the full match?',
       ['You leave the match uncollected', 'The IRS fines you the same amount', 'Your standard deduction shrinks'], 0,
       'The match is pay you do not receive. It is not a fine.'),
    tf('This order is required by the tax code.', False,
       'It is a common sketch. A household with no match, or no qualifying health plan, starts in a different place.'),
    fill('The first stop in this sketch is the employer ___.',
         ['match', 'penalty', 'extension'], 0,
         'Match. It is the piece of pay that depends on your contribution.'),
])

early = lesson('ta-early', 'Early Withdrawals', 'Usually a 10% penalty, plus the tax.', [
    info('Before 59½',
         'Money taken from a [[traditional IRA]] or a 401(k) before age **59½** is usually hit with a **10%** penalty, and it is usually taxed as income. Exceptions exist. This lesson stays with the common case.\n\nA **$1,000** early traditional withdrawal has a **$100** penalty. The **$1,000** is also income. Roth contributions, not the earnings, can usually come out without tax or penalty. Do not treat the whole Roth account that way.'),
    num('What is the 10% penalty on a $1,000 early traditional withdrawal?', 100,
        '$1,000 × 0.10 = $100.'),
    num('The $1,000 is also taxed in the 12% bracket. How much income tax does that add, on top of the penalty?', 120,
        '$1,000 × 0.12 = $120. The penalty is separate.'),
    num('What do the $100 penalty and the $120 of income tax cost together?', 220,
        '$100 + $120 = $220. You also no longer have the $1,000 invested.'),
    tf('Roth contributions and Roth earnings follow the exact same early-withdrawal rule.', False,
       'Contributions can usually come out. Earnings have their own rules. The traditional withdrawal is the one with the usual 10% penalty.'),
])

spot_doc = doc('statement', 'Retirement account, March', [
    ('defer', 'Employee 401(k) deferral', 4000),
    ('out', 'Early traditional IRA withdrawal', 1000),
    ('pen', '10% early-withdrawal penalty', 100),
])
assert 1000 * 0.10 == 100

spot = lesson('ta-spot', 'The Withdrawal on the Statement', 'The deferral is the plan. The withdrawal is the leak.', [
    info('Three lines',
         'The **$4,000** deferral is money going in. The **$1,000** line is an early withdrawal from a [[traditional IRA]]. The **$100** is the 10% penalty.\n\nThe deferral is not the problem.'),
    spot('Which line is the early withdrawal?', spot_doc, 'out',
         'The $1,000 traditional IRA withdrawal is the line. The penalty is the cost of that line, not a second withdrawal.'),
    num('What is 10% of that $1,000 withdrawal?', 100, '$1,000 × 0.10 = $100.', doc=spot_doc),
    mc('Which line is the useful one?',
       ['The $4,000 deferral', 'The early withdrawal', 'The penalty'], 0,
       'The deferral is the contribution. The other two are the leak and its cost.'),
    tf('The penalty replaces the income tax on the withdrawal.', False,
       'The $100 is the penalty. The $1,000 is usually income as well.'),
], fmt='spot')

kim_story = {
    'title': 'Kim splits $6,000',
    'character': 'Kim, 36',
    'body': 'Kim is 36 and a nurse. She has **$6,000** to assign this year, after she has already taken her employer match. She is in the 12% bracket.\n\nA **$2,000** [[traditional IRA]] deduction would save **$240**. She still wants at least **$2,000** in a [[Roth IRA]], because she wants qualified withdrawals later to be tax-free. The 2026 IRA limit is **$7,500**, so **$6,000** fits inside it if every IRA dollar stays at or under that cap.\n\nShe assigns the whole $6,000. The Roth gets at least $2,000. The rest can be a traditional IRA or a taxable brokerage account.',
}
kim = lesson('ta-kim', 'Kim’s $6,000', 'The IRA cap is $7,500. She is assigning less than that.', [
    alloc('Assign $6,000. The Roth IRA needs at least $2,000. Assign every dollar.', 6000, 100,
          [{'label': 'Roth IRA', 'min': 2000}, {'label': 'Traditional IRA'}, {'label': 'Taxable brokerage'}],
          'The Roth gets at least $2,000. All $6,000 is assigned, and $6,000 is under the 2026 IRA limit of $7,500.'),
    num('If all $6,000 went into IRAs, how much of the $7,500 limit would be left?', 1500,
        '$7,500 − $6,000 = $1,500.'),
    num('A $2,000 traditional deduction in her 12% bracket saves how much this year?', 240,
        '$2,000 × 0.12 = $240.'),
    mc('Why can she put the whole $6,000 into IRAs and still be inside the 2026 limit?',
       ['$6,000 is less than $7,500', '$6,000 is the 401(k) limit', 'Roth dollars do not count toward the IRA limit'], 0,
       'Traditional and Roth share the $7,500 limit. $6,000 fits.'),
    tf('Her employer match is part of the $24,500 employee deferral limit.', False,
       'The $24,500 is what she defers from her pay. The match is the employer’s money, under a different cap.'),
], fmt='story', story=kim_story)

trial_steps = [
    num('A $3,000 deductible traditional contribution is in the 22% bracket. How much tax does it save this year?', 660,
        '$3,000 × 0.22 = $660.'),
    num('What is the 2026 employee 401(k) deferral limit before catch-up?', 24500,
        '$24,500.'),
    num('An early traditional withdrawal is $2,000. What is the 10% penalty?', 200,
        '$2,000 × 0.10 = $200.'),
    tf('Qualified Roth withdrawals are taxed a second time.', False,
       'Qualified Roth withdrawals are tax-free. That is the point of paying tax on the way in.'),
]

lessons = [which, limits, hsa, college, order, early, spot, kim,
           review('ta'), trial('ta', 'Tax-Advantaged Accounts', trial_steps)]
write_unit('07-tax-advantaged.json', 'tax-advantaged', 7, 'Tax-Advantaged Accounts',
           'Traditional or Roth, the 2026 limits, and the penalty on an early traditional withdrawal.',
           'The match is free pay. The early withdrawal is a penalty.', terms, lessons, section=S)
