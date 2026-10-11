from lib import *

S = 'home-life'
terms = {
    'adjustable-rate-mortgage': term('Adjustable-rate mortgage',
                                     'A mortgage whose interest rate can change after a starter period. The payment can rise.',
                                     'An ARM at $1,100 a month for five years. The estimate says it could become $1,450.'),
    'amortization': term('Amortization',
                         'The schedule that splits each mortgage payment into interest and principal. Early payments are mostly interest.',
                         'A $1,200 payment. The first month, $1,000 is interest and $200 is principal.'),
    'mortgage-points': term('Points',
                            'An upfront fee equal to 1% of the loan for each point. You pay it at closing to get a lower rate. It pays off only if you keep the loan long enough.',
                            'One point on a $200,000 loan is $2,000.'),
    'refinancing': term('Refinancing',
                        'Replacing your mortgage with a new one, usually to lower the rate or the payment. You pay closing costs again.',
                        'A refinance that costs $4,000 and saves $100 a month takes 40 months to break even.'),
}

what = lesson('mg-what', 'What You Are Paying', 'A mortgage is the loan. The payment is not all principal.', [
    info('The loan, named',
         'A [[mortgage]] is a loan to buy a home, usually paid over 15 or 30 years. The house is the collateral.\n\nEach payment has [[interest]] and [[principal]]. On a **$200,000** loan, a **$1,200** payment can send most of the early dollars to interest.'),
    mc('What is a mortgage?',
       ['A loan used to buy a home, paid back over many years', 'The cash you pay up front so you borrow less', 'A fee the seller pays at closing'], 0,
       'The down payment is the cash up front. The mortgage is what you still owe.'),
    mc('What is the collateral on a home loan?',
       ['The house', 'Your paycheck', 'The inspection'], 0,
       'If you do not pay, the lender can take the house.'),
    tf('The first payments on a typical mortgage are mostly principal.', False,
       'They are mostly interest. Principal is the smaller slice at the start.'),
    fill('The part of the payment that reduces what you owe is the ___.',
         ['principal', 'interest', 'premium'], 0,
         'Principal pays the loan down. Interest is the cost of borrowing.'),
])

fixed_doc = doc('statement', 'Fixed rate', [
    ('pay', 'Principal and interest', 1200),
], subtitle='Stays $1,200', meta=['6% for the whole term'])
arm_doc = doc('statement', 'Adjustable rate', [
    ('pay', 'Principal and interest, for now', 1100),
], subtitle='Can become $1,450', meta=['5% for 5 years, then it can change'])
assert 1200 - 1100 == 100 and 1450 - 1200 == 250

arm = lesson('mg-arm', 'Fixed or Adjustable', 'The cheaper payment today can be the expensive one later.', [
    num('How much less is the adjustable payment today?', 100,
        '$1,200 − $1,100 = $100.',
        context='A fixed rate keeps the same [[interest]] rate. An [[adjustable-rate mortgage]] can change after the starter period.',
        docs=[fixed_doc, arm_doc]),
    num('If the adjustable payment becomes $1,450, how much more is that than the fixed $1,200?', 250,
        '$1,450 − $1,200 = $250.', docs=[fixed_doc, arm_doc]),
    mc('You will keep the loan for 30 years and you need a payment that cannot jump. Which page fits?',
       ['The fixed rate', 'The adjustable rate', 'Either. The law freezes both'], 0,
       'The fixed page stays at $1,200. The adjustable page says it can become $1,450.',
       why=['The rate and the payment stay.', 'The starter rate ends.', 'Nothing freezes an ARM at the starter payment.'],
       docs=[fixed_doc, arm_doc]),
    tf('The adjustable payment on this page is promised for all 30 years.', False,
       'It is promised for the starter period. After that it can rise.'),
    fill('The loan whose rate can change is the ___ one.',
         ['adjustable', 'fixed', 'insured'], 0,
         'Adjustable means it can move. Fixed means it stays.'),
], fmt='call')

