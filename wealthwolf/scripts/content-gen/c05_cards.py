from lib import *

S = 'credit-debt'
terms = {
    'statement-balance': term('Statement balance', 'The total you owed on a card at the end of the billing period. Pay this by the due date and you usually avoid interest.',
                              'A statement balance of $480, paid in full by the due date, means $0 interest on those purchases.'),
    'grace-period': term('Grace period', 'The time between the statement date and the due date. Pay the statement balance in full by the due date and new purchases from that period are not charged interest.',
                         'Statement balance $480, due on the 21st. Pay $480 by the 21st and the grace period holds.'),
    'cash-advance': term('Cash advance', 'Cash you take from a credit card. A fee applies, interest usually starts the same day, and there is no grace period.',
                         'Take $200 cash. A 5% fee adds $10, so you owe $210 before a single day’s interest.'),
}

stmt_lines = [('purch', 'Purchases this period', 480)]
assert stmt_lines[0][2] == 480
STMT = doc('bill', 'Harbor Card', stmt_lines, subtitle='October statement',
           meta=[['Statement balance', '$480.00'], ['Minimum payment', '$25.00'], ['Due date', 'Oct 21']],
           totals=[('Statement balance', 480, True)],
           note='Interest rate 24% APR. Pay the statement balance by Oct 21 to avoid interest.')
statement = lesson('cc-statement', 'The Card Statement', 'Three numbers matter: the statement balance, the minimum, and the due date.', [
    num('What is the statement balance?', 480, 'The total for this period: $480.',
        context='The [[statement balance]] is what you owed when the bill was cut. The [[minimum payment]] is the smallest amount that keeps the account in good standing. The [[due date]] is the last day to pay on time.',
        doc=STMT),
    num('What is the minimum payment on this bill?', 25, 'The bill asks for at least $25.', doc=STMT),
    mc('When is this bill due?', ['Oct 21', 'Whenever you feel like it', 'The day you opened the card'], 0,
       'Oct 21 is printed on the statement.', doc=STMT),
    num('You pay the $480 statement balance. How much of this period’s purchases is left unpaid?', 0, '$480 − $480 = $0.'),
    tf('Paying the minimum keeps you from being late. It does not pay off the balance.', True,
       'On time and paid off are two different jobs.'),
    mc('Which number, paid by the due date, usually avoids interest on these purchases?',
       ['The statement balance', 'The minimum payment', 'Half the minimum'], 0,
       'The full statement balance. The minimum leaves the rest to grow.'),
], fmt='document')

grace = lesson('cc-grace', 'The Grace Period', 'Pay the statement in full and the interest waits. Carry a balance and it does not.', [
    mc('What is a grace period on a credit card?',
       ['The stretch after the statement when you can pay in full and skip interest', 'An extra year to pay', 'A fee for paying early'], 0,
       'It is time, not a discount on the price.',
       context='A [[grace period]] is the time between the statement and the [[due date]]. Pay the [[statement balance]] in full by that date and those purchases are not charged interest. Carry a balance, and the grace period usually disappears until you catch up.'),
    tf('Pay the statement balance by the due date and those purchases usually cost no interest.', True,
       'That is the grace period doing its job.'),
    mc('You pay $25 of a $480 statement and leave $455. What happens to the grace period?',
       ['It is gone until you pay in full again', 'It stays, because you paid something', 'It doubles'], 0,
       'A partial payment is not “in full.”'),
    num('Statement balance $640. You pay $640 on the due date. How much interest do you owe on that statement?', 0,
        'Paid in full, on time: $0.'),
    mc('You lost the grace period last month. A new $50 purchase today is charged interest…',
       ['Starting right away, not after a fresh grace period', 'Never', 'Only if the purchase is over $500'], 0,
       'Until you pay the statement in full, new charges often start accruing immediately.'),
    fill('Pay the statement balance by the due date and you keep the ___ period.', ['grace', 'intro', 'tax'], 0, 'Grace period.'),
])

