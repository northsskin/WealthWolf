from lib import *

terms = {
    'smart-goal': term('SMART goal', 'A goal that’s Specific, Measurable, Achievable, Relevant and Time-bound: exactly what, how much, and by when.',
                       'Save $1,500 for an emergency fund in 10 months.'),
    'time-horizon': term('Time horizon', 'How far away a goal is. Short-term is under a year, mid-term is 1 to 5 years, long-term is more than 5.',
                         'A car in 3 years has a mid-term time horizon.'),
    'present-bias': term('Present bias', 'The pull to choose a smaller reward now over a bigger one later.',
                         'Spending your trip savings on a sale today.'),
}

smart = lesson('gh-goals', 'Goals That Work', 'Turn “save more” into a number and a date.', [
    mc('Which is a SMART goal?', ['Save $3,000 for a car down payment by next December', 'Get better with money', 'Be rich'], 0,
       'What, how much, by when. The other two can’t be measured.',
       context='A [[SMART goal|smart-goal]] is Specific, Measurable, Achievable, Relevant and Time-bound. In plain words: exactly what, how much, and by when.'),
    sort('SMART or vague?', ['SMART', 'Vague'],
         [('Save $500 for a laptop by March', 0), ('Save more this year', 1), ('Build a $1,500 emergency fund in 10 months', 0),
          ('Stop wasting money', 1), ('Be better with spending', 1), ('Put $50 into savings every payday this year', 0)]),
    num('Goal: $1,500 in 10 months. How much a month?', 150, '$1,500 ÷ 10 = $150.'),
    tf('Writing a goal down and checking it every month makes you more likely to hit it.', True, 'What gets checked gets done.'),
    mc('Your $1,500 goal is at $600 after 6 months. Are you on track?', ['Behind: you should be at $900', 'On track', 'Ahead'], 0,
       '$150 × 6 = $900 planned. You’re $300 behind.'),
    num('To still finish on time in the last 4 months, how much a month do you need now?', 225, '($1,500 − $600) ÷ 4 = $225.'),
], fmt='sort')

horizons = lesson('gh-horizons', 'Short, Mid and Long Term', 'When you need the money changes where it should live.', [
    mc('Saving for a car in 3 years is…', ['Mid-term', 'Short-term', 'Long-term'], 0, 'Between 1 and 5 years away.',
       context='A goal’s [[time horizon]] is how far away it is. Short-term: under a year. Mid-term: 1 to 5 years. Long-term: more than 5 years.'),
    sort('Sort the goals by time horizon.', ['Short', 'Mid', 'Long'],
         [('A concert in 2 months', 0), ('Retirement', 2), ('A home deposit in 4 years', 1), ('A new phone this year', 0),
          ('A child’s college in 15 years', 2), ('A wedding in 2 years', 1)]),
    mc('Where should money for a short-term goal live?', ['Somewhere safe and easy to reach, like savings', 'Somewhere its value might drop', 'Under the mattress'], 0,
       'If you need it soon, it can’t be at risk.'),
    tf('Long-term goals can wait until you’re older.', False, 'Long goals need the most time. Starting early is the cheat code.'),
    num('A $3,600 goal in 3 years. How much a month?', 100, '3 years = 36 months. $3,600 ÷ 36 = $100.'),
    mc('Money is tight. Which goal do you fund first?', ['A small emergency fund', 'A luxury trip', 'A new TV'], 0,
       'Protection first, fun second.'),
], fmt='sort')

priorities = lesson('gh-priorities', 'What Comes First', 'Every goal wants your money. Put them in line.', [
    info('A common order',
         'Every goal wants your money. A common order: keep the lights on, build a small cushion, grow it to a real safety net, '
         'then work on bigger goals. You can work on several at once, but the order tells you what wins when money is short.'),
    order('Put these in the usual priority order.',
          ['Pay rent, food and bills', 'Build a $1,000 starter emergency fund', 'Grow it to 3 months of essential expenses', 'Save for bigger goals like a car or a trip'],
          'Survive, cushion, safety net, then goals.'),
    mc('You have $1,000 spare and no emergency fund yet. Best move?', ['Start the emergency fund', 'Book a trip', 'Buy new headphones'], 0,
       'The cushion protects every other goal.'),
    tf('You can work on more than one goal at a time by splitting each paycheck.', True, 'Splitting keeps every goal moving.'),
    num('You save $300 a month: 60% to the emergency fund, 40% to a trip. How much goes to the trip?', 120, '$300 × 0.40 = $120.'),
    mc('A goal stops mattering to you. What now?', ['Move its money to a goal that does matter', 'Keep saving for it anyway', 'Spend the money right away'], 0,
       'Goals change. Let the money follow.'),
])

