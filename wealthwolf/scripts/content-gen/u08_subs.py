from lib import *

terms = {
    'subscription': term('Subscription', 'A service that charges you again and again, monthly or yearly, until you cancel.',
                         'A $15.99 streaming service billed on the 4th of every month.'),
    'auto-renewal': term('Auto-renewal', 'When a subscription renews and charges you automatically unless you cancel first.',
                         'Your yearly app plan charges $59.99 again on its anniversary.'),
    'free-trial': term('Free trial', 'A free taste of a paid service that usually turns into a paid subscription when it ends, unless you cancel.',
                       'Seven days free, then $14.99 a month on the card you entered.'),
    'utility': term('Utility', 'A basic home service you pay for as you use it, like electricity, water, gas or trash.',
                    'A water bill based on how many gallons you used.'),
    'autopay': term('Autopay', 'Letting a company take a bill out of your account automatically each month.',
                    'Your phone bill pulls itself from checking on the 14th.'),
    'promotional-rate': term('Promotional rate', 'A low starting price for new customers that jumps after a set time, often 12 months.',
                             'Internet at $40 a month for year one, then $70.'),
}

subs = lesson('sb-subscriptions', 'The Subscription Pile', 'Little monthly charges, big yearly totals.', [
    mc('Which of these is a subscription?', ['A streaming service that bills you every month', 'A pair of shoes', 'A bus ticket'], 0,
       'It charges again every month until you stop it.',
       context='A [[subscription]] charges you again and again, monthly or yearly, until you cancel.'),
    num('You pay for 4 streaming services: $12, $16, $9 and $15 a month. What’s the monthly total?', 52, '$12 + $16 + $9 + $15 = $52.'),
    num('What’s that over a year?', 624, '$52 × 12 = $624.'),
    tf('Small subscriptions are harmless because each one is cheap.', False, 'Five $10 subscriptions are $600 a year.'),
    mc('Your yearly app plan renews tomorrow and you never use it. What do you do?',
       ['Cancel it today', 'Let it renew', 'Delete the app'], 0, 'Cancel before the renewal date and you won’t be charged again.',
       context='Most subscriptions have [[auto-renewal]]: they renew and charge you automatically unless you cancel first.',
       why=['', 'That’s another year paid for something you don’t use.', 'Deleting the app doesn’t cancel the subscription. You’d keep paying.']),
    fill('A subscription keeps charging you until you ___.', ['cancel it', 'stop using it', 'delete the app'], 0, 'Only canceling stops the charges.'),
])

trial_lines = [
    ('groc', 'City Grocer', -61.30, {'date': 'Nov 2'}),
    ('stream', 'StreamMax', -15.99, {'date': 'Nov 4'}),
    ('fit', 'FitPro Premium, trial ended', -19.99, {'date': 'Nov 5'}),
    ('gas', 'Shell gas station', -33.00, {'date': 'Nov 6'}),
    ('phone', 'Ridgeline Mobile', -69.34, {'date': 'Nov 8'}),
]
TRIAL_DOC = doc('statement', 'Harbor Bank', trial_lines, subtitle='Checking · Nov 1–8', meta=[['Account', '•••• 4417']])
free = lesson('sb-free-trials', 'Free Trials', 'Free until it isn’t. Set the reminder.', [
    mc('Why do free trials ask for your card?', ['So they can start charging when the trial ends', 'To check your age', 'To send you a gift'], 0,
       'The card is how “free” becomes “paid.”',
       context='A [[free trial]] gives you a service free for a while, but you usually enter your card first. When it ends, it becomes a paid subscription.'),
    mc('Best habit when you start a free trial?', ['Set a reminder to cancel a day or two before it ends', 'Trust yourself to remember', 'Use a different email each time'], 0,
       'Reminders beat memory every time.'),
    num('You forget to cancel a trial for a $14.99-a-month app and notice 3 months later. How much did you pay?', 44.97, '$14.99 × 3 = $44.97.'),
    tf('Canceling a free trial early usually still lets you use it until the trial ends.', True,
       'Most services keep it running to the end date, so cancel right after signing up.'),
    spot('You only meant to try FitPro for free. Tap the charge to stop.', TRIAL_DOC, 'fit', 'The trial ended and turned into a paid plan.'),
    mc('A “free” gift box only asks you to pay $4.95 shipping. What should you check first?',
       ['Whether it signs you up for a monthly subscription', 'The color of the box', 'Nothing, it’s free'], 0,
       '“Just pay shipping” offers often hide a monthly plan in the small print.'),
])

