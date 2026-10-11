from lib import *

S = 'credit-debt'
terms = {
    'payday-loan': term('Payday loan', 'A small, short loan due on your next payday. The fee looks tiny and the yearly cost is enormous.',
                        'Borrow $100 for two weeks and pay a $15 fee. That is about a 390% APR.'),
    'buy-now-pay-later': term('Buy now, pay later', 'A plan that splits a purchase into a few payments, often four. On time, interest is often $0. Miss one, and a fee can land. Several plans stack.',
                              'Four payments of $50 cover a $200 purchase. Three plans at once can mean $150 leaving your account in one week.'),
    'title-loan': term('Title loan', 'A short loan that uses your car title as collateral. Miss the payments and the lender can take the car.',
                       'Borrow $1,000 against a car worth $8,000. The car is on the line for a $1,000 emergency.'),
}

payday = lesson('lt-payday', 'Payday Loan Math', 'Fifteen dollars on a hundred, for two weeks, is not a small price.', [
    mc('What is a payday loan?',
       ['A small loan due on your next payday, with a fee that hides a huge yearly cost', 'A cheaper form of a credit card', 'An advance from your employer’s paycheck with no lender'], 0,
       'The fee is the whole product.',
       context='A [[payday loan]] of $100 with a $15 fee, due in two weeks, does not look like much. There are 26 two-week periods in 52 weeks. 15% × 26 = 390% [[APR]].'),
    num('The fee is $15 on $100. What percent of the loan is the fee?', 15, '$15 ÷ $100 = 15%.', unit='%'),
    num('How many two-week periods are in a 52-week year?', 26, '52 ÷ 2 = 26.', unit='periods'),
    num('What APR does 15% every two weeks work out to?', 390, '15% × 26 = 390%.', unit='%'),
    num('You roll the $100 loan four times, paying the $15 fee each time, and never cut the principal. How much have the fees cost?', 60,
        '$15 × 4 = $60, and you still owe the $100.'),
    tf('A $15 fee on $100 is cheap because 15 is a small number.', False, 'For two weeks, that fee is about a 390% APR.'),
])

rent = lesson('lt-rent-to-own', 'Rent to Own', 'The weekly payment is the advertisement. The year of weeks is the price.', [
    num('A laptop is $900 in cash, or $35 a week for 104 weeks. What do the weekly payments add up to?', 3640, '$35 × 104 = $3,640.',
        context='Rent-to-own lets you take an item home for a weekly fee. You can pay several times the cash price before you own it.'),
    num('How much more is that than the $900 cash price?', 2740, '$3,640 − $900 = $2,740.'),
    mc('What are you mostly paying for?',
       ['The right to spread a $900 item across two years, at a very high price', 'A cheaper laptop', 'A warranty that cuts the price'], 0,
       'Same laptop, $2,740 extra.'),
    tf('Stopping the weekly payments usually means you own a share of the item.', False,
       'In a typical rent-to-own deal you return it, and the payments you made do not buy you equity.'),
    num('You can save $45 a week. How many weeks to reach the $900 cash price?', 20,
        '$900 ÷ $45 = 20 weeks. Then you own it, for $900.', unit='weeks'),
    mc('Which is the careful path if the laptop can wait?',
       ['Save $45 a week and buy it for $900', 'Start the 104-week plan today', 'Put it on a payday loan'], 0,
       'Twenty-six weeks of saving beats two years of fees.'),
])

title = lesson('lt-title', 'Title Loans', 'The loan is small. The collateral is your way to work.', [
    mc('What does a title loan use as collateral?',
       ['Your car’s title', 'Your next paycheck', 'Your credit score'], 0,
       'The car is how they get paid if you do not.',
       context='A [[title loan]] is secured by your car. Borrow $1,000 and the lender holds the title. Miss the payments and they can take a car worth far more than $1,000.'),
    num('The car is worth $8,000. The loan is $1,000. How much of the car’s value is at risk for that loan?', 8000,
        'The whole car. They do not repossess $1,000 worth of it.'),
    mc('Why is that a bad trade for a $1,000 emergency?',
       ['You can lose an $8,000 car over a $1,000 debt', 'The car becomes more valuable', 'Title loans build a credit score for free'], 0,
       'The collateral is oversized on purpose.'),
    tf('Paying the title loan off on time means you get the title back.', True,
       'The danger is the miss, not the paperwork itself.'),
    mc('The fee is $25 per $100 borrowed, per month. On $1,000, what is one month’s fee?',
       ['$250', '$25', '$2,500'], 0, '$25 × 10 = $250. That is 25% in a single month.'),
    mc('What is the thing you are really risking?',
       ['The car you use to get to work', 'Only the $25', 'Nothing, if the ad says “easy”'], 0,
       'Easy to get is not easy to escape.'),
])

