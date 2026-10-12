from lib import *

S = 'taxes'
terms = {
    'withholding': term('Withholding',
                        'Tax your employer takes out of each paycheck and sends to the IRS in your name. It is a prepayment, not a separate extra tax.',
                        'A $2,620 income-tax bill and $3,000 withheld means a $380 refund.'),
    'w-4': term('W-4',
                'The form you give your employer so it knows how much federal income tax to withhold. You can change it when a job, a marriage, or a second paycheck changes the picture.',
                'Chris has two jobs. Each W-4 was filled out as if it were his only job, so too little was withheld.'),
}

what = lesson('wh-what', 'What Withholding Is', 'The IRS is already collecting during the year.', [
    info('A prepayment',
         '[[Withholding]] is federal income tax taken from the paycheck. It is credited against the bill you saw in the last unit.\n\nIt is not [[FICA]]. FICA is Social Security and Medicare. A W-4 changes the income-tax withholding, not the FICA rate.'),
    mc('What is withholding?',
       ['Income tax your employer sends ahead, in your name', 'A fee the employer keeps', 'The standard deduction'], 0,
       'It is your money, parked with the IRS until the return sorts it out.'),
    num('The tax is $2,620 and withholding is $3,000. How much comes back?', 380,
        '$3,000 − $2,620 = $380.'),
    num('The tax is $2,620 and withholding is $2,000. How much do you still owe?', 620,
        '$2,620 − $2,000 = $620.'),
    tf('Withholding is a second tax on top of the income tax.', False,
       'It is the income tax, paid early. The return compares it with the real bill.'),
])

when = lesson('wh-when', 'When to Update the W-4', 'A life change is a form, not a hope.', [
    info('The form is yours',
         'A [[W-4|w-4]] tells the employer how much federal income tax to withhold. Fill a new one when you marry, have a child, add a job, or your refund or your bill keeps surprising you.\n\nThe IRS withholding estimator on irs.gov is the tool. This lesson does not fill the form for you.'),
    mc('Which change is a reason to look at the W-4 again?',
       ['You take a second job', 'You buy the same groceries', 'Your commute is one block shorter'], 0,
       'A second paycheck changes the tax. The estimator is built for that.'),
    tf('A W-4 changes the FICA rate.', False,
       'FICA is set by law. The W-4 changes income-tax withholding.'),
    mc('Where is the careful place to estimate a new W-4?',
       ['The IRS withholding estimator', 'A comment thread', 'Last year’s refund, with no new numbers'], 0,
       'The estimator uses your pay, your other job, and your filing status.'),
    fill('You give the W-4 to your ___.',
         ['employer', 'state legislature', 'bank'], 0,
         'The employer is who withholds. The IRS is who receives it.'),
])

either = lesson('wh-either', 'Refund or a Bill', 'Both are your money. The timing is the difference.', [
    info('A refund is not a prize',
         'A refund means withholding was larger than the tax. A bill means it was smaller. The tax can be the same either way.\n\nOn a **$2,620** tax, withholding of **$3,000** refunds **$380**. Withholding of **$2,200** means you owe **$420**.'),
    num('Tax $2,620, withholding $2,200. How much do you owe?', 420, '$2,620 − $2,200 = $420.'),
    num('How much more was withheld in the $3,000 case than in the $2,200 case?', 800,
        '$3,000 − $2,200 = $800.'),
    mc('What is a refund?',
       ['Your own overpayment, sent back', 'A bonus from the IRS', 'Proof you paid no tax'], 0,
       'You paid $3,000 toward a $2,620 bill. The $380 was always yours.'),
    tf('Owing at filing time means the return was done wrong.', False,
       'It means withholding was short of the bill. The return can still be right.'),
])

