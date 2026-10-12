from lib import *

S = 'taxes'
terms = {
    'filing-extension': term('Filing extension',
                             'Extra time to send the return, usually to October 15. It does not give extra time to pay the tax.',
                             'An extension filed on April 15 still leaves an $800 tax due on April 15.'),
    'amended-return': term('Amended return',
                           'A form, usually Form 1040-X, that fixes a return you already filed. You generally have about three years, and the exact deadline is on irs.gov for that year.',
                           'A missed $200 credit is fixed on an amended return, not by filing the original form again and hoping.'),
}

who = lesson('fi-who', 'Who Must File', 'The common cases, not every exception.', [
    info('Usually, not always',
         'You usually must file if your income is above the filing threshold for your status, and if you had at least **$400** of net self-employment income. That $400 rule is the common case.\n\nYou may still want to file when you do not have to, so a refund or a refundable credit can reach you. This is the usual rule, not a ruling on your year.'),
    mc('Who usually must file even with a small income?',
       ['Someone with $400 or more of net self-employment income', 'Someone with no income and no credits', 'Someone whose only mail was a grocery flyer'], 0,
       'Self-employment of $400 or more is a common filing trigger.'),
    tf('If a refund is waiting, filing can still be worth it when you are not required to file.', True,
       'The IRS does not mail the refund just because it would have been nice.'),
    mc('What is the careful way to know if you must file this year?',
       ['Check the filing threshold for your status on irs.gov', 'Ask whether your friend filed', 'File only if you owe more than $1,000'], 0,
       'Thresholds depend on age, status, and the year. The IRS page is the list.'),
    fill('Net self-employment of $___ or more usually means you must file.',
         ['400', '4,000', '40,000'], 0,
         'The common figure is $400 of net self-employment income.'),
])

when = lesson('fi-when', 'Deadlines and Extensions', 'More time to file is not more time to pay.', [
    info('April, then October',
         'A calendar-year return is usually due **April 15**. If that day is a weekend or a holiday, the due date moves to the next business day.\n\nA [[filing extension]] usually gives you until **October 15** to send the form. The tax is still due in April. An **$800** tax unpaid from April 15 to October 15 is six months late even if the form is on time.'),
    mc('What does an extension extend?',
       ['The time to file the return', 'The time to pay the tax', 'The time to earn the income'], 0,
       'File later. Pay on time.'),
    num('The tax due on April 15 is $800. An extension is filed and the return is sent on October 15. How much of that tax was still due in April?', 800,
        'All $800. The extension did not move the payment.'),
    num('April 15 to October 15 is how many months?', 6, 'October 15 is six months after April 15.', unit='months'),
    tf('A return filed on October 15, under an extension, was required to include the payment back in April.', True,
       'The form may be on time in October. The payment was due in April.'),
])

papers = lesson('fi-papers', 'What to Gather', 'The return is only as good as the stack.', [
    info('The usual pile',
         'Bring the [[W-2|w-2]] from each job, any [[1099|form-1099]], and the records of a credit you will claim. A grocery receipt is not a tax form.\n\nLast year’s return helps you type the numbers. It does not replace this year’s W-2.'),
    sort('Sort the pile.',
         ['Bring it', 'Leave it out'],
         [('This year’s W-2', 0),
          ('A Form 1099-INT for bank interest', 0),
          ('A grocery receipt for ordinary food', 1),
          ('A birthday card', 1)],
         'Income forms come in. Ordinary groceries and greeting cards do not.'),
    mc('You had two jobs. How many W-2s do you need?',
       ['Both', 'The larger one', 'Neither, if you remember the pay'], 0,
       'Each employer reports its own wages and withholding.'),
    tf('A grocery receipt belongs in the tax pile for a person who did not itemize and did not run a business.', False,
       'Ordinary food is not a line on that return.'),
    fill('Bank interest arrives on a Form ___.',
         ['1099-INT', 'W-4', 'extension'], 0,
         '1099-INT. The W-4 is the withholding form, not the interest form.'),
], fmt='sort')