full = lesson('cc-full-vs-min', 'In Full or the Minimum', 'The minimum keeps the account current. The rest keeps costing you.', [
    num('Statement balance $625. Minimum $25. You pay the minimum. How much is still unpaid?', 600, '$625 − $25 = $600.',
        context='At 24% [[APR]], a rough monthly rate is 2%. Interest lands on what you did not pay.'),
    num('About how much interest hits that $600 in the next month?', 12, '$600 × 0.02 = $12.'),
    num('Of the $25 minimum, if $12 was interest, how much actually cut the balance?', 13, '$25 − $12 = $13. Just under half the payment was interest.'),
    num('You pay the $625 in full instead. How much interest do you owe on it?', 0, 'Paid in full: $0, against about $12 if you had paid only the minimum.'),
    mc('Which payment costs less interest?', ['$625, the statement balance', '$25, the minimum', 'They cost the same'], 0,
       'Zero interest beats $12, and the $12 repeats.'),
    tf('The minimum payment is designed to clear a typical card balance in one month.', False,
       'It is the smallest on-time payment, not a payoff plan.'),
])

trap = lesson('cc-min-trap', 'The Minimum Trap', 'Small payments stretch a balance for years.', [
    num('You owe $2,400 at 18% APR. The monthly rate is 1.5%. How much interest this month?', 36, '$2,400 × 0.015 = $36.',
        context='If the [[minimum payment]] is $50 and interest is $36, only $14 of your payment touches the [[balance]].'),
    num('You pay that $50 minimum. How much of it cuts the principal?', 14, '$50 − $36 = $14.'),
    num('What is the balance after that one payment?', 2386, '$2,400 − $14 = $2,386. Next month’s interest is worked out on almost the same debt.'),
    mc('What is the trap?',
       ['You pay every month and the balance barely moves', 'The balance vanishes after one minimum', 'The bank forgives the rest at month 12'], 0,
       'Most of the payment is interest.'),
    tf('Paying more than the minimum, and aiming it at this card, shortens the trap.', True,
       'Extra dollars go to principal, which cuts next month’s interest.'),
    mc('You can afford $150 this month, not just $50. Where should the extra $100 go?',
       ['Onto this balance', 'Into a second purchase on the same card', 'Nowhere. The minimum is the goal'], 0,
       'The extra $100 cuts principal. A new purchase digs the hole again.'),
])

limit = lesson('cc-limit-use', 'Limit and Utilization', 'The limit is a ceiling. Using all of it is not the goal.', [
    num('Limit $2,000. Balance $500. What is your utilization?', 25, '$500 ÷ $2,000 = 25%.',
        context='Your [[credit limit]] is the most you can owe on the card. [[Credit utilization]] is the balance divided by that limit. Lower is easier on a [[credit score]].', unit='%'),
    num('You spend another $700. What is the new balance?', 1200, '$500 + $700 = $1,200.'),
    num('What is utilization on the $2,000 limit now?', 60, '$1,200 ÷ $2,000 = 60%.', unit='%'),
    mc('The card company raises your limit from $2,000 to $4,000 and you still owe $1,200. What happens to utilization?',
       ['It falls from 60% to 30%', 'It doubles', 'It stays 60%'], 0,
       '$1,200 ÷ $4,000 = 30%. A higher limit helps only if you do not spend it.'),
    tf('A higher limit is a reason to spend more.', False, 'It is room, not a target.'),
    mc('Which habit keeps utilization in better shape?',
       ['Pay the balance down before the statement is cut, when you can', 'Wait until the card is maxed', 'Skip the bill'], 0,
       'The balance that gets reported is the one the score sees.'),
])

cash = lesson('cc-cash-advance', 'Cash Advances', 'The ATM on your card is the expensive door.', [
    mc('What is a cash advance?',
       ['Cash borrowed from the card, usually with a fee and interest from day one', 'A refund from a store', 'Free money from the bank'], 0,
       'It is a loan inside the card, on worse terms.',
       context='A [[cash advance]] is cash you take on a credit card. Expect a fee, often about 5%, and interest that starts immediately. There is no [[grace period]].'),
    num('You take a $200 cash advance with a 5% fee. How much is the fee?', 10, '$200 × 0.05 = $10.'),
    num('What do you owe before any interest?', 210, '$200 + $10 = $210.'),
    num('The cash-advance APR is 30%, about 2.5% a month. Rough interest on $210 for one month?', 5.25,
        '$210 × 0.025 = $5.25. And it started the day you took the cash.'),
    tf('A cash advance gets the same grace period as a normal purchase.', False, 'Interest starts right away.'),
    mc('You need $200 before payday. Which is usually cheaper?',
       ['Wait, cut a cost, or ask the biller for a few extra days', 'A credit-card cash advance', 'A second cash advance to pay the fee on the first'], 0,
       'The fee plus immediate interest is a steep price for two weeks of cash.'),
])

