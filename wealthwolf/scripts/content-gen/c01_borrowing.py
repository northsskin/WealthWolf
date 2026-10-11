from lib import *
from preserved import kept, kept_term

S = 'credit-debt'
terms = {
    'debt': kept_term('debt'),
    'loan': kept_term('loan'),
    'credit-card': kept_term('credit-card'),
    'good-debt': kept_term('good-debt'),
    'bad-debt': kept_term('bad-debt'),
    'mortgage': kept_term('mortgage'),
    'principal': term('Principal', 'The amount you borrowed, not counting interest.', 'Borrow $2,400 for a laptop. The principal is $2,400.'),
    'secured-loan': term('Secured loan', 'A loan backed by something the lender can take if you stop paying, such as a car.',
                         'A car loan: miss enough payments and the lender can take the car.'),
    'unsecured-loan': term('Unsecured loan', 'A loan with no property behind it. The lender trusts you to pay, and charges more when that trust is thin.',
                           'Most credit cards and many personal loans are unsecured.'),
    'cosigner': term('Co-signer', 'Someone who signs a loan with you and has to pay it if you do not.',
                     'A parent co-signs a $4,000 loan. If you miss payments, the lender can collect from your parent.'),
}

cost = lesson('dc-what-it-costs', 'What Borrowing Costs', 'You pay back more than you borrowed. That gap is the price.', [
    mc('You borrow $800 and pay back $920. What is the extra $120?', ['Interest', 'Principal', 'A fee the store keeps'], 0,
       'The extra is the price of the loan.',
       context='[[Debt]] means you pay the money back. The extra on top is [[interest]], and this time you are the one paying it.'),
    num('You borrow $3,000 and pay back $3,450. How much interest did you pay?', 450, '$3,450 − $3,000 = $450.'),
    tf('If a friend lends you $200 and you pay back exactly $200, you paid no interest.', True,
       'No extra money changed hands. You still owed the $200 until you paid it.'),
    mc('Which borrowing is closest to good debt?',
       ['A low-rate loan for training that raises your pay', 'A vacation on a card you cannot pay off', 'New shoes you do not need, financed for a year'], 0,
       'Cheap borrowing that builds your future can be worth it. The other two are expensive and gone fast.',
       why=['A skill that raises your pay can outlast the loan.', 'High interest, and the trip is over.', 'The shoes wear out. The payments do not.']),
    mc('Why do lenders charge interest?', ['They are paid for letting you use their money', 'The law says every loan costs 10%', 'Interest is a tax'], 0,
       'Their money is busy working for you, so they charge rent on it.'),
    num('A $1,500 loan costs $180 in interest. How much do you pay back in total?', 1680, '$1,500 + $180 = $1,680.'),
])

principal = lesson('dc-principal', 'Principal and Interest', 'One part is what you borrowed. The other part is the price.', [
    mc('You borrow $2,000. In loan words, what is that $2,000 called?', ['Principal', 'Interest', 'A credit limit'], 0,
       'Principal is the amount you borrowed.',
       context='The [[principal]] is the amount you borrowed, not counting interest. Pay $2,200 back on a $2,000 loan and $200 of it is interest.'),
    num('Principal $4,000. You pay back $4,640. How much is interest?', 640, '$4,640 − $4,000 = $640.'),
    num('Each month you pay $150. $110 of it cuts the principal. How much of the payment is interest?', 40, '$150 − $110 = $40.'),
    tf('Paying extra, above the required payment, usually cuts the principal faster.', True,
       'Less principal left means less interest next time.'),
    mc('Two loans, same principal. One charges more interest. Which costs more in total?',
       ['The one with more interest', 'They cost the same', 'The one you pay first'], 0,
       'Same amount borrowed, higher price.'),
    fill('The amount you borrowed, before interest, is the ___.', ['principal', 'interest', 'due date'], 0, 'Principal first. Interest is the extra.'),
])