status = lesson('fi-status', 'Filing Status', 'It picks the deduction and the brackets.', [
    info('Five names',
         'The common statuses are single, married filing jointly, married filing separately, head of household, and qualifying surviving spouse.\n\nHead of household is not “I own a house.” It is usually an unmarried person who paid for a home for a qualifying person. The 2026 standard deduction you already saw is **$16,100** single and **$24,150** head of household.'),
    mc('Two spouses can choose which pair?',
       ['Married filing jointly or married filing separately', 'Single and head of household, both at once', 'A status from a different year'], 0,
       'Spouses pick joint or separate. They do not each file as single.'),
    tf('Owning a house, by itself, makes you head of household.', False,
       'The status is about a qualifying person and paying for the home, not about the mortgage.'),
    num('How much larger is the 2026 head-of-household standard deduction than the single one?', 8050,
        '$24,150 − $16,100 = $8,050.'),
    fill('Spouses who file together use married filing ___.',
         ['jointly', 'single', 'separately and jointly'], 0,
         'Jointly is the shared return. Separately is the other choice.'),
])

free = doc('statement', 'Do it yourself, if you qualify', [
    ('fee', 'Software fee on this Free File offer', 0),
], subtitle='IRS Free File or VITA', note='A $0 fee only if you qualify. Check irs.gov.')
paid = doc('statement', 'A paid preparer', [
    ('fee', 'Preparer fee', 350),
], subtitle='You still sign the return')
assert 350 - 0 == 350

help_ = lesson('fi-help', 'Free Help or a Preparer', 'The fee is not the same thing as a correct return.', [
    info('Three doors',
         'IRS Free File and VITA can cost nothing if you qualify. Paid software and a preparer charge a fee. This page does not grade an income cap, because those caps change. Check irs.gov for the year.\n\nWhoever prepares it, you sign it. The **$350** fee does not move the tax rules.'),
    num('How much more is the preparer’s fee than the $0 Free File offer, if you qualify for that offer?', 350,
        '$350 − $0 = $350.', docs=[free, paid]),
    mc('You qualify for Free File and your return is the single-filer case from this course. Which page has the lower fee?',
       ['Free File or VITA', 'The $350 preparer', 'The fees match'], 0,
       'Qualify first. If you do, the fee on this pair is $0 versus $350.',
       why=['The offer on this page is $0 if you qualify.', 'The preparer charges $350.', 'They differ by $350.'],
       docs=[free, paid]),
    tf('A preparer’s signature replaces yours.', False,
       'You sign your return. The preparer can be wrong, and the return is still yours.'),
    mc('VITA and Free File are the right first look when what is true?',
       ['You might qualify for free help', 'You want a fee in every case', 'You would rather skip the W-2'], 0,
       'Check the qualification. Then decide if a fee buys you something the free option does not.'),
], fmt='call')

form = doc('statement', 'A simplified Form 1040', [
    ('wages', 'Wages', 40000),
    ('agi', 'Adjusted gross income', 40000),
    ('taxable', 'Taxable income', 23900),
    ('tax', 'Tax', 2620),
    ('held', 'Federal income tax withheld', 3000),
], subtitle='Single, 2026', note='Taxable income is wages minus the $16,100 standard deduction. The lines are not one total.')
assert 40000 - 16100 == 23900 and 3000 - 2620 == 380

page = lesson('fi-1040', 'A Simplified Form 1040', 'Five lines. The refund is not one of the wages.', [
    info('The story you already know',
         'This is the single filer with **$40,000** of wages, the 2026 [[standard deduction]] of **$16,100**, tax of **$2,620**, and withholding of **$3,000**.\n\nThe lines are different kinds of numbers. Do not add the wages to the tax.'),
    num('What is taxable income on this form?', 23900,
        '$40,000 − $16,100 = $23,900.', doc=form),
    num('What is the refund?', 380, '$3,000 − $2,620 = $380.', doc=form),
    mc('Which line is the prepayment?',
       ['Federal income tax withheld, $3,000', 'Wages, $40,000', 'Taxable income, $23,900'], 0,
       'Withholding is what was already sent. Wages are what you earned.'),
    tf('Adding all five lines gives a number the IRS uses.', False,
       'They are not the same kind of dollar. The refund is withholding minus tax.'),
], fmt='document')

