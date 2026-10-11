import json, os
from lib import *

path = os.path.join(DATA, SECTION, '01-money-fundamentals.json')
old = json.load(open(path))
L = [l for l in old['lessons'] if l['id'] != 'mf-snapshot']

maya_story = {
    'title': 'A one-page check-up',
    'character': 'Maya, 28, retail manager',
    'body': 'Maya sat down to see where she stands. Each month she takes home **$3,200**. Her expenses: rent **$1,300**, groceries **$350**, '
            'a car payment of **$280**, her phone **$60**, and about **$700** on eating out and shopping.\n\n'
            'She owns a car worth **$9,000** and has **$2,500** in the bank. She still owes **$6,000** on the car and **$1,200** to a friend.',
}
assert 1300 + 350 + 280 + 60 + 700 == 2690 and 9000 + 2500 == 11500 and 6000 + 1200 == 7200
snapshot = lesson('mf-snapshot', 'Maya’s Money Check-Up', 'Cash flow and net worth for one real-feeling person.', [
    num('Add up Maya’s monthly expenses.', 2690, '$1,300 + $350 + $280 + $60 + $700 = $2,690.'),
    num('What’s her monthly cash flow?', 510, '$3,200 − $2,690 = $510.'),
    num('Add up her assets.', 11500, 'Car $9,000 + bank $2,500 = $11,500.'),
    num('Add up her liabilities.', 7200, 'Car $6,000 + friend $1,200 = $7,200.'),
    num('What’s her net worth?', 4300, '$11,500 − $7,200 = $4,300.'),
    sort('Need or want?', ['Need', 'Want'], [('Rent', 0), ('Groceries', 0), ('Car payment', 0), ('Phone', 0), ('Eating out and shopping', 1)]),
    mc('Maya wants her net worth to grow faster. Best first move?',
       ['Trim eating out and shopping, and save the difference', 'Buy a more expensive car', 'Stop paying what she owes on the car'], 0,
       'Every dollar moved from wants to savings raises her net worth.',
       why=['', 'A pricier car usually means more owed, and a car loses value.', 'Missing payments brings fees and bigger trouble.']),
], fmt='story', story=maya_story)

i = next(k for k, l in enumerate(L) if l['id'] == 'mf-bills')
lessons = L[:i + 1] + [snapshot] + L[i + 1:]
write_unit('01-money-fundamentals.json', old['id'], 1, old['title'], old['description'], old['wolfLine'], old['terms'], lessons)