secured = lesson('dc-secured', 'Secured or Unsecured', 'Some loans have something to take. Some only have your promise.', [
    mc('A car loan lets the lender take the car if you stop paying. What kind of loan is that?',
       ['Secured', 'Unsecured', 'A gift'], 0, 'The car is the backup.',
       context='A [[secured loan]] is backed by something the lender can take, like the car. An [[unsecured loan]] has no property behind it. A typical [[credit card]] is unsecured, which is one reason its interest is often high.'),
    sort('Secured or unsecured?', ['Secured', 'Unsecured'],
         [('Car loan, and the lender can take the car', 0), ('Loan for a boat, and the lender can take the boat', 0),
          ('Ordinary credit card', 1), ('Personal loan with no property behind it', 1), ('Store card', 1)]),
    tf('An unsecured loan is always cheaper than a secured one.', False,
       'No collateral usually means a higher rate, not a lower one.'),
    mc('You stop paying a secured car loan. What can the lender do?',
       ['Take the car and sell it', 'Nothing, the car is yours', 'Erase the loan'], 0,
       'That is the deal you signed.'),
    mc('Why might a lender offer a lower rate on a secured loan?',
       ['They can take the property if you do not pay', 'The loan is smaller, so the bank charges less', 'Your credit score stops mattering'], 0,
       'Less risk for them, so they can charge less.'),
    match('Match each loan to what sits behind it.',
          [('Car loan', 'The car'), ('Typical credit card', 'Only your promise to pay'), ('Boat loan', 'The boat')]),
], fmt='sort')

agree_lines = [
    ('prin', 'Amount borrowed (principal)', 2400),
    ('int', 'Interest over the full loan', 360),
    ('mon', 'Monthly payment', 115),
]
assert 115 * 24 == 2760 and 2760 - 2400 == 360
AGREE = doc('statement', 'Northline Credit Union', agree_lines, subtitle='Personal loan agreement',
            meta=[['Term', '24 months'], ['Amount you receive', '$2,400']],
            totals=[('Total you pay back', 2760, True)],
            note='24 payments of $115. Miss a payment and a late fee can be added.')
agreement = lesson('dc-agreement', 'The Loan Agreement', 'The page you sign is the whole deal. Read it.', [
    num('What is the principal on this agreement?', 2400, 'The amount borrowed: $2,400.',
        context='A loan agreement is the written deal: how much you borrow, what you pay, and how long it lasts.',
        doc=AGREE),
    num('How much interest do you pay over the full 24 months?', 360, 'The interest line: $360.', doc=AGREE),
    num('What do you pay back in total?', 2760, '$2,400 + $360 = $2,760. That matches 24 × $115.', doc=AGREE),
    num('Check the monthly payment against the total. $2,760 ÷ 24 months equals?', 115, '$2,760 ÷ 24 = $115.'),
    tf('Once you sign, a late payment can cost an extra fee on top of the payment.', True,
       'The note says so. The payment is not the only number that matters.'),
    mc('What should you know before you sign?',
       ['The total you will pay, not just the monthly payment', 'Only the monthly payment', 'Only the interest rate'], 0,
       'The monthly number hides the $360.'),
], fmt='document')

offer_a = [
    ('pay', 'Monthly payment', 200),
    ('mos', 'Number of payments', 36),
]
offer_b = [
    ('pay', 'Monthly payment', 140),
    ('mos', 'Number of payments', 60),
]
assert 200 * 36 == 7200 and 140 * 60 == 8400
OFFER_A = doc('statement', 'Offer A · shorter loan', offer_a, subtitle='Borrow $6,000',
              totals=[('Total you pay', 7200, True)])
OFFER_B = doc('statement', 'Offer B · longer loan', offer_b, subtitle='Borrow $6,000',
              totals=[('Total you pay', 8400, True)])
afford = lesson('dc-afford', 'Can You Afford the Payment?', 'A payment that fits this month can still cost more overall.', [
    num('You bring home $2,800. Needs take $2,200. How much is left?', 600, '$2,800 − $2,200 = $600.',
       context='A payment you cannot cover after needs is a payment you cannot afford. Run the numbers before you sign.'),
    mc('A loan wants $700 a month and you have $600 left after needs. What do you do?',
       ['Do not take it. The payment does not fit', 'Take it and skip groceries', 'Take it. The lender would not offer it otherwise'], 0,
       'If it does not fit, it is not affordable.'),
    num('Offer A: $200 × 36 payments. What do you pay in total?', 7200, '$200 × 36 = $7,200.', docs=[OFFER_A, OFFER_B]),
    num('Offer B: $140 × 60 payments. What do you pay in total?', 8400, '$140 × 60 = $8,400.', docs=[OFFER_A, OFFER_B]),
    num('How much more does Offer B cost than Offer A?', 1200, '$8,400 − $7,200 = $1,200.'),
    mc('Both loans hand you $6,000. Which one costs less overall?',
       ['Offer A, the shorter loan', 'Offer B, because the payment is smaller', 'They cost the same'], 0,
       'The smaller payment lasts longer and costs $1,200 more.',
       why=['$7,200 back, against $8,400.', 'Smaller each month, more in the end.', 'The totals on the two sheets do not match.']),
], fmt='call')