habits = lesson('gh-habits', 'Small Habits, Big Numbers', 'Tiny daily amounts, huge yearly totals.', [
    num('$4 a day for a year. What’s the total?', 1460, '$4 × 365 = $1,460.', context='Tiny daily amounts become big yearly ones. Multiply by 365.'),
    num('$10 a week for 10 years, which is 520 weeks?', 5200, '$10 × 520 = $5,200.'),
    mc('Which habit is easiest to keep?', ['An automatic $20 transfer every payday', 'Remembering to save whatever is left', 'Saving only when you feel rich'], 0,
       'Automatic means it happens even on bad weeks.',
       context='Habits stick when they’re easy and automatic. Make the good choice the default.'),
    tf('Rounding every card purchase up to the next dollar and saving the change can add up.', True, 'Many banks will do it for you.'),
    num('Round-ups average $0.45 a purchase, and you make 60 purchases a month. How much do you save a month?', 27, '$0.45 × 60 = $27.'),
    mc('You missed your savings transfer one month. Best response?', ['Restart on the next payday', 'Give up', 'Stop saving for a year'], 0,
       'One miss is a blip. Quitting is the real cost.'),
])

traps = lesson('gh-brain-traps', 'Brain Traps', 'Why smart people still overspend.', [
    mc('Which is present bias?', ['Spending your trip savings on a sale today', 'Making a budget', 'Checking your balance'], 0,
       'Today’s deal beat next month’s trip.',
       context='[[Present bias]] is the pull to choose a reward now over a bigger one later.'),
    mc('Why is “it’s only $5” dangerous?', ['Lots of “only $5” adds up fast', '$5 is a lot', 'It isn’t'], 0,
       'Twenty “only $5” moments is $100.'),
    tf('Treating a tax refund as free money and spending it all is a common trap.', True,
       'A refund is your own money coming back. Give it a job like any other.'),
    mc('Your friends eat out a lot and you feel the pressure. Healthy move?', ['Suggest cheaper plans sometimes, or join less often', 'Go every time and stop saving', 'Stop seeing your friends'], 0,
       'Friends who matter will take a picnic.'),
    sort('Trap or smart move?', ['Trap', 'Smart move'],
         [('Buying it because everyone has one', 0), ('Waiting a day before a big buy', 1), ('Spending a bonus in a week', 0),
          ('Saving half of every raise', 1), ('“I deserve it” purchases every week', 0), ('Automating your savings', 1)]),
    mc('What’s the best defense against brain traps?', ['Rules decided in advance, like a budget and a waiting rule', 'Willpower in the moment', 'Never shopping again'], 0,
       'Decide when you’re calm, not when you’re in the store.'),
])

date = lesson('gh-money-date', 'Your Weekly Money Date', 'Ten minutes a week keeps the whole plan on track.', [
    info('Ten minutes, once a week',
         'Once a week, take ten minutes: check your balance and pending transactions, look at spending by category, move money if a category ran hot, '
         'and nudge your goals.'),
    order('Put the weekly check-in in order.',
          ['Check your balance and pending transactions', 'Look at this week’s spending', 'Move money between categories if needed', 'Check progress on your goals'],
          'Where you stand, what happened, fix it, look ahead.'),
    tf('A weekly check-in only matters when something went wrong.', False, 'It’s how you catch things before they go wrong.'),
    mc('When’s the best time for a money date?', ['The same time every week, like Sunday evening', 'Only when you feel like it', 'Once a year'], 0,
       'A fixed time turns it into a habit.'),
    mc('At your check-in you see $45 on snacks this week. The budget was $25. What do you do?',
       ['Move $20 from fun to food and plan better next week', 'Ignore it', 'Stop eating snacks forever'], 0, 'Patch it, then plan.'),
    num('Ten minutes a week for 52 weeks. About how many hours a year is that? Round to the nearest hour.', 9,
        '10 × 52 = 520 minutes. 520 ÷ 60 = 8.7, about 9 hours a year.', unit='hours'),
])

