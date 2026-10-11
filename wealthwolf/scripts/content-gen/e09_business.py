from lib import *

S = 'earning'
terms = {
    'startup-costs': term('Startup costs', 'What you spend to get a business going, before your first sale.', 'A $150 stall permit and a $220 canopy.'),
    'revenue': term('Revenue', 'All the money customers pay you, before any costs come out.', '60 loaves at $8 = $480 of revenue.'),
    'profit': term('Profit', 'What’s left of revenue after you pay your costs.', '$480 revenue − $220 costs = $260 profit.'),
    'sole-proprietorship': term('Sole proprietorship', 'A business owned by one person with no legal separation from them. You’re one by default when you start selling on your own.',
                                'Selling bread at a market under your own name.'),
    'llc': term('LLC', 'A limited liability company: a business registered with your state that keeps business debts separate from your personal money.',
                'Imani’s Bakery LLC, so a business lawsuit can’t take her savings.'),
    'ein': term('EIN', 'Employer Identification Number: a free business tax ID from the IRS, like a Social Security number for your business.',
                'Needed to open some business bank accounts or hire employees.'),
}

idea = lesson('bz-idea', 'From Idea to Business', 'A business solves a problem people will pay for.', [
    info('A problem people pay to solve',
         'Before spending a dollar, check three things: who has this problem, will they pay to fix it, and can you deliver it for less than they’ll pay?'),
    mc('Which is the strongest business idea?', ['Something people already pay for, that you can do better or cheaper', 'Something only you would want', 'A cool name with no customers yet'], 0,
       'Proven demand beats a clever idea.'),
    mc('What’s the cheapest way to test an idea?', ['Sell a small batch to real customers', 'Rent a shop first', 'Print 5,000 business cards'], 0,
       'Real sales are the only real proof.'),
    tf('Talking to potential customers before you build anything saves money.', True, 'They’ll tell you what they’d actually buy.'),
    order('Put these in order.', ['Spot a problem people pay to solve', 'Ask potential customers', 'Test with a small batch', 'Grow what works'],
          'Problem, people, proof, growth.'),
    mc('Friends say they’d “totally buy it.” What’s better proof?', ['Someone actually paying', 'More compliments', 'Likes on a post'], 0,
       'Compliments are free. Money isn’t.'),
])

su_lines = [('permit', 'Market stall permit', 150.00), ('canopy', 'Folding table and canopy', 220.00), ('supplies', 'Baking supplies, first batch', 180.00),
            ('pack', 'Packaging and labels', 95.00), ('reader', 'Card reader', 49.00), ('cert', 'Food handler certificate', 25.00)]
SU = doc('bill', 'Imani’s bakery stall', su_lines, subtitle='Startup costs')
assert total(l[2] for l in su_lines) == 719
startup = lesson('bz-startup-costs', 'Startup Costs', 'What it takes to make the first sale.', [
    mc('Which of these is a startup cost?', ['The stall permit', 'A customer’s payment', 'Profit'], 0, 'Spent before the first sale.',
       context='[[Startup costs]] are what you spend to get a business going, before your first sale.', doc=SU),
    num('Add up the startup costs.', 719, '$150 + $220 + $180 + $95 + $49 + $25 = $719.', doc=SU),
    num('Imani set aside $1,000 for the business. How much is left as a cushion?', 281, '$1,000 − $719 = $281.', doc=SU),
    mc('Which cost will she pay again for every market?', ['Baking supplies', 'The canopy', 'The card reader'], 0, 'The canopy and reader last. Flour doesn’t.', doc=SU),
    tf('Buying used equipment can cut startup costs a lot.', True, 'A secondhand canopy works the same.'),
    mc('Should Imani use her emergency fund to start?', ['No: use money set aside for the business', 'Yes, all of it', 'Borrow at 30%'], 0,
       'The emergency fund is for emergencies. A business is a choice.'),
], fmt='document')

