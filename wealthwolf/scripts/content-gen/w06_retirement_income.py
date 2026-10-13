from lib import *

S = 'building-wealth'
terms = {
    'required-minimum-distribution': term('Required minimum distribution',
                                          'The minimum you must withdraw from a traditional IRA and most workplace retirement plans. For an owner, it currently starts at age 73. A Roth IRA owner does not have this requirement during their lifetime.',
                                          'Turn 73 this year and the traditional IRA starts a required withdrawal. The Roth IRA does not.'),
    'sequence-of-returns-risk': term('Sequence-of-returns risk',
                                'The danger that bad returns arrive early in retirement, while you are withdrawing. The same average return is harsher if the bad years come first.',
                                'A 20% drop and then a $20,000 withdrawal leaves less than withdrawing from a pile that had not fallen.'),
    'annuity': term('Annuity',
                    'A contract with an insurance company. You pay a lump sum, and it pays you an income. The pile is often no longer yours to leave to someone else. This is a description, not a recommendation.',
                    'Handing over $100,000 for a lifetime income, and giving up that $100,000 as a pile.'),
}

pay_doc = doc('statement', 'Year one of a $1,000,000 pile',
              [('pile', 'Portfolio', 1000000), ('out', 'Year-one withdrawal at 4%', 40000)],
              subtitle='A rule of thumb, not a required minimum',
              note='Later years adjust the $40,000 for inflation. They do not restart 4% on a new balance.')

rate = lesson('ri-rate', 'The Withdrawal', 'Four percent, once, then inflate the dollars.', [
    info('Year one',
         'The [[4% rule|four-percent-rule]] in year one is 4% of the portfolio. On $1,000,000 that is $40,000. Next year you adjust those dollars for inflation. You do not have to spend it all. Taking less is allowed. This is a sketch, and it is not the same thing as a required minimum distribution.'),
    num('How many dollars is the year-one withdrawal on this page?', 40000,
        doc=pay_doc,
        explain='$1,000,000 × 0.04 = $40,000.'),
    num('Example inflation is 2%. What is the year-two withdrawal if you adjust the $40,000?', 40800,
        '$40,000 × 1.02 = $40,800.'),
    tf('You must spend the whole $40,000.', False,
       'It is a ceiling people use for planning. Spending less leaves more in the pile.'),
    mc('What does year two adjust?',
       ['The $40,000 dollar amount, for inflation', 'The percent, restarted on whatever is left', 'The federal funds rate'], 0,
       'Inflate the dollars. Do not recompute 4% of a shrunken balance and call it the same rule.'),
], fmt='document')

draw = lesson('ri-order', 'Which Account First', 'A common order, not the only one.', [
    info('Taxable, then traditional, Roth last',
         'A common draw order: spend taxable brokerage money first, then [[traditional IRA|traditional-ira]] money, and leave the [[Roth IRA|roth-ira]] last. Roth withdrawals that are qualified are tax-free, and the owner has no required distribution. Traditional withdrawals are taxed. This is a common order. A tax pro can have a reason to swap it. It is not a command.'),
    order('Put the common draw order in order, Roth last.',
          ['Spend taxable brokerage money',
           'Withdraw from the traditional IRA',
           'Leave the Roth IRA for last'],
          'Taxable first, traditional in the middle, Roth last so the tax-free pile can keep growing.'),
    tf('The common order empties the Roth IRA first.', False,
       'Roth is last in this common order, not first.'),
    mc('Why do people often save the Roth for last?',
       ['Qualified withdrawals are tax-free, and the owner is not forced to take them', 'Because a Roth cannot hold a fund', 'Because traditional withdrawals are tax-free'], 0,
       'Tax-free and no owner RMD. Traditional withdrawals are the taxable ones.'),
    fill('In this common order, the account you spend first is the ___ brokerage.',
         ['taxable', 'Roth', 'mystery'], 0,
         'Taxable. Roth waits.'),
])

