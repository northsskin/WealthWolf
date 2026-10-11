from lib import *

S = 'home-life'
terms = {
    'property-tax': term('Property tax',
                         'A tax from your local government based on what your home is worth. Owners pay it. Renters pay it only inside the rent.',
                         'A $3,600 yearly bill is $300 a month.'),
    'escrow': term('Escrow',
                   'An account the lender uses to collect property tax and homeowners insurance along with the mortgage, then pay those bills for you.',
                   'A $1,400 mortgage plus $300 of tax and $100 of insurance is an $1,800 payment into the loan and the escrow.'),
    'homeowners-association': term('HOA',
                                   'A homeowners association. It charges a fee and sets rules for the neighborhood or the building. The fee is on top of the mortgage.',
                                   'An HOA fee of $250 a month is $3,000 a year.'),
    'home-equity': term('Home equity',
                        'What you own in the house: its value minus the loans against it.',
                        'A home worth $320,000 with a $240,000 loan has $80,000 of equity.'),
    'heloc': term('HELOC',
                  'A home equity line of credit. You borrow against the equity, and the house is the collateral. If you cannot pay, you can lose the house.',
                  'Borrowing $20,000 of an $80,000 equity stake leaves $60,000 if the value stays put.'),
}

tax = lesson('oh-tax', 'Property Tax', 'The bill comes from the town, not the bank.', [
    info('A local bill',
         '[[Property tax]] is based on the home’s value. This home’s bill is **$3,600** a year. That is **$300** a month.\n\nThere is no single national rate. Use the bill, not a rumor about “what tax usually is.”'),
    num('The yearly property tax is $3,600. What is that per month?', 300, '$3,600 ÷ 12 = $300.'),
    num('You set aside $300 a month. After 12 months, how much have you set aside?', 3600,
        '$300 × 12 = $3,600, which matches the bill.'),
    mc('Who sends the property tax bill?',
       ['Your local government', 'The inspector', 'The previous owner, forever'], 0,
       'The town or county assesses it. The lender may collect it, but the tax is not the lender’s fee.'),
    tf('Renters never feel property tax, because only owners are billed.', False,
       'Owners are billed. Landlords fold the tax into the rent.'),
])

insure = lesson('oh-escrow', 'Insurance and Escrow', 'The lender often collects the tax and the premium for you.', [
    info('One payment, three jobs',
         'Homeowners insurance here costs **$1,200** a year, so **$100** a month. The [[deductible]] is **$1,000**. The [[premium]] is the yearly price.\n\n[[Escrow]] adds that **$100** and **$300** of tax to a **$1,400** [[mortgage]] payment. You pay **$1,800**, and the lender pays the tax and the insurance when they come due.'),
    num('A $1,200 yearly premium is how much per month?', 100, '$1,200 ÷ 12 = $100.'),
    num('Mortgage $1,400, tax $300, insurance $100. What is the full monthly payment?', 1800,
        '$1,400 + $300 + $100 = $1,800.'),
    sort('On this loan, where does each bill get paid from?',
         ['In the escrow payment', 'Outside escrow'],
         [('This loan’s property tax', 0),
          ('This loan’s homeowners insurance', 0),
          ('The HOA fee', 1),
          ('A broken water heater', 1)],
         'Tax and insurance ride in the payment. The HOA and the repairs do not.'),
    tf('Escrow means the tax and the insurance are free.', False,
       'You pay them every month inside the $1,800. Escrow only changes who holds the money until the bill is due.'),
], fmt='sort')

maintain = lesson('oh-maintain', 'The 1% Sketch', 'A rough jar for the things that break.', [
    info('One percent, as a sketch',
         'A common sketch is to set aside about **1%** of the home’s value each year for maintenance. On a **$300,000** home, that is **$3,000** a year, or **$250** a month.\n\nA new roof can cost more than a year of that jar. The 1% is a starting point, not a quote.'),
    num('What is 1% of a $300,000 home?', 3000, '$300,000 × 0.01 = $3,000 a year.'),
    num('What is that $3,000 per month?', 250, '$3,000 ÷ 12 = $250.'),
    num('The water heater costs $900. How much of a $3,000 jar is left?', 2100,
        '$3,000 − $900 = $2,100.'),
    tf('The 1% sketch is the most a repair is allowed to cost.', False,
       'It is a savings target. A repair can cost more, which is why the jar exists before the break.'),
])

hoa_doc = doc('statement', 'October housing', [
    ('mort', 'Mortgage payment', 1400),
    ('tax', 'Property tax, escrow', 300),
    ('ins', 'Home insurance, escrow', 100),
    ('hoa', 'HOA fee', 250),
], totals=[('This month', 2050, True)])
assert 1400 + 300 + 100 + 250 == 2050

hoa = lesson('oh-hoa', 'The HOA Line', 'It is easy to budget the mortgage and miss the fee.', [
    info('A third bill',
         'An [[HOA|homeowners-association]] fee is not part of the mortgage and not part of escrow. On this statement it is **$250**.\n\n**$250** a month is **$3,000** a year, on top of the **$1,800** you already counted for the loan, the tax, and the insurance.'),
    spot('Which line is the HOA fee?', hoa_doc, 'hoa',
         'It is the $250 line. Escrow did not include it.'),
    num('What is this whole October statement?', 2050,
        '$1,400 + $300 + $100 + $250 = $2,050.', doc=hoa_doc),
    num('What is the HOA fee for a year at $250 a month?', 3000, '$250 × 12 = $3,000.'),
    tf('An HOA fee is optional once you have already closed.', False,
       'If the home is in the association, the fee is part of owning it. Read it before you offer.'),
], fmt='spot')