rp = lesson('bz-revenue-profit', 'Revenue vs. Profit', 'Sales feel great. Profit pays you.', [
    mc('Which tells you whether the business is working?', ['Profit', 'Revenue'], 0, 'Revenue is busy. Profit is working.',
       context='[[Revenue]] is all the money customers pay you. [[Profit]] is what’s left after your costs.'),
    num('You sell 60 loaves at $8 each. What’s the revenue?', 480, '60 × $8 = $480.'),
    num('Ingredients and packaging cost $3 a loaf, and the stall fee is $40. What are the total costs?', 220, '60 × $3 + $40 = $220.'),
    num('What’s the profit?', 260, '$480 − $220 = $260.'),
    tf('A business can have big revenue and still lose money.', True, 'If costs are bigger than revenue, more sales can mean bigger losses.'),
    num('That $260 of profit took 10 hours of baking and selling. What’s that per hour?', 26, '$260 ÷ 10 = $26.'),
])

struct = lesson('bz-structures', 'Sole Proprietor or LLC?', 'How the law sees you and your business.', [
    mc('What’s the risk of being a sole proprietorship?', ['Business debts can come after your personal money', 'None', 'You can’t sell anything'], 0,
       'You and the business are the same in the eyes of the law.',
       context='If you start selling on your own, you’re a [[sole proprietorship]] by default: legally, you and the business are the same.'),
    mc('What’s the main reason people form an LLC?', ['To protect personal money from business debts and lawsuits', 'To avoid all taxes', 'Because it’s free'], 0,
       'A wall between the business and your savings.',
       context='An [[LLC]] (limited liability company) is a business you register with your state. It keeps business debts separate from your personal money, for a filing fee.'),
    sort('Sole proprietorship or LLC?', ['Sole proprietorship', 'LLC'],
         [('You’re one automatically when you start selling', 0), ('You file paperwork with your state', 1), ('No legal separation from your personal money', 0),
          ('Your personal savings are shielded from business debts', 1), ('Usually has a yearly state fee', 1), ('The simplest way to test a small idea', 0)]),
    tf('Forming an LLC means you pay no taxes.', False, 'An LLC changes your legal protection, not whether you pay tax.'),
    mc('Testing a $500 side business, most people start as…', ['a sole proprietor, then form an LLC as it grows', 'a big corporation', 'a nonprofit'], 0,
       'Start simple, protect as you grow.'),
    mc('Who should you ask about structure as you grow?', ['An accountant, or free advisors through the SBA and SCORE', 'A random forum', 'Nobody'], 0,
       'Free, expert help exists.'),
], fmt='sort')

sep = lesson('bz-separate', 'Keep Business Money Separate', 'One account for the business, one for you.', [
    mc('Why open a separate business bank account?', ['Clean records, easier taxes and a clear view of profit', 'Banks require it for everyone', 'No real reason'], 0,
       'Mixed money hides whether you’re making any.'),
    mc('What does an EIN cost from the IRS?', ['Nothing', '$250', '$1,000'], 0, 'It’s free on IRS.gov. Sites that charge are middlemen.',
       context='An [[EIN]] is a free business tax ID from the IRS, like a Social Security number for your business.'),
    tf('Mixing business and personal spending makes it hard to know if you’re profitable.', True, 'You can’t measure what you can’t separate.'),
    sort('Business account or personal?', ['Business', 'Personal'],
         [('Flour for the bakery', 0), ('Your own groceries', 1), ('The stall permit', 0), ('Movie tickets', 1), ('Card reader fees', 0)]),
    mc('You need business money for yourself. What’s the proper way?', ['Transfer a set amount to your personal account and record it', 'Use the business card at dinner', 'Take cash from the till and not note it'], 0,
       'Clean, recorded, on purpose.'),
    order('Setting up business money. Put it in order.', ['Get an EIN if you need one', 'Open a business account', 'Run all sales and costs through it', 'Pay yourself by transfer'],
          'ID, account, discipline, paycheck.'),
])

