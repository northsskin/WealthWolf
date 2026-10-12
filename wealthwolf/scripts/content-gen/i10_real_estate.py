from lib import *

S = 'investing'
terms = {
    'reit': term('REIT',
                 'A real estate investment trust. A company that owns property, and whose shares you can buy. You do not fix the building. The share can fall.',
                 'Buying shares of a REIT that owns many apartment buildings.'),
    'cap-rate': term('Cap rate',
                     'A property’s yearly net operating income divided by its price. The mortgage is not in that income. It is a comparison, not a promise.',
                     'Net operating income of $12,000 on a $200,000 price is a 6% cap rate.'),
}

reit_page = doc('statement', 'A REIT share',
                [('shares', 'What you paid for the shares', 2000)],
                subtitle='No tenants, no water heater',
                note='The share price can fall. You do not collect the rent yourself.')
rent_page = doc('statement', 'A rental house',
                [('price', 'Purchase price', 200000)],
                subtitle='You are the landlord',
                note='Rent comes to you. Repairs, vacancy, and night calls come to you too.')

which = lesson('re-which', 'A REIT or a Rental', 'Shares of buildings, or the building itself.', [
    info('Two ways to “own property”',
         'A [[REIT]] is a company that owns real estate. You buy shares. You do not find tenants or fix toilets, and the share can fall like other stocks. A rental is the building. You get the rent, and you get the broken water heater. Neither one is guaranteed income.'),
    mc('The water heater dies at 9pm. Which page is the owner who has to deal with it?',
         [reit_page['title'], rent_page['title']], 1,
         docs=(reit_page, rent_page),
         explain='The rental house is yours to maintain. The REIT share is a stock. Someone else runs the buildings, and you live with the share price.'),
    tf('A REIT share cannot fall, because it owns buildings.', False,
       'It is still a share. Buildings do not make the price frozen.'),
    mc('Why might someone pick a REIT instead of a rental?',
       ['They want the rent and the repair calls', 'They want real estate without being the landlord', 'REITs are FDIC insured savings'], 1,
       'No tenants. Also no control, and the price still moves. It is not a savings account.'),
    mc('Why might someone pick the rental instead?',
       ['They want a ticker and nothing else', 'They want the building, the rent, and they accept the work', 'Because cap rates cannot be negative'], 1,
       'The work is the difference. Wanting the rent means taking the vacancy and the repairs.'),
], fmt='call')

flow = doc('statement', 'One rented month',
           [('rent', 'Rent', 1500),
            ('mort', 'Mortgage', -1100),
            ('ti', 'Tax and insurance', -200),
            ('fix', 'Repair reserve', -100)],
           totals=[('Cash flow', 100, True)],
           subtitle='Every line except rent leaves',
           note='This month assumes the tenant paid. Cash flow here is after the mortgage.')

cash = lesson('re-flow', 'Cash Flow', 'Rent minus the costs, including the mortgage.', [
    info('What is left',
         'Cash flow is the rent minus the costs of the month, including the mortgage. This page assumes the tenant paid $1,500. The mortgage is $1,100, tax and insurance $200, and a repair reserve $100. What remains is the cash flow. A pretty month is not every month.'),
    num('How many dollars of cash flow does this rented month show?', 100,
        doc=flow,
        explain='$1,500 − $1,100 − $200 − $100 = $100.'),
    num('How many dollars leave for the mortgage, tax and insurance, and the repair reserve combined?', 1400,
        '$1,100 + $200 + $100 = $1,400. Rent of $1,500 minus that $1,400 is the $100.'),
    tf('Cash flow on this page is the rent before any costs.', False,
       'Cash flow is what remains. The rent is the top line, not the result.'),
    mc('What does this page quietly assume?',
       ['The tenant paid the full rent', 'The property was empty', 'There is no mortgage'], 0,
       'An empty month has a $0 rent line. The other bills stay.'),
], fmt='document')