estimator = lesson('wh-estimator', 'The IRS Estimator', 'Use the official one when two numbers disagree.', [
    info('Bring the paystubs',
         'The IRS withholding estimator asks for pay, how often you are paid, other jobs, and credits. It suggests a [[W-4|w-4]].\n\nA guess that “a refund is always good” skips the tool. A **$1,200** refund on a **$2,620** tax means **$3,820** was withheld. That is **$1,200** you did not have during the year.'),
    num('The tax is $2,620 and the refund is $1,200. How much was withheld?', 3820,
        '$2,620 + $1,200 = $3,820.'),
    num('How much more is that than a withholding of $2,620, which would refund $0 of income tax?', 1200,
        '$3,820 − $2,620 = $1,200. A $0 refund here means withholding matched the tax.'),
    mc('What should you type into the estimator?',
       ['The pay on your stubs, including a second job', 'The refund you wish you could have', 'Only the FICA line'], 0,
       'The tool is only as good as the pay you enter.'),
    tf('A big refund is proof the estimator is required by law.', False,
       'The estimator is a tool. A big refund is a clue that withholding was high, not a legal duty to use one website.'),
])

two = lesson('wh-two', 'Two Jobs', 'Each job may withhold as if it were the only one.', [
    info('The brackets do not know about each other',
         'Job A pays **$30,000** and withholds **$1,500**. Job B pays **$20,000** and withholds **$800**. Together the wages are **$50,000** and the withholding is **$2,300**.\n\nEach [[W-4|w-4]] may assume it is the only job, so each one aims at the low brackets. The combined taxable income does not.'),
    num('What are the two jobs’ wages together?', 50000, '$30,000 + $20,000 = $50,000.'),
    num('What is the withholding from both jobs?', 2300, '$1,500 + $800 = $2,300.'),
    num('Single, 2026. Taxable income on $50,000 is $33,900. The tax is $1,240 plus 12% of $21,500, which is $3,820. How much is still unpaid?', 1520,
        '$3,820 − $2,300 = $1,520. $50,000 − $16,100 = $33,900. $33,900 − $12,400 = $21,500. $21,500 × 0.12 = $2,580. $1,240 + $2,580 = $3,820.'),
    tf('Two small withholdings add up to the same result as one W-4 that knows about both jobs.', False,
       'Each job may withhold too little because it cannot see the other paycheck.'),
])

w4 = doc('statement', 'Withholding you asked for', [
    ('base', 'Federal income tax withheld before the extra', 2200),
    ('extra', 'Extra withholding, $40 × 26 paychecks', 1040),
], subtitle='One employer', totals=[('Federal income tax withheld', 3240, True)])
assert 40 * 26 == 1040 and 2200 + 1040 == 3240

form = lesson('wh-form', 'A W-4’s Extra Line', 'The extra box is a dollar amount, not a feeling.', [
    info('Twenty-six paychecks',
         'This [[W-4|w-4]] asks the employer to withhold an extra **$40** each paycheck. There are **26** paychecks. That extra is **$1,040** for the year.\n\nIt sits on top of the **$2,200** the employer was already withholding.'),
    num('What is $40 extra across 26 paychecks?', 1040, '$40 × 26 = $1,040.', doc=w4),
    num('What is total federal income tax withheld on this page?', 3240,
        '$2,200 + $1,040 = $3,240.', doc=w4),
    mc('Why would someone add the extra $40?',
       ['A second job is not withholding enough', 'To increase the FICA rate', 'To raise the standard deduction'], 0,
       'The extra line is how you catch up when the ordinary withholding is short.'),
    tf('The extra $40 is paid once a year.', False,
       'It is per paycheck. Twenty-six of them make $1,040.'),
], fmt='document')

high = doc('statement', 'Withholding that overshoots', [
    ('tax', 'Federal income tax', 2620),
    ('held', 'Federal income tax withheld', 4000),
], totals=[('Refund', 1380, True)])
close = doc('statement', 'Withholding that lands closer', [
    ('tax', 'Federal income tax', 2620),
    ('held', 'Federal income tax withheld', 2800),
], totals=[('Refund', 180, True)])
assert 4000 - 2620 == 1380 and 2800 - 2620 == 180 and 4000 - 2800 == 1200 and 1380 - 180 == 1200