SHOP = doc('bill', 'Plan A: open a shop', [('rent', 'Shop rent, per month', 1800.00), ('build', 'Build-out and equipment, once', 15000.00)], subtitle='Quit and go all in')
STALL = doc('bill', 'Plan B: market stall', [('fee', 'Stall fee, per market', 40.00), ('setup', 'Setup costs, once', 719.00)], subtitle='Keep your job, sell on Saturdays')
assert 1800 * 12 == 21600 and 21600 + 15000 == 36600 and 50 * 40 + 719 == 2719
test = lesson('bz-test', 'Test Before You Quit', 'Find out if people buy, as cheaply as possible.', [
    mc('Which risks less money to learn whether people will buy?', ['Plan B: the market stall', 'Plan A: the shop'], 0, 'A $719 experiment vs. a $36,600 one.', docs=[SHOP, STALL]),
    num('What’s Plan A’s rent for the first year?', 21600, '$1,800 × 12 = $21,600.', docs=[SHOP, STALL]),
    num('Plan A’s first-year cost, including the $15,000 build-out?', 36600, '$21,600 + $15,000 = $36,600.', docs=[SHOP, STALL]),
    num('Plan B: 50 markets at $40, plus $719 of setup. Cost for the year?', 2719, '50 × $40 + $719 = $2,719.', docs=[SHOP, STALL]),
    mc('When does a shop start to make sense?', ['When the stall keeps selling out and you know your numbers', 'Day one', 'Never'], 0, 'Let demand pull you into bigger costs.'),
    tf('Keeping your job while testing a business lowers the risk a lot.', True, 'Your rent is covered while you learn.'),
], fmt='call')

fund = lesson('bz-funding', 'Paying to Get Started', 'Savings, partners, loans and grants.', [
    mc('What’s the safest way to fund a small start?', ['Savings set aside for the business', 'Your emergency fund', 'Credit cards at 25%'], 0, 'Money you can afford to risk.'),
    mc('A friend offers $5,000 for “part of the business.” What do you need?', ['A written agreement on what they own and get back', 'A handshake', 'Nothing'], 0,
       'Friendships survive clear paperwork better than vague promises.'),
    num('A $10,000 loan at 12% a year. Interest in the first year if you don’t repay any of it?', 1200, '$10,000 × 0.12 = $1,200.'),
    tf('Many small businesses start with very little money and grow from their own profits.', True, 'Slow and self-funded is a real path.'),
    mc('Business grants are…', ['money you don’t repay, but competitive and with rules', 'loans', 'taxes'], 0, 'Worth applying for, not worth counting on.'),
    mc('Before borrowing for a business, you should know…', ['how the business will make the payments', 'the bank’s logo', 'nothing'], 0, 'Debt needs a plan to pay it back.'),
])

imani_story = {
    'title': 'Saturday bread',
    'character': 'Imani, 32, dental office manager',
    'body': 'Imani works weekdays at a dental office and sells bread at a Saturday market. In her first month she went to **4** markets.\n\n'
            'She sold **210** loaves at **$8** each. Ingredients and packaging cost **$3** a loaf, and the stall costs **$40** per market. '
            'Baking and selling took her **36** hours.',
}
assert 210 * 8 == 1680 and 210 * 3 == 630 and 1680 - 630 - 160 == 890 and round(890 / 36, 2) == 24.72
imani = lesson('bz-imani', 'Imani’s Bakery Stall', 'One month of a real small business, by the numbers.', [
    num('What was her revenue for the month?', 1680, '210 × $8 = $1,680.'),
    num('What did ingredients and packaging cost?', 630, '210 × $3 = $630.'),
    num('What did the stall fees cost?', 160, '4 × $40 = $160.'),
    num('What was her profit?', 890, '$1,680 − $630 − $160 = $890.'),
    num('What’s her profit per hour? Round to the cent.', 24.72, '$890 ÷ 36 = $24.72.'),
    mc('What should Imani do with the profit first?', ['Set aside about 25% for taxes', 'Spend it all', 'Quit her job'], 0, 'Business profit is taxable income.'),
], fmt='story', story=imani_story)

trial_steps = [
    num('Revenue $900, costs $540. What’s the profit?', 360, '$900 − $540 = $360.'),
    mc('What’s the main reason to form an LLC?', ['Protect personal money from business debts', 'Avoid all taxes', 'It’s required for every business'], 0, 'Liability protection.'),
    tf('An EIN from the IRS is free.', True, 'Don’t pay a website for it.'),
    mc('What’s the cheapest way to test a business idea?', ['Sell a small batch to real customers', 'Sign a shop lease', 'Hire staff first'], 0, 'Proof before spending.'),
]

lessons = [idea, startup, rp, struct, sep, test, fund, imani, review('bz'), trial('bz', 'Starting a Business', trial_steps)]
write_unit('09-small-business.json', 'small-business', 9, 'Starting a Small Business', 'Test an idea, count the costs, and set the business up properly.',
           'Every pack started with one wolf and a good idea.', terms, lessons, section=S)
