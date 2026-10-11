from lib import *

S = 'earning'
terms = {
    'markup': term('Markup', 'Your profit on an item, as a percent of what it cost you.', 'Cost $6, price $15: $9 profit is a 150% markup.'),
    'profit-margin': term('Profit margin', 'Your profit on an item, as a percent of its price.', 'Price $15, profit $9: a 60% margin.'),
    'break-even-point': term('Break-even point', 'How many sales it takes to cover all your costs. Below it you lose money, above it you profit.',
                             'Costs of $600 a month, $15 left per sale: break even at 40 sales.'),
    'profit-and-loss': term('Profit and loss statement', 'A report of a period’s revenue, costs and profit. Often called a P&L.',
                            'March: $3,750 revenue, $1,821.50 costs, $1,928.50 profit.'),
    'owners-draw': term('Owner’s draw', 'Moving profit from your business account to your personal account to pay yourself.',
                        'Transferring $1,200 to yourself on the 1st of each month.'),
}

pricing = lesson('bc-pricing', 'Price to Cover Your Costs', 'Every price has to beat your costs and survive your customers.', [
    info('Three numbers behind every price',
         'What each item costs you to make, what the business costs to run each month, and what customers will pay. '
         'Your price has to beat the first two, and survive the third.'),
    num('A candle costs you $6 to make. You sell it for $15. How much is left per candle?', 9, '$15 − $6 = $9.'),
    num('Your booth costs $120 a month. How many candles must you sell just to cover it? Round up to a whole candle.', 14,
        '$120 ÷ $9 = 13.3, so 14 candles.', unit='candles'),
    mc('A competitor sells similar candles for $12. What do you do?', ['Show why yours are worth $15, or find ways to cut costs', 'Sell at $5 to win', 'Ignore them'], 0,
       'Racing to the bottom rarely ends well.'),
    tf('Pricing too low can make a busy business lose money.', True, 'More sales at a loss is more loss.'),
    mc('Which costs belong in your price?', ['Materials, your time, fees and overhead', 'Only materials', 'None'], 0, 'If it costs you, the price must cover it.'),
])

mm = lesson('bc-markup-margin', 'Markup and Margin', 'Two ways to measure the same profit.', [
    num('Cost $6, price $15, profit $9. What’s the markup?', 150, '$9 ÷ $6 = 1.5, which is 150%.', unit='%',
        context='[[Markup]] compares your profit to your cost. [[Profit margin]] compares your profit to the price.'),
    num('And the profit margin?', 60, '$9 ÷ $15 = 0.6, which is 60%.', unit='%'),
    mc('Which is always the smaller percent?', ['Margin', 'Markup'], 0, 'Margin divides by the bigger number, the price.'),
    num('You want a 50% margin on something that costs you $10. What price? (Price = cost ÷ 0.5)', 20, '$10 ÷ 0.5 = $20.'),
    tf('A 100% markup means you charge double your cost.', True, 'Cost $10, profit $10, price $20.'),
    num('Cost $8, price $10. What’s the profit margin?', 20, '$2 ÷ $10 = 0.2, which is 20%.', unit='%'),
])

be = lesson('bc-break-even', 'The Break-Even Point', 'How many sales before you make a dime.', [
    mc('What happens at the break-even point?', ['Revenue equals costs: no profit, no loss', 'Profit is highest', 'You go broke'], 0, 'Every sale after it is profit.',
       context='Your [[break-even point]] is how many sales it takes to cover all your costs. Below it you lose money, above it you profit.'),
    num('Monthly costs are $600. Each sale leaves $15 after its own costs. How many sales to break even?', 40, '$600 ÷ $15 = 40.', unit='sales'),
    num('You make 55 sales. What’s the profit?', 225, '15 sales past break-even × $15 = $225.'),
    num('Raise the price so each sale leaves $20. What’s the new break-even?', 30, '$600 ÷ $20 = 30.', unit='sales'),
    tf('Lowering your monthly costs lowers your break-even point.', True, 'Less to cover, fewer sales needed.'),
    mc('You sell 25 a month and break-even is 40. Your options?', ['Raise prices, cut costs, or sell more', 'Ignore it', 'Hire more people'], 0,
       'Three levers. Pull at least one.'),
])