years = lesson('mg-years', '15 Years or 30', 'The shorter loan costs more each month and less in interest.', [
    info('This lender’s estimate',
         'Same **$200,000** loan. The 30-year estimate charges **$232,000** of interest over the life of the loan. The 15-year estimate charges **$104,000**.\n\nThe 30-year payment shown is **$1,200**. The 15-year payment shown is **$1,700**. These are the lender’s figures, not a formula to memorize.'),
    num('How much less interest does the 15-year estimate charge?', 128000,
        '$232,000 − $104,000 = $128,000.'),
    num('How much more is the 15-year payment each month?', 500,
        '$1,700 − $1,200 = $500.'),
    num('What do you pay extra each year if you take the 15-year payment?', 6000,
        '$500 × 12 = $6,000 a year, in exchange for far less interest over the life of the loan.'),
    tf('The 30-year loan is cheaper in total interest on this estimate.', False,
       'It is cheaper each month. Over the life of the loan it costs $128,000 more in interest.'),
])

amort = lesson('mg-amort', 'Where the Payment Goes', 'Early on, you are mostly paying for the loan, not paying it off.', [
    info('One month, up close',
         '[[Amortization]] splits the payment. Balance **$200,000**. This month’s interest is **$1,000**. The payment is **$1,200**.\n\nLater, interest is **$600** on a smaller balance, and more of the same $1,200 hits principal.'),
    num('Payment $1,200 and interest $1,000. How much principal do you pay this month?', 200,
        '$1,200 − $1,000 = $200.'),
    num('The balance was $200,000. After that $200 of principal, what do you owe?', 199800,
        '$200,000 − $200 = $199,800.'),
    num('A later month: interest is $600 of the same $1,200 payment. How much is principal then?', 600,
        '$1,200 − $600 = $600.'),
    mc('Why does the early payment feel slow?',
       ['Most of it is interest', 'The lender keeps the principal and applies it at the end', 'Principal is optional in the first five years'], 0,
       'The interest is the cost of a large balance. As the balance falls, the interest slice shrinks.'),
])

points = lesson('mg-points', 'Points', 'You pay interest up front for a lower rate later.', [
    info('One point, one percent',
         'One [[points|mortgage-points]] is **1%** of the loan, paid at closing. On **$200,000**, one point is **$2,000**.\n\nIn this example it saves **$50** a month. You need **40** months to get the $2,000 back. If you sell before that, the point was a loss.'),
    num('What is one point on a $200,000 loan?', 2000, '$200,000 × 0.01 = $2,000.'),
    num('The point saves $50 a month. How many months to earn back $2,000?', 40,
        '$2,000 ÷ $50 = 40 months.', unit='months'),
    num('You sell after 24 months. How much of the $2,000 have the monthly savings not covered yet?', 800,
        '24 × $50 = $1,200. $2,000 − $1,200 = $800 still uncovered.'),
    tf('Points are always worth it because a lower rate is always better.', False,
       'They are worth it if you keep the loan past the break-even month. A short stay can make them a loss.'),
])

estimate = doc('statement', 'Loan Estimate', [
    ('loan', 'Loan amount', 200000),
    ('pi', 'Principal and interest, monthly', 1200),
    ('close', 'Estimated closing costs', 6000),
    ('down', 'Down payment', 40000),
], subtitle='Fixed rate', meta=['6% fixed'],
   totals=[('Estimated cash to close', 46000, True)])
assert 40000 + 6000 == 46000

page = lesson('mg-estimate', 'The Loan Estimate', 'The shopping page. Compare it before you fall in love with a house.', [
    info('Read the cash, not just the rate',
         'A Loan Estimate shows the loan, the monthly principal and interest, the [[closing costs]], and the cash to close.\n\nThis one is a **$200,000** loan. Cash to close is the **$40,000** [[down payment]] plus **$6,000** of costs.'),
    num('What is the estimated cash to close?', 46000,
        '$40,000 + $6,000 = $46,000.', doc=estimate),
    num('What is the monthly principal and interest on this estimate?', 1200,
        'The page lists it: $1,200. Tax and insurance are not in that line.', doc=estimate),
    mc('Two lenders offer the same rate. One’s closing costs are $2,000 higher. What is the honest comparison?',
       ['The higher closing costs make that loan more expensive up front', 'The rates match, so the loans match', 'Pick the longer packet'], 0,
       'The rate is one line. The cash to close is another.'),
    tf('The $1,200 line is your whole housing payment, including tax and insurance.', False,
       'It is principal and interest only. Escrow for tax and insurance would be extra.'),
], fmt='document')

