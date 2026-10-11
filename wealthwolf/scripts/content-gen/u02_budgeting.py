import json, os
from lib import *

path = os.path.join(DATA, SECTION, '02-budgeting.json')
old = json.load(open(path))
L = {l['id']: l for l in old['lessons']}

# "Track the Leaks" moves to the Tracking unit, with its two words.
moved = os.path.join(os.path.dirname(__file__), 'moved-bg-tracking.json')
if 'bg-tracking' in L:
    json.dump({'lesson': L['bg-tracking'], 'terms': {k: old['terms'][k] for k in ('tracking', 'budget-leak')}},
              open(moved, 'w'), indent=2, ensure_ascii=False)
terms = {k: v for k, v in old['terms'].items() if k not in ('tracking', 'budget-leak')}
terms['irregular-income'] = term('Irregular income', 'Pay that changes from month to month, like tips, gig work or commission.',
                                 'Earning $2,900 one month and $1,800 the next driving for delivery apps.')
terms['income-buffer'] = term('Income buffer', 'Money saved from good months to cover slow ones, so your bills still get paid when income dips.',
                              'Parking $1,500 from a strong month and drawing on it when a slow month comes in short.')

why = lesson('bg-why-budget', 'Why Budget?', 'A plan you make before the money shows up.', [
    info('Money with a plan',
         'A [[budget]] is a plan for your money. Before the month starts, you decide how much goes to rent, food, fun and saving.\n\n'
         'Without one, the month decides for you. Money goes wherever the day takes it, and you find out what happened once it’s gone.'),
    mc('When do you make a budget?', ['Before the money is spent', 'After the month ends', 'Only when you’re broke'], 0,
       'A budget is a plan, and plans come first.'),
    tf('A budget means you can never spend money on fun.', False,
       'A good budget includes fun on purpose. Then you can enjoy it without guilt.',
       context='A budget isn’t only about cutting back. It also tells you how much you **can** spend on fun without worrying.'),
    mc('Your pay before taxes is $3,200. $2,600 lands in your account. Which number should your budget start from?',
       ['$3,200', '$2,600', '$600'], 1, 'Budget the money you actually get: $2,600.',
       context='Every budget starts with one number: how much actually comes in. Use your [[take-home pay]], not your pay before taxes.'),
    num('You take home $2,600. You’ve planned $1,200 for rent, $350 for food and $150 for your phone and bus pass. How much is still unplanned?',
        900, '$2,600 − $1,200 − $350 − $150 = $900. That money still needs a job.',
        context='A budget is simple subtraction: money in, minus everything you’ve planned. Whatever is left still needs a plan.'),
    mc('Which is the best reason to budget?', ['To decide where your money goes before it goes', 'Because banks require it', 'To make your income bigger'], 0,
       'A budget doesn’t change what you earn. It changes how much of it you control.'),
    order('Put these first budget steps in order.',
          ['Find your take-home pay', 'List your must-pay bills', 'Plan food, transport and fun', 'Give what’s left to saving'],
          'Money in, must-pays, everyday costs, then the rest gets a job.'),
])