bnpl = lesson('lt-bnpl', 'Buy Now, Pay Later', 'Four small payments feel like zero. Three plans do not.', [
    num('A $200 purchase is split into 4 payments. How much is each payment, with no fee?', 50, '$200 ÷ 4 = $50.',
        context='[[Buy now, pay later]] splits a purchase, often into four payments. Pay on time and interest is often $0. A late payment can cost a fee, and the plans stack if you open several.'),
    tf('On-time buy-now-pay-later payments are often interest-free.', True, 'The trap is missing one, or opening too many.'),
    num('You miss a payment and the fee is $10. What did that “free” plan just cost, on top of the $50 you still owe?', 10,
        'The fee is $10. The $50 payment is still due too.'),
    num('Three plans want $45, $30, and $25 in the same week. How much leaves your account?', 100, '$45 + $30 + $25 = $100.'),
    mc('You have $80 that week. What is the problem?',
       ['The plans want $100. You are $20 short', 'Nothing. The apps wait forever', 'The $80 covers them'], 0,
       '$100 − $80 = $20 short. That is how a pile of small plans becomes a late fee.'),
    mc('When is buy now, pay later least dangerous?',
       ['One plan, for something you needed, that fits the weeks you will pay it', 'Five plans for things you wanted', 'A plan you already cannot see how to pay'], 0,
       'One at a time, and only if the payments are already in the budget.'),
])

nocredit = lesson('lt-no-check', '“No Credit Check”', 'The ad is loud because the price is the part they hope you will not do.', [
    mc('An offer says “no credit check.” What is that usually a sign of?',
       ['A high price, because the lender is not using your score to set a fair rate', 'A cheaper loan', 'A federal student loan'], 0,
       'They are not skipping the check to be kind.',
       context='“No credit check” means the lender is not using your [[credit score]] to price the loan. Payday loans, title loans, and some rent-to-own deals live here. The cost is in the fee.'),
    tf('No credit check means the loan cannot hurt you.', False,
       'It can still take a fee, a car, or a chunk of your next paycheck.'),
    mc('Which question matters more than “Will they approve me?”',
       ['What do I pay back, in dollars, and what can they take?', 'How fast can I get the money', 'Whether the payment is under $100'], 0,
       'Approval is easy when the price is ugly.'),
    num('The ad: borrow $200, pay back $260 in two weeks. How much is the fee?', 60, '$260 − $200 = $60.'),
    num('That $60 fee is what percent of the $200?', 30, '$60 ÷ $200 = 30%, for two weeks.', unit='%'),
    mc('What do you do with an offer that will not show the total you repay?',
       ['Walk away', 'Sign and read it later', 'Assume the total equals what you borrowed'], 0,
       'If the total is hidden, the total is the product.'),
])

ad_lines = [
    ('now', 'Cash you receive today', 200),
    ('back', 'Amount due in 14 days', 260),
    ('fine', '“No credit check” processing charge, extra', 25),
]
assert 260 - 200 == 60 and 60 + 25 == 85
AD = doc('receipt', 'Payday ad', ad_lines, subtitle='Due on your next payday',
         totals=[('You pay back', 285, True)],
         note='The $260 already includes a $60 fee. The $25 is on top.')
spot = lesson('lt-spot-ad', 'Spot the Trap', 'The friendly line is not the expensive one.', [
    spot('Which line is an extra charge stacked on top of the $260 payoff?', AD, 'fine',
         'The $25 “processing charge” sits on top of a payoff that already includes a $60 fee.',
         context='Read the ad as a receipt. What you receive and what you pay back are the only honest numbers.'),
    num('How much more than $200 do you pay if every line on this ad is real?', 85, '$260 − $200 = $60, plus $25 = $85.', doc=AD),
    num('What do you hand over in 14 days?', 285, '$260 + $25 = $285.', doc=AD),
    mc('What did “no credit check” cost you here?',
       ['$85 for a two-week, $200 loan', 'Nothing', '$25 only'], 0,
       '$85 ÷ $200 = 42.5% in two weeks.'),
    tf('A processing charge in the fine print is optional if you did not notice it.', False,
       'If it is on the paper you sign, it is in the deal.'),
    mc('What would a fair ad lead with?',
       ['You receive $200 and pay back $285', '“Approved”', '“No credit check needed”'], 0,
       'Dollars in, dollars out.'),
], fmt='spot')

PAYDAY = doc('bill', 'QuickCash payday loan', [('get', 'You receive', 300.00), ('fee', 'Fee for every two weeks you keep it', 45.00)],
             subtitle='Due in full on your next payday', note='Can’t repay in full? Rolling it over means paying the $45 again.')
