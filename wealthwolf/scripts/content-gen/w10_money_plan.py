from lib import *

S = 'building-wealth'

page = doc('statement', 'One page',
           [('cash', 'Emergency fund', 1000),
            ('month', 'Invested each month', 100),
            ('spend', 'Yearly spending sketch', 36000)],
           subtitle='The whole course, in three lines',
           note='The FI sketch on the spending line is 25 times $36,000, which is $900,000. It is a target, not a balance.')

overview = lesson('mp-map', 'The Whole Path', 'One page that already has names.', [
    info('You have the pieces',
         'Income comes in. A budget gives it jobs. An [[emergency fund]] sits in cash. High-interest debt gets a plan. Insurance covers the catastrophe. A [[three-fund portfolio|three-fund-portfolio]] takes the long money, usually starting with the [[employer match|employer-match]]. A [[will]] and the [[beneficiary]] forms cover the ending. This unit does not add a new trick. It puts the pieces in one place.'),
    mc('Which pile is cash on purpose?',
       ['The emergency fund', 'The stock index fund for age 65', 'A coin you cannot afford to lose'], 0,
       'Cash. The long fund is allowed to fall. The coin is not the plan.'),
    tf('The match is optional if you prefer to pick a single stock.', False,
       'The match is pay. A single stock is a bet you already learned to keep small.'),
    mc('What does the will not replace?',
       ['A beneficiary form that still names the wrong person', 'A guardian for a child', 'A list of what you own'], 0,
       'The form wins for that account. The will does not edit it.'),
    fill('The long investment in this course is a cheap, broad ___ portfolio.',
         ['three-fund', 'meme', 'gift-card'], 0,
         'Three-fund. Home stocks, the rest of the world, and bonds.'),
])

month = lesson('mp-month', 'Assign the Month', 'Needs, goals, then wants.', [
    info('Four thousand dollars',
         'This drill is a $4,000 month. Needs are at least $2,200. Goals, the emergency fund top-up and the investing transfer together, are at least $800. Wants get whatever is left, and at least $200. Assign every dollar.'),
    alloc('Assign all $4,000. Meet each floor.', 4000, 100,
          [{'label': 'Needs', 'min': 2200},
           {'label': 'Goals', 'min': 800},
           {'label': 'Wants', 'min': 200}],
          'The floors are $2,200, $800, and $200, which add to $3,200. The other $800 can sit in wants, so a simple fill ends at $1,000 of wants.'),
    num('Needs, goals, and wants: how many dollars are those three floors before the extra?', 3200,
        '$2,200 + $800 + $200 = $3,200.'),
    tf('Wants are allowed to take the rent money if the month looks dull.', False,
       'Needs have a floor. Wants get what is left after the floors, not before them.'),
    mc('What is inside the goals floor in this drill?',
       ['The cash top-up and the investing transfer', 'A guaranteed 12% product', 'A gift-card text'], 0,
       'Safety and the long transfer. Not a promise, and not a stranger’s text.'),
])

year = lesson('mp-year', 'The Yearly Look', 'A date you picked, not a red afternoon.', [
    info('Once, on purpose',
         'Pick a date. Read the balances, confirm the [[emergency fund]], rebalance if the mix drifted, and update [[beneficiary]] forms if the family changed. Then close the app. A [[recession]] headline is not an extra meeting.'),
    order('Put the yearly look in order.',
          ['Read the balances',
           'Confirm the emergency fund is still funded',
           'Rebalance only if the mix drifted from its target',
           'Update beneficiary forms if the family changed'],
          'See the money, protect the cash pile, fix the mix if it drifted, then the names on the forms.'),
    tf('The yearly look means selling because the screen is red.', False,
       'Red is not a new date. Rebalance if the mix drifted. Do not invent a new plan from one afternoon.'),
    mc('When do the beneficiary forms get a look even if the mix is fine?',
       ['After a birth, a death, a marriage, or a divorce', 'After a good week in the market', 'Never, because the will covers them'], 0,
       'Family changes. The will does not rewrite the forms.'),
    fill('Do this on a date you ___, then close it.',
         ['chose', 'fear', 'guess'], 0,
         'Chose. The date is the discipline.'),
])

baby = doc('statement', 'A new child',
           [('note', 'Guardian not yet named', 0)],
           subtitle='The will is out of date')
red = doc('statement', 'A red month',
          [('drop', 'Long fund, down this month', -1500)],
          subtitle='The goal is still decades away')

life = lesson('mp-life', 'When Life Changes', 'A person changes the papers. A red month does not.', [
    info('Two kinds of news',
         'A child, a marriage, a divorce, a death, or a job loss can change the plan. A red month in a fund you need at 65 does not. Job loss spends the [[emergency fund]]. It does not, by itself, rewrite a 30-year mix.'),
    mc('Which page means you update the will?',
       [baby['title'], red['title']], 0,
       docs=(baby, red),
       explain='A child needs a guardian. A $1,500 drop in a long fund is the reason you wrote the “do not sell on a red month” rule.'),
    num('How many dollars did the long fund fall on the red-month page? Enter the drop as a positive number.', 1500,
        doc=red,
        explain='The line is −$1,500, a drop of $1,500. The date you need the money did not move.'),
    tf('A 15-style red month is a reason to throw out the three-fund mix.', False,
       'The mix changes when the date changes. A down month is what the mix was built to survive.'),
    mc('You lose the job. What do you spend first?',
       ['The emergency fund', 'The retirement fund dated for age 65', 'A new margin loan'], 0,
       'Cash. The retirement date is still out there. Margin is still a skip.'),
], fmt='call')

