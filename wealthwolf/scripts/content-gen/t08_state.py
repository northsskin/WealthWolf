from lib import *

S = 'taxes'
terms = {
    'flat-tax': term('Flat tax',
                     'A state income tax that uses one rate on the taxable wages, instead of a series of brackets.',
                     'A flat 3% of $60,000 is $1,800. The next dollar is taxed at that same 3%.'),
}

none = lesson('st-none', 'No Wage Tax Is Not No Tax', 'A state can skip wages and still tax a purchase or a house.', [
    info('Read the missing tax carefully',
         'Some states do not tax wages. This lesson does not grade a list of them, because a list goes stale. Check the state before a move.\n\nA state with no wage tax can still charge [[sales tax]], [[property tax]], or a tax on investment gains. “No income tax” on a job posting is not “no tax.”'),
    tf('A state with no wage tax charges no tax of any kind.', False,
       'Sales tax, property tax, or a tax on gains can still be there.'),
    mc('A job posting says the state has no wage tax. What do you still price?',
       ['Sales tax, property tax, and any tax on gains', 'Nothing. The posting covered every tax', 'Only the federal standard deduction'], 0,
       'The posting named one tax. The others can still change the move.'),
    num('A state wage tax of $0 versus a state wage tax of $2,000. How much wage tax do you save?', 2000,
        '$2,000 − $0 = $2,000. That savings is only the wage tax.'),
    fill('No wage tax does not mean no ___.',
         ['tax', 'rent', 'paycheck'], 0,
         'Tax. Other taxes can remain.'),
])

shape = lesson('st-shape', 'Flat or Graduated', 'These rates are an example, not a real state.', [
    info('One rate, or a stack',
         'A [[flat tax]] in this example is **5%** of **$40,000**, which is **$2,000**.\n\nA graduated example taxes the first **$20,000** at **2%**, which is **$400**, and the next **$20,000** at **4%**, which is **$800**. The bill is **$1,200**. Neither pair is a real state’s law. The shape is the lesson.'),
    num('What is 5% of $40,000 in the flat example?', 2000, '$40,000 × 0.05 = $2,000.'),
    num('What is 2% of the first $20,000 in the graduated example?', 400, '$20,000 × 0.02 = $400.'),
    num('What is the graduated example’s total tax?', 1200,
        '$400 + $800 = $1,200. The second $20,000 at 4% is $800.'),
    num('How much more is the flat example than the graduated example?', 800,
        '$2,000 − $1,200 = $800.'),
])

local = lesson('st-local', 'A City Can Add Its Own', 'The state bill is not always the last bill.', [
    info('On top',
         'A city or county may tax wages too. In this example the city rate is **2%** of **$40,000**, which is **$800**, on top of whatever the state charges.\n\nThe lesson is the extra line. The 2% is not a national city rate.'),
    num('What is 2% of $40,000?', 800, '$40,000 × 0.02 = $800.'),
    num('The state tax in this example is $2,000 and the city tax is $800. What do they add up to?', 2800,
        '$2,000 + $800 = $2,800.'),
    mc('Where does a city wage tax sit?',
       ['On top of the state tax, when the city charges one', 'Inside FICA', 'Instead of the federal standard deduction'], 0,
       'It is an extra income tax. It is not FICA and it is not the federal deduction.'),
    tf('If the state tax is $2,000, no city can add more.', False,
       'This example’s city adds $800. Some places have no city tax. The paycheck is where you look.'),
])

prop = doc('bill', 'Property tax bill', [
    ('tax', 'Property tax for the year', 2400),
], subtitle='One house, this city')
assert 2400 / 12 == 200

house = lesson('st-prop', 'Property Tax, One Bill', 'The rate is local. The bill in front of you is the number.', [
    info('Use the bill',
         '[[Property tax]] is still the local tax on the home. This city’s bill is **$2,400** for the year, which is **$200** a month.\n\nA different city can bill a different amount on a similar house. Do not carry this $2,400 with you as a national rate.'),
    num('What is the yearly bill on this page?', 2400, 'The bill says $2,400.', doc=prop),
    num('What is that $2,400 per month?', 200, '$2,400 ÷ 12 = $200.', doc=prop),
    num('Another city bills $1,200 for the year. How much less is that per year?', 1200,
        '$2,400 − $1,200 = $1,200.'),
    tf('This $2,400 is the property tax in every city.', False,
       'It is this bill. The next city has its own.'),
], fmt='document')

sales = lesson('st-sales', 'Sales Tax Is Local Too', 'The price on the shelf is not always the price you pay.', [
    info('At the register',
         '[[Sales tax]] is added at purchase. A **$50** item with **6%** sales tax costs **$3** in tax and **$53** in all.\n\nA state that skips a wage tax may still charge this. The 6% is this example’s rate.'),
    num('What is 6% sales tax on a $50 item?', 3, '$50 × 0.06 = $3.'),
    num('What do you pay in all?', 53, '$50 + $3 = $53.'),
    num('The same $50 item in a place with no sales tax costs $50. How much more is the 6% place?', 3,
        '$53 − $50 = $3.'),
    tf('Sales tax is withheld from the paycheck like FICA.', False,
       'You pay it at the register. It is not a line on the W-2.'),
])

