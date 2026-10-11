from lib import *

terms = {
    'bank-statement': term('Bank statement', 'The monthly record of your account: the starting balance, every transaction, and the ending balance.',
                           'September’s statement: opened at $640.00, closed at $1,609.12.'),
    'maintenance-fee': term('Maintenance fee', 'A monthly charge just for having the account, often waived if you meet a condition like a minimum balance.',
                            '$12 a month unless you keep $1,500 in the account.'),
    'overdraft': term('Overdraft', 'Spending more than you have in your account, when the bank lets the payment go through anyway.',
                      'Buying a $26 lunch with $20 in the account.'),
    'overdraft-fee': term('Overdraft fee', 'What a bank charges each time a payment overdraws your account, often about $35.',
                          'A $6 overdraft plus a $35 fee: that lunch really cost $41 more than you had.'),
    'overdraft-protection': term('Overdraft protection', 'A setting that covers a shortfall by moving money from your savings, instead of charging an overdraft fee.',
                                 'You’re $6 short, so $6 moves over from savings automatically.'),
    'dispute': term('Dispute', 'Asking your bank to investigate a charge you think is wrong and reverse it.',
                    'Reporting a $64 charge from a store you’ve never shopped at.'),
    'reconcile': term('Reconcile', 'Checking your own record of spending against the bank’s, line by line, until they match.',
                      'Your notes say $450 left, the bank says $415. Reconciling finds the missing $35.'),
}

# ---- September statement ----------------------------------------------------------
sep_lines = [
    ('pay1', 'Direct deposit, Northside Coffee', 1079.40, {'date': 'Sep 5'}),
    ('rent', 'Rent, Oak Street Apartments', -950.00, {'date': 'Sep 6'}),
    ('groc', 'City Grocer', -82.35, {'date': 'Sep 9'}),
    ('phone', 'Ridgeline Mobile', -69.34, {'date': 'Sep 14'}),
    ('pay2', 'Direct deposit, Northside Coffee', 1079.40, {'date': 'Sep 19'}),
    ('atm', 'ATM withdrawal', -60.00, {'date': 'Sep 21'}),
    ('stream', 'StreamMax', -15.99, {'date': 'Sep 24'}),
    ('fee', 'Monthly maintenance fee', -12.00, {'date': 'Sep 30'}),
]
sep_in = total(l[2] for l in sep_lines if l[2] > 0)
sep_out = total(-l[2] for l in sep_lines if l[2] < 0)
sep_close = total([640.00, sep_in, -sep_out])
assert sep_in == 2158.80 and sep_out == 1189.68 and sep_close == 1609.12
SEP = doc('statement', 'Harbor Bank', sep_lines, subtitle='Checking statement · Sep 1–30',
          meta=[['Account', '•••• 4417']], totals=[('Opening balance', 640.00), ('Closing balance', sep_close, True)])

statement = lesson('bf-statement', 'Reading a Bank Statement', 'What came in, what went out, and what was left.', [
    mc('What was the balance at the start of September?', ['$640.00', '$1,609.12', '$1,079.40'], 0,
       'The opening balance, at the bottom of the statement.',
       context='A [[bank statement]] is the monthly record of your account: what you started with, every transaction, and what you ended with.', doc=SEP),
    num('How much money came in this month?', sep_in, 'Two paychecks: $1,079.40 + $1,079.40 = $2,158.80.', doc=SEP),
    num('How much went out?', sep_out, '$950.00 + $82.35 + $69.34 + $60.00 + $15.99 + $12.00 = $1,189.68.', doc=SEP),
    mc('Which line is a fee the bank charged you?', ['Sep 30, Monthly maintenance fee', 'Sep 21, ATM withdrawal', 'Sep 6, Rent'], 0,
       'The ATM withdrawal was your own cash. The $12 is the bank’s fee.', doc=SEP),
    num('Check the math: $640.00 + money in − money out. What should the closing balance be?', sep_close,
        '$640.00 + $2,158.80 − $1,189.68 = $1,609.12. It matches.',
        context='Every statement balances: opening + money in − money out = closing.', doc=SEP),
    tf('It’s worth reading your statement every month, even if you check your app.', True, 'Fees and mistakes hide in plain sight.'),
], fmt='document')

