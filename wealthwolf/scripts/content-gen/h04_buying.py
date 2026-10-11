from lib import *

S = 'home-life'
terms = {
    'pmi': term('PMI',
                'Private mortgage insurance. On a conventional loan, lenders generally require it when the down payment is under 20%. It protects the lender, not you.',
                '10% down on a $240,000 home. PMI on this estimate is $110 a month until you can cancel it.'),
    'closing-costs': term('Closing costs',
                          'The fees due when the sale is finished: lender charges, title, and taxes and insurance prepaid into escrow. A common sketch is about 2% to 5% of the price.',
                          '3% of a $240,000 purchase is $7,200, on top of the down payment.'),
    'pre-approval': term('Pre-approval',
                         'A lender’s look at your income, debts, and credit, and a letter that says how much they might lend. It is not the final loan, and it is not the seller’s promise.',
                         'A letter for up to $220,000. The real loan still waits on the appraisal and the final papers.'),
}

house = lesson('bh-house', 'How Much House', 'The cap is the whole housing payment, not the loan alone.', [
    info('Start from the month',
         'Gross pay is **$6,000**. The 30% sketch is **$1,800** for housing.\n\nOn this house, tax and insurance are **$400** a month. That leaves **$1,400** for the [[mortgage]] itself. A bigger loan that blows past $1,800 is the house you cannot afford.'),
    num('What is 30% of $6,000?', 1800, '$6,000 × 0.30 = $1,800.'),
    num('The housing cap is $1,800 and tax plus insurance is $400. How much is left for the mortgage payment?', 1400,
        '$1,800 − $400 = $1,400.'),
    num('A loan payment of $1,600 plus $400 of tax and insurance is how much over the $1,800 cap?', 200,
        '$1,600 + $400 = $2,000. $2,000 − $1,800 = $200.'),
    tf('If you can afford the mortgage payment, you can ignore tax and insurance.', False,
       'Those bills arrive whether the lender printed them or not. The cap is the whole month.'),
])

pmi = lesson('bh-pmi', 'Down Payment and PMI', 'Under 20% down, a conventional loan usually adds PMI.', [
    info('Two down payments',
         'The price is **$240,000**. **20%** down is **$48,000**, and a conventional loan generally skips [[PMI|pmi]]. **10%** down is **$24,000**, and PMI on this estimate is **$110** a month.\n\nPMI protects the lender. Under the Homeowners Protection Act you can ask to cancel it around **80%** of the home’s original value, and it must end automatically around **78%** if you are current. FHA mortgage insurance follows different rules.',
         callout='The 80% request can use the original value. The automatic stop follows the schedule, and only if you are current.'),
    num('What is 20% of this $240,000 price?', 48000, '$240,000 × 0.20 = $48,000.'),
    num('What is 10% of this $240,000 price?', 24000, '$240,000 × 0.10 = $24,000.'),
    num('At about 80% of the original $240,000 value, what loan balance lets you ask to cancel PMI?', 192000,
        '$240,000 × 0.80 = $192,000.'),
    num('PMI on the 10% loan is $110 a month. What is that per year?', 1320, '$110 × 12 = $1,320.'),
    tf('FHA mortgage insurance cancels on the same schedule as conventional PMI.', False,
       'FHA insurance follows its own rules, and it often lasts longer. Do not assume the 80% and 78% stops apply.'),
])

closing = lesson('bh-closing', 'Closing Costs', 'The down payment is not the only check you bring.', [
    info('A 3% sketch on this purchase',
         '[[Closing costs]] vary. On this **$240,000** purchase the estimate uses **3%**, which is **$7,200**.\n\nThat sits on top of a **$24,000** down payment. Cash to close in this sketch is **$31,200**. The 3% is an example for this sale, not a national fee.'),
    num('What is 3% of $240,000?', 7200, '$240,000 × 0.03 = $7,200.'),
    num('Down payment $24,000 plus closing costs $7,200. What is cash to close?', 31200,
        '$24,000 + $7,200 = $31,200.'),
    mc('You saved the down payment and nothing else. What is missing?',
       ['The closing costs', 'The right to a lower price', 'PMI, which the seller pays'], 0,
       'The keys need both checks. Closing costs are yours unless the contract says someone else pays them.'),
    tf('Closing costs are a deposit you get back after the first year.', False,
       'They pay the people who close the sale. They are spent.'),
])

