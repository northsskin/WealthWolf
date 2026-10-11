from lib import *

S = 'protecting'
terms = {
    'explanation-of-benefits': term('Explanation of benefits',
                                    'A statement from the health plan, not a bill. It shows what was charged, what the plan allowed, what it paid, and what you may owe.',
                                    'Charged $640. Allowed $400. Plan paid $320. You may owe $80.'),
    'health-savings-account': term('Health savings account',
                                   'A tax-favored account you can fund only with a high-deductible health plan. The money can carry over year to year and be used for qualified medical costs.',
                                   'The 2026 HSA limit is $4,400 for self-only coverage and $8,750 for family coverage, plus $1,000 if you are 55 or older.'),
    'flexible-spending-account': term('Flexible spending account',
                                      'A work account for medical costs. For 2026 the employee salary-reduction limit is $3,400. Unused money is usually lost, unless the plan allows a carryover of up to $680.',
                                      'You put in $3,400 for 2026 and spend $3,000. If the plan allows the maximum carryover, $400 can move forward, because $400 is under $680.'),
}

eob_lines = [
    ('charged', 'Amount charged', 640),
    ('discount', 'Plan discount', -240),
    ('allowed', 'Amount allowed', 400),
    ('paid', 'Plan paid', -320),
    ('owe', 'You may owe', 80),
]
assert 640 - 240 == 400 and 400 - 320 == 80
EOB = doc('statement', 'Explanation of benefits', eob_lines, subtitle='Not a bill',
          meta=[('Provider', 'City Clinic'), ('Date', 'April 2')],
          note='Wait for this before you pay a big hospital balance.')
eob = lesson('mb-eob', 'The Explanation of Benefits', 'This page is the plan talking. It is not the bill.', [
    mc('What is an explanation of benefits?',
       ['The plan’s statement of what it allowed and what you may owe', 'The bill you must pay today', 'A receipt from the pharmacy'], 0,
       'Read it before you pay. The hospital’s first number is often not your number.',
       context='An [[explanation of benefits]] comes from the plan. It is not itself a bill.'),
    num('What was charged?', 640, 'The charged line is $640.', doc=EOB),
    num('What did the plan allow after its discount?', 400, '$640 − $240 = $400.', doc=EOB),
    num('How much may you owe?', 80, '$400 − $320 = $80.', doc=EOB),
    tf('You should pay the $640 charged amount because it is the largest number.', False,
       'The amount you may owe is $80. The discount and the plan’s payment did the rest.'),
], fmt='document')

bill_lines = [
    ('visit', 'Clinic visit', 140),
    ('xray', 'X-ray', 180),
    ('again', 'X-ray, billed again', 180),
    ('labs', 'Lab work', 60),
]
assert 140 + 180 + 180 + 60 == 560
BILL = doc('bill', 'Hospital bill', bill_lines, subtitle='Itemized',
           totals=[('Amount billed', 560, True)],
           note='The explanation of benefits lists one x-ray, not two.')
spot = lesson('mb-spot', 'Check the Bill', 'Two x-rays were not what happened.', [
    spot('Which line does not belong?', BILL, 'again',
         'The second x-ray is a double charge. The EOB listed one.',
         context='Match the bill to the [[explanation of benefits]]. One service, one line.'),
    num('How much is the duplicate x-ray?', 180, 'The repeated line is $180.', doc=BILL),
    num('What should the bill add up to without that duplicate?', 380,
        '$140 + $180 + $60 = $380.'),
    mc('What do you ask the hospital for when the bill is a lump sum?',
       ['An itemized bill that lists each service', 'A higher total', 'A gift card'], 0,
       'You cannot spot a double charge on a single number.'),
    tf('Paying a bill you have not compared to the EOB is the careful path.', False,
       'Compare first. Then pay what you actually owe.'),
], fmt='spot')

