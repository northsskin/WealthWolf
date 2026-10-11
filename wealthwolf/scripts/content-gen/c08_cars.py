from lib import *

S = 'credit-debt'
terms = {
    'down-payment': term('Down payment', 'Cash you pay up front so you borrow less.',
                         'A $16,000 car with $2,000 down means you borrow $14,000.'),
    'car-lease': term('Lease', 'A deal where you pay to use a car for a set number of months, then give it back. You do not own it at the end.',
                      '$250 a month for 36 months is $9,000 to drive the car, and then you hand the keys back.'),
    'upside-down': term('Upside down', 'Owing more on a car than the car is worth.',
                       'You owe $11,000. The car is worth $8,000. You are upside down by $3,000.'),
}

short_lines = [
    ('pay', 'Monthly payment', 380),
    ('mos', 'Months', 48),
]
long_lines = [
    ('pay', 'Monthly payment', 300),
    ('mos', 'Months', 72),
]
assert 380 * 48 == 18240 and 300 * 72 == 21600
assert 18240 - 16000 == 2240 and 21600 - 16000 == 5600
SHORT = doc('statement', '4-year loan', short_lines, subtitle='Borrow $16,000', totals=[('Total of the payments', 18240, True)])
LONG = doc('statement', '6-year loan', long_lines, subtitle='Borrow $16,000', totals=[('Total of the payments', 21600, True)])

total = lesson('cl-total', 'What the Car Really Costs', 'Price on the window, plus every payment after it.', [
    num('You borrow $16,000 and pay $380 a month for 48 months. What do the payments add up to?', 18240, '$380 × 48 = $18,240.'),
    num('How much of that is interest?', 2240, '$18,240 − $16,000 = $2,240.'),
    num('Add a $2,000 down payment you already paid. How much cash left you in total?', 20240, '$18,240 + $2,000 = $20,240.'),
    mc('Which number is the real cost of the purchase?',
       ['Every payment, plus the down payment', 'The monthly payment alone', 'The price before tax'], 0,
       'The monthly number is the bait.'),
    tf('A car priced at $16,000 costs $16,000 if you finance it.', False, 'Interest sits on top. This loan added $2,240.'),
    fill('Interest is the total of the payments minus the ___.', ['principal', 'down payment', 'tax'], 0,
         'You borrowed $16,000. That is the principal in this loan.'),
])

length = lesson('cl-length', 'Shorter Loan, Smaller Total', 'Stretch the loan and the payment shrinks. The interest does the opposite.', [
    num('The 4-year loan: how much interest on $16,000?', 2240, '$18,240 − $16,000 = $2,240.',
        context='Same car, same amount borrowed. More months means more interest.', docs=[SHORT, LONG]),
    num('The 6-year loan: how much interest?', 5600, '$21,600 − $16,000 = $5,600.', docs=[SHORT, LONG]),
    num('How much extra interest does the longer loan cost?', 3360, '$5,600 − $2,240 = $3,360.'),
    mc('The 6-year payment is $80 smaller. Why can it still be the worse deal?',
       ['You pay $3,360 more interest', 'Shorter loans are illegal', 'The car costs less on the long loan'], 0,
       '$300 looks easier. The total is $21,600 instead of $18,240.',
       why=['$3,360 more interest.', 'Both loans are ordinary.', 'You borrowed $16,000 either way.']),
    tf('Pick the longest loan whenever the monthly payment is the only number you can see.', False,
       'See the total before you pick the term.'),
    mc('You can afford $380. What is the careful choice?',
       ['The shorter loan, if the $380 fits after needs', 'The longer loan, to keep cash “free” for more spending', 'Skip the total and sign'], 0,
       'If the higher payment fits, you buy the same car for less.'),
], fmt='call')

down = lesson('cl-down', 'The Down Payment', 'Cash now, less borrowed, less interest later.', [
    mc('What does a down payment do?', ['It cuts the amount you have to borrow', 'It raises the interest rate', 'It is a fee the dealer keeps on top of the price'], 0,
       'You pay cash so the loan is smaller.',
       context='A [[down payment]] is cash at the start. On a $16,000 car, $2,000 down means the [[principal]] is $14,000, not $16,000.'),
    num('Price $18,000. Down payment $3,000. How much do you borrow?', 15000, '$18,000 − $3,000 = $15,000.'),
    num('You borrow that $15,000 at 6% simple interest for 1 year, as a rough look. How much interest?', 900, '$15,000 × 0.06 = $900.'),
    num('Same rate and year with no down payment, borrowing the full $18,000. How much interest?', 1080, '$18,000 × 0.06 = $1,080.'),
    num('How much interest does the $3,000 down payment save in that rough year?', 180, '$1,080 − $900 = $180.'),
    tf('A down payment is wasted money because you could have financed the whole price.', False,
       'It is money you were going to pay anyway, and it shrinks the interest.'),
])