rmd = lesson('ri-rmd', 'Required Minimums', 'Age 73 for the traditional pile.', [
    info('The age, for now',
         'A [[required minimum distribution]] is the least you must take from a traditional IRA and from most workplace plans. The starting age is 73. The first one can wait until April 1 of the next year, which can put two withdrawals in that next tax year. A Roth IRA owner does not have this requirement during their lifetime. The dollar amount uses an IRS table. This lesson grades the age, not a homemade table.'),
    num('At what age do traditional IRA required minimums currently start?', 73, unit=None,
        explain='Age 73. The first withdrawal can be delayed until April 1 of the following year.'),
    tf('A Roth IRA owner must start required minimums at 73.', False,
       'Not during the owner’s lifetime. The traditional IRA is the one with the age-73 rule.'),
    mc('Why might you take the first required withdrawal in the year you turn 73, instead of waiting until April 1?',
       ['So you do not have two taxable withdrawals in the next year', 'Because April 1 is illegal', 'Because Roth IRAs require it'], 0,
       'Waiting until April 1 can stack two withdrawals into one tax year. Taking the first one in the year you turn 73 spreads them.'),
    tf('You are allowed to withdraw more than the minimum.', True,
       'The minimum is a floor. More is allowed, and it is taxable if it comes from a traditional account.'),
])

seq = lesson('ri-seq', 'Bad Years First', 'The order of returns matters once you are spending.', [
    info('Same average, harsher path',
         '[[Sequence-of-returns risk]] is what happens when the bad year comes while you are withdrawing. A $500,000 pile falls 20%, to $400,000, and you still take out $20,000. You have $380,000. If the pile had not fallen, the same withdrawal would leave $480,000. The early drop and the withdrawal stack.'),
    num('A $500,000 portfolio falls 20%. How many dollars is it worth before the withdrawal?', 400000,
        '$500,000 × 0.80 = $400,000.'),
    num('You then withdraw $20,000. How many dollars are left?', 380000,
        '$400,000 − $20,000 = $380,000.'),
    num('Without the drop, the same $20,000 withdrawal from $500,000 leaves how many dollars?', 480000,
        '$500,000 − $20,000 = $480,000. The gap versus $380,000 is $100,000.'),
    tf('The order of returns stops mattering after you retire, because you are no longer contributing.', False,
       'It matters more. Withdrawals turn an early drop into a smaller pile that then has to recover.'),
])

keep = doc('statement', 'Keep the portfolio',
           [('pile', 'Still yours', 100000)],
           subtitle='You withdraw from it over time')
hand = doc('statement', 'Hand it to an insurer',
           [('paid', 'Paid for an annuity', 100000)],
           subtitle='The pile is no longer yours to leave',
           note='Income in exchange for the lump sum. Not a recommendation.')

ann = lesson('ri-annuity', 'Annuities, Lightly', 'Income in exchange for the pile.', [
    info('What you give up',
         'An [[annuity]] here means you pay an insurer a lump sum and it pays you an income, sometimes for life. The $100,000 is often no longer a pile you can leave to a child. Fees and the insurer’s promise are the whole product. This is a definition, not a suggestion to buy one.'),
    mc('Which page still leaves the $100,000 in your name?',
       [keep['title'], hand['title']], 0,
       docs=(keep, hand),
       explain='The portfolio page is still yours. The annuity page traded the pile for an income stream.'),
    tf('Buying an annuity is required once you retire.', False,
       'It is one product. The withdrawal sketch does not require it.'),
    mc('What is the usual trade?',
       ['You give up the pile and receive an income', 'You keep the pile and the insurer also sends a gift', 'The Fed sets the payment'], 0,
       'Income, in exchange for the lump sum. Read the fees before you ever think about it.'),
    num('How many dollars leave your name on the annuity page?', 100000,
        doc=hand,
        explain='The $100,000 is what you paid. It is not still a pile you control.'),
], fmt='call')

paycheck = lesson('ri-pay', 'A Retirement Paycheck', 'Assign the $40,000.', [
    info('Floors, then the rest',
         'The year-one sketch is $40,000. Housing needs at least $15,000, food at least $8,000, health at least $6,000, and everything else at least $1,000. Assign every dollar. The floors are the lesson. A real budget uses your bills.'),
    alloc('Assign all $40,000. Meet each floor.', 40000, 1000,
          [{'label': 'Housing', 'min': 15000},
           {'label': 'Food', 'min': 8000},
           {'label': 'Health', 'min': 6000},
           {'label': 'Everything else', 'min': 1000}],
          'The floors are $15,000, $8,000, $6,000, and $1,000, which add to $30,000. The other $10,000 can sit in everything else. That fill ends with $11,000 there.'),
    num('How many dollars do the four floors add up to, before the extra $10,000?', 30000,
        '$15,000 + $8,000 + $6,000 + $1,000 = $30,000.'),
    tf('The $40,000 assignment is a bill from the IRS.', False,
       'It is a spending sketch. The required minimum, if you are 73, is a different rule and a different math.'),
    mc('What should a real version of this page use?',
       ['Your actual bills', 'A friend’s floors', 'The federal funds rate'], 0,
       'Your rent, your food, your premiums. The round numbers are only a drill.'),
])

