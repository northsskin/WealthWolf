from lib import *
from preserved import kept, kept_term

S = 'credit-debt'
terms = {
    'avalanche-method': kept_term('avalanche-method'),
    'snowball-method': kept_term('snowball-method'),
    'debt-consolidation': term('Debt consolidation', 'Replacing several debts with one new loan, ideally at a lower rate. It only helps if the new loan is cheaper and you stop adding debt.',
                               'Roll a 24% card and a 22% card into one 12% loan, and do not spend on the cards again.'),
}

list_lines = [
    ('store', 'Store card · 26% APR', 600),
    ('card', 'Credit card · 20% APR', 1400),
    ('auto', 'Car loan · 7% APR', 5000),
]
assert 600 + 1400 + 5000 == 7000
LIST = doc('statement', 'Every debt', list_lines, subtitle='Balances today',
           totals=[('Total owed', 7000, True)])
listing = lesson('dp-list', 'List Every Debt', 'You cannot aim at a debt you have not written down.', [
    num('What is the store-card balance?', 600, 'The first line: $600.',
        context='Write every debt: who you owe, the [[balance]], the [[APR]], and the [[minimum payment]]. The list is the map.',
        doc=LIST),
    num('What do all three balances add up to?', 7000, '$600 + $1,400 + $5,000 = $7,000.', doc=LIST),
    mc('Which debt has the highest APR?', ['The store card, 26%', 'The car loan, 7%', 'They are equal'], 0,
       '26% costs the most per dollar.', doc=LIST),
    mc('Which balance is the smallest?', ['The store card, $600', 'The credit card, $1,400', 'The car loan, $5,000'], 0,
       '$600 is the small one. That matters for one payoff method, and the APR matters for the other.', doc=LIST),
    tf('A debt you leave off the list still charges interest.', True, 'Unlisted is not unpaid. It is just invisible to you.'),
    num('The minimums are $25, $40, and $150. How much do the minimums cost each month, before any extra?', 215,
        '$25 + $40 + $150 = $215.'),
], fmt='document')

trap = lesson('dp-minimums', 'Minimums Keep the Debt', 'Pay every minimum. Then attack one balance with everything else.', [
    num('You owe $2,400 at 18% APR. The monthly rate is 1.5%. How much is this month’s interest?', 36,
        '$2,400 × 0.015 = $36.',
        context='The [[minimum payment]] keeps the account current. On a high [[APR]] it may barely touch the [[balance]].'),
    num('The minimum is $50. How much of it cuts the principal?', 14, '$50 − $36 = $14.'),
    num('You send an extra $100 to this debt. How much principal do you cut this month, interest included in the $50?', 114,
        '$14 from the minimum, plus $100 extra = $114.'),
    mc('What is the rule while you attack one debt?',
       ['Keep paying the minimum on the others', 'Stop paying the others', 'Pay a different debt each day at random'], 0,
       'Missed minimums mean fees and marks. Extra money has one target.'),
    tf('Paying only the minimums is a payoff plan.', False, 'It is the floor. The payoff is the extra.'),
    num('After the $114 principal payment, what is the balance?', 2286, '$2,400 − $114 = $2,286.'),
])

consol = lesson('dp-consolidate', 'Consolidation', 'One payment can be simpler. It is not automatically cheaper.', [
    mc('What is debt consolidation?',
       ['One new loan that replaces several debts', 'A program that erases the balances', 'Skipping the minimums'], 0,
       'The debts move. They do not vanish.',
       context='[[Debt consolidation]] rolls several balances into one loan. It helps when the new [[APR]] is lower and the total you pay goes down. It hurts when the new loan lasts so long that you pay more, or when you run the old cards back up.'),
    num('You roll $4,000 at a rough 24% into a loan at 12%. Rough yearly interest before: $4,000 × 0.24. What is that?', 960,
        '$4,000 × 0.24 = $960.'),
    num('Rough yearly interest after, at 12%?', 480, '$4,000 × 0.12 = $480.'),
    num('How much less is that rough yearly interest?', 480, '$960 − $480 = $480. A real loan amortizes, so treat this as the size of the gap, not a quote.'),
    tf('Consolidation saves money even if the new loan’s total payments are higher.', False,
       'Cheaper means fewer dollars over the life of the loan, not a tidier bill.'),
    mc('You consolidate, then spend $1,000 on the old card. What happened?',
       ['You added a new debt on top of the consolidation loan', 'The new spending is free', 'The consolidation paid it off too'], 0,
       'Cut up the habit, or the cards fill again.'),
])

nego = lesson('dp-negotiate', 'Ask for a Lower Rate', 'A phone call is free. The worst answer is the rate you already have.', [
    mc('You have a year of on-time payments. What can you ask the card issuer?',
       ['A lower APR', 'A higher balance', 'To skip reporting your payments'], 0,
       'Polite, specific, and ready to leave for a better offer.',
       context='A lower [[APR]] on a [[balance]] you are actually carrying is worth asking for. They do not have to say yes. A no leaves you where you were.'),
    num('You owe $2,000. A drop from 24% to 15% APR. Rough yearly interest before?', 480, '$2,000 × 0.24 = $480.'),
    num('Rough yearly interest after the drop?', 300, '$2,000 × 0.15 = $300.'),
    num('How much does that rough year save?', 180, '$480 − $300 = $180.'),
    tf('The issuer can say no, and your rate stays the same.', True, 'Asking did not raise it.'),
    mc('They say no. What else can still cut the cost?',
       ['Pay the balance faster, or move it if a cheaper offer is real', 'Stop paying', 'Open three store cards'], 0,
       'The rate is one lever. The balance is the other.'),
])

