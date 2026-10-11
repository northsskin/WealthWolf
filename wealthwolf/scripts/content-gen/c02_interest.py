from lib import *
from preserved import kept, kept_term

S = 'credit-debt'
terms = {
    'apr': kept_term('apr'),
    'balance': kept_term('balance'),
    'minimum-payment': kept_term('minimum-payment'),
    'simple-interest': term('Simple interest', 'Interest worked out only on the principal: principal × rate × time.',
                            '$1,000 at 8% for one year is $1,000 × 0.08 × 1 = $80.'),
    'origination-fee': term('Origination fee', 'A fee some lenders charge for setting up a loan. It is part of the cost, on top of interest.',
                            'A $100 origination fee on a $2,000 loan adds $100 to what the loan costs you.'),
}

simple = lesson('ia-simple', 'Simple Interest', 'Principal times rate times time. One clean formula.', [
    mc('What does simple interest get multiplied by?', ['The principal, the rate, and the time', 'Only the monthly payment', 'Your credit score'], 0,
       'Principal × rate × time.',
       context='[[Simple interest]] is principal × rate × time. $1,000 at 8% for one year is $1,000 × 0.08 × 1 = $80. It does not add interest on the interest.'),
    num('$1,200 at 9% simple interest for 1 year. How much interest?', 108, '$1,200 × 0.09 × 1 = $108.'),
    num('The same $1,200 at 9% for 3 years, simple interest. How much interest?', 324, '$1,200 × 0.09 × 3 = $324.'),
    num('You borrow $800 at 5% simple interest for 2 years. How much do you pay back in total?', 880,
        'Interest is $800 × 0.05 × 2 = $80. Total is $800 + $80 = $880.'),
    tf('Simple interest charges interest on the interest from last year.', False,
       'That would be compounding. Simple interest stays on the original principal.'),
    fill('Simple interest equals principal × rate × ___.', ['time', 'credit score', 'minimum payment'], 0, 'How long you borrow is the third number.'),
])

monthly = lesson('ia-monthly', 'Interest, Month by Month', 'Cards usually charge interest every month, not once a year.', [
    mc('A card lists 24% APR. About what monthly rate is that?', ['2%', '24%', '0.24%'], 0,
       '24% ÷ 12 months = 2% a month.',
       context='A card’s [[APR]] is a yearly rate. Divide by 12 for a rough monthly rate. On a [[balance]] of $1,000 at 24% APR, one month of interest is about $1,000 × 0.02 = $20.'),
    num('$1,000 balance, 24% APR. About how much interest in the first month?', 20, '$1,000 × 0.02 = $20.'),
    num('You pay nothing. The balance becomes $1,020. About how much interest in the second month?', 20.40,
        '$1,020 × 0.02 = $20.40. The interest itself starts getting interest.'),
    num('$2,000 balance at 18% APR. Monthly rate is 1.5%. How much interest this month?', 30, '$2,000 × 0.015 = $30.'),
    tf('Paying the balance in full stops this month’s interest from piling onto next month.', True,
       'Nothing left to charge. The [[minimum payment]] alone usually does not do that.'),
    mc('Why is the second month’s interest higher if you pay nothing?',
       ['The balance grew, so the rate hits a bigger number', 'The APR went up by itself', 'The lender adds a fee every second month'], 0,
       '$20 of interest became part of the balance.'),
])

apy = lesson('ia-apr-apy', 'APR and APY', 'One is the price of borrowing. The other is what savings earn.', [
    mc('Which number is the yearly cost of borrowing?', ['APR', 'APY', 'Your paycheck'], 0,
       'APR is what a loan or card costs you.',
       context='[[APR]] is the yearly cost of borrowing. [[APY]] is what savings earn in a year, counting interest on the interest. A 5% APR loan and a 5% APY savings account are not the same kind of deal.'),
    num('A savings account holds $2,000 at 4% APY for a year. About how much does it earn?', 80, '$2,000 × 0.04 = $80.',
        context='APY already includes compounding, so a one-year estimate is balance × APY.'),
    num('You owe $2,000 on a card at 20% APR for a year, and you pay nothing. Roughly how much interest?', 400,
        '$2,000 × 0.20 = $400. Monthly compounding makes the real bill a bit higher.'),
    mc('You want a savings account to grow. Which number do you compare?',
       ['APY', 'The APR on someone else’s car loan', 'The due date'], 0,
       'APY is the earnings number.'),
    tf('A lower APR on a loan means cheaper borrowing.', True, 'Lower price to borrow.'),
    mc('Why can a 20% APR card cost a bit more than balance × 0.20?',
       ['Interest is added month by month, and then interest hits that too', 'APR ignores the balance', 'The rate is applied once a year, to the highest balance'], 0,
       'The rough yearly figure is a floor, not the whole story.'),
])