stack = lesson('ri-stack', 'The Check and the Pile', 'Do not withdraw spending that Social Security already covers.', [
    info('Add them',
         'If Social Security pays $18,000 and spending is $50,000, the portfolio’s job is the $32,000 gap, not the whole $50,000. Withdrawing $50,000 anyway spends the pile faster than the plan. This is the same idea as a base and a gap, with a new set of numbers.'),
    num('Spending is $50,000 and Social Security is $18,000. How many dollars does the portfolio need to cover?', 32000,
        '$50,000 − $18,000 = $32,000.'),
    num('You withdraw the whole $50,000 anyway. How many extra dollars did you take beyond the gap?', 18000,
        '$50,000 − $32,000 = $18,000. That extra is the Social Security you could have spent instead.'),
    tf('Social Security and the portfolio withdrawal should both be large enough to cover all the spending, on purpose.', False,
       'They stack. Covering the spending twice drains the portfolio.'),
    mc('What is the portfolio’s job in this sketch?',
       ['The gap after Social Security', 'A second copy of all the spending', 'The Medicare premium table'], 0,
       'The gap. $32,000 here, not $50,000.'),
])

joe = lesson('ri-joe', 'Joe and Ann’s First Year', 'They are 66. The required minimum is not here yet.', [
    info('Meet Joe and Ann',
         'Joe and Ann are both 66 and newly retired. Their portfolio is $1,000,000. A 4% year-one sketch is $40,000. They are not 73, so a required minimum does not apply yet. The $40,000 is a choice.\n\nThey will spend taxable money first and leave the Roth IRA alone. They also write down what a 20% drop in year one would do, so the first bad year does not surprise them into selling everything.',
         ),
    num('What is their year-one 4% withdrawal, in dollars?', 40000,
        '$1,000,000 × 0.04 = $40,000.'),
    tf('Because they retired, they must take a required minimum at 66.', False,
       'The traditional required minimum starts at 73. Sixty-six is a choice, not that rule.'),
    mc('Which account do they spend first in the common order?',
       ['The Roth IRA', 'Taxable brokerage money', 'A new annuity, required by law'], 1,
       'Taxable first. The Roth waits. An annuity is not required.'),
    num('If the $1,000,000 fell 20% before any withdrawal, how many dollars would it be worth?', 800000,
        '$1,000,000 × 0.80 = $800,000. That is the sequence risk they wrote down, not a prediction.'),
], fmt='story', story={
    'title': 'The first retired year',
    'character': 'Joe and Ann, both 66, newly retired',
    'body': 'Joe and Ann have a **$1,000,000** portfolio. A 4% year-one sketch is **$40,000**. They are **66**, so a required minimum has not started.\n\nThey spend taxable money first and leave the Roth IRA alone.',
})

write_unit('06-retirement-income.json', 'retirement-income', 6, 'Turning Savings into Income',
           'A first-year withdrawal, the order of accounts, and the age-73 rule.',
           'The 4% sketch is a choice. Age 73 is the requirement.',
           terms, [rate, draw, rmd, seq, ann, paycheck, stack, joe, review('ri'), trial('ri', 'Turning Savings into Income', [
               num('4% of $750,000 is how many dollars in year one?', 30000,
                   '$750,000 × 0.04 = $30,000.'),
               tf('Roth IRA owners must take required minimums at 73.', False,
                  'Not during the owner’s lifetime. Traditional IRAs are the age-73 account.'),
               num('A $200,000 pile falls 20% and you then withdraw $10,000. How many dollars are left?', 150000,
                   '$200,000 × 0.80 = $160,000, then $160,000 − $10,000 = $150,000.'),
               mc('In the common draw order, which account waits until last?',
                  ['Taxable brokerage', 'Traditional IRA', 'Roth IRA'], 2,
                  'Roth last. Taxable first, traditional in the middle.'),
           ])],
           section=S)