cosign = lesson('dc-cosign', 'Co-signing', 'Your name on someone else’s loan is your loan too.', [
    mc('You co-sign a friend’s $4,000 loan. They stop paying. What can the lender do?',
       ['Collect the payments from you', 'Nothing. You only wrote a reference', 'Take the debt off both of you'], 0,
       'A co-signer agrees to pay.',
       context='A [[co-signer|cosigner]] signs with the borrower and has to pay if the borrower does not. The loan can show on both credit records.'),
    tf('Co-signing is just a character reference. You cannot be made to pay.', False,
       'It is a legal promise to pay the debt.'),
    num('The friend misses payments and $1,600 is still owed. You are the co-signer. How much can the lender ask you for?', 1600,
        'The remaining $1,600. Co-signing means you owe it too.'),
    mc('Your own loan application asks about debts. Does the co-signed loan count?',
       ['Yes. Lenders treat it as your debt too', 'No. It is only the friend’s', 'Only if you live together'], 0,
       'It can use up room you needed for your own loan.'),
    mc('When is co-signing least risky?',
       ['When you can afford the full payment yourself, and you trust them to pay', 'When you cannot afford it', 'When you have not read the agreement'], 0,
       'Assume you might be the one paying.'),
    mc('The friend pays the loan off on time. What was the cost to you?',
       ['Maybe nothing in money, but your name was on the debt the whole time', 'A required $500 fee', 'You still owe half'], 0,
       'The risk was real even though the bill never landed on you.'),
])

leo_story = {
    'title': 'The first loan',
    'character': 'Leo, 22, warehouse associate',
    'body': 'Leo wants a $2,000 certificate course that could raise his pay. The school offers a loan: **$2,000** now, then **24** payments of **$105**.\n\n'
            'Leo brings home **$2,600** a month. Rent and other needs take **$2,150**. He has been late on a phone bill before, and his cousin offered to co-sign.',
}
assert 105 * 24 == 2520 and 2520 - 2000 == 520 and 2600 - 2150 == 450
leo = lesson('dc-leo', 'Leo’s First Loan', 'A course that raises pay can still be a bad loan.', [
    num('How much interest does Leo pay over the full loan?', 520, '24 × $105 = $2,520. $2,520 − $2,000 = $520.'),
    num('After needs, how much of Leo’s paycheck is left each month?', 450, '$2,600 − $2,150 = $450.'),
    mc('The payment is $105 and Leo has $450 left. Does the payment fit?',
       ['Yes. $105 is well under $450', 'No. $105 is more than he brings home', 'Only if his cousin co-signs'], 0,
       'The payment fits. Fitting is not the same as being worth it.'),
    mc('Leo has been late on bills. What is the risk if his cousin co-signs?',
       ['His cousin has to pay if Leo falls behind', 'The cousin’s name is only a reference', 'The loan becomes interest-free'], 0,
       'Co-signing puts the cousin on the hook.'),
    tf('Because the course might raise Leo’s pay, the loan is automatically good debt.', False,
       'Good debt is cheap borrowing that builds your future. $520 of interest on $2,000, plus a shaky payment history, is worth a hard look.'),
    mc('What is the careful move before Leo signs?',
       ['Compare the total cost, and ask if a cheaper way to pay for the course exists', 'Sign today so the seat does not vanish', 'Let his cousin sign without reading'], 0,
       'The monthly $105 is the easy number. The $2,520 is the real one.'),
], fmt='story', story=leo_story)

trial_steps = [
    num('You borrow $5,000 and pay back $5,800. How much is interest?', 800, '$5,800 − $5,000 = $800.'),
    mc('Which one lets the lender take the car if the payments stop?',
       ['A car loan', 'A typical credit card', 'Money a friend gave you as a gift'], 0,
       'The car backs the loan. A typical card has no property behind it.'),
    tf('A co-signer can be forced to pay the full remaining debt.', True, 'That is what the signature means.'),
    mc('You have $300 left after needs. The payment would be $450. What is true?',
       ['The payment does not fit', 'The payment fits easily', 'Lenders only offer payments you can afford'], 0,
       '$450 is more than $300.'),
]

lessons = [kept('dc-good-bad-debt'), cost, principal, secured, agreement, afford, cosign, leo,
           review('dc'), trial('dc', 'Borrowing Basics', trial_steps)]
write_unit('01-debt-credit.json', 'debt-credit', 1, 'Borrowing Basics',
           'What borrowing costs, what secures a loan, and whether the payment fits.',
           'Borrow the money. Read the leash before you sign.', terms, lessons, section=S)