build = lesson('bg-50-30-20-build', 'Build a 50/30/20 Budget', 'Sort real costs into needs, wants and saving, then split a paycheck.', [
    sort('Sort Priya’s monthly costs.', ['Need', 'Want', 'Saving'],
         [('Rent', 0), ('Bus pass', 0), ('Groceries', 0), ('Streaming service', 1), ('Weekend brunch', 1),
          ('Emergency fund deposit', 2), ('Holiday savings', 2), ('Gym membership', 1)],
         context='Quick reminder: 50% needs, 30% wants, 20% saving.'),
    num('Priya takes home $3,400 a month. What’s her 50% needs budget?', 1700, '$3,400 × 0.50 = $1,700.'),
    num('And her 30% wants budget?', 1020, '$3,400 × 0.30 = $1,020.'),
    num('And the 20% for saving?', 680, '$3,400 × 0.20 = $680.'),
    num('Priya’s needs: rent $1,250, groceries $370, bus pass $85, phone $45. What do her needs cost in total?', 1750,
        '$1,250 + $370 + $85 + $45 = $1,750.', context='Now add up what her needs really cost and compare.'),
    mc('Her needs ($1,750) are $50 over the $1,700 needs budget. What’s the best fix?',
       ['Take the $50 from wants', 'Take the $50 from saving', 'Ignore it'], 0,
       'Wants drop to $970. Saving stays at $680.',
       why=['', 'Protect the 20%. Squeeze wants first.', 'Then the plan stops matching real life.']),
    alloc('Split Priya’s $3,400. Needs must cover at least $1,750, and saving gets at least $680. Type an amount or use the buttons.',
          3400, 10, [{'label': 'Needs', 'min': 1750}, {'label': 'Wants'}, {'label': 'Saving', 'min': 680}],
          'Needs covered, saving protected, and every dollar has a job.',
          context='Now give every dollar a job, the 50/30/20 way.'),
    tf('In 50/30/20, paying off money you owe faster than required counts toward the 20%.', True,
       'The 20% is for future you: saving, and paying down what you owe.'),
], fmt='sort')

pay_period = lesson('bg-pay-period', 'Budgeting by Paycheck', 'Paid every two weeks? Match each bill to the paycheck that pays it.', [
    info('Paydays and due dates',
         'Many jobs pay every two weeks, not once a month. Your money arrives in pieces, while your bills are due on their own dates.\n\n'
         'The trick is to plan **per paycheck**: decide which bills each paycheck pays, so the rent money is already there when rent is due.'),
    mc('Paid every two weeks, why do most months have two paychecks but a couple have three?',
       ['52 weeks ÷ 2 = 26 paychecks, and 26 doesn’t split evenly into 12 months', 'Employers pay extra in some months', 'It’s a payroll mistake'], 0,
       '26 paychecks across 12 months means two months get a third one.'),
    num('You get $1,200 every two weeks. How much is that in a year of 26 paychecks?', 31200, '$1,200 × 26 = $31,200.'),
    num('Spread over 12 months, what’s that per month on average?', 2600, '$31,200 ÷ 12 = $2,600.'),
    mc('A month brings a third paycheck. Smart move?',
       ['Give it a job, like savings or a goal', 'Spend it, it was unexpected', 'Ignore it and see where it goes'], 0,
       'Your budget runs on two paychecks. The third can jump-start a goal.',
       context='Plan each month on **two** paychecks. When a third arrives, it’s a bonus you can give a job.'),
    sort('Your paychecks land on the 1st and the 15th. Which paycheck should pay each bill?', ['1st paycheck', '15th paycheck'],
         [('Rent, due the 1st', 0), ('Internet, due the 5th', 0), ('Electricity, due the 12th', 0),
          ('Phone, due the 20th', 1), ('Car insurance, due the 25th', 1)],
         'Each bill comes out of the last paycheck before its due date.'),
    tf('A bill due on the 10th should come out of the paycheck you get on the 15th.', False,
       'The 15th is too late. Pay it from the paycheck that arrives before the due date.'),
])