morgan_story = {
    'title': 'One year, three goals',
    'character': 'Morgan, 25, dental assistant',
    'body': 'Morgan takes home **$3,000** a month. Needs (rent, food, transport, phone) cost **$1,850**. Morgan wants three things this year:\n\n'
            'A **$1,200** starter emergency fund within 12 months. A **$900** trip in August, eight months away. A new laptop for **$720**, a year from now.\n\n'
            'Right now Morgan spends whatever isn’t needed, about **$1,150** a month on wants, and saves nothing.',
}
assert 900 / 8 == 112.5 and 112.5 + 60 + 100 == 272.5
morgan = lesson('gh-morgan', 'Morgan’s Plan', 'Three goals, one paycheck. Make it fit.', [
    num('How much a month for the trip, eight months away?', 112.50, '$900 ÷ 8 = $112.50.'),
    num('How much a month for the laptop, 12 months away?', 60, '$720 ÷ 12 = $60.'),
    num('And for the $1,200 emergency fund in 12 months?', 100, '$1,200 ÷ 12 = $100.'),
    num('What’s Morgan’s total monthly saving for all three goals?', 272.50, '$112.50 + $60 + $100 = $272.50.'),
    num('After needs and goals, how much is left for wants?', 877.50, '$3,000 − $1,850 − $272.50 = $877.50.'),
    alloc('Plan Morgan’s month. Needs are fixed, and goals need at least $300 (rounded up from $272.50 to leave some slack).',
          3000, 50, [{'label': 'Needs', 'fixed': 1850}, {'label': 'Goals', 'min': 300}, {'label': 'Wants'}],
          'Every plan works if needs are covered, goals get at least $300, and nothing is left without a job.'),
], fmt='story', story=morgan_story)

plan = lesson('gh-plan', 'Your First Money Plan', 'Everything from this section, on one page.', [
    info('Everything in one plan',
         'You’ve learned to track, budget, bank, save and spend smart. A money plan puts it on one page: what comes in, what goes out, '
         'what you’re building, and the habits that keep it running.'),
    order('Put your money plan in order.',
          ['Know your take-home pay', 'Cover needs and bills', 'Pay yourself first: savings and goals', 'Plan wants with what’s left', 'Check in weekly, review monthly'],
          'In, out, future you, fun, follow-up.'),
    mc('Which account setup supports the plan?', ['Checking for bills, a separate savings account, alerts on', 'One account for everything, no alerts', 'All cash at home'], 0,
       'Separate pots and early warnings.'),
    alloc('Plan a $2,800 take-home month. Rent and phone are fixed. Groceries need at least $300, transport at least $150, savings at least $300.',
          2800, 50, [{'label': 'Rent', 'fixed': 1100}, {'label': 'Phone', 'fixed': 50}, {'label': 'Groceries', 'min': 300},
                     {'label': 'Transport', 'min': 150}, {'label': 'Savings', 'min': 300}, {'label': 'Fun'}],
          'Needs covered, savings protected, every dollar given a job.',
          context='Put it all together: give every dollar of one month a job.'),
    tf('A money plan should change when your life changes.', True, 'New job, new city, new goal: new plan.'),
    mc('Which one habit holds the whole plan together?', ['Checking in regularly', 'Earning more', 'Never spending on fun'], 0,
       'A plan you look at is a plan that works.'),
], fmt='call')

trial_steps = [
    num('A $2,400 goal in 12 months. How much a month?', 200, '$2,400 ÷ 12 = $200.'),
    mc('A home deposit in 4 years has what time horizon?', ['Mid-term', 'Short-term', 'Long-term'], 0, 'Between 1 and 5 years.'),
    tf('Choosing a sale today over your planned trip is an example of present bias.', True, 'Now beat later.'),
    order('Put these in priority order.', ['Cover rent, food and bills', 'Starter emergency fund', 'Bigger goals'], 'Survive, cushion, then build.'),
]

lessons = [smart, horizons, priorities, habits, traps, date, morgan, plan,
           review('gh'), trial('gh', 'Goals & Habits', trial_steps)]
write_unit('10-goals-habits.json', 'goals-habits', 10, 'Goals & Money Habits',
           'Turn wishes into numbers, and numbers into habits.',
           'A goal without a number is just a wish.', terms, lessons)