pre = lesson('bh-pre', 'Pre-Approval', 'A letter about you, not a promise about the house.', [
    mc('What is a pre-approval?',
       ['A lender’s estimate of what they might lend you', 'The seller’s agreement to your price', 'The final loan, already funded'], 0,
       'It looks at your income, your debts, and your [[credit score]]. The house still has to pass inspection and appraisal.',
       context='[[Pre-approval]] happens before you make an offer, so you know the size of the loan a lender will consider.'),
    mc('A letter says “up to $220,000.” Your full housing cap only supports a smaller payment. What do you shop with?',
       ['The payment you can actually afford', 'The top of the letter', 'Whatever the seller asks'], 0,
       'The letter is a ceiling. Your budget can be lower.'),
    tf('A pre-approval means the seller has accepted your offer.', False,
       'You do not have an offer yet. You have a lender’s early yes.'),
    tf('The lender can still say no later if the appraisal or your job changes.', True,
       'Pre-approval is an early look. The final loan waits on the house and on you staying qualified.'),
    fill('Get a pre-approval before you ___, so you are not guessing at the loan.',
         ['make an offer', 'skip the inspection', 'pay the seller in cash'], 0,
         'The letter tells you the range. The offer comes after.'),
])

steps = lesson('bh-steps', 'Offer to Keys', 'The house is not yours at the handshake.', [
    info('One path',
         'Budget, then a [[pre-approval]], then an offer, then an inspection and the Closing Disclosure, then the keys.\n\nSkipping the inspection to “win” the house is how you buy someone else’s leak.'),
    order('Put the purchase in order.',
          ['Set a housing budget',
           'Get pre-approved',
           'Make an offer',
           'Inspect the home and read the Closing Disclosure',
           'Sign and get the keys'],
          'The budget and the letter come before the offer. The inspection and the disclosure come before you sign.'),
    mc('Why is the inspection before the keys?',
       ['So you can still walk away or renegotiate if the house has a serious flaw', 'Because the seller wants you to meet the neighbors', 'So PMI can start earlier'], 0,
       'Once you sign and fund, the flaw is yours.'),
    tf('A verbal “we have a deal” is the moment you own the house.', False,
       'You own it at closing, when the papers are signed and the money moves.'),
    fill('The last step on this list is to sign and get the ___.',
         ['keys', 'pre-approval', 'application fee'], 0,
         'The keys come after the disclosure, not before.'),
])

inspect = lesson('bh-inspect', 'Inspection and Appraisal', 'One looks at the roof. One looks at the price.', [
    info('Two different visits',
         'An inspection is for you. It looks for leaks, a failing furnace, and other condition problems.\n\nAn appraisal is for the lender. It says what the home is worth. If it comes in low, the lender may not lend the full price.'),
    sort('Sort the inspection and the appraisal.',
         ['Inspection', 'Appraisal'],
         [('Looks for a leaking roof', 0),
          ('Tells the lender what the home is worth', 1),
          ('You hire it to learn the condition', 0),
          ('A low result can shrink the loan', 1)],
         'Condition is the inspection. Value, for the lender, is the appraisal.'),
    mc('The inspection finds a furnace that needs a $6,000 replacement. What can you still do, if the contract allows?',
       ['Ask for a repair, a price cut, or walk away', 'Nothing. You already own it', 'Send the bill to the lender as PMI'], 0,
       'That is why the inspection happens before closing.'),
    num('The furnace repair is $6,000 and you split it evenly with the seller. What is your half?', 3000,
        '$6,000 ÷ 2 = $3,000.'),
    tf('A clean appraisal means the roof does not leak.', False,
       'The appraisal is a value. The inspection is the condition. You want both.'),
], fmt='sort')

