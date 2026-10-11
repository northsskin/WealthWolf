import json, os
from decimal import Decimal as Dc
from lib import *

path = os.path.join(DATA, SECTION, '06-saving.json')
old = json.load(open(path))
L = {l['id']: l for l in old['lessons']}
terms = dict(old['terms'])
terms['apy'] = term('APY', 'Annual percentage yield: what your savings earn in a year, counting the interest your interest earns.',
                    '$5,000 at 4.00% APY earns about $200 in a year.')
terms['savings-goal'] = term('Savings goal', 'A target with three parts: what it’s for, how much it costs, and when you need it.',
                             '$1,800 for a used scooter by June.')

why = lesson('sv-why-save', 'Why Save?', 'Savings turn emergencies into inconveniences.', [
    info('Future you is counting on you',
         'Saving means keeping some of today’s money for later. It turns a broken phone, a lost job or a surprise bill from a crisis into an annoyance.\n\n'
         'It’s also how you pay for big things (a car, a trip, a deposit on an apartment) without borrowing.'),
    mc('Your laptop dies. Which is the better place to be?',
       ['Having $800 saved and buying a new one', 'Having nothing and borrowing at a high cost', 'Going without one for months'], 0,
       'Savings make it a shopping trip instead of a crisis.'),
    sort('What kind of saving is it? Sort them.', ['Safety net', 'Goal'],
         [('A surprise car repair', 0), ('A trip to Japan next year', 1), ('Rent if you lose your job', 0),
          ('A new bike in the spring', 1), ('A vet bill you didn’t see coming', 0), ('A deposit on your own apartment', 1)]),
    num('Saving $25 a week, how much do you have after a year of 52 weeks?', 1300, '$25 × 52 = $1,300.'),
    tf('You need a big income before saving is worth it.', False, '$25 a week is $1,300 a year. Starting small builds the habit.'),
    mc('What’s the hardest part of saving for most people?', ['Starting, then sticking with it', 'Finding a bank', 'Doing the math'], 0,
       'That’s why the next lessons are about making it automatic.'),
])

dana_story = {
    'title': 'The transmission',
    'character': 'Dana, 31, home care nurse',
    'body': 'Dana needs a car to get to patients’ homes. Last Tuesday the transmission failed. The repair: **$1,450**.\n\n'
            'A few years ago that would have meant borrowing. This time Dana had an emergency fund of **$4,200**, built up at **$145** a month.\n\n'
            'Dana’s essential expenses are **$1,900** a month.',
}
dana = lesson('sv-dana', 'Dana’s Rainy Day', 'A real emergency, a real fund, and what happens next.', [
    num('How much is left in the fund after the repair?', 2750, '$4,200 − $1,450 = $2,750.'),
    mc('Was this a real emergency?', ['Yes: Dana needs the car to earn a living', 'No: it’s a want', 'No: it was planned'], 0,
       'Unexpected, necessary and urgent. That’s exactly what the fund is for.'),
    num('Before the repair, how many full months of essential expenses did Dana have saved? Round down to whole months.', 2,
        '$4,200 ÷ $1,900 = 2.2, so 2 full months.', unit='months'),
    num('At $145 a month, how many months will it take to rebuild the $1,450?', 10, '$1,450 ÷ $145 = 10 months.', unit='months'),
    mc('What should Dana do now?', ['Keep saving $145 a month until it’s back to $4,200', 'Stop saving, the emergency is over', 'Spend the rest on something fun'], 0,
       'Refill the cushion before the next surprise.'),
    tf('Using an emergency fund for an emergency means you failed.', False, 'That’s exactly what it’s for. Then you refill it.'),
], fmt='story', story=dana_story)

# Quarterly interest at 4.00% APY on $5,000: each quarter's interest is a little bigger than the last.
rate = (Dc('1.04') ** (Dc(1) / Dc(4))) - 1
bal = Dc('5000.00')
quarters = []
for q, date in enumerate(['Mar 31', 'Jun 30', 'Sep 30', 'Dec 31']):
    i = (bal * rate).quantize(Dc('0.01'))
    quarters.append((f'q{q + 1}', 'Interest paid', float(i), {'date': date}))
    bal += i
