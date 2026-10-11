import json, os
from lib import *

moved = json.load(open(os.path.join(os.path.dirname(__file__), 'moved-bg-tracking.json')))
terms = dict(moved['terms'])
terms.update({
    'spending-category': term('Spending category', 'A bucket you group purchases into, like housing, food, transport or fun, so you can see totals.',
                              'Groceries, lunch at work and coffee all go in “Food.”'),
    'transaction': term('Transaction', 'One movement of money: a purchase, a payment or a deposit, with a date and an amount.',
                        'Oct 2, City Grocer, $54.20.'),
    'envelope-method': term('Envelope method', 'Budgeting with cash: each category gets its own envelope, and when it’s empty, that category is done for the month.',
                            'Put $200 in a “Food” envelope. Spend it, and food is done until next month.'),
    'emotional-spending': term('Emotional spending', 'Buying things to change how you feel (bored, stressed, sad or celebrating) rather than because you planned to.',
                               'Ordering clothes at midnight after a terrible day.'),
})

categories = lesson('tr-categories', 'Spending Categories', 'Put every purchase in a bucket so you can see the pattern.', [
    mc('Which category does a bus ticket belong in?', ['Transport', 'Food', 'Housing'], 0, 'Getting around is transport.',
       context='To see where money goes, group each purchase into a [[spending category]]: housing, food, transport, fun and so on.'),
    sort('Sort last week’s spending into categories.', ['Food', 'Transport', 'Fun'],
         [('Groceries', 0), ('Gas', 1), ('Movie tickets', 2), ('Lunch at work', 0), ('Bus pass', 1), ('Video game', 2), ('Coffee', 0)]),
    mc('Which set of categories is easiest to stick with?',
       ['Housing, food, transport, fun, saving, other', 'A separate category for every store', 'No categories at all'], 0,
       'Five to eight categories is plenty. Too many and you’ll stop tracking.'),
    num('Food this week: groceries $64, lunch $12, coffee $9, more groceries $38. What’s the food total?', 123,
        '$64 + $12 + $9 + $38 = $123.', context='What matters is the total in each bucket. Add up everything in one category.'),
    num('If every week looks like that, about how much goes on food in a month? Use 4 weeks.', 492, '$123 × 4 = $492.'),
    tf('A coffee bought on the way to work belongs in the transport category.', False,
       'It’s food. Where you bought it doesn’t change what it is.'),
    mc('What’s the point of categories?', ['To see which kind of spending is biggest', 'To keep your bank happy', 'To spend more in each one'], 0,
       'Totals by category show you where to look first.'),
], fmt='sort')

log_lines = [
    ('rent', 'Rent, Oak Street Apartments', -1150.00, {'date': 'Oct 1'}),
    ('groc1', 'City Grocer', -54.20, {'date': 'Oct 2'}),
    ('gas', 'Shell gas station', -38.00, {'date': 'Oct 2'}),
    ('lunch', 'Taco Spot', -11.75, {'date': 'Oct 3'}),
    ('stream', 'StreamMax', -15.99, {'date': 'Oct 4'}),
    ('groc2', 'City Grocer', -27.40, {'date': 'Oct 5'}),
    ('movie', 'Cinema 8', -24.00, {'date': 'Oct 6'}),
    ('coffee', 'Bean There Café', -6.25, {'date': 'Oct 7'}),
]
log_total = total(l[2] for l in log_lines)
assert log_total == -1327.59
LOG = doc('statement', 'Your spending', log_lines, subtitle='Budgeting app · Oct 1–7', totals=[('Total spent', log_total, True)])
food = total([54.20, 11.75, 27.40, 6.25])
assert food == 99.60
spending_log = lesson('tr-spending-log', 'Read Your Spending Log', 'One week of real transactions. Find the pattern.', [
    mc('How many transactions happened on Oct 2?', ['One', 'Two', 'Three'], 1, 'City Grocer and the gas station.',
       context='Every purchase is a [[transaction]]: one line with a date, a name and an amount.', doc=LOG),
    num('How much went on groceries this week?', 81.60, '$54.20 + $27.40 = $81.60.', doc=LOG),
    num('Not counting rent, how much was spent this week?', 177.59, '$1,327.59 − $1,150.00 = $177.59.', doc=LOG),
    mc('After rent, which category was biggest this week?', ['Food', 'Transport', 'Fun'], 0,
       'Food: $54.20 + $11.75 + $27.40 + $6.25 = $99.60. Transport was $38.00, fun $39.99.', doc=LOG),
    num('How much did fun cost: the streaming service and the movie?', 39.99, '$15.99 + $24.00 = $39.99.', doc=LOG),
    tf('One week of transactions is enough to plan a whole year.', False,
       'One week is a snapshot. Track a full month to see the real pattern.'),
], fmt='document')