efile = lesson('fi-efile', 'E-file and Direct Deposit', 'The refund goes where the numbers say.', [
    info('Type the account twice',
         'E-file sends the return electronically. Direct deposit sends a refund to the routing number and account number you enter.\n\nA refund of **$380** deposited to the right account is $380. The same refund sent to a wrong account is a problem you have to unwind. Paper checks are slower.'),
    mc('What does direct deposit need?',
       ['The right routing number and account number', 'Only your employer’s name', 'A paper check from last year'], 0,
       'Those two numbers are the address of the account.'),
    num('The refund is $380 and the preparer fee was $0. How much of the refund is left after a $0 fee?', 380,
        '$380 − $0 = $380. A fee would come out of your pocket, not out of the tax math.'),
    tf('E-file means you no longer need the W-2.', False,
       'E-file is how the return travels. The W-2 is still the source of the wages and the withholding.'),
    fill('A wrong account number can send the refund to the wrong ___.',
         ['account', 'bracket', 'state'], 0,
         'Check the digits before you submit.'),
])

denise_story = {
    'title': 'Denise fixes a return',
    'character': 'Denise, 41',
    'body': 'Denise is 41 and a clinic manager. She filed an extension and paid her **$800** tax on April 15, then sent the return in June. The payment was on time. The form used the extra time.\n\nIn August she finds a **$200** credit the return left off. She files an [[amended return]], usually Form 1040-X. She does not file the original form a second time.\n\nThe credit would have cut her tax from **$800** to **$600**. She checks irs.gov for how long an amended return for that year is allowed. The usual window is about three years.',
}
denise = lesson('fi-denise', 'Denise Fixes a Mistake', 'An extension paid on time. A credit fixed later.', [
    num('Denise’s original tax was $800. The missed credit is $200. What should the tax have been?', 600,
        '$800 − $200 = $600.'),
    num('How much did she overpay if she already paid the $800?', 200,
        '$800 − $600 = $200.'),
    mc('How does she fix the filed return?',
       ['An amended return, usually Form 1040-X', 'A second copy of the original return', 'A new W-4 sent to the IRS'], 0,
       'The amended return is the correction. A second original is not.'),
    tf('Her extension let her pay the $800 in October.', False,
       'She paid in April. The extension covered the form, not the payment.'),
    fill('The form that usually fixes a filed return is Form ___.',
         ['1040-X', 'W-4', '1099'], 0,
         '1040-X. Then check the deadline for that year on irs.gov.'),
], fmt='story', story=denise_story)

trial_steps = [
    tf('An extension to file is also an extension to pay.', False,
       'The return can wait until October. The tax is still due in April.'),
    mc('Which paper reports wages and federal income tax withheld?',
       ['Form W-2', 'A grocery receipt', 'Form W-4'], 0,
       'The W-2 is the wage report. The W-4 is the withholding request.'),
    num('A return left off a $150 credit. The tax paid was $900. What should the tax have been?', 750,
        '$900 − $150 = $750.'),
    mc('You qualify for free help. What is the first door?',
       ['IRS Free File or VITA', 'The most expensive preparer in town', 'Skipping the return'], 0,
       'Check that you qualify, then use the free door before you pay $350.'),
]

lessons = [who, when, papers, status, help_, page, efile, denise,
           review('fi'), trial('fi', 'Filing Your Return', trial_steps)]
write_unit('03-filing.json', 'filing', 3, 'Filing Your Return',
           'Who files, when the money is due, and how a mistake gets fixed.',
           'The extension moves the form. It does not move the payment.', terms, lessons, section=S)