loan_a = [
    ('amt', 'Amount borrowed', 4000),
    ('fee', 'Upfront fee', 0),
    ('int', 'Interest for the year', 320),
]
loan_b = [
    ('amt', 'Amount borrowed', 4000),
    ('fee', 'Upfront fee', 200),
    ('int', 'Interest for the year', 240),
]
assert 4000 + 320 == 4320 and 4000 + 200 + 240 == 4440
LOAN_A = doc('statement', 'Loan A', loan_a, subtitle='One-year loan', totals=[('Total you pay back', 4320, True)])
LOAN_B = doc('statement', 'Loan B', loan_b, subtitle='One-year loan', totals=[('Total you pay back', 4440, True)])
offers = lesson('ia-two-offers', 'Two Loan Offers', 'The lower rate can still lose if a fee is riding along.', [
    num('What is the interest on Loan A?', 320, '$4,000 × 0.08 = $320.',
        context='Compare the total you pay back, not the rate alone.', docs=[LOAN_A, LOAN_B]),
    num('What do you pay back on Loan A, fee included?', 4320, '$4,000 + $320 = $4,320.', docs=[LOAN_A, LOAN_B]),
    num('What do you pay back on Loan B?', 4440, '$4,000 + $200 + $240 = $4,440.', docs=[LOAN_A, LOAN_B]),
    num('How much more does Loan B cost than Loan A?', 120, '$4,440 − $4,320 = $120.'),
    mc('Loan B’s interest rate is lower. Why does it still cost more?',
       ['The $200 fee outweighs the cheaper interest', 'Loan A is a scam', 'The totals are the same'], 0,
       '$240 of interest plus a $200 fee is $440. Loan A’s interest is $320.',
       why=['$440 of cost against $320.', 'Both are real offers. One is just pricier.', 'The sheets differ by $120.']),
    tf('The offer with the smaller interest line is always the cheaper loan.', False,
       'Add the fee before you decide.'),
], fmt='call')

total = lesson('ia-total-cost', 'The Total Cost', 'Monthly payments hide the real price. Multiply them.', [
    num('A $9,000 loan asks for $250 a month for 48 months. How much do you pay in total?', 12000, '$250 × 48 = $12,000.',
        context='The total cost is every payment added up. Interest is that total minus the [[principal]].'),
    num('How much of that $12,000 is interest?', 3000, '$12,000 − $9,000 = $3,000.'),
    num('$150 a month for 36 months. What is the total?', 5400, '$150 × 36 = $5,400.'),
    num('That loan’s principal was $4,500. How much interest?', 900, '$5,400 − $4,500 = $900.'),
    mc('Two loans offer the same monthly payment. One lasts 3 years, one lasts 5. Which costs more in total?',
       ['The 5-year loan', 'The 3-year loan', 'They cost the same'], 0,
       'Same payment, more months, more money.'),
    tf('A smaller monthly payment can mean a higher total cost.', True, 'You are paying interest for longer.'),
])

DISC = doc('bill', 'Lakeshore Credit Union', [
    ('amount', 'Amount you receive', 2000.00),
    ('fee', 'Origination fee, paid at signing', 100.00)],
    subtitle='Personal loan disclosure', meta=[['Interest rate', '10% a year'], ['Term', '12 months, repaid at the end']],
    note='The fee is part of what this loan costs you.')