lease = lesson('cl-lease', 'Buy or Lease', 'A lease rents the car. A loan is a path to owning it.', [
    mc('At the end of a lease, what do you usually have?',
       ['Nothing. You give the car back', 'The car, free and clear', 'A second car'], 0,
       'You paid for the use, not the title.',
       context='A [[lease|car-lease]] (the car kind) is paying to drive a car for a set term, then returning it. Miles over the limit cost extra. A loan ends with a car you own, if you finish the payments.'),
    num('A lease is $250 a month for 36 months. How much do you pay to use the car?', 9000, '$250 × 36 = $9,000.'),
    num('A loan is $320 a month for 48 months. How much do you pay?', 15360, '$320 × 48 = $15,360.'),
    mc('The lease costs less cash over its term. What do you not get?',
       ['Ownership. You hand the car back', 'The right to drive it during the lease', 'A monthly payment'], 0,
       '$9,000 of driving, then no car. The loan costs more and leaves you the car.'),
    tf('Going over the mileage limit on a lease can cost an extra fee per mile.', True,
       'The cheap payment assumes you stay under the cap.'),
    mc('You drive 18,000 miles a year and the lease allows 10,000. What is the risk?',
       ['A big mileage bill when you return it', 'Nothing. Limits are suggestions', 'The loan gets cheaper'], 0,
       'Match the contract to how you actually drive.'),
])

order_lines = [
    ('price', 'Sale price', 11000),
    ('tax', 'Sales tax', 770),
    ('doc', 'Document fee', 150),
    ('paint', 'Paint protection package', 799),
]
assert 11000 + 770 + 150 + 799 == 12719
ORDER = doc('receipt', 'Buyer’s order', order_lines, subtitle='You did not ask for paint protection',
            totals=[('Amount due', 12719, True)])
addons = lesson('cl-addons', 'Dealer Add-Ons', 'Tap the charge you never agreed to.', [
    spot('Which line is the add-on you did not ask for?', ORDER, 'paint',
         'Paint protection, $799, was not part of the car you agreed to buy.',
         context='A buyer’s order should match the deal you discussed. Extra packages are easy to bury in the total.'),
    num('How much is the paint protection?', 799, 'The line says $799.', doc=ORDER),
    num('What would the total be without that $799?', 11920, '$12,719 − $799 = $11,920.'),
    mc('The dealer says the package is “already on the car.” What can you do?',
       ['Ask for it to be removed from the contract before you sign', 'You must pay it', 'Drive away and let them bill you later'], 0,
       'Before you sign, the line can come off. After you sign, it is yours.'),
    tf('A document fee and an unwanted protection package are the same kind of charge.', False,
       'A filing fee can be ordinary. A $799 package you did not ask for is optional, and optional means you can say no.'),
    mc('Where do you catch this?',
       ['On the buyer’s order, before your signature', 'A month later, on a guess', 'Never. Add-ons are free'], 0,
       'Read every line. The total is not the only number.'),
], fmt='spot')

upside = lesson('cl-upside', 'Upside Down', 'The loan can outlive the car’s value.', [
    mc('What does upside down mean on a car loan?',
       ['You owe more than the car is worth', 'The car is paid off', 'You have equity'], 0,
       'The loan is heavier than the car.',
       context='You are [[upside down]] when the balance is higher than the car’s value. Sell it and you still owe the gap. A long loan and a small down payment get you there faster.'),
    num('You owe $11,000. The car is worth $8,000. How much is the gap?', 3000, '$11,000 − $8,000 = $3,000.'),
    tf('You owe $12,500 and the car is worth $13,000. You are upside down.', False,
       'The car is worth $500 more than the loan. Upside down means the loan is bigger.'),
    mc('You sell the car for $8,000 and still owe $11,000. What happens?',
       ['You still owe the $3,000 gap', 'The loan disappears with the car', 'The buyer pays the gap for you'], 0,
       'Selling the car does not sell the rest of the loan.'),
    mc('Which habit makes upside-down less likely?',
       ['A bigger down payment and a shorter loan', 'Zero down and a 7-year term', 'Rolling an old loan into the new one'], 0,
       'Borrow less, and pay it off before the car’s value falls past it.'),
    num('You are $3,000 upside down and the dealer offers to add that gap onto a new loan. How much extra principal are you dragging forward?', 3000,
        'The whole $3,000. The new car starts life already partly unpaid.'),
])