fees = lesson('bf-fees', 'The Fee List', 'Small charges that add up to real money.', [
    mc('Your bank charges $12 a month unless you keep $1,500 in the account. You keep about $900. Do you pay?',
       ['Yes, $12 every month', 'No', 'Only once a year'], 0, '$900 is under the $1,500 needed to skip the fee.',
       context='A [[maintenance fee]] is what a bank charges each month just for having the account. Many banks waive it if you meet a condition.'),
    num('What does that fee cost you over a year?', 144, '$12 × 12 = $144.'),
    mc('What’s the cheapest fix?', ['Switch to a no-fee account', 'Keep paying $144 a year', 'Close every account and use only cash'], 0,
       'Plenty of insured accounts charge nothing.',
       why=['', 'That’s $144 a year for nothing.', 'You’d lose insurance, direct deposit and your debit card.']),
    sort('Fee or free? Sort these.', ['Often a fee', 'Usually free'],
         [('Using another bank’s ATM', 0), ('Depositing your paycheck', 1), ('Maintenance, below the minimum balance', 0),
          ('Checking your balance in the app', 1), ('Paper statements by mail', 0), ('Debit card purchases', 1)]),
    num('This year you paid $144 in maintenance fees, $78 in ATM fees and $24 for paper statements. What’s the total?', 246,
        '$144 + $78 + $24 = $246.', context='Fees add up like any other cost.'),
    mc('Many banks drop the maintenance fee if you…', ['set up direct deposit', 'visit the branch every week', 'ask for paper statements'], 0,
       'Direct deposit is the most common way to get the fee waived.'),
])

overdraft = lesson('bf-overdraft', 'Overdrafts', 'How a $6 shortfall becomes a $41 coffee.', [
    mc('Your account has $20. You buy a $26 lunch and the bank lets it through. What happened?',
       ['You overdrew the account', 'You earned interest', 'You made a deposit'], 0, 'You spent $6 more than you had.',
       context='An [[overdraft]] happens when you spend more than is in your account. Some banks let the payment through anyway, then charge an [[overdraft fee]].'),
    num('You overdraw by $6 and the bank charges a $35 fee. How much did that $6 really cost you?', 41, '$6 + $35 = $41.',
        context='Overdraft fees are often around $35, no matter how small the overdraft is.'),
    num('Three small purchases each overdraw your account on the same day, at $35 each. Total fees?', 105, '3 × $35 = $105.'),
    mc('Which costs less for a $6 shortfall?', ['A free or cheap transfer from savings', 'A $35 overdraft fee'], 0,
       'Moving your own $6 beats paying $35 for the privilege.',
       context='[[Overdraft protection]] links your savings to checking, so a shortfall is covered by a transfer instead of a fee.'),
    tf('You can usually ask your bank to decline card payments instead of overdrafting.', True,
       'Opting out means a declined card instead of a $35 fee.'),
    mc('What’s the best way to avoid overdrafts?', ['Low-balance alerts, and checking your available balance', 'Hoping for the best', 'Spending only on weekends'], 0,
       'An alert at $50 gives you time to act.'),
])

# ---- Spot the fee -------------------------------------------------------------------------
oct_lines = [
    ('groc', 'City Grocer', -46.10, {'date': 'Oct 2'}),
    ('gas', 'Shell gas station', -31.00, {'date': 'Oct 3'}),
    ('atm', 'ATM withdrawal, Corner Mart', -40.00, {'date': 'Oct 4'}),
    ('atmfee', 'Out-of-network ATM fee', -3.50, {'date': 'Oct 4'}),
    ('stream', 'StreamMax', -15.99, {'date': 'Oct 7'}),
    ('lunch', 'Taco Spot', -12.40, {'date': 'Oct 9'}),
]
OCT = doc('statement', 'Harbor Bank', oct_lines, subtitle='Checking · Oct 1–10', meta=[['Account', '•••• 4417']])
od_lines = [
    ('rent', 'Rent, Oak Street Apartments', -950.00, {'date': 'Oct 12'}),
    ('coffee', 'Bean There Café', -5.75, {'date': 'Oct 14'}),
    ('odfee', 'Overdraft fee', -35.00, {'date': 'Oct 14'}),
    ('groc', 'City Grocer', -38.20, {'date': 'Oct 15'}),
    ('pay', 'Direct deposit, Northside Coffee', 1079.40, {'date': 'Oct 17'}),
]
OD = doc('statement', 'Harbor Bank', od_lines, subtitle='Checking · Oct 11–17', meta=[['Account', '•••• 4417']])
paper_lines = [
    ('maint', 'Monthly maintenance fee, waived', 0.00, {'date': 'Oct 31'}),
    ('paper', 'Paper statement fee', -2.00, {'date': 'Oct 31'}),
    ('interest', 'Interest earned', 0.04, {'date': 'Oct 31'}),
]
PAPER = doc('statement', 'Harbor Bank', paper_lines, subtitle='Account charges · Oct 31', meta=[['Account', '•••• 4417']])
spot_fee = lesson('bf-spot-fee', 'Spot the Fee', 'Three statements. Find the charge you could have dodged.', [
    spot('Tap the fee.', OCT, 'atmfee', '$3.50 just to reach your own money. Your own bank’s ATMs are usually free.',
         context='Fees don’t announce themselves. They sit quietly between normal purchases.'),
    tf('A $3.50 ATM fee on a $40 withdrawal is almost 9% of the cash.', True, '$3.50 ÷ $40 = 0.0875. Nearly 9%.'),
    spot('Which charge could you have avoided by opting out of overdraft?', OD, 'odfee',
         'Opted out, the coffee would have been declined. Annoying, but free.'),
    num('How much did that $5.75 coffee really cost?', 40.75, '$5.75 + $35.00 = $40.75.', doc=OD),
    mc('What would have prevented it?', ['A low-balance alert, or opting out of overdraft', 'Paying for coffee with a card next time', 'Buying a bigger coffee'], 0,
       'Either one turns a $40 coffee back into a $6 one.'),
    spot('You already get statements in the app. Which charge can you switch off?', PAPER, 'paper',
         'Go paperless and the $2 a month disappears: $24 a year.'),
], fmt='spot')