interest = total(q[2] for q in quarters)
assert abs(interest - 200) < 0.05, interest
SAV = doc('statement', 'Harbor Bank Savings', quarters, subtitle='Year summary', meta=[['Account', '•••• 9902'], ['APY', '4.00%']],
          totals=[('Opening balance', 5000.00), ('Closing balance', float(bal), True)])
LOW = doc('bill', 'Main Street Savings', [('fee', 'Monthly fee', 0.00)], subtitle='Savings account', meta=[['APY', '0.50%']])
HIGH = doc('bill', 'Cloud High-Yield Savings', [('fee', 'Monthly fee', 0.00)], subtitle='Online savings account', meta=[['APY', '4.00%']])
grow = lesson('sv-interest-math', 'Watch It Grow', 'Read a savings statement and see interest earning interest.', [
    mc('What APY does this account pay?', ['4.00%', '1.00%', '40%'], 0, 'It’s right at the top: 4.00%.',
       context='Banks show savings rates as [[APY]], the annual percentage yield: what you’ll earn in a year, counting the interest your interest earns.', doc=SAV),
    num('Add up the four interest lines. How much did the account earn this year?', interest,
        ' + '.join(f'${q[2]:.2f}' for q in quarters) + f' = ${interest:.2f}.', doc=SAV),
    num('Without the statement: what’s 4% of $5,000?', 200, '$5,000 × 0.04 = $200. APY tells you the year’s total up front.'),
    mc('Why does each interest line get a little bigger?', ['Earlier interest is now earning interest too', 'The bank feels generous', 'The APY went up'], 0,
       'Each quarter’s interest joins the balance, so the next quarter pays on a bigger number.', doc=SAV),
    num('Same $5,000 for a year. How much more does the 4.00% account earn than the 0.50% one?', 175,
        '4.00%: $5,000 × 0.04 = $200. 0.50%: $5,000 × 0.005 = $25. $200 − $25 = $175.', docs=[LOW, HIGH]),
    tf('Savings account rates can change over time.', True, 'Most savings rates move with the economy. Check yours once or twice a year.'),
], fmt='document')

goals = lesson('sv-goals', 'Saving for a Goal', 'What, how much, by when. Then divide.', [
    mc('Which is a real savings goal?', ['$1,800 for a used scooter by June', 'Save more', 'Be rich someday'], 0,
       'It has all three parts: what, how much and when.',
       context='A [[savings goal]] has three parts: what it’s for, how much it costs, and when you need it.'),
    num('You need $1,800 in 9 months. How much a month?', 200, '$1,800 ÷ 9 = $200.'),
    num('You can only manage $150 a month. How many months will $1,800 take?', 12, '$1,800 ÷ $150 = 12 months.', unit='months'),
    mc('Two goals: $600 for a trip in 4 months, and $2,400 for a car in 24 months. You can save $250 a month. Which split works?',
       ['$150 to the trip and $100 to the car', 'All $250 to the car, then the trip', '$125 to each'], 0,
       '$150 × 4 = $600 for the trip. $100 × 24 = $2,400 for the car. Both on time.',
       why=['', 'The trip would get nothing before it’s due.', 'The trip would only reach $500 by month four.']),
    tf('Giving each goal its own savings bucket makes progress easier to see.', True, 'Many banks let you split savings into named pots for exactly this.'),
    order('Set up a goal. Put the steps in order.',
          ['Name the goal', 'Price it', 'Pick a deadline', 'Divide to get the monthly amount', 'Automate the transfer'],
          'What, how much, when, how much a month, then put it on autopilot.'),
])

lessons = [why, L['sv-pay-yourself-first'], L['sv-emergency-fund'], dana, L['sv-where-to-park'], grow, goals, L['sv-automate'],
           L['sv-review'], L['sv-trial']]
write_unit('06-saving.json', 'saving', 6, old['title'], old['description'], old['wolfLine'], terms, lessons)