equity = lesson('oh-equity', 'Home Equity', 'Value minus what you owe.', [
    info('The stake',
         '[[Home equity]] is the home’s value minus the loans against it.\n\nWorth **$320,000**. Loan **$240,000**. Equity **$80,000**. If the value falls and the loan does not, the equity shrinks.'),
    num('The home is worth $320,000 and the loan is $240,000. How much equity is that?', 80000,
        '$320,000 − $240,000 = $80,000.'),
    num('The value falls to $300,000 and the loan is still $240,000. How much equity is left?', 60000,
        '$300,000 − $240,000 = $60,000.'),
    mc('Which event raises your equity if the value stays the same?',
       ['Paying principal down', 'Paying interest', 'Paying the insurance deductible'], 0,
       'Principal reduces the loan. Interest and the deductible do not.'),
    tf('Equity is cash in your checking account.', False,
       'It is a stake in the house. Turning it into cash means selling, or borrowing against it.'),
])

heloc = lesson('oh-heloc', 'A HELOC', 'Borrowing the equity puts the house on the line.', [
    info('The house is the collateral',
         'A [[HELOC]] lets you borrow against [[home equity]]. This example borrows **$20,000** of an **$80,000** stake.\n\nThe old mortgage is **$240,000**. After the draw, you owe **$260,000**. If the value stays **$320,000**, equity left is **$60,000**. Miss the payments and you can lose the house.'),
    num('The mortgage is $240,000 and you draw $20,000. How much do you owe in total?', 260000,
        '$240,000 + $20,000 = $260,000.'),
    num('The home is still worth $320,000. How much equity is left after that draw?', 60000,
        '$320,000 − $260,000 = $60,000.'),
    mc('What is the risk that a credit card does not have?',
       ['The lender can take the house', 'The interest is always zero', 'You must sell the house to open the line'], 0,
       'The house is the collateral. That is the difference.'),
    tf('A HELOC is a gift of your equity, so there is nothing to pay back.', False,
       'It is a loan. The equity is the collateral, not a present.'),
])

budget = lesson('oh-budget', 'A Housing Jar', 'Give the repair jar a number before the year spends it.', [
    info('Five hundred dollars',
         'You set aside **$500** a month for the house beyond the mortgage payment. The 1% sketch says maintenance wants at least **$250** of that.\n\nThe rest can go to a project or a roof jar. Every dollar gets a job.'),
    alloc('Set aside $500. Maintenance needs at least $250. Assign every dollar.', 500, 10,
          [{'label': 'Maintenance', 'min': 250}, {'label': 'A project'}, {'label': 'Roof jar'}],
          'Maintenance gets at least $250. All $500 is assigned.'),
    num('Maintenance takes $250 of the $500. How much is left for the project and the roof jar together?', 250,
        '$500 − $250 = $250.'),
    num('The roof jar gets $100 a month. How much is that in a year?', 1200, '$100 × 12 = $1,200.'),
    tf('Once the mortgage is paid this month, the housing budget is finished.', False,
       'The mortgage does not include the HOA, the repairs, or the roof jar.'),
])

nia_story = {
    'title': 'Nia’s first year',
    'character': 'Nia, 33',
    'body': 'Nia is 33 and a graphic designer. Her home is worth **$250,000**. She saved the 1% sketch, **$2,500**, and felt ready.\n\nThe water heater died in March and cost **$900**. That fit in the jar. The [[HOA|homeowners-association]] fee did not. It is **$200** a month, **$2,400** a year, and she had budgeted **$0**.\n\nThe repair jar was never going to pay the association. She adds the fee to the monthly housing number before she calls the year a success.',
}
nia = lesson('oh-nia', 'Nia’s First Year', 'The surprise was a bill she could have read at closing.', [
    num('What is 1% of Nia’s $250,000 home?', 2500, '$250,000 × 0.01 = $2,500.'),
    num('The water heater is $900. How much of the $2,500 jar is left?', 1600,
        '$2,500 − $900 = $1,600.'),
    num('The HOA fee is $200 a month. What is that for the year?', 2400, '$200 × 12 = $2,400.'),
    num('She tries to pay the $2,400 HOA from the $1,600 left in the repair jar. How short is she?', 800,
        '$2,400 − $1,600 = $800. The fee needed its own line.'),
    mc('What should next year’s budget do with the HOA?',
       ['Give it a monthly line of its own', 'Hope the repair jar covers it', 'Treat it as optional'], 0,
       'A fee you can see at closing is not a surprise. It is a bill.'),
], fmt='story', story=nia_story)

trial_steps = [
    num('Property tax is $4,800 a year. What is the monthly set-aside?', 400, '$4,800 ÷ 12 = $400.'),
    num('A home is worth $280,000 and the loan is $200,000. How much equity is that?', 80000,
        '$280,000 − $200,000 = $80,000.'),
    mc('Which bill is the house itself on the line for?',
       ['A HELOC', 'A streaming subscription', 'An application fee'], 0,
       'The HELOC uses the house as collateral.'),
    tf('An HOA fee is included in a typical mortgage payment.', False,
       'It is a separate bill. Read it before you buy.'),
]

lessons = [tax, insure, maintain, hoa, equity, heloc, budget, nia,
           review('oh'), trial('oh', 'Owning a Home', trial_steps)]
write_unit('06-owning-a-home.json', 'owning-a-home', 6, 'Owning a Home',
           'Tax, insurance, repairs, the HOA, and the risk in borrowing your equity.',
           'The mortgage is the payment you expected. The rest is the year you live.', terms, lessons, section=S)