cash = lesson('bc-cash-timing', 'Profit Isn’t Cash', 'Why profitable businesses still run out of money.', [
    info('Profitable and broke',
         'A business can be profitable on paper and still run out of cash, because money goes out before it comes in. '
         'You pay for supplies today, and customers may pay you in 30 or 60 days.'),
    num('You buy $2,000 of supplies on May 1. The client pays $3,500 on June 15. What’s the profit on the job?', 1500, '$3,500 − $2,000 = $1,500.'),
    mc('On May 31, how does your cash look?', ['Down $2,000, waiting on payment', 'Up $1,500', 'Even'], 0, 'The profit exists, but not in your account yet.'),
    mc('How can you close the gap?', ['Deposits upfront, faster invoicing, or a cash cushion', 'Ignore it', 'Pay suppliers late on purpose'], 0, 'Get money in sooner, or keep more on hand.'),
    tf('Cash flow problems sink many profitable small businesses.', True, 'Running out of cash ends a business faster than low profit.'),
    mc('Which habit speeds up cash coming in?', ['Invoicing the day the work is done', 'Waiting a month to invoice', 'Offering 90-day terms'], 0,
       'The clock on net 30 only starts when you invoice.'),
])

pl_lines = [('candles', 'Candle sales', 3150.00, {'section': 'Revenue'}), ('workshops', 'Workshop tickets', 600.00, {'section': 'Revenue'}),
            ('materials', 'Wax, wicks and jars', -1260.00, {'section': 'Costs'}), ('booth', 'Booth rent', -240.00, {'section': 'Costs'}),
            ('cardfees', 'Card fees', -112.50, {'section': 'Costs'}), ('pack', 'Packaging', -180.00, {'section': 'Costs'}),
            ('web', 'Website', -29.00, {'section': 'Costs'})]
PL = doc('bill', 'Wick & Co. Candles', pl_lines, subtitle='Profit and loss · March')
assert total([3150, 600]) == 3750 and total([1260, 240, 112.5, 180, 29]) == 1821.50 and total(l[2] for l in pl_lines) == 1928.50
pl = lesson('bc-pl', 'Read a Profit & Loss', 'One page that tells you if the month worked.', [
    num('What was total revenue in March?', 3750, '$3,150 + $600 = $3,750.',
        context='A [[profit and loss statement|profit-and-loss]] (P&L) lists a period’s revenue, then its costs, and ends with profit.', doc=PL),
    num('Add up the costs.', 1821.50, '$1,260.00 + $240.00 + $112.50 + $180.00 + $29.00 = $1,821.50.', doc=PL),
    num('What was the profit?', 1928.50, '$3,750.00 − $1,821.50 = $1,928.50.', doc=PL),
    num('What’s the profit margin? Round to the nearest whole percent.', 51, '$1,928.50 ÷ $3,750 = 0.514, about 51%.', unit='%', doc=PL),
    mc('Which cost is the biggest?', ['Wax, wicks and jars', 'Booth rent', 'Website'], 0, '$1,260, about two thirds of all costs.', doc=PL),
    tf('Comparing this month’s P&L with last month’s shows whether you’re improving.', True, 'One month is a photo. Several are a movie.'),
], fmt='document')

leak_lines = [('etsy', 'Marketplace selling fees', -96.40, {'date': 'Apr 2'}), ('labels', 'Shipping labels', -61.25, {'date': 'Apr 5'}),
              ('design', 'DesignPro subscription', -29.99, {'date': 'Apr 8'}), ('wax', 'Wax supplier', -310.00, {'date': 'Apr 12'}),
              ('ads', 'Online ads, spring sale', -50.00, {'date': 'Apr 15'})]