move = lesson('st-move', 'Moving Mid-Year', 'Two states can mean two returns.', [
    info('This example’s rule',
         'You earned **$30,000** in state A and **$20,000** in state B. In this example, each state taxes only the wages you earned there. State A’s wage tax is **0**. State B’s tax is **5%** of its **$20,000**, which is **$1,000**.\n\nReal states split income in more than one way. The lesson is that a move can create two filings. Check both states.'),
    num('What is 5% of the $20,000 earned in state B?', 1000, '$20,000 × 0.05 = $1,000.'),
    num('What are the wages in the two states together?', 50000, '$30,000 + $20,000 = $50,000.'),
    mc('Why might you file two state returns?',
       ['You earned wages in both states', 'The federal standard deduction requires it', 'FICA is paid to the state'], 0,
       'Each state may want a return for the wages earned there. This example’s tax happens to be $1,000, all in state B.'),
    tf('State A’s $0 wage tax in this example means state B also charges $0.', False,
       'State B charges $1,000. Each state’s rule is its own.'),
])

low = doc('statement', 'State A', [
    ('tax', 'State wage tax, 3% of $60,000', 1800),
], subtitle='This example')
high = doc('statement', 'State B', [
    ('tax', 'State wage tax, 6% of $60,000', 3600),
], subtitle='This example')
assert 60000 * 0.03 == 1800 and 60000 * 0.06 == 3600 and 3600 - 1800 == 1800

call = lesson('st-call', 'Two Take-Home Sketches', 'Same wages. The state line is the difference.', [
    num('What is state A’s wage tax on $60,000?', 1800,
        '$60,000 × 0.03 = $1,800.',
        context='Both sketches use the same **$60,000** of wages and ignore federal tax, sales tax, and rent. Only the state wage tax changes.',
        docs=[low, high]),
    num('What is state B’s wage tax on $60,000?', 3600,
        '$60,000 × 0.06 = $3,600.', docs=[low, high]),
    num('How much less state wage tax does state A charge?', 1800,
        '$3,600 − $1,800 = $1,800.', docs=[low, high]),
    mc('Looking only at these two state wage taxes, which page leaves more of the wages?',
       ['State A', 'State B', 'They take the same tax'], 0,
       'State A takes $1,800. State B takes $3,600.',
       why=['$1,800 is the smaller tax.', 'State B takes twice as much in this example.', 'The taxes differ by $1,800.'],
       docs=[low, high]),
    tf('The $1,800 gap is your full savings after rent and sales tax.', False,
       'This pair ignores rent and sales tax. Either one can be larger than the wage-tax gap.'),
], fmt='call')

leo_story = {
    'title': 'Leo’s two offers',
    'character': 'Leo, 31',
    'body': 'Leo is 31 and an electrician. Both offers pay **$60,000**. State A’s wage tax in this example is **$1,800**. State B’s is **$3,600**. State A saves **$1,800** of wage tax.\n\nRent in state A costs **$400** more a month, which is **$4,800** a year. The tax savings do not cover the rent.\n\nState A costs **$3,000** more after that rent. A missing wage tax, or a smaller one, is not a cheaper life until the rent and the other taxes are on the same page.',
}
leo = lesson('st-leo', 'Leo’s Offer', 'The wage-tax savings lose to the rent.', [
    num('How much wage tax does Leo save in state A?', 1800, '$3,600 − $1,800 = $1,800.'),
    num('What is $400 more rent for 12 months?', 4800, '$400 × 12 = $4,800.'),
    num('How much more does state A cost after that rent?', 3000,
        '$4,800 − $1,800 = $3,000.'),
    mc('Which offer costs less in this story, once rent is included?',
       ['State B', 'State A', 'They cost the same'], 0,
       'State A’s tax savings are $1,800. Its extra rent is $4,800. State B is $3,000 cheaper here.'),
    tf('The lower wage tax makes state A the cheaper place to live in this story.', False,
       'The rent gap is larger than the tax gap. State A costs $3,000 more.'),
], fmt='story', story=leo_story)

trial_steps = [
    num('A flat example taxes $30,000 at 4%. What is the tax?', 1200, '$30,000 × 0.04 = $1,200.'),
    num('A property tax bill is $1,800. What is the monthly set-aside?', 150, '$1,800 ÷ 12 = $150.'),
    tf('A state with no wage tax cannot charge sales tax.', False,
       'Sales tax is a different tax. It can still be on the receipt.'),
    num('State wage tax is $2,400 and extra rent is $3,600 a year. How much larger is the rent than the tax?', 1200,
        '$3,600 − $2,400 = $1,200.'),
]

lessons = [none, shape, local, house, sales, move, call, leo,
           review('st'), trial('st', 'State & Local Taxes', trial_steps)]
write_unit('08-state-local-tax.json', 'state-local-tax', 8, 'State & Local Taxes',
           'A wage tax is one line. Rent, sales tax, and the house can be larger.',
           'The state with the smaller wage tax is not automatically the cheaper life.', terms, lessons, section=S)