cap = lesson('re-cap', 'Cap Rate', 'Yearly income, before the loan, divided by price.', [
    info('Leave the mortgage out',
         '[[Cap rate]] uses net operating income: yearly rent minus operating costs such as tax, insurance, repairs, and a vacancy allowance. The mortgage is not subtracted. On this example the rent is $18,000 a year, operating costs are $6,000, so net operating income is $12,000. The price is $200,000. Cap rate is $12,000 ÷ $200,000 = 6%. It compares properties. It does not promise 6% in your pocket, because the loan payment is still real.'),
    num('Yearly rent is $18,000 and operating costs are $6,000. What is net operating income, in dollars?', 12000,
        '$18,000 − $6,000 = $12,000. The mortgage is not in this subtraction.'),
    num('That $12,000 of net operating income is on a $200,000 price. What is the cap rate, in percent?', 6, unit='%',
        explain='$12,000 ÷ $200,000 = 0.06, which is 6%.'),
    tf('Cap rate is the same number as the monthly cash flow after the mortgage.', False,
       'Cap rate is before the mortgage, and it is a yearly percent of the price. Cash flow is the dollars left after the loan payment.'),
    num('A property has $10,000 of net operating income and a 5% cap rate. What price does that describe, in dollars?', 200000,
        '$10,000 ÷ 0.05 = $200,000. Same cap-rate idea, different building.'),
])

empty = lesson('re-empty', 'Vacancy and Repairs', 'The empty month still has a mortgage.', [
    info('The spreadsheet’s skipped lines',
         'One empty month means $0 of the $1,500 rent, and the $1,100 mortgage still leaves your account. A $2,400 roof does not care that cash flow was $100 in a good month. Landlords who skip these lines are surprised. The lines are the job.'),
    num('The tenant is gone for one month and rent is $1,500. How many dollars of rent do you not receive?', 1500,
        'The missing rent is $1,500. That is before the bills you still pay.'),
    num('The mortgage is $1,100 that empty month. How many dollars do you pay the lender with no rent coming in?', 1100,
        'The loan does not pause. $1,100 goes out while rent is $0.'),
    num('A good month cash-flows $100. A $2,400 roof is how many of those months?', 24, unit='months',
        explain='$2,400 ÷ $100 = 24 months. Two years of the good-month cash flow, for one roof.'),
    tf('A repair reserve on the cash-flow page means repairs will not happen.', False,
       'The reserve is you admitting they will. Skipping it makes the $100 look safer than it is.'),
])

land = lesson('re-land', 'Being a Landlord', 'It is a part-time job with a building.', [
    info('Not a ticker',
         'A landlord screens tenants, follows the law on deposits and notices, and answers the phone. A [[REIT]] is the version where you do none of that and you own a share instead. Calling a rental “passive income” skips the work. Some months are quiet. The quiet is not the job description.'),
    mc('Which task belongs to a landlord and not to a REIT shareholder?',
       ['Watching a share price', 'Showing the unit and handling a broken lock', 'Rebalancing an index fund'], 1,
       'The building is a job. The share is not.'),
    tf('Rental income is passive, so the work is optional.', False,
       'The rent and the work come together. A REIT is what you buy when you want the work to be someone else’s.'),
    mc('A tenant does not pay. What is the grown-up framing?',
       ['Buildings always pay', 'Vacancy and unpaid rent are part of the job, not a surprise you can ignore', 'SIPC covers the missed rent'], 1,
       'You plan for empty months. You do not pretend the lease is a bond.'),
    fill('Someone who owns a rental and deals with tenants is a ___.',
         ['landlord', 'coupon', 'ticker'], 0,
         'Landlord. A REIT shareholder is not on that call list.'),
])

hack = lesson('re-hack', 'House Hacking', 'Live in one unit. Rent the other.', [
    info('The duplex version',
         'House hacking means you live in one unit and a tenant pays rent on the other. A duplex mortgage is $2,000 a month. The other unit rents for $1,200. Your housing cost that month is $800, before repairs and before a vacant month. You are still the landlord for that unit.'),
    num('The mortgage is $2,000 and the other unit pays $1,200. How many dollars of the mortgage are left for you that month?', 800,
        '$2,000 − $1,200 = $800. That is before repairs, tax, and vacancy.'),
    tf('House hacking means you are not a landlord.', False,
       'The other unit has a tenant. Their leak is your leak.'),
    num('The other unit sits empty for a month. How many dollars of the $2,000 mortgage do you cover yourself?', 2000,
        'No rent comes in. You cover the whole $2,000 that month.'),
    mc('What is the actual benefit when the tenant pays?',
       ['The mortgage disappears', 'Their rent covers part of a mortgage you would have paid anyway', 'The duplex cannot fall in value'], 1,
       'The $1,200 reduces what you pay. It does not remove the loan, the repairs, or price risk.'),
])