LEAK = doc('statement', 'Wick & Co. business account', leak_lines, subtitle='Checking · Apr 1–15')
leak = lesson('bc-find-leak', 'Find the Leak', 'Old subscriptions quietly eat small businesses too.', [
    spot('You switched to a free design app in January. Tap the charge that’s still running.', LEAK, 'design',
         'An old subscription you no longer use.', context='Business accounts leak like personal ones. Read the statement every month.'),
    num('What does that leak cost over a year?', 359.88, '$29.99 × 12 = $359.88.'),
    num('Your profit margin is 50%. How much in extra sales would it take to earn that $359.88 back?', 719.76, 'At 50%, $719.76 of sales leaves $359.88 of profit.'),
    tf('Cutting a cost can be worth more than the same amount of new sales.', True, 'A dollar saved is a whole dollar. A dollar of sales is only its margin.'),
    mc('What’s the habit that catches these?', ['A monthly review of every business charge', 'Checking once a year', 'Never'], 0, 'The same check-in you do at home.'),
], fmt='spot')

draw = lesson('bc-pay-yourself', 'Paying Yourself', 'Taxes first, cushion second, you third.', [
    mc('What’s an owner’s draw?', ['Moving business profit to yourself', 'A drawing contest', 'A bank loan'], 0, 'Your paycheck, when you’re the boss.',
       context='When you own the business, you pay yourself with an [[owner’s draw|owners-draw]]: moving profit from the business account to your personal one.'),
    num('Profit is $2,000 this month. Set aside 25% for taxes. How much is left?', 1500, '$2,000 × 0.75 = $1,500.'),
    num('Keep 20% of that in the business as a cushion. What can you draw?', 1200, '$1,500 × 0.80 = $1,200.'),
    mc('Why pay yourself a steady amount instead of everything in good months?', ['It smooths out the slow months', 'It’s the law', 'For taxes only'], 0,
       'The same idea as an income buffer.'),
    tf('Taking every dollar out leaves nothing for slow months or growth.', True, 'The business needs savings too.'),
    mc('The business has a great month. Best move?', ['Keep your usual draw and grow the cushion', 'Draw it all and spend it', 'Close the account'], 0,
       'Good months pay for bad ones.'),
])

busy_story = {
    'title': 'The big order',
    'character': 'Imani, 32, now baking full time',
    'body': 'In December, a company orders **$4,200** of holiday bread, to be paid **30** days after delivery.\n\n'
            'On Dec 1 Imani spends **$1,800** on ingredients. Her business account had **$2,500**. Her kitchen rent of **$400** is due Dec 15.\n\n'
            'On Dec 20 her oven needs a **$500** repair. The client’s payment arrives Jan 5.',
}
busy = lesson('bc-imani-busy', 'Imani’s Busy Season', 'A great order, and a cash crunch anyway.', [
    num('What’s the profit on the order, before kitchen rent?', 2400, '$4,200 − $1,800 = $2,400.'),
    num('After buying ingredients on Dec 1, what’s left in her account?', 700, '$2,500 − $1,800 = $700.'),
    num('After the $400 kitchen rent on Dec 15, what’s left?', 300, '$700 − $400 = $300.'),
    mc('The $500 oven repair on Dec 20. What’s the problem?', ['She can’t cover it until the client pays', 'No problem', 'The profit covers it'], 0,
       '$2,400 of profit, $300 of cash. Profit isn’t cash.'),
    mc('What would have prevented the crunch?', ['Asking for a 50% deposit on the order', 'Lower prices', 'Buying more ingredients'], 0, 'Deposits fund the work.'),
    num('A 50% deposit on $4,200 would have brought in how much on Dec 1?', 2100, '$4,200 × 0.50 = $2,100.'),
], fmt='story', story=busy_story)

trial_steps = [
    num('Monthly costs $900, and each sale leaves $30. How many sales to break even?', 30, '$900 ÷ $30 = 30.', unit='sales'),
    num('Cost $12, price $20. What’s the profit margin?', 40, '$8 ÷ $20 = 0.4, which is 40%.', unit='%'),
    tf('A profitable business can still run out of cash.', True, 'Timing matters as much as profit.'),
    mc('Moving business profit into your personal account is called…', ['an owner’s draw', 'a business loan', 'a tax form'], 0, 'Profit moving to you.'),
]

lessons = [pricing, mm, be, cash, pl, leak, draw, busy, review('bc'), trial('bc', 'Business Cash', trial_steps)]
write_unit('10-business-cash.json', 'business-cash', 10, 'Business Cash Flow & Pricing', 'Price for profit, read a P&L, and keep cash coming in.',
           'Profit is the kill. Cash is what you can eat today.', terms, lessons, section=S)
