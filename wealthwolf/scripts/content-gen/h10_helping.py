from lib import *

S = 'home-life'
terms = {}

sink = lesson('hf-sink', 'Help Without Sinking', 'A gift that spends the rent creates a second emergency.', [
    info('Your bills stay funded',
         'Help is what you can give after rent and the [[emergency fund]] are covered.\n\nRent is **$1,400**. Other bills are **$1,100**. Income is **$3,000**. That leaves **$500** before any gift. A **$700** gift does not fit.'),
    num('Income is $3,000. Rent is $1,400 and other bills are $1,100. What is left before a gift?', 500,
        '$3,000 − $1,400 − $1,100 = $500.'),
    num('A relative asks for $700. How far past that $500 is the ask?', 200,
        '$700 − $500 = $200.'),
    mc('Which gift fits this month?',
       ['Up to $500, and only if the emergency fund is already intact', 'The $700, paid by skipping rent', 'The $700, on a new credit card'], 0,
       'The $500 is the room. Skipping rent or borrowing to donate creates the next crisis.'),
    tf('If the need is family, the rent can wait.', False,
       'Unpaid rent becomes your emergency. You cannot help for long from a place you are about to lose.'),
])

gift = doc('statement', 'A gift', [
    ('amt', 'You give', 2000),
], subtitle='You do not expect it back')
loan = doc('statement', 'A written loan', [
    ('amt', 'They repay', 2000),
    ('pay', 'Each month', 200),
], subtitle='Ten months')
assert 200 * 10 == 2000

kind = lesson('hf-kind', 'Gift or Loan', 'Say which one it is before the money moves.', [
    num('The loan is $200 a month until $2,000 is repaid. How many months is that?', 10,
        '$2,000 ÷ $200 = 10 months.',
        context='A gift is gone on purpose. A loan has an amount and a date, in writing.',
        docs=[gift, loan], unit='months'),
    mc('You will be hurt if you never see the $2,000 again. Which page matches that?',
       ['The written loan', 'The gift', 'Either. Family erases the difference'], 0,
       'If you need it back, it is a loan, and it needs a written amount and a date.',
       why=['A loan is the one you expect back.', 'A gift is money you have decided to lose.', 'The difference is whether you need it back.'],
       docs=[gift, loan]),
    mc('You can afford to lose $2,000, and you do not want to collect from your brother. Which page matches?',
       ['The gift', 'The written loan', 'A cosigned bank loan'], 0,
       'Call it a gift up front. A surprise loan is how holidays get ruined.',
       docs=[gift, loan]),
    tf('Calling it a gift later, after they miss payments, is the same as agreeing up front.', False,
       'The agreement has to exist when the money moves. A rewrite during a fight is not a plan.'),
    fill('If you need the money back, write down the amount and the ___.',
         ['date', 'excuse', 'party'], 0,
         'The date is what “back” means.'),
], fmt='call')

cosign = lesson('hf-cosign', 'Co-signing', 'Their loan becomes a loan you can be made to pay.', [
    info('You are not a reference',
         'A [[co-signer|cosigner]] has to pay if the borrower does not. On this **$12,000** family loan, the payment is **$250** a month.\n\nThree missed payments are **$750** already late. The other **$11,250** can still become yours too. “I only vouched” is not how the note reads.'),
    num('Three missed payments of $250. How much is already late?', 750, '$250 × 3 = $750.'),
    num('The loan is $12,000 and $750 is late. How much of the original loan is not in those three payments?', 11250,
        '$12,000 − $750 = $11,250. You can still be asked for that too.'),
    mc('Who can the lender require to pay?',
       ['You, the co-signer, for the whole loan if they do not pay', 'Only the relative who drives the car', 'Nobody, because it was a favor'], 0,
       'The signature is the promise. A favor does not shrink it.'),
    tf('Co-signing is safe if your credit score is higher than theirs.', False,
       'Your good credit is why they asked. It is also what the missed payments can damage.'),
])

bound = lesson('hf-bound', 'A Boundary', 'Pick the number before the ask, not during it.', [
    info('A cap you chose on a calm day',
         'Your cap is **$200** a month. An ask for **$500** is **$300** past it.\n\nThe boundary is the number you can say out loud. It is not a measure of how much you love someone.'),
    num('The ask is $500 and your cap is $200. How far over the cap is the ask?', 300,
        '$500 − $200 = $300.'),
    num('You hold the cap for 6 months. How much have you given?', 1200, '$200 × 6 = $1,200.'),
    mc('They ask again for $500, and the reason is urgent. What does a real boundary do?',
       ['Stay at $200, and help in non-money ways past that', 'Become $500, because urgency deletes a cap', 'Become $0, to prove a point'], 0,
       'Urgency is when a pre-committed number earns its keep.'),
    tf('A boundary means you never help.', False,
       'It means the help has a size. $200 is still help.'),
])

aging = lesson('hf-aging', 'Aging Parents', 'Daily help is a wage, and Medicare is not the wallet for it.', [
    info('Price the hours',
         'An aide at **$25** an hour, **8** hours a week, is **$200** a week. Across **4** weeks that is **$800** a month.\n\nMedicare generally does not pay for long-term daily help at home. [[Medicaid]] may, if your parent qualifies. Rules differ by state. This is not a benefits decision. It is the price of the hours.'),
    num('What does $25 an hour for 8 hours cost?', 200, '$25 × 8 = $200.'),
    num('What is that $200 week across 4 weeks?', 800, '$200 × 4 = $800.'),
    num('What is that help for a year, at $800 a month?', 9600, '$800 × 12 = $9,600.'),
    tf('Medicare generally pays for long-term daily help at home.', False,
       'It generally does not. Medicaid may, if the person qualifies. Check the state program rather than assuming the hospital coverage continues at home.'),
])