audit_lines = [
    ('stream', 'StreamMax', -15.99, {'date': 'Nov 4'}),
    ('music', 'Spotlite Music', -10.99, {'date': 'Nov 6'}),
    ('cloud', 'CloudBox Storage', -2.99, {'date': 'Nov 9'}),
    ('gym', 'PowerGym membership', -39.99, {'date': 'Nov 12'}),
    ('news', 'NewsDaily app', -4.99, {'date': 'Nov 20'}),
]
sub_total = total(-l[2] for l in audit_lines)
assert sub_total == 74.95
AUDIT = doc('statement', 'Harbor Bank', audit_lines, subtitle='Repeating charges · November', meta=[['Account', '•••• 4417']])
audit = lesson('sb-audit', 'Subscription Audit', 'List every repeating charge. Keep what earns its place.', [
    info('Once a year, audit everything',
         'Pull up your last two months of statements and list every repeating charge. For each one, ask: did I use this in the last month? '
         'Would I sign up again today, at this price?'),
    spot('You haven’t been to the gym since spring. Tap the subscription to cancel first.', AUDIT, 'gym',
         'The biggest charge, for something you don’t use.'),
    num('Add up every subscription on this statement.', sub_total, '$15.99 + $10.99 + $2.99 + $39.99 + $4.99 = $74.95.', doc=AUDIT),
    num('How much does canceling the gym save over a year?', 479.88, '$39.99 × 12 = $479.88.'),
    sort('Keep or cancel?', ['Keep', 'Cancel'],
         [('Music app you use every day', 0), ('Gym you haven’t visited in 4 months', 1), ('A second streaming service you forgot about', 1),
          ('Cloud storage holding your photos', 0), ('News app you never open', 1)]),
    mc('Not sure whether you’ll miss it?', ['Cancel it. You can always sign up again', 'Keep paying just in case', 'Pay for a full year upfront'], 0,
       'If you miss it, rejoin. Most people never do.'),
], fmt='sort')

water_lines = [('base', 'Base charge', 18.00), ('water', 'Water used, 4,000 gallons', 24.00), ('sewer', 'Sewer service', 22.50), ('tax', 'Taxes and fees', 3.25)]
water_total = total(l[2] for l in water_lines)
assert water_total == 67.75
WATER = doc('bill', 'Clearwater Utilities', water_lines, subtitle='Water bill',
            meta=[['Account', '7720-3341'], ['Service period', 'Oct 1–31'], ['Due date', 'Nov 18']],
            totals=[('Total due', water_total, True)], note='Water is charged at $6.00 per 1,000 gallons.')
utilities = lesson('sb-utilities', 'Utility Bills', 'Read a water bill and see which part you control.', [
    mc('Which of these is a utility?', ['Water', 'Streaming', 'A gym'], 0, 'A basic home service you pay for as you use it.',
       context='A [[utility]] is a basic home service you pay for as you use it: electricity, water, gas, trash.'),
    num('What’s the total due on this bill?', water_total, '$18.00 + $24.00 + $22.50 + $3.25 = $67.75.', doc=WATER),
    num('How much of the bill depends on how much water you used?', 24, 'Just the “Water used” line: $24.00.', doc=WATER),
    num('Next month you use 6,000 gallons. At the same rate, what will the water line cost?', 36,
        '6 × $6.00 = $36.00.', doc=WATER, context='Use-based charges grow with use.'),
    tf('The base charge stays the same even if you use less water.', True, 'It’s a fixed cost. Only the use-based line moves.', doc=WATER),
    mc('A bill says “Estimated reading.” What does that mean?',
       ['They guessed your usage, and the next real reading will correct it', 'It’s a fake bill', 'You don’t have to pay it'], 0,
       'Pay it, but expect an adjustment next time.'),
], fmt='document')

autopay = lesson('sb-autopay', 'Autopay: Friend or Foe', 'Never miss a due date, without getting blindsided.', [
    mc('What’s the biggest upside of autopay?', ['You never miss a due date', 'Your bills get cheaper', 'You never need to look at them again'], 0,
       'No late fees from forgetting.',
       context='[[Autopay]] lets a company take the bill out of your account automatically every month.'),
    mc('What’s the biggest risk?', ['A bill pulls when your account is low and overdraws it', 'Your bill vanishes', 'You pay twice as much'], 0,
       'Autopay doesn’t check your balance first.'),
    tf('With autopay on, you can stop reading your bills.', False, 'A wrong charge on autopay just gets paid. Still read every bill.'),
    sort('Good fit for autopay?', ['Good fit', 'Watch closely'],
         [('Rent that’s the same every month', 0), ('A phone plan with a fixed price', 0), ('Electricity that swings with the seasons', 1),
          ('A bill you think has mistakes', 1), ('Car insurance', 0)]),
    mc('Payday is the 15th. Your phone autopay pulls on the 10th, when your account is lowest. What’s the fix?',
       ['Move the autopay date to after the 15th', 'Hope there’s enough', 'Turn off direct deposit'], 0,
       'Most companies let you choose the date. Line it up with payday.'),
    num('Your account has $310. Three autopays hit on the same day: $85 phone, $140 insurance, $95 internet. How much are you short?', 10,
        '$85 + $140 + $95 = $320. $320 − $310 = $10 short.'),
])