refi = lesson('cl-refi', 'Refinancing the Car', 'A lower rate helps. A longer term can give the savings back.', [
    num('Your payment is $320. A new loan would be $280. How much a month do you keep?', 40, '$320 − $280 = $40.'),
    num('How much is that over a year?', 480, '$40 × 12 = $480.'),
    mc('The new loan is cheaper each month because it lasts two extra years. What else must you check?',
       ['The total you will pay, not just the $40', 'Nothing. A smaller payment is always cheaper', 'The color of the car'], 0,
       'A longer loan can cost more interest even when the payment drops.'),
    tf('Refinancing makes sense when the new loan’s total cost is lower, and the payment still fits.', True,
       'Rate, term, and fees. All three.'),
    num('The new lender charges a $200 fee. After a year of saving $480, how much are you ahead of that fee?', 280,
        '$480 − $200 = $280. Still ahead, if you keep the loan long enough to get there.'),
    mc('You are upside down and the new lender says no. What is a reasonable next step?',
       ['Keep the current loan and pay extra toward it', 'Skip payments until they say yes', 'Trade the car in and roll the gap again'], 0,
       'Extra principal is a refinance you give yourself.'),
])

sofia_story = {
    'title': 'The used car',
    'character': 'Sofia, 28, medical assistant',
    'body': 'Sofia finds a used car for **$12,000**. She has **$2,000** saved for a down payment, so she would borrow **$10,000**. The lender offers **48** payments of **$230**.\n\n'
            'A dealer also waves a **$699** protection package and a 72-month loan with a smaller payment. She wants the car for work, and she wants to own it.',
}
assert 230 * 48 == 11040 and 11040 - 10000 == 1040 and 2000 + 11040 == 13040
sofia = lesson('cl-sofia', 'Sofia Buys Used', 'She can own the car. The package is optional.', [
    num('How much interest is in the 48 payments of $230?', 1040, '48 × $230 = $11,040. $11,040 − $10,000 = $1,040.'),
    num('Add the $2,000 down payment. How much does Sofia pay for the $12,000 car, before the package?', 13040,
        '$11,040 + $2,000 = $13,040.'),
    mc('What does the $699 package do to the deal if she did not ask for it?',
       ['It adds $699 she can refuse before signing', 'It is required by law', 'It lowers the interest'], 0,
       'Optional means optional.'),
    tf('The 72-month offer is automatically cheaper because the payment is smaller.', False,
       'A longer term often adds interest. She should see the total.'),
    num('She pays an extra $50 a month on the $230 loan. How much principal does that extra $50 cut in one month?', 50,
        '$50. Extra, on top of the payment, goes to principal.'),
    mc('She needs the car for work and can afford $230. What fits the goal of owning it?',
       ['The 48-month loan, $2,000 down, no package she did not ask for', 'The longest loan and every package', 'A lease that ends with no car'], 0,
       'Shorter loan, real down payment, no extras.'),
], fmt='story', story=sofia_story)

trial_steps = [
    num('Borrow $9,000. Pay $250 a month for 48 months. How much interest is that?', 3000, '$250 × 48 = $12,000. $12,000 − $9,000 = $3,000.'),
    num('A $14,000 car with $4,000 down. How much do you borrow?', 10000, '$14,000 − $4,000 = $10,000.'),
    tf('At the end of a car lease you usually own the car.', False, 'You give it back, unless you pay extra to buy it.'),
    mc('You owe $7,500 and the car is worth $6,000. What are you?',
       ['Upside down by $1,500', 'Ahead by $1,500', 'Paid off'], 0, '$7,500 − $6,000 = $1,500 still owed above the car’s value.'),
]

lessons = [total, length, down, lease, addons, upside, refi, sofia,
           review('cl'), trial('cl', 'Car Loans & Leases', trial_steps)]
write_unit('08-car-loans.json', 'car-loans', 8, 'Car Loans & Leases',
           'The payment, the term, the add-ons, and whether you end up owning the car.',
           'The monthly payment is the bait. The total is the hook.', terms, lessons, section=S)