methods = lesson('tr-methods', 'Ways to Track', 'App, spreadsheet, envelopes or a notebook: pick the one you’ll keep.', [
    info('Pick a method you’ll keep',
         'There’s no single right way to track. What matters is doing it every week.\n\n'
         '**Bank app:** already lists every card payment. **Budgeting app:** sorts transactions into categories for you. '
         '**Spreadsheet:** you type them in and see totals. **Notebook:** old school, and it works.'),
    mc('Your fun envelope is empty on the 22nd. What does the envelope method say?',
       ['No more fun spending until next month', 'Take money from the rent envelope', 'Use a card instead'], 0,
       'An empty envelope means that category is done. That’s the whole point.',
       context='The [[envelope method]] is an old trick: cash for each category goes in its own envelope. When an envelope is empty, that category is done for the month.'),
    tf('Cash purchases still need tracking, even though they don’t show up in your bank app.', True,
       'Cash leaves no trail unless you write it down.'),
    mc('How often should you check your spending?', ['About once a week', 'Once a year', 'Only when your account is empty'], 0,
       'Weekly is often enough to catch problems, and rare enough to stick with.'),
    match('Match each method to what it’s best at.', [
        ('Bank app', 'Already lists every card payment'),
        ('Envelopes', 'Makes overspending physically impossible'),
        ('Spreadsheet', 'Totals and charts you control'),
        ('Notebook', 'Works with zero tech'),
    ]),
    mc('Which tracking method is best?', ['The one you’ll actually keep using', 'The most expensive app', 'Whatever your friends use'], 0,
       'A simple method you use beats a perfect one you abandon.'),
])

cats = [('Housing (planned $1,150)', 1150, 1150), ('Groceries (planned $320)', 310, 320), ('Transport (planned $150)', 140, 150),
        ('Eating out (planned $120)', 260, 120), ('Fun (planned $100)', 95, 100)]
ids = ['housing', 'groceries', 'transport', 'eatout', 'fun']
OCT = doc('statement', 'October by category', [(i, label, -spent) for i, (label, spent, _) in zip(ids, cats)],
          subtitle='Budgeting app · Spent vs. planned', totals=[('Total spent', -sum(c[1] for c in cats), True)])
assert sum(c[1] for c in cats) == 1955 and sum(c[2] for c in cats) == 1840
over = lesson('tr-over-budget', 'Where It Went Over', 'Compare the month with the plan and find what broke it.', [
    spot('Tap the category that went way over its plan.', OCT, 'eatout', 'Eating out: $260 spent against $120 planned.',
         context='Tracking pays off when you compare it with your plan. Each line shows what you planned, and the amount is what you actually spent.'),
    num('By how much did eating out go over?', 140, '$260 − $120 = $140.', doc=OCT),
    num('The plan for all five categories added up to $1,840. How far over was the whole month?', 115,
        '$1,955 − $1,840 = $115.', doc=OCT),
    mc('What’s the most useful next step?',
       ['Find out why eating out ran over, then set a realistic limit', 'Delete the budget', 'Spend less on groceries to make up for it'], 0,
       'The budget just showed you something useful. Use it.',
       why=['', 'The budget did its job: it showed you the leak.', 'Groceries were already under plan, and they’re a need.']),
    tf('The money left over in groceries, transport and fun can cover part of the overspend.', True,
       '$10 + $10 + $5 = $25 under plan. Moving it helps, but it doesn’t cover $140.'),
], fmt='spot')

riley_story = {
    'title': 'The receipt shoebox',
    'character': 'Riley, 24, junior designer',
    'body': 'Riley kept every receipt in a shoebox for a month, then added them up on a Sunday night.\n\n'
            'The big ones were no surprise: **$1,050** rent and **$340** groceries. The surprise was everything else: '
            '**22** coffees at **$5** each, **9** takeout dinners at about **$18**, and **$64** of apps and games Riley barely remembered buying.\n\n'
            'Riley takes home **$2,500** a month and had been wondering why there was never anything left.',
}
riley = lesson('tr-riley', 'Riley’s Receipts', 'A month of receipts tells a story. Add it up.', [
    num('How much did the coffees cost?', 110, '22 × $5 = $110.'),
    num('And the takeout dinners?', 162, '9 × $18 = $162.'),
    num('Add up coffee, takeout and the apps.', 336, '$110 + $162 + $64 = $336.'),
    num('Now add rent and groceries. What was the shoebox total for the month?', 1726, '$1,050 + $340 + $336 = $1,726.'),
    mc('Riley takes home $2,500 but the receipts only add to $1,726. What’s the most likely reason nothing is left?',
       ['Some spending never made it into the shoebox', 'The bank lost the money', 'Riley’s rent is too low'], 0,
       '$774 is missing. Card taps, bills that pay themselves and cash rarely all come with receipts. That’s why tracking in a bank app helps.'),
    mc('Riley wants to free up $150 a month. Which plan does it?',
       ['Cut takeout to 2 dinners and coffee to 10 cups', 'Skip rent once', 'Stop buying groceries'], 0,
       '7 fewer dinners × $18 = $126, plus 12 fewer coffees × $5 = $60. That’s $186 a month.'),
], fmt='story', story=riley_story)