CU = doc('bill', 'Lakeshore Credit Union', [('get', 'You receive', 300.00), ('app', 'Application fee', 20.00), ('pay', '3 monthly payments of $104.70', 314.10)],
         subtitle='Small-dollar loan for members', meta=[['APR', '28%']], totals=[('Total you pay back', 334.10, True)])
assert 3 * 104.70 == 314.10 or abs(3 * 104.70 - 314.10) < 0.001
assert round(334.10 - 300, 2) == 34.10 and 6 * 45 == 270 and round(270 - 34.10, 2) == 235.90
better = lesson('lt-better', 'Better Options When You Are Short', 'Slow help is usually cheaper than fast cash. Compare two loans.', [
    mc('A $300 car repair can’t wait, and you need about three months to pay it back. Which costs less?',
       ['The credit-union loan', 'The payday loan'], 0,
       'Compare the dollars you pay back, not how fast the money arrives.',
       context='When cash is short, try billers and payment plans first, then anything you can sell or pause, then a credit union. Many credit unions offer members small loans with capped fees. A payday loan is the last door, not the first.',
       docs=[PAYDAY, CU]),
    num('The credit-union loan: what does it cost you beyond the $300?', 34.10, '$334.10 − $300.00 = $34.10.', docs=[PAYDAY, CU]),
    num('Rolled over every two weeks for 12 weeks, the payday loan means six $45 fees. What do they add up to?', 270,
        '6 × $45 = $270, and you still owe the $300.', docs=[PAYDAY, CU]),
    num('How much more does the payday route cost than the whole credit-union loan?', 235.90, '$270.00 − $34.10 = $235.90.'),
    tf('A payment plan with the repair shop or a hospital can cost less than either loan.', True,
       'Many billers will split a balance. Ask before you borrow.'),
    order('Put the short-on-cash options from first try to last resort.',
          ['Call the biller and ask for a plan', 'Pause spending and sell something unused', 'A small credit-union loan if you can get one', 'A payday or title loan'],
          'Ask, then cut, then a normal loan, then the expensive door.'),
], fmt='call')

dev_story = {
    'title': 'Four small plans',
    'character': 'Dev, 23, rideshare driver',
    'body': 'Dev used buy now, pay later four times in a month: **$20**, **$35**, **$15**, and **$40**. Each one looked fine alone. They all come out the same week.\n\n'
            'He has **$80** in the account after gas. He also saw a payday ad: **$100** now, **$130** back in two weeks.',
}
assert 20 + 35 + 15 + 40 == 110 and 130 - 100 == 30 and 110 - 80 == 30
dev = lesson('lt-dev', 'Dev’s Pile-Up', 'The plans were small. The week they landed was not.', [
    num('How much do the four plans want in the same week?', 110, '$20 + $35 + $15 + $40 = $110.'),
    num('He has $80 after gas. How much is he short?', 30, '$110 − $80 = $30.'),
    num('The payday ad wants $130 back on $100. How much is that fee?', 30, '$130 − $100 = $30.'),
    mc('He takes the payday loan to cover the $30 gap. What is wrong with that fix?',
       ['He pays a $30 fee to cover a $30 gap, and he still owes the $100', 'It is free', 'It pays off all four plans forever'], 0,
       'A $30 fee to borrow the $30 he is short is a terrible trade. He would owe $130.'),
    tf('One buy-now-pay-later plan is the same risk as four of them due the same week.', False,
       'The stack is the problem. $110 is not $20.'),
    mc('What is the better move this week?',
       ['Pay what he can, ask one plan or biller for a few days, and do not open the payday loan', 'Take the payday loan', 'Open a fifth plan'], 0,
       'A short delay beats a two-week fee the size of the gap.'),
], fmt='story', story=dev_story)

trial_steps = [
    num('A $20 fee on a $100 loan, every two weeks, for a full year of 26 periods. What is the APR?', 520,
        '20% × 26 = 520%.', unit='%'),
    mc('A title loan puts which asset on the line?', ['Your car', 'Your paycheck', 'Your credit score'], 0,
       'The title is the collateral.'),
    tf('Four buy-now-pay-later plans due the same week cost the same as one of them.', False, 'Add the payments. They leave together.'),
    num('$45 a week for 80 weeks, versus a $500 cash price. How much more do the weekly payments cost?', 3100,
        '$45 × 80 = $3,600. $3,600 − $500 = $3,100.'),
]

lessons = [payday, rent, title, bnpl, nocredit, spot, better, dev,
           review('lt'), trial('lt', 'Payday, BNPL & Other Traps', trial_steps)]
write_unit('10-lending-traps.json', 'lending-traps', 10, 'Payday Loans, BNPL & Other Traps',
           'Fast cash, weekly payments, and the price hidden in a small fee.',
           'Fast cash is the most expensive money in the woods.', terms, lessons, section=S)