plan = lesson('dp-plan', 'A Payoff Plan', 'Extra money needs a job. The expensive debt gets the first claim.', [
    mc('You have $180 extra this month. Which debt gets it first under the avalanche method?',
       ['The 26% store card', 'The 7% car loan', 'Split it into equal tiny piles'], 0,
       'Highest APR first.',
       context='Keep every [[minimum payment]]. Put the extra on one target. [[Avalanche method]]: highest APR. [[Snowball method]]: smallest balance.'),
    alloc('You have $180 extra. Give at least $90 to the highest-APR debt. Assign every dollar.', 180, 10,
          [{'label': 'Highest-APR debt', 'min': 90}, {'label': 'Another debt'}, {'label': 'A small cash buffer'}],
          'The highest-APR debt gets at least $90, and all $180 is assigned.'),
    num('You send $90 extra to a card every month for a year. How much principal is that, before counting the interest you also avoid?', 1080,
        '$90 × 12 = $1,080.'),
    tf('The snowball method is wrong if it is the one you will actually stick to.', False,
       'Avalanche saves more interest. Snowball’s quick wins keep some people going. The plan you follow beats the plan you abandon.'),
    order('Put a payoff month in order.',
          ['Pay every minimum', 'Send the extra to this month’s target', 'Write the new balances down', 'Do it again next month'],
          'Floor first, then the target, then the updated list.'),
    mc('A bonus of $500 lands. What does the plan say?',
       ['It goes to the target debt, unless an emergency has emptied your buffer', 'It is free spending', 'It raises every minimum'], 0,
       'Windfalls are how balances actually die.'),
], fmt='sort')

motivation = lesson('dp-stick', 'Staying With It', 'The math is the avalanche. The calendar is the hard part.', [
    mc('You miss one month of the extra payment. What now?',
       ['Pay the minimums, then resume the extra next month', 'Quit the plan', 'Skip the minimums to “catch up” on the extra'], 0,
       'A pause is not a failure. A missed minimum is a new problem.',
       context='Payoff plans die when they are too tight to live in. Leave a small buffer so a flat tire does not go back on the card.'),
    tf('An emergency fund, even a thin one, protects a payoff plan.', True,
       'Without it, the next surprise becomes new debt.'),
    num('Your extra payment is $150. You drop it to $100 for three months after a car repair. How much extra did you still send?', 300,
        '$100 × 3 = $300. Less than $450, and more than zero.'),
    mc('Which progress is worth noticing?',
       ['The balance is lower than last month', 'Only a balance of zero counts', 'The APR, which you cannot change today'], 0,
       'A smaller balance is the scoreboard.'),
    mc('You cleared the smallest card. What happens to the money that was its minimum?',
       ['It joins the extra payment on the next target', 'It becomes spending', 'It disappears'], 0,
       'That roll-forward is the snowball, and it works inside the avalanche too.'),
    fill('The plan you will still be doing in six months beats a perfect plan you ___.', ['quit', 'funded', 'wrote down'], 0, 'Quit is the failure. Boring and continuing is the method.'),
])

ray_story = {
    'title': 'The $9,000 climb',
    'character': 'Ray, 34, line cook',
    'body': 'Ray owes **$9,000**: a **$1,000** store card at **28%**, a **$3,000** credit card at **18%**, and a **$5,000** credit-union loan at **8%**. Every minimum gets paid.\n\n'
            'He can put an extra **$200** a month on one debt. He wants the path that wastes the least on interest.',
}
assert 1000 + 3000 + 5000 == 9000 and 200 * 5 == 1000
ray = lesson('dp-ray', 'Ray’s $9,000', 'Highest rate first. The small store card is also the expensive one.', [
    num('What do Ray’s three balances add up to?', 9000, '$1,000 + $3,000 + $5,000 = $9,000.'),
    mc('Avalanche method: which debt gets the extra $200 first?',
       ['The store card at 28%', 'The credit-union loan at 8%', 'Whichever statement arrives first'], 0,
       '28% is the most expensive dollar.'),
    num('At $200 extra a month, how many months of extra payments clear the $1,000 store card, ignoring the interest that stops along the way?', 5,
        '$1,000 ÷ $200 = 5 months. Interest makes it a bit longer. The minimum on that card shortens it.', unit='months'),
    mc('Snowball method: which debt would go first instead?',
       ['The $1,000 store card, because it is the smallest balance', 'The $5,000 loan', 'Split the $200 three ways'], 0,
       'On Ray’s list the smallest balance and the highest APR are the same card. Both methods start there.'),
    num('After the store card, the extra $200 moves to the 18% card. How much extra hits that card in a year?', 2400,
        '$200 × 12 = $2,400.'),
    tf('Once the store card is gone, Ray should start spending on it again.', False,
       'A zero balance stays zero. The $200 moves to the next debt.'),
], fmt='story', story=ray_story)

trial_steps = [
    mc('Extra money, avalanche style, goes to which debt?',
       ['The highest APR', 'The lowest APR', 'The newest account'], 0, 'The expensive interest dies first.'),
    num('Minimum $40, of which $25 is interest. How much principal does the minimum cut?', 15, '$40 − $25 = $15.'),
    tf('A consolidation loan saves money even when you charge the old cards back up.', False, 'New charges are a new debt beside the new loan.'),
    num('Three balances: $400, $900, and $1,700. What is the total?', 3000, '$400 + $900 + $1,700 = $3,000.'),
]

lessons = [listing, trap, kept('dc-avalanche-snowball'), consol, nego, plan, motivation, ray,
           review('dp'), trial('dp', 'Getting Out of Debt', trial_steps)]
write_unit('09-debt-payoff.json', 'debt-payoff', 9, 'Getting Out of Debt',
           'List the debts, pick a method, and give every extra dollar one job.',
           'Pick a method. Then throw money at one debt until it dies.', terms, lessons, section=S)