send = doc('receipt', 'Money abroad', [
    ('xfer', 'Value you want them to receive', 500),
    ('fee', 'Company fee', 15),
    ('fx', 'Exchange-rate cost', 20),
], totals=[('You pay', 535, True)],
   note='The rate cost is how much less a mid-market rate would have taken.')
assert 500 + 15 + 20 == 535

abroad = lesson('hf-abroad', 'Sending Money Abroad', 'The fee is the line you see. The rate is the line people skip.', [
    info('Two costs',
         'You want **$500** of value to arrive. This service adds a **$15** fee and an exchange rate that costs about **$20** more than a mid-market rate.\n\nYou pay **$535**. The cost of the service is **$35**, not $15.'),
    num('What do you pay on this receipt?', 535,
        '$500 + $15 + $20 = $535.', doc=send),
    num('What is the cost of the service, fee plus the rate?', 35,
        '$15 + $20 = $35.', doc=send),
    num('You send this same transfer twice. What do the two fees and two rate costs add up to?', 70,
        '$35 × 2 = $70.'),
    mc('A service advertises “$0 fee” and a worse exchange rate. What do you compare?',
       ['The amount they receive against what you paid', 'The fee line alone', 'The logo'], 0,
       'A $0 fee can hide a $20 rate. The test is what arrives, and what you paid to make it arrive.'),
], fmt='document')

mask = lesson('hf-mask', 'Your Oxygen Mask', 'You cannot send help from an account that cannot cover you.', [
    info('The order',
         'Rent, food, and a small [[emergency fund]] come before a transfer to family.\n\nThis month those three need **$2,200**. Take-home pay is **$2,600**. The room for help is **$400**. Sending **$600** puts you **$200** underwater.'),
    num('Pay is $2,600 and your own floor is $2,200. How much room is there for help?', 400,
        '$2,600 − $2,200 = $400.'),
    num('You send $600 anyway. How much short of your own floor are you?', 200,
        '$600 − $400 = $200.'),
    mc('Which order matches the oxygen mask?',
       ['Your floor first, then help from what remains', 'Help first, then hope the rent can wait', 'Split the shortfall across two credit cards'], 0,
       'The mask line is practical. A person who misses rent becomes the next person who needs help.'),
    tf('Sending the $600 is fine if you plan to catch up next month.', False,
       'Next month has its own floor. Starting it $200 behind is how the gap compounds.'),
])

lina_story = {
    'title': 'Lina and her mom',
    'character': 'Lina, 29',
    'body': 'Lina is 29. Take-home pay is **$3,200**. Rent is **$1,400**. Her other bills are **$1,600**. That is **$3,000** before she helps anyone, so **$200** is what the month has left.\n\nHer mom needs **$300**. Sending it would leave Lina **$100** short of her own bills.\n\nShe tells her mom the truth: she can do **$200**, which is the whole remainder, or less if she wants any cushion. She does not put the last **$100** on a card.',
}
lina = lesson('hf-lina', 'Lina and Her Mom', 'The number she can give is $200. Love does not add the other $100.', [
    num('What do Lina’s rent and other bills add up to?', 3000, '$1,400 + $1,600 = $3,000.'),
    num('Take-home pay is $3,200. How much is left before any help?', 200,
        '$3,200 − $3,000 = $200.'),
    num('If she sends $300, how short of her own bills is she?', 100,
        '$300 − $200 = $100.'),
    mc('Which amount keeps her bills paid?',
       ['$200 or less', '$300', '$300, plus a $100 card charge she will “figure out”'], 0,
       'The month has $200 left. $300 spends bills she has already counted.'),
    tf('Because the gap is only $100, the card is a harmless bridge.', False,
       'The $100 is a debt, and next month’s $200 of room has to cover it before she can help again.'),
], fmt='story', story=lina_story)

trial_steps = [
    num('Pay is $2,800. Your floor is $2,400. How much can you give without cutting the floor?', 400,
        '$2,800 − $2,400 = $400.'),
    mc('You co-sign a $9,000 loan. They stop paying. Who can be collected from?',
       ['You', 'Only the person who spent the money', 'The bank’s customer service line, and nobody else'], 0,
       'A co-signer is responsible for the loan.'),
    num('An aide is $20 an hour for 10 hours. What is the week?', 200, '$20 × 10 = $200.'),
    tf('A “$0 fee” transfer cannot cost you anything.', False,
       'The exchange rate can still take a cut. Compare what arrives with what you paid.'),
]

lessons = [sink, kind, cosign, bound, aging, abroad, mask, lina,
           review('hf'), trial('hf', 'Helping Family', trial_steps)]
write_unit('10-helping-family.json', 'helping-family', 10, 'Helping Family',
           'A cap you can keep, the difference between a gift and a loan, and the cost of sending money.',
           'Help from what remains. The rent is not a gift you can give.', terms, lessons, section=S)