cd = doc('statement', 'Closing Disclosure', [
    ('loan', 'Loan amount', 216000),
    ('down', 'Down payment', 24000),
    ('close', 'Closing costs', 7200),
], subtitle='Cash you bring', meta=['Price $240,000', 'Conventional loan'],
   totals=[('Cash to close', 31200, True)])
assert 24000 + 7200 == 31200

disclosure = lesson('bh-disclose', 'The Closing Disclosure', 'This is the page that should match the money you bring.', [
    info('Read it with time to spare',
         'The Closing Disclosure is the lender’s final accounting of the loan, the [[down payment]], and the [[closing costs]].\n\nOn this one the price is **$240,000**, the loan is **$216,000**, and the cash you bring is **$31,200**.'),
    num('What is cash to close on this disclosure?', 31200,
        '$24,000 + $7,200 = $31,200.', doc=cd),
    num('Price $240,000 minus the $216,000 loan. What is the down payment?', 24000,
        '$240,000 − $216,000 = $24,000.', doc=cd),
    mc('The disclosure shows $2,000 more in closing costs than your last estimate. What do you do before you sign?',
       ['Ask the lender to explain the new line', 'Sign anyway so the rate does not vanish', 'Pay it in cash without reading it'], 0,
       'A new number needs a name. You still have time to ask.'),
    tf('The loan amount on this page is the same as the cash you bring to closing.', False,
       'The loan is $216,000. The cash you bring is the $31,200 of down payment and closing costs.'),
], fmt='document')

devon_story = {
    'title': 'Devon checks the programs',
    'character': 'Devon, 31',
    'body': 'Devon is 31 and a warehouse supervisor. He has **$30,000** saved. The home he wants is **$200,000**.\n\n**20%** down would be **$40,000**. He is **$10,000** short of that, so a conventional loan would generally add [[PMI|pmi]]. **10%** down is **$20,000**, which would leave him **$10,000**.\n\nHe does not count on a grant he saw in an ad. He checks HUD and his state housing agency for programs that are real this year, and he does not spend the last of the $30,000 to get there.',
}
devon = lesson('bh-devon', 'Devon’s First Home', 'No grant number until a real program says so.', [
    num('What is 20% of Devon’s $200,000 home?', 40000, '$200,000 × 0.20 = $40,000.'),
    num('He has $30,000. How short of that 20% is he?', 10000, '$40,000 − $30,000 = $10,000.'),
    num('What is 10% of the $200,000 price?', 20000, '$200,000 × 0.10 = $20,000.'),
    mc('A website promises a $15,000 first-time grant with no official page behind it. What should Devon do?',
       ['Check HUD and his state housing agency, and ignore the ad until then', 'Pay the site a fee to “unlock” the grant', 'Subtract $15,000 from the price in his offer'], 0,
       'A grant you cannot confirm is not part of the budget. Programs change, and the state agency is the source.'),
    tf('Because Devon is buying his first home, conventional PMI is automatically waived.', False,
       'First-time status is not a waiver. Under 20% down, PMI is still the usual conventional rule. A real program would say so in writing.'),
], fmt='story', story=devon_story)

trial_steps = [
    num('A $180,000 home. What is 20% down?', 36000, '$180,000 × 0.20 = $36,000.'),
    mc('Which visit tells the lender the home’s value?',
       ['The appraisal', 'The inspection', 'The roommate agreement'], 0,
       'The appraisal is the value. The inspection is the condition.'),
    tf('On a conventional loan, PMI is generally required when the down payment is under 20%.', True,
       'That is the usual rule. FHA insurance is a different product.'),
    num('Closing costs of $6,000 plus a $20,000 down payment. What is cash to close?', 26000,
        '$6,000 + $20,000 = $26,000.'),
]

lessons = [house, pmi, closing, pre, steps, inspect, disclosure, devon,
           review('bh'), trial('bh', 'Buying a Home', trial_steps)]
write_unit('04-buying-a-home.json', 'buying-a-home', 4, 'Buying a Home',
           'A housing cap, PMI, closing costs, and the path from offer to keys.',
           'The letter says what a lender might do. Your budget says what you will do.', terms, lessons, section=S)