refi = lesson('mg-refi', 'Refinancing', 'A new loan is worth it when the savings outlast the costs.', [
    info('Pay the cover charge again',
         '[[Refinancing]] replaces the old [[mortgage]] with a new one. This example costs **$4,000** to close and saves **$100** a month.\n\nBreak-even is **40** months. A move in two years does not get there.'),
    num('Closing costs are $4,000 and you save $100 a month. How many months to break even?', 40,
        '$4,000 ÷ $100 = 40 months.', unit='months'),
    num('You will move in 24 months. How short of the 40-month break-even is that?', 16,
        '40 − 24 = 16 months short.'),
    mc('You will move in two years. What does this example say?',
       ['Do not refinance. You will not earn back the $4,000', 'Refinance, because any lower rate is a win', 'Refinance and roll the $4,000 in so it becomes free'], 0,
       'Rolling the cost into the loan does not erase it. You still pay it, with interest.'),
    tf('A refinance with a lower rate is free if you do not write a check at closing.', False,
       'The cost can be added to the loan. It is still a cost.'),
])

luis_story = {
    'title': 'Luis pays a little extra',
    'character': 'Luis, 34',
    'body': 'Luis is 34. His required principal and interest is **$1,200**. He adds **$100** when the month allows.\n\nIn a month where interest is **$1,000**, the required principal is **$200**. The extra $100 makes that month’s principal **$300**.\n\nHe does not send the extra $100 if it would empty his emergency fund. A paid-down loan is a poor trade for a car repair you cannot cover.',
}
extra = lesson('mg-extra', 'Extra Payments', 'A small extra payment hits principal. It is not a fee.', [
    num('Luis adds $100 a month. How much extra principal is that in a year?', 1200,
        '$100 × 12 = $1,200.'),
    num('Interest is $1,000 of a $1,200 payment. With no extra, how much is principal?', 200,
        '$1,200 − $1,000 = $200.'),
    num('He adds $100 that month. How much principal does he pay?', 300,
        '$200 + $100 = $300.'),
    mc('The emergency fund is down to one week of expenses. Should he send the extra $100?',
       ['No. Refill the cushion first', 'Yes. Principal always outranks a cushion', 'Yes, but put the $100 on a credit card'], 0,
       'The extra payment is optional. The cushion is what keeps a surprise from becoming debt.'),
    tf('An extra principal payment is the same thing as buying points.', False,
       'Points are an upfront fee for a lower rate. An extra payment reduces the balance directly.'),
], fmt='story', story=luis_story)

trial_steps = [
    mc('Which loan can raise the payment after a starter period?',
       ['An adjustable-rate mortgage', 'A fixed-rate mortgage', 'A security deposit'], 0,
       'Adjustable means the rate can change. Fixed stays.'),
    num('One point on a $150,000 loan. How many dollars is that?', 1500,
        '$150,000 × 0.01 = $1,500.'),
    num('A refinance costs $3,000 and saves $150 a month. How many months to break even?', 20,
        '$3,000 ÷ $150 = 20 months.', unit='months'),
    tf('Early mortgage payments are mostly principal.', False,
       'They are mostly interest. Principal is the small slice at the start.'),
]

lessons = [what, arm, years, amort, points, page, refi, extra,
           review('mg'), trial('mg', 'Mortgages', trial_steps)]
write_unit('05-mortgages.json', 'mortgages', 5, 'Mortgages',
           'Fixed and adjustable loans, where the payment goes, and when a refinance pays off.',
           'The rate is the headline. The cash to close and the break-even are the decision.', terms, lessons, section=S)