patterns = lesson('tr-patterns', 'Spotting Patterns', 'Payday splurges, weekend leaks, bad-day buys.', [
    mc('Most of your spending happens in the three days after payday. What’s that?',
       ['A payday splurge', 'A budget', 'A deduction'], 0, 'Money feels endless right after payday. It isn’t.',
       context='Look past single purchases to patterns: when, where and why you spend.'),
    mc('Which is most likely emotional spending?',
       ['Ordering $60 of clothes at midnight after a terrible day', 'Buying groceries for the week', 'Paying your phone bill'], 0,
       'A bad day, a late hour, an unplanned buy: classic emotional spending.',
       context='[[Emotional spending]] means buying to change how you feel: bored, stressed, sad, or celebrating.'),
    tf('Noticing what triggers your spending makes it easier to change.', True,
       'Once you know the trigger, you can plan around it.'),
    num('You spend about $45 every Saturday on things you didn’t plan. What’s that over a year of 52 Saturdays?', 2340,
        '$45 × 52 = $2,340.'),
    mc('What’s a good fix for a payday splurge?',
       ['Move savings out on payday, before you can spend it', 'Get paid less often', 'Delete your bank app'], 0,
       'If it’s gone before the splurge starts, there’s less to splurge.'),
    sort('Planned or emotional? Sort them.', ['Planned', 'Emotional'],
         [('Weekly grocery shop', 0), ('Late-night shopping after a fight', 1), ('Birthday gift you budgeted for', 0),
          ('Retail therapy after a bad exam', 1), ('Monthly bus pass', 0), ('Buying something because you were bored', 1)]),
])

check_in = lesson('tr-monthly-review', 'The Monthly Check-In', 'Fifteen minutes that steer next month.', [
    info('Fifteen minutes, once a month',
         'At the end of each month, sit down with your tracking and your budget. Compare, adjust, and set up next month. Fifteen minutes is enough.'),
    order('Put the monthly check-in in order.',
          ['Add up spending by category', 'Compare each category with the plan', 'Work out why anything ran over', 'Set next month’s budget'],
          'Total, compare, understand, plan.'),
    mc('You came in $60 under budget this month. What’s a good use of it?',
       ['Give it a job, like savings or a goal', 'Let it sit and quietly disappear', 'Spend it fast before it’s gone'], 0,
       'Money without a job wanders off. Give it one.'),
    tf('If a category is under budget three months in a row, you can shrink it and move the money somewhere useful.', True,
       'Your plan should match real life. Free that money up.'),
    num('Eating out was $310 in September and $240 in October. How much less did you spend?', 70, '$310 − $240 = $70.',
        context='Compare months to see whether you’re improving.'),
    num('If you keep October’s level, how much do you save over 12 months compared with September’s?', 840, '$70 × 12 = $840.'),
    mc('What’s the real goal of tracking?', ['Making better choices next month', 'Feeling guilty about last month', 'Having the most detailed spreadsheet'], 0,
       'Tracking looks back so you can plan forward.'),
])

trial_steps = [
    num('Your food spending for four weeks was $88, $102, $95 and $115. What’s the total for the month?', 400, '$88 + $102 + $95 + $115 = $400.'),
    mc('Which habit catches spending problems early?', ['Checking your spending every week', 'Checking once a year', 'Never looking'], 0,
       'Weekly checks catch a leak before it becomes a flood.'),
    tf('The envelope method works by limiting each category to the cash in its envelope.', True, 'Empty envelope, category done.'),
    mc('Your transport plan was $150 and you spent $190. What’s the honest next move?',
       ['Find out why, then adjust the plan', 'Pretend it didn’t happen', 'Stop tracking transport'], 0,
       'Either the plan was too low or something changed. Find out which.'),
]

lessons = [moved['lesson'], categories, spending_log, methods, over, riley, patterns, check_in,
           review('tr'), trial('tr', 'Tracking', trial_steps)]
write_unit('03-tracking.json', 'tracking', 3, 'Tracking Your Spending',
           'Find out where your money really goes, not where you think it goes.',
           'You can’t fix what you won’t look at.', terms, lessons)