card_a = [
    ('fee', 'Annual fee', 0),
    ('apr', 'APR, as a yearly interest estimate on $1,000 carried', 220),
]
card_b = [
    ('fee', 'Annual fee', 95),
    ('apr', 'APR, as a yearly interest estimate on $1,000 carried', 180),
]
assert 180 + 95 == 275 and 275 - 220 == 55
CARD_A = doc('statement', 'Card A', card_a, subtitle='No annual fee · 22% APR',
             totals=[('Rough yearly cost if you carry $1,000', 220, True)])
CARD_B = doc('statement', 'Card B', card_b, subtitle='$95 annual fee · 18% APR',
             totals=[('Rough yearly cost if you carry $1,000', 275, True)])
pick = lesson('cc-first-card', 'Picking a First Card', 'If you pay in full, the fee matters more than the rate.', [
    mc('You plan to pay the statement in full every month. Which card is the cheaper tool?',
       ['Card A, with no annual fee', 'Card B, because 18% is lower than 22%', 'Whichever has the higher limit'], 0,
       'Paid in full, the APR rarely touches you. A $95 fee still does.',
       context='A first card should be one you can pay in full. Compare the annual fee and the [[APR]], and ignore rewards until those two are boring and cheap.',
       docs=[CARD_A, CARD_B]),
    num('If you do carry $1,000 for a year, what is Card A’s rough interest?', 220, '$1,000 × 0.22 = $220.', docs=[CARD_A, CARD_B]),
    num('Card B’s rough interest on that $1,000, plus its fee. What is the total?', 275, '$180 + $95 = $275.', docs=[CARD_A, CARD_B]),
    num('How much more is Card B in that “carry $1,000” case?', 55, '$275 − $220 = $55.'),
    tf('A lower APR always makes a card cheaper, even when you never carry a balance.', False,
       'If you pay in full, a $0 fee beats a $95 fee.'),
    mc('What is a solid rule for a first card?',
       ['No annual fee, and pay the statement in full', 'The highest limit you can get, spent at once', 'A store card at 30% because of today’s discount'], 0,
       'Boring and paid off builds the record. The fancy card can wait.'),
], fmt='call')

trial_steps = [
    num('Statement balance $360. You pay $40. How much is still unpaid?', 320, '$360 − $40 = $320.'),
    tf('A cash advance usually has a grace period.', False, 'Interest starts the day you take the cash.'),
    mc('Which payment usually avoids interest on a card statement?',
       ['The statement balance, by the due date', 'The minimum payment', 'One dollar'], 0,
       'In full, on time, keeps the grace period.'),
    num('$800 unpaid at a 2% monthly rate. About how much interest next month?', 16, '$800 × 0.02 = $16.'),
]

lessons = [statement, grace, full, trap, limit, cash, pick,
           lesson('cc-pay-on-time', 'Paying Late', 'A late card bill costs a fee, interest, and a mark.', [
               mc('You miss the due date. What can the issuer add?',
                  ['A late fee', 'A reward bonus', 'A higher savings rate'], 0,
                  'A [[late fee]] is the first hit.',
                  context='Miss a card’s [[due date]] and you can owe a [[late fee]], lose the [[grace period]], and, if it goes 30 days past due, pick up a mark on your [[credit report]].'),
               num('The bill is $84 and the late fee is $25. What do you owe before any extra interest?', 109, '$84 + $25 = $109.'),
               tf('A payment one day late can cost a late fee even if you pay the rest in full.', True,
                  'The due date is a cliff, not a suggestion.'),
               mc('When does a late card payment become a long-lived credit-report mark?',
                  ['Once it is about 30 days past due', 'One hour past the due date', 'Never, if you pay the late fee'], 0,
                  'The fee can hit immediately. The seven-year mark is the 30-day version.'),
               num('You pay the $84 two days late and the fee is $25. How much extra did being late cost, before interest?', 25,
                   'The fee is $25. The $84 was already yours to pay.'),
               mc('What prevents the fee?',
                  ['Pay at least the minimum by the due date', 'Pay sometime this season', 'Call after the fee posts and hope'], 0,
                  'On time beats an apology. Autopay the minimum, then pay the rest.'),
           ]),
           review('cc'), trial('cc', 'Credit Cards', trial_steps)]
write_unit('05-credit-cards.json', 'credit-cards', 5, 'Credit Cards',
           'Read the statement, keep the grace period, and treat the minimum as a warning.',
           'The minimum is a trap with a due date.', terms, lessons, section=S)