loan = lesson('wh-loan', 'A Refund Is a 0% Loan', 'The bigger refund is the same tax, paid earlier.', [
    num('How much is the refund when $4,000 was withheld?', 1380,
        '$4,000 − $2,620 = $1,380.',
        context='Both pages have the same **$2,620** tax. The large refund is your money, returned later, with no interest.',
        docs=[high, close]),
    num('How much is the refund when $2,800 was withheld?', 180,
        '$2,800 − $2,620 = $180.', docs=[high, close]),
    num('How much more stayed out of the paychecks on the $4,000 page?', 1200,
        '$4,000 − $2,800 = $1,200. That is also $1,380 − $180.', docs=[high, close]),
    mc('The tax is the same. Which page leaves more money in the paychecks during the year?',
       ['Withholding of $2,800', 'Withholding of $4,000', 'They leave the same amount in the paychecks'], 0,
       'The $4,000 page withholds $1,200 more and refunds that $1,200 later.',
       why=['$2,800 is the smaller prepayment.', 'The extra $1,200 comes back only as a refund.', 'The withholdings differ by $1,200.'],
       docs=[high, close]),
    tf('The $1,380 refund is interest the IRS pays you for waiting.', False,
       'It is your own $1,200 of extra withholding, plus the smaller refund on the other page. No interest is added here.'),
], fmt='call')

chris_story = {
    'title': 'Chris has two jobs',
    'character': 'Chris, 24',
    'body': 'Chris is 24 and works two jobs. One pays **$30,000** and withholds **$1,500** of federal income tax. The other pays **$20,000** and withholds **$800**.\n\nTogether that is **$50,000** of wages and **$2,300** withheld. He is single. The 2026 [[standard deduction]] leaves taxable income of **$33,900**, and the tax is **$3,820**.\n\nHe owes **$1,520**. Each [[W-4|w-4]] was filled out as if it were the only job. The IRS estimator is the next step, not a bigger hope for a refund.',
}
chris = lesson('wh-chris', 'Chris Has Two Jobs', 'The shortfall is the tax minus what both jobs sent.', [
    num('How much did both jobs withhold?', 2300, '$1,500 + $800 = $2,300.'),
    num('His tax is $3,820. How much does he still owe?', 1520, '$3,820 − $2,300 = $1,520.'),
    num('What is his taxable income on $50,000 of wages?', 33900, '$50,000 − $16,100 = $33,900.'),
    mc('What is the useful fix before next April?',
       ['A new W-4, checked with the IRS estimator', 'Ignore the second job on both forms', 'Ask payroll to stop FICA'], 0,
       'The estimator can see both jobs. The old forms could not.'),
    tf('Chris owes $1,520 because the 12% bracket taxed his first dollar.', False,
       'The first $12,400 was still taxed at 10%. He owes because $2,300 was withheld toward a $3,820 bill.'),
], fmt='story', story=chris_story)

trial_steps = [
    num('Tax is $1,800 and withholding is $1,250. How much is still owed?', 550, '$1,800 − $1,250 = $550.'),
    mc('A second job starts in June. What should you revisit?',
       ['The W-4, with the IRS estimator', 'Only the FICA percent', 'Nothing until the refund arrives'], 0,
       'The new paycheck changes the withholding math.'),
    tf('A larger refund means you paid less tax.', False,
       'It means more tax was prepaid. The bill is a separate number.'),
    num('An extra $25 is withheld for 24 paychecks. How much is that for the year?', 600, '$25 × 24 = $600.'),
]

lessons = [what, when, either, estimator, two, form, loan, chris,
           review('wh'), trial('wh', 'Withholding & the W-4', trial_steps)]
write_unit('02-withholding.json', 'withholding', 2, 'Withholding & the W-4',
           'The prepayment on the paycheck, the form that sets it, and the refund that is not a prize.',
           'A refund is your money coming home late.', terms, lessons, section=S)