plan = lesson('mp-page', 'The Page Itself', 'Three lines you can actually read.', [
    info('Small enough to reread',
         'This page is a finished sketch: $1,000 in the emergency fund, $100 a month invested, and $36,000 a year of spending. Twenty-five times that spending is a $900,000 [[FI number|fi-number]]. You may not have the $900,000. The page is how you remember what the $100 is for.'),
    num('How many dollars are in the emergency fund on this page?', 1000,
        doc=page,
        explain='The cash line is $1,000. It stays cash.'),
    num('How many dollars a year is the $100 monthly investment?', 1200,
        '12 × $100 = $1,200.'),
    num('What is 25 times the $36,000 spending sketch?', 900000,
        '25 × $36,000 = $900,000. A target. Not a balance the market owes you.'),
    tf('The $900,000 is money this page says you already have.', False,
       'It is 25 times spending. The page’s actual investing line is $100 a month.'),
], fmt='document')

mixed = lesson('mp-mix', 'A Last Pass', 'The ideas, side by side.', [
    info('Nothing new',
         'These questions use the course you already have. [[Inflation]] shrinks a basket. The [[4% rule|four-percent-rule]] is a first-year sketch. [[Medicare]] is at 65. A [[fiduciary]] must put you first. None of these is a product to buy today.'),
    num('A $100 basket rises 3%. How many dollars does it cost now?', 103,
        '$100 × 1.03 = $103.'),
    num('What is 4% of $500,000, the year-one sketch?', 20000,
        '$500,000 × 0.04 = $20,000.'),
    tf('Medicare waits until full retirement age of 67.', False,
       'Medicare’s window is around 65. Full retirement age for people born in 1960 or later is 67.'),
    mc('Which promise do you refuse?',
       ['A stated fee you can turn into dollars', 'A guaranteed market return', 'An offer to look the person up before you hire them'], 1,
       'The guarantee. A fee and a lookup are ordinary questions.'),
])

keep = lesson('mp-keep', 'Stay Editable', 'The page changes when your life does.', [
    info('Not a tattoo',
         'The page is right until it is not. A new city, a child, a paid-off debt, or a parent you are caring for can change the spending number, and the spending number changes the target. A noisy week does not. Edit on the yearly date, and edit when the family changes. Then leave it.'),
    mc('Which event edits the spending number?',
       ['You take in a parent and the grocery bill jumps', 'The fund is down 2% today', 'A friend bought a coin'], 0,
       'A real new bill. Two percent today is noise.'),
    tf('Once the page is written, editing it means you failed.', False,
       'Editing for a real life change is the plan. Editing for a headline is the failure.'),
    num('Spending rises from $36,000 to $42,000. How many dollars did the yearly sketch increase?', 6000,
        '$42,000 − $36,000 = $6,000. The FI sketch moves with it: 25 times the new number, not the old one.'),
    num('What is 25 times the new $42,000 spending?', 1050000,
        '25 × $42,000 = $1,050,000. The target moved because the life moved.'),
])

alpha = lesson('mp-alpha', 'You’re the Alpha Now', 'The rank at the end of the path.', [
    info('The last lesson',
         'You started with what income is. You can now read a paycheck, a bill, a fund fee, a beneficiary form, and a retirement sketch. The rank near the end of this course is Alpha. It is not a stock tip and it is not permission to bet the emergency fund.\n\nThe plan on the page is enough to continue: cash for a surprise, a cheap broad mix for the long money, papers a person you love can find, and a date to look again.',
         ),
    mc('Which rank is the one near the end of this course?',
       ['Pup', 'Alpha', 'A guaranteed 12%'], 1,
       'Alpha. Pup was the start. A guaranteed return was never a rank.'),
    tf('Alpha means you should empty the emergency fund into one exciting stock.', False,
       'The cash pile stays. Alpha is the person who can leave it there.'),
    mc('What do you do on the date you chose?',
       ['Read the page, fix what life changed, and close it', 'Rebuild the plan from a headline', 'Send gift cards to a text'], 0,
       'Read, edit for a real change, close it. That is the whole habit.'),
    order('Put the ongoing plan in order.',
          ['Keep the emergency fund in cash',
           'Keep the automatic investment in the broad mix',
           'Keep the will and the beneficiary forms findable',
           'Look again on the date you chose'],
          'Cash, the mix, the papers, the date. Then go live your life.'),
], fmt='story', story={
    'title': 'You’re the Alpha now',
    'character': 'You, at the end of the path',
    'body': 'The rank near the end of this course is **Alpha**.\n\nCash for a surprise. A cheap broad mix for the long money. Papers someone can find. A date to look again. That is the plan.',
})

write_unit('10-money-plan.json', 'money-plan', 10, 'Your Money Plan',
           'The whole course on one page, and a date to read it.',
           'You have the pieces. The page is how you keep them.',
           {}, [overview, month, year, life, plan, mixed, keep, alpha, review('mp'), trial('mp', 'Your Money Plan', [
               num('25 times $24,000 of yearly spending is what FI sketch, in dollars?', 600000,
                   '25 × $24,000 = $600,000.'),
               tf('A red month in a long-term fund means you rewrite the will.', False,
                  'A new person in the family changes the will. A red month is not that event.'),
               mc('On the yearly look, selling because the screen is red is what?',
                  ['The point of the meeting', 'Not the point. You rebalance only if the mix drifted', 'Required by the Fed'], 1,
                  'Read, confirm the cash, rebalance if the target drifted, update forms if the family changed.'),
               num('$150 a month is how many dollars a year?', 1800,
                   '12 × $150 = $1,800.'),
           ])],
           section=S)