sam_story = {
    'title': 'Feast or famine',
    'character': 'Sam, 26, delivery driver',
    'body': 'Sam drives for two delivery apps. Some months are great, some are slow. Over the last four months Sam earned '
            '**$2,900**, **$1,800**, **$2,400** and **$3,300**.\n\n'
            'In the good months Sam spent freely. In the slow month, rent was late and Sam paid a **$50** late fee.\n\n'
            'Sam’s must-pay costs (rent, phone, insurance, groceries) come to **$1,700** a month.',
}
assert (2900 + 1800 + 2400 + 3300) / 4 == 2600
sam = lesson('bg-irregular-income', 'Sam’s Uneven Paychecks', 'When income jumps around, budget for the slow months.', [
    num('What was Sam’s lowest month?', 1800, '$1,800, in the second month.'),
    num('What’s Sam’s average month? Add up the four months and divide by 4.', 2600,
        '($2,900 + $1,800 + $2,400 + $3,300) ÷ 4 = $10,400 ÷ 4 = $2,600.'),
    mc('Which number should Sam build the monthly budget on?', ['$3,300, the best month', '$2,600, the average', '$1,800, the lowest month'], 2,
       'Plan on $1,800. Anything above it is extra.',
       context='With [[irregular income]], plan each month around your **lowest** month, not your best one.',
       why=['A plan built on the best month breaks in a slow one.', 'Closer, but plenty of months come in under the average.', '']),
    num('Sam’s must-pays are $1,700. In the lowest month, how much is left after them?', 1800 - 1700,
        '$1,800 − $1,700 = $100. Tight, but covered.'),
    mc('In a $3,300 month, Sam plans on $1,800. What should happen to the other $1,500?',
       ['It goes into the buffer for slow months', 'Spend it, it’s a good month', 'Leave it in checking and see'], 0,
       'Good months fill the buffer. Slow months draw from it.',
       context='A good-month habit: park the extra in an [[income buffer]], then pay yourself a steady amount from it in slow months.'),
    tf('With an income buffer, Sam wouldn’t have paid that $50 late fee.', True,
       'The slow month could have borrowed from the good ones.'),
], fmt='story', story=sam_story)

breaks = lesson('bg-when-it-breaks', 'When the Budget Breaks', 'Overspent? Move money, don’t quit.', [
    mc('You’ve spent your whole $300 food budget by the 20th. What’s the best move?',
       ['Move $80 from your fun budget to food', 'Stop eating', 'Give up on budgeting this month', 'Borrow from next month’s budget'], 0,
       'Move money from a want to the need. The plan still balances.',
       context='Every budget breaks sometimes: a car repair, a birthday, a bad week. The fix isn’t to quit. It’s to move money from one category to another.',
       why=['', 'Food is a need. Cut wants, not meals.', 'One overspend doesn’t cancel the whole plan.', 'That starts next month already in a hole.']),
    num('Your fun budget was $200. You move $80 to food. How much fun money is left?', 120, '$200 − $80 = $120.'),
    mc('A friend’s wedding costs $250 you didn’t plan for. Which category should pay first?',
       ['Fun and eating out', 'Rent', 'Your emergency savings'], 0,
       'Take it from wants. Next year, a [[sinking fund]] for gifts and events means no scramble.',
       why=['', 'Rent can’t move. It’s a need with a due date.', 'A wedding you knew about isn’t an emergency.']),
    tf('If you overspend one month, you should cut next month’s saving to make up for it.', False,
       'Trim next month’s wants instead, and keep saving first.'),
    mc('Your gas budget is $120, but you spend about $160 every month. What’s the fix?',
       ['Raise gas to $160 and take $40 from somewhere else', 'Keep it at $120 and try harder', 'Stop tracking gas'], 0,
       'Budget what things actually cost, then balance it somewhere else.',
       context='When a category runs over every single month, it isn’t bad luck. The plan is wrong.'),
    order('You overspent. Put the fix in order.',
          ['Notice which category ran over', 'Move money in from a want', 'Work out why it happened', 'Adjust next month’s plan'],
          'Spot it, patch it, understand it, plan better.'),
    mc('Which mindset keeps a budget alive?', ['Progress, not perfection', 'One slip and it’s over', 'Only budget in good months'], 0,
       'Most months won’t be perfect. That’s normal.'),
], fmt='call')

lessons = [why, L['bg-50-30-20'], build, L['bg-zero-based'], pay_period, sam, L['bg-sinking-funds'], breaks,
           L['bg-review'], L['bg-trial']]
write_unit('02-budgeting.json', 'budgeting', 2, old['title'], old['description'], old['wolfLine'], terms, lessons)