dup_lines = [
    ('groc', 'City Grocer', -52.80, {'date': 'Oct 17'}),
    ('tech1', 'TechWorld, headphones', -89.99, {'date': 'Oct 18'}),
    ('tech2', 'TechWorld, headphones', -89.99, {'date': 'Oct 18'}),
    ('quik', 'QuikShop Online', -64.00, {'date': 'Oct 20'}),
    ('gas', 'Shell gas station', -35.50, {'date': 'Oct 21'}),
]
DUP = doc('statement', 'Harbor Bank', dup_lines, subtitle='Checking · Oct 17–23', meta=[['Account', '•••• 4417']])
double = lesson('bf-double-charge', 'Charged Twice', 'Mistakes and strangers on your statement: how to fight back.', [
    spot('You’ve never shopped at QuikShop. Tap the charge that isn’t yours.', DUP, 'quik',
         'A charge from a store you’ve never used can mean someone has your card details.',
         context='Mistakes happen, and so does fraud. Read every line, not just the total.'),
    mc('You bought one pair of headphones. How many times were you charged?', ['Twice', 'Once', 'Three times'], 0,
       'Two identical TechWorld lines on the same day.', doc=DUP),
    num('Counting the double charge and the QuikShop charge, how much should come back to you?', 153.99,
        '$89.99 + $64.00 = $153.99.', doc=DUP),
    mc('A charge is wrong. When should you dispute it?', ['As soon as you notice', 'After a year', 'Never, banks don’t make mistakes'], 0,
       'Act fast. You get the most protection when you report quickly, usually within 60 days of the statement.',
       context='To [[dispute]] a charge means asking your bank to investigate it and reverse it.'),
    order('Put a dispute in order.',
          ['Lock your card if it might be fraud', 'Report the charge to your bank', 'Explain what’s wrong and keep your records', 'Check the refund shows up on your statement'],
          'Stop it, report it, document it, confirm it.'),
    tf('If a card charge is fraud, keep using the card until the bank calls you.', False, 'Lock it now. A new card is free.'),
], fmt='spot')

rec_lines = [
    ('pay', 'Direct deposit, Harbor Grocery', 845.00, {'date': 'Nov 1'}),
    ('rent', 'Rent', -600.00, {'date': 'Nov 2'}),
    ('groc', 'City Grocer', -63.45, {'date': 'Nov 6'}),
    ('power', 'Bright Power', -84.12, {'date': 'Nov 9'}),
]
rec_close = total([210.00] + [l[2] for l in rec_lines])
assert rec_close == 307.43
REC = doc('statement', 'Harbor Bank', rec_lines, subtitle='Checking · Nov 1–10', meta=[['Account', '•••• 4417']],
          totals=[('Opening balance', 210.00)])
reconcile = lesson('bf-reconcile', 'Does It Add Up?', 'Check your numbers against the bank’s.', [
    mc('What’s the point of reconciling?', ['Catching mistakes, fees and fraud', 'Earning interest', 'Paying less tax'], 0,
       'If your numbers and the bank’s don’t match, something happened you didn’t know about.',
       context='To [[reconcile]] your account means checking your own records against the bank’s, line by line, so nothing surprises you.'),
    num('Opening balance $300. Money in $1,200. Money out $1,050. What’s the closing balance?', 450, '$300 + $1,200 − $1,050 = $450.'),
    num('Your records say $450, but the bank shows $415. How big is the gap?', 35, '$450 − $415 = $35.'),
    mc('A $35 gap. What’s the most likely cause?', ['An overdraft fee or charge you didn’t record', 'The bank gave you money', 'A math error the bank makes every month'], 0,
       '$35 is exactly a typical overdraft fee. Check the statement.'),
    tf('Pending transactions can make your records and the bank’s balance disagree for a day or two.', True,
       'Give pending payments time to post before you worry.'),
    num('Work out the closing balance for this statement.', rec_close,
        '$210.00 + $845.00 − $600.00 − $63.45 − $84.12 = $307.43.', doc=REC),
])