item = lesson('mb-itemized', 'Ask for the Itemized Bill', 'A single total hides the duplicate.', [
    mc('An itemized bill shows:',
       ['Each service and its price', 'Only the hospital’s logo', 'Your credit score'], 0,
       'The lines are how you find the mistake.'),
    tf('A one-line total is enough to check for a double charge.', False,
       'The double hides inside the total.'),
    num('The itemized lines are $220, $80, and $140. What is the total?', 440,
        '$220 + $80 + $140 = $440.'),
    mc('A line says “misc.” and costs $600. What do you do?',
       ['Ask what the service was', 'Pay it because misc. sounds official', 'Ignore every other line'], 0,
       'A vague line is a question, not a verdict.'),
    fill('Compare each line to the ___.',
         ['explanation of benefits', 'weather report', 'car title'], 0,
         'The plan already said what it allowed.'),
])

deal = lesson('mb-negotiate', 'Negotiating and Payment Plans', 'The first number is an offer, not always the end.', [
    num('The bill is $3,200. The hospital offers 25% off if you pay within 30 days. How much is the discount?', 800,
        '$3,200 × 0.25 = $800.',
        context='Hospitals often have a prompt-pay discount or a monthly plan. Ask before you put it on a credit card.'),
    num('How much do you pay if you take that 25% off?', 2400, '$3,200 − $800 = $2,400.'),
    num('A payment plan is $200 a month for 16 months. What is the total?', 3200,
        '$200 × 16 = $3,200.'),
    mc('Which is usually worse than a hospital payment plan?',
       ['A credit card at a high interest rate', 'Asking for an itemized bill', 'Reading the EOB'], 0,
       'The card keeps charging after the hospital would have stopped.'),
    tf('You have to accept the first total on the letter.', False,
       'Ask. A discount or a plan is a normal conversation.'),
])

help_ = lesson('mb-help', 'Hospital Financial Assistance', 'Nonprofit hospitals have a program. You have to ask.', [
    info('Aid is a form, not a secret',
         'Many hospitals, especially nonprofit ones, have financial assistance, sometimes called charity care. It can reduce or erase a bill if your income qualifies.\n\nThe form is the door. The program does not knock.'),
    mc('What is hospital financial assistance?',
       ['A program that can lower a bill based on your income', 'A loan from the parking garage', 'A higher deductible'], 0,
       'It is aid, not a new debt.'),
    tf('You should wait until the bill is in collections before you ask about assistance.', False,
       'Ask while the bill is still at the hospital. Collections is a harder room.'),
    mc('What do you ask the billing office?',
       ['For the financial assistance application and the income rules', 'For a gift card', 'For them to skip the itemized bill'], 0,
       'The rules are written. Get the form.'),
    fill('Financial assistance is based on whether your ___ qualifies.',
         ['income', 'shoe size', 'area code'], 0,
         'Bring the proof they ask for.'),
])

accounts = lesson('mb-hsa-fsa', 'HSA or FSA', 'One can travel with you. The other is use it, mostly, this year.', [
    sort('Which account is this?',
         ['HSA', 'FSA'],
         [('You need a high-deductible health plan to contribute', 0),
          ('The money can stay year after year', 0),
          ('It is offered through work and unused money is usually lost', 1),
          ('A 2026 carryover, if the plan allows one, is capped at $680', 1),
          ('The 2026 self-only contribution limit is $4,400', 0)],
         'The HSA is the one that stays. The FSA is the work account with a clock.',
         context='An [[HSA|health-savings-account]] is paired with a high-deductible plan. For 2026 the limit is $4,400 self-only and $8,750 family, plus $1,000 at age 55 or older. An [[FSA|flexible-spending-account]] has a 2026 employee limit of $3,400. If the employer allows a carryover, the 2026 maximum is $680. Those figures are from the IRS for 2026.'),
    num('The 2026 self-only HSA limit is $4,400. You contribute $200 a month. How much is that in a year?', 2400,
        '$200 × 12 = $2,400.'),
    num('How much of the $4,400 limit is left?', 2000, '$4,400 − $2,400 = $2,000.'),
    num('You are 55. Add the $1,000 catch-up to the $4,400 self-only limit. What is the total you can put in for 2026?', 5400,
        '$4,400 + $1,000 = $5,400.'),
    tf('An FSA and an HSA have the same rule about leftover money.', False,
       'HSA money stays. FSA money is usually lost, except a carryover the plan chose to allow.'),
], fmt='sort')