assert 2000 * 0.10 == 200 and 200 + 100 == 300 and 300 / 2000 == 0.15
fees = lesson('ia-fees-in-apr', 'Fees Inside the APR', 'Read a loan disclosure and find the cost the rate leaves out.', [
    mc('What is the origination fee on this loan?', ['A $100 charge for setting up the loan', 'Interest the lender takes in advance', 'A deposit you get back at the end'], 0,
       'It’s a cost of borrowing, and you don’t get it back.',
       context='An [[origination fee]] is money the lender takes for setting up the loan. [[APR]] is meant to include fees like this, so you can compare offers. The interest rate alone can make a loan look cheaper than it is.',
       doc=DISC),
    num('How much interest will the $2,000 cost over the year at 10%?', 200, '$2,000 × 0.10 = $200.', doc=DISC),
    num('Add the fee. What does this loan cost you in total?', 300, '$200 interest + $100 fee = $300.', doc=DISC),
    num('That $300 is what percent of the $2,000 you borrowed?', 15, '$300 ÷ $2,000 = 0.15, which is 15%. The headline rate said 10%.', unit='%', doc=DISC),
    tf('The interest rate and the APR can be different numbers when a loan has fees.', True,
       'The APR rolls the fee into the yearly cost.'),
    mc('Two loans both say 10% interest. One has a $100 fee and one has none. What do you compare?',
       ['The APR, or the total dollars you pay', 'The interest rate alone', 'The monthly payment alone'], 0,
       'Dollars out the door beat a single percentage.',
       why=['', 'Both say 10%. The fee is what makes one dearer.', 'A small payment can hide a longer or costlier loan.']),
], fmt='document')

maya_story = {
    'title': 'The phone plan',
    'character': 'Maya, 26, barista',
    'body': 'Maya’s phone died. The shop will finance a **$840** phone: **$35** a month for **36** months. No money down.\n\n'
            'She can also buy a refurbished phone for **$220** in cash. She has **$300** in savings and did not want to touch it.',
}
assert 35 * 36 == 1260 and 1260 - 840 == 420
maya = lesson('ia-maya', 'Maya’s Phone', 'A small monthly number can double the price of a phone.', [
    num('How much does Maya pay in total on the 36-month plan?', 1260, '$35 × 36 = $1,260.'),
    num('How much extra is that, above the $840 price?', 420, '$1,260 − $840 = $420.'),
    num('How much does she save by paying $220 cash instead of the plan’s $1,260?', 1040, '$1,260 − $220 = $1,040.'),
    mc('The $35 payment fits her month easily. What is still true?',
       ['The plan costs $420 more than the phone’s price', 'The plan is free', 'Cash always costs more'], 0,
       'A payment that fits can still be a bad price.'),
    tf('Using $220 of her $300 savings leaves her with some cash still set aside.', True, '$300 − $220 = $80 left.'),
    mc('What is the careful comparison?',
       ['Total dollars, not the size of the monthly payment', 'Whichever offer says 0% in the ad', 'The number of months alone'], 0,
       '36 small payments hid a $420 charge.'),
], fmt='story', story=maya_story)

trial_steps = [
    num('$2,500 at 8% simple interest for 2 years. How much interest?', 400, '$2,500 × 0.08 × 2 = $400.'),
    num('$500 balance at 24% APR. About how much interest in one month? Use a 2% monthly rate.', 10, '$500 × 0.02 = $10.'),
    mc('A one-year loan charges $160 of interest and a $40 fee on $2,000 borrowed. What did the year cost?',
       ['$200', '$160', '$40'], 0, '$160 + $40 = $200.'),
    tf('APY is the yearly cost of a credit card.', False, 'APY is what savings earn. APR is the borrowing cost.'),
]

lessons = [kept('dc-apr'), simple, monthly, apy, offers, total, fees, maya,
           review('ia'), trial('ia', 'Interest & APR', trial_steps)]
write_unit('02-interest-apr.json', 'interest-apr', 2, 'Interest & APR',
           'How interest builds, how APR differs from APY, and where fees hide.',
           'The rate is the bite. The fee is the second bite.', terms, lessons, section=S)