calendar = lesson('sb-bill-calendar', 'Your Bill Calendar', 'Line up due dates with paydays so no week is a surprise.', [
    info('Every bill, on one page',
         'Write down every bill, its amount and its due date, then sort them by date. Now you can see which paycheck pays what, and which week is tight.'),
    order('Put these bills in due-date order.', ['Rent, due the 1st', 'Internet, due the 7th', 'Phone, due the 14th', 'Car insurance, due the 22nd'],
          'Earliest first.'),
    num('Bills due between the 1st and the 14th: rent $1,100, internet $60, phone $45. How much has to come from your first paycheck?', 1205,
        '$1,100 + $60 + $45 = $1,205.'),
    num('Your first paycheck is $1,250. How much is left after those bills?', 45, '$1,250 − $1,205 = $45.'),
    mc('That leaves $45 for two weeks of food. What helps?', ['Ask to move a due date later in the month', 'Skip the internet bill', 'Pay rent late'], 0,
       'Moving the phone bill to the 20th puts it on the second paycheck.'),
    tf('Many companies will move your due date if you ask.', True, 'It’s usually a two-minute call or a setting in your account.'),
])

NOW = doc('bill', 'Your current plan', [('price', 'Monthly price, after promotion', 70.00)], subtitle='Lakeside Internet')
NEXT = doc('bill', 'New provider', [('price', 'Monthly price', 45.00), ('install', 'Installation, one time', 99.00)], subtitle='Fiberline')
assert 70 * 12 == 840 and 45 * 12 + 99 == 639
lower = lesson('sb-lower-bills', 'Lower Your Bills', 'Promotions end. Prices are negotiable.', [
    mc('Your internet was $40 a month for the first year and is now $70. What happened?', ['The promotional rate ended', 'You used more internet', 'It’s a late fee'], 0,
       'Introductory prices quietly expire.',
       context='A [[promotional rate]] is a low price for new customers that jumps after a set time, often 12 months.'),
    num('How much more is that per year?', 360, '($70 − $40) × 12 = $360.'),
    mc('What’s the best first move?', ['Call and ask for a better rate, mentioning other offers', 'Pay it and say nothing', 'Stop paying'], 0,
       'Companies often have a retention offer for customers who ask.'),
    mc('Over one year, which is cheaper?', ['Switching to Fiberline', 'Staying with Lakeside'], 0,
       'Lakeside: $70 × 12 = $840. Fiberline: $45 × 12 + $99 = $639.', docs=[NOW, NEXT]),
    num('How much does switching save in the first year?', 201, '$840 − $639 = $201.', docs=[NOW, NEXT]),
    tf('Phone, internet and insurance prices are often negotiable.', True, 'Ask once a year. The worst they can say is no.'),
], fmt='call')

yearly = lesson('sb-monthly-yearly', 'Monthly or Yearly?', 'Paying upfront saves money, if you’ll really use it.', [
    mc('$12 a month, or $99 for the year. Which is cheaper over a full year?', ['The yearly plan', 'The monthly plan'], 0,
       'Monthly: $12 × 12 = $144. Yearly: $99.',
       context='Many subscriptions are cheaper if you pay for a whole year at once.'),
    num('How much does the yearly plan save?', 45, '$144 − $99 = $45.'),
    mc('When is the yearly plan a bad idea?', ['When you’re not sure you’ll use it all year', 'When it’s cheaper', 'Never'], 0,
       'A discount on something you stop using isn’t a saving.'),
    num('You’d quit after 6 months. What would monthly cost you?', 72, '$12 × 6 = $72.'),
    mc('So for 6 months of use, which was cheaper?', ['Monthly, at $72', 'Yearly, at $99'], 0, '$72 beats $99 if you only use it half the year.'),
    tf('A yearly plan auto-renews too, so set a reminder before it does.', True, 'Otherwise next year’s $99 arrives on its own.'),
])

trial_steps = [
    num('Three subscriptions at $11, $15 and $8 a month. What do they cost in a year?', 408, '($11 + $15 + $8) × 12 = $408.'),
    tf('Deleting an app cancels its subscription.', False, 'You have to cancel the subscription itself.'),
    mc('Internet was $45 for a year and is now $75. What ended?', ['A promotional rate', 'A free trial', 'Autopay'], 0, 'The intro price expired.'),
    mc('What’s the main risk of autopay?', ['It can overdraw your account if the balance is low', 'It makes bills more expensive', 'It cancels your plan'], 0,
       'Line autopay dates up with payday.'),
]

lessons = [subs, free, audit, utilities, autopay, calendar, lower, yearly,
           review('sb'), trial('sb', 'Subscriptions & Bills', trial_steps)]
write_unit('08-subscriptions-bills.json', 'subscriptions-bills', 8, 'Subscriptions & Bills',
           'Tame the charges that come back every month.',
           'Every subscription is a little hand in your pocket. Count the hands.', terms, lessons)