taxadv = lesson('mb-hsa-tax', 'Why an HSA Is Favored', 'The tax break is the point. The receipt is the proof.', [
    mc('A qualified medical expense paid from an HSA is:',
       ['Generally free of income tax', 'Taxed twice', 'Illegal'], 0,
       'That is the favor. Sunglasses you do not need are not a qualified expense.',
       context='Money in an [[HSA|health-savings-account]] can go in tax-favored, and qualified medical withdrawals come out tax-free. Keep the receipts.'),
    num('You contribute $2,400. In a simple example your income-tax rate is 20%. How much income tax do you not pay on that contribution this year?', 480,
        '$2,400 × 0.20 = $480. Real taxes depend on your return. This is the shape of the break.'),
    tf('You can spend HSA money on anything, tax-free, the week you deposit it.', False,
       'A non-medical withdrawal can be taxed, and it can be penalized if you are under 65.'),
    mc('Why keep receipts?',
       ['They show the withdrawal was for a qualified medical cost', 'The IRS does not allow receipts', 'Receipts raise the contribution limit'], 0,
       'The favor depends on the expense being qualified.'),
    num('The 2026 family HSA limit is $8,750. The self-only limit is $4,400. How much higher is the family limit?', 4350,
        '$8,750 − $4,400 = $4,350.'),
])

jordan_story = {
    'title': 'The bill that was not his',
    'character': 'Jordan, 33, bookstore manager',
    'body': 'Jordan leaves the ER with a sore ankle and, two weeks later, a letter asking for **$3,200**. The [[explanation of benefits]] arrives the next day. It says the plan allowed less, paid its share, and Jordan may owe **$640**.\n\nHe has an [[HSA|health-savings-account]] with **$700** in it. He has not asked the hospital for an itemized bill yet.',
}
jordan = lesson('mb-jordan', 'Jordan’s Surprise Bill', 'The letter shouted. The EOB whispered the real number.', [
    num('How much does the EOB say Jordan may owe?', 640, 'The EOB says $640.'),
    num('How much of the $3,200 letter is not his, according to that EOB?', 2560,
        '$3,200 − $640 = $2,560.'),
    mc('What should he do before paying the $3,200?',
       ['Pay the $640 the EOB supports, and dispute the rest', 'Put $3,200 on a credit card tonight', 'Throw away the EOB'], 0,
       'The EOB is the plan’s accounting. The letter has not caught up.'),
    num('His HSA has $700. After a qualified $640 payment, how much is left in the account?', 60,
        '$700 − $640 = $60.'),
    tf('The HSA payment makes the extra $2,560 his responsibility.', False,
       'He owes what the EOB says he owes, not the loudest number on the letter.'),
], fmt='story', story=jordan_story)

trial_steps = [
    num('Charged $500. Plan discount $150. What is allowed?', 350, '$500 − $150 = $350.'),
    mc('A second charge for a test you had once is:',
       ['A double charge to dispute', 'Proof you had it twice', 'The out-of-pocket maximum'], 0,
       'One test, one line.'),
    tf('An FSA balance always rolls over in full, like an HSA.', False,
       'FSA money is usually lost. A 2026 carryover, if allowed, stops at $680.'),
    num('A $2,000 bill is cut by 20% for prompt payment. How much do you pay?', 1600,
        '$2,000 × 0.20 = $400 off. $2,000 − $400 = $1,600.'),
]

lessons = [eob, spot, item, deal, help_, accounts, taxadv, jordan,
           review('mb'), trial('mb', 'Medical Bills', trial_steps)]
write_unit('07-medical-bills.json', 'medical-bills', 7, 'Medical Bills, HSAs & FSAs',
           'Read the plan’s statement, then the bill, then the account that can pay it.',
           'The biggest number on the letter is not always the one you owe.', terms, lessons, section=S)