HARBOR = doc('bill', 'Harbor Classic', [
    ('fee', 'Monthly fee', 10.00), ('atm', 'Other banks’ ATMs, each time', 3.00), ('od', 'Overdraft fee', 35.00)],
    subtitle='Checking account', note='Monthly fee waived with a $1,000 balance.')
CLOUD = doc('bill', 'Cloud Free Checking', [
    ('fee', 'Monthly fee', 0.00), ('atm', 'ATMs in network', 0.00), ('od', 'Overdraft fee (purchases declined instead)', 0.00)],
    subtitle='Online bank checking', note='No branches.')
assert 10 * 12 + 2 * 3 * 12 == 192
choose = lesson('bf-choose', 'Pick the Better Account', 'Compare two accounts on what you’d actually pay.', [
    mc('You keep about $400 in checking and use other banks’ ATMs twice a month. Which account costs less?', ['Cloud Free Checking', 'Harbor Classic'], 0,
       'With $400 you’d pay Harbor’s $10 fee every month, plus ATM fees.', docs=[HARBOR, CLOUD],
       context='Compare accounts on what **you** would pay, based on how you actually bank.'),
    num('With Harbor Classic, what would you pay in a year? $10 a month, plus two $3 ATM fees a month.', 192,
        '$10 × 12 = $120, plus 2 × $3 × 12 = $72. $192 a year.', docs=[HARBOR, CLOUD]),
    num('And with Cloud Free Checking?', 0, 'Nothing. Same insurance, no fees.', docs=[HARBOR, CLOUD]),
    mc('When could Harbor Classic make sense?', ['If you always keep $1,000 or more and use their ATMs', 'If you like paying fees', 'Never'], 0,
       'Then the fees disappear, and you get branches too.'),
    tf('The account with the most branches is always the best deal.', False, 'Branches cost money, and someone pays for them: often you.'),
], fmt='call')

kai_story = {
    'title': '$31 of spending, $70 of fees',
    'character': 'Kai, 20, college student',
    'body': 'Kai’s checking account had **$18** on Monday. Payday wasn’t until Friday.\n\n'
            'On Monday Kai bought a **$5** coffee. On Tuesday, another **$5** coffee and a **$9** lunch. On Wednesday, a **$12** phone top-up. '
            'Kai’s bank lets payments through when the account is short, and charges **$35** for each one that overdraws it.\n\n'
            'On Friday Kai’s **$420** paycheck arrived, and the account looked strangely small.',
}
kai = lesson('bf-kai', 'Kai’s Expensive Week', 'Follow one week of small purchases into a big hole.', [
    num('Add up everything Kai spent from Monday to Wednesday.', 31, '$5 + $5 + $9 + $12 = $31.'),
    num('Kai started with $18. By how much did Kai overdraw the account?', 13, '$31 − $18 = $13.'),
    mc('Which purchase was the first to overdraw the account?', ['Tuesday’s lunch', 'Monday’s coffee', 'Tuesday’s coffee'], 0,
       '$18 − $5 − $5 = $8 left. The $9 lunch took it to −$1.'),
    num('Two purchases went through while the account was short. How much in overdraft fees?', 70, '2 × $35 = $70.'),
    num('Friday’s $420 paycheck arrives. What’s left after the −$13 balance and the $70 of fees?', 337, '$420 − $13 − $70 = $337.'),
    mc('Which one change would have saved Kai the $70?', ['Opting out of overdraft, so the card was declined', 'Buying a bigger lunch', 'Checking the balance on Friday'], 0,
       'A declined card is embarrassing for a second. $70 hurts for a week.'),
], fmt='story', story=kai_story)

trial_steps = [
    num('You overdraw by $4 and pay a $35 fee. What did the overdraft really cost?', 39, '$4 + $35 = $39.'),
    mc('What does reconciling your account catch?', ['Fees, mistakes and fraud', 'Extra interest', 'A higher credit score'], 0, 'If the numbers don’t match, find out why.'),
    tf('A maintenance fee can often be avoided with direct deposit or a minimum balance.', True, 'Ask your bank exactly what waives it.'),
    num('Opening balance $500. In $900, out $1,150. What’s the closing balance?', 250, '$500 + $900 − $1,150 = $250.'),
]

lessons = [statement, fees, overdraft, spot_fee, double, reconcile, choose, kai,
           review('bf'), trial('bf', 'Fees & Statements', trial_steps)]
write_unit('05-bank-fees.json', 'bank-fees', 5, 'Bank Fees & Statements',
           'Read a statement, dodge the fees, and catch the bank’s mistakes.',
           'Fees are small bites. Enough small bites and you’re dinner.', terms, lessons)