lever = lesson('re-lev', 'Leverage Cuts Both Ways', 'A loan makes the gain bigger and the loss bigger.', [
    info('The $40,000 that can vanish',
         'A $200,000 place with $40,000 down means a $160,000 loan. Your equity is $40,000. If the value falls 20%, to $160,000, the loan is still $160,000 and the equity is $0. Had you paid all cash, the same 20% drop would leave you $160,000 of a $200,000 place. The loan is why the whole down payment can disappear. A rise would have magnified the gain the same way. Both directions are the deal.'),
    num('The value falls from $200,000 to $160,000. How many dollars did the price drop?', 40000,
        '20% of $200,000 is $40,000. The new price is $160,000.'),
    num('The loan is still $160,000 and the place is worth $160,000. How many dollars of equity are left?', 0,
        '$160,000 − $160,000 = $0. The $40,000 down payment is gone on paper.'),
    tf('The loan shrinks when the property value shrinks.', False,
       'The loan stays. The equity takes the drop, which is why a 20% price drop can erase a 20% down payment.'),
    mc('All-cash, the same 20% drop on $200,000 leaves you with how much property?',
       ['$0', '$160,000 of property and no loan', '$200,000, because cash cannot fall'], 1,
       'You would still own a $160,000 place free and clear. Leverage is what turned that same drop into $0 of equity.'),
])

sofia = lesson('re-sofia', 'Sofia Runs the Numbers', 'The good month is not the year.', [
    info('Meet Sofia',
         'Sofia is 38 and a nurse. A duplex is listed at $200,000. Both units together could rent for $1,500 a month, $18,000 a year. Operating costs of $6,000 leave $12,000 of net operating income, a 6% cap rate.\n\nA loan would make a good month cash-flow about $100 after the mortgage, tax, insurance, and a small repair reserve. She notices that one empty month erases $1,500 of rent and still wants the mortgage paid. She has not decided to buy.'),
    num('What is the cap rate, in percent, on Sofia’s $12,000 of net operating income and the $200,000 price?', 6, unit='%',
        explain='$12,000 ÷ $200,000 = 6%. That figure is before the mortgage.'),
    num('One empty month skips $1,500 of rent. How many of the $100 cash-flow months does that one month wipe out?', 15, unit='months',
        explain='$1,500 ÷ $100 = 15 months. One vacancy is not a rounding error.'),
    tf('Sofia should buy because a 6% cap rate is a guaranteed 6% profit.', False,
       'Cap rate leaves out the mortgage, and vacancy can erase the cash flow. It is a comparison, not a promise.'),
    mc('What is Sofia doing in this lesson?',
       ['Buying because a friend said property always wins', 'Running the rent, the costs, and the empty month before she decides', 'Trading a REIT on margin'], 1,
       'The numbers come first. The decision can still be no.'),
], fmt='story', story={
    'title': 'Before she bids',
    'character': 'Sofia, 38, nurse',
    'body': 'A duplex is listed at **$200,000**. Rent of **$18,000** a year minus **$6,000** of operating costs leaves **$12,000**, a **6%** cap rate, before any mortgage.\n\nA good month might cash-flow **$100** after the loan. One empty month skips **$1,500** of rent. Sofia has not decided to buy.',
})

write_unit('10-real-estate.json', 'real-estate', 10, 'Real Estate Investing',
           'Shares of buildings, or the building, the loan, and the empty month.',
           'Run the empty month before you fall in love with the rent.',
           terms, [which, cash, cap, empty, land, hack, lever, sofia, review('re'), trial('re', 'Real Estate Investing', [
               num('Yearly rent is $24,000 and operating costs are $8,000. What is net operating income?', 16000,
                   '$24,000 − $8,000 = $16,000. Do not subtract the mortgage for this figure.'),
               num('Net operating income is $16,000 and the price is $200,000. What is the cap rate, in percent?', 8, unit='%',
                   explain='$16,000 ÷ $200,000 = 0.08, which is 8%.'),
               tf('A REIT shareholder is the person who fixes the tenant’s sink.', False,
                  'That is the landlord. A REIT is the share. The share can still fall.'),
               num('You put $50,000 down on a $250,000 place, so the loan is $200,000. The value falls to $200,000. How many dollars of equity are left?', 0,
                   '$200,000 of value minus a $200,000 loan is $0 of equity.'),
           ])],
           section=S)
