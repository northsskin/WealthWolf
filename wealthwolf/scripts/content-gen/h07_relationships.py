from lib import *

S = 'home-life'
terms = {
    'financial-infidelity': term('Financial infidelity',
                                 'Hiding money, debt, or spending from the person you share finances with.',
                                 'A $650 transfer the other person did not know about, on an account you both use.'),
    'prenuptial-agreement': term('Prenup',
                                 'An agreement before marriage about what stays separate, such as a house or a business one person already owns. It is a legal document. This lesson is not legal advice.',
                                 'One person owns a house before the wedding. A prenup can say that house stays theirs.'),
}

early = lesson('rl-early', 'Talk Early', 'The lease is a bad moment to meet each other’s debts.', [
    info('Before the shared signature',
         'Talk about pay, debts, and savings before you sign a [[lease]] together, and before you mix accounts.\n\nThe talk is a budget, not a confession booth. Each person names what they earn, what they owe, and what they will not risk.'),
    mc('When is the useful time for the money talk?',
       ['Before you sign a lease or mix accounts', 'The week after a missed rent payment', 'Only if a wedding is already booked'], 0,
       'A shared signature is harder to undo than a conversation.'),
    mc('What belongs in that talk?',
       ['Income, debts, and what each of you will not risk', 'Only the rent, so the rest stays private forever', 'A promise that love makes a budget unnecessary'], 0,
       'The rent is one line. The debts and the cushion decide whether the rent is safe.'),
    tf('If you are not married, you do not need to talk about money before sharing a lease.', False,
       'The landlord can ask either signer for the full rent. Marriage is not what creates that risk.'),
    fill('Have the money talk before you ___ a lease together.',
         ['sign', 'celebrate', 'ignore'], 0,
         'The signature is the point of no easy return.'),
])

accounts = lesson('rl-accounts', 'Joint, Separate, or Both', 'There is a third design: shared bills, private spending.', [
    info('Three ways to hold it',
         'Joint: one account for the money you both earn. Separate: each person keeps their own, and you split the bills. Both: a shared account for the bills, plus an account that is only yours.\n\nNone of these is the moral choice. The worst one is the one you never agreed on.'),
    sort('Sort each setup.',
         ['Joint', 'Separate', 'Both'],
         [('Every paycheck lands in one shared account', 0),
          ('Each person keeps their own account and you split the bills', 1),
          ('A shared bills account, plus an account that is only yours', 2)],
         'Joint is one pot. Separate is two pots. Both is a pot for the bills and a pot of your own.'),
    mc('You want shared bills without asking permission for a haircut. Which setup is built for that?',
       ['Both: a bills account and a personal account', 'Joint only', 'Separate, with no plan for the rent'], 0,
       'The bills are shared. The haircut is not a committee decision.'),
    tf('A joint account means each person can only see their own half.', False,
       'A joint account is visible to both people, and either person can usually spend from it.'),
    fill('A shared bills account plus a personal account is the ___ setup.',
         ['both', 'joint', 'separate'], 0,
         'Both means you did not have to pick only one.'),
], fmt='sort')

split = lesson('rl-split', 'Split by Income', 'Equal shares are fair when the pay is equal.', [
    info('Use the incomes',
         'Alex earns **$4,000**. Jordan earns **$2,000**. Together that is **$6,000**.\n\nRent is **$1,800**. Alex’s share is 4,000 ÷ 6,000, or **$1,200**. Jordan’s is **$600**. A **$300** grocery run follows the same split: **$200** and **$100**.'),
    num('Alex earns $4,000 and Jordan earns $2,000. What is their combined income?', 6000,
        '$4,000 + $2,000 = $6,000.'),
    num('Rent is $1,800. What is Alex’s share at $4,000 of the $6,000?', 1200,
        '$4,000 ÷ $6,000 = 2/3. $1,800 × 2/3 = $1,200.'),
    num('What is Jordan’s share of that $1,800 rent?', 600,
        '$1,800 − $1,200 = $600. That is 1/3.'),
    num('Groceries are $300. What is Alex’s 2/3 share?', 200, '$300 × 2/3 = $200.'),
])

goals = lesson('rl-goals', 'A Shared Goal', 'Name it, date it, and give it a monthly number.', [
    info('One trip, one number',
         'A shared goal needs a name and a date. This trip costs **$3,000** and they have **10** months.\n\nThat is **$300** a month. On their income split, Alex puts in **$200** and Jordan puts in **$100**.'),
    num('The trip is $3,000 and they have 10 months. What do they save per month?', 300,
        '$3,000 ÷ 10 = $300.'),
    num('Alex pays 2/3 of that $300. How much does Alex put in?', 200, '$300 × 2/3 = $200.'),
    num('How much does Jordan put in?', 100, '$300 − $200 = $100.'),
    tf('A shared goal can live only in someone’s head, as long as both people want it.', False,
       'A date and a monthly number are what make it a plan. Wanting it is the start.'),
])

secret = doc('statement', 'Joint account, March', [
    ('rent', 'Rent, you both agreed', 1800),
    ('food', 'Groceries', 420),
    ('hide', 'Transfer the other person did not know about', 650),
])
flags = lesson('rl-flags', 'Money You Hide', 'A shared account with a secret is the red flag.', [
    info('The secret is the problem',
         '[[Financial infidelity]] is hiding spending, debt, or an account from the person who shares the money.\n\nThe rent and the groceries on this page were agreed. The **$650** transfer was not.'),
    spot('Which line is the red flag?', secret, 'hide',
         'The $650 transfer was hidden. The rent and the groceries were not.'),
    num('How much left the account in the transfer nobody agreed to?', 650,
        'The line is $650.', doc=secret),
    mc('What is the repair for a hidden transfer?',
       ['Tell the truth and agree on a rule for the account', 'Hide the next one better', 'Close the talk and keep the password'], 0,
       'The account only works if both people can see it.'),
    tf('A surprise gift on a personal account is the same thing as a hidden debt on a joint one.', False,
       'A gift from your own account is not a secret debt. Hiding a $650 transfer on the shared account is.'),
], fmt='spot')

lend = lesson('rl-lend', 'Lending to Friends', 'If you need it back, write it down. If you cannot lose it, do not lend it.', [
    info('Two tests',
         'A loan to a friend has two tests. Do you need the money back? Then write the amount and the date. Can you afford to lose it? If the answer is no, it is not a loan you can make.\n\n**$500** taken from an [[emergency fund]] fails the second test. That cash has a job already.'),
    mc('You would be in trouble if the friend never paid. What should you do?',
       ['Do not lend it', 'Lend it and hope', 'Lend it from the rent money'], 0,
       'A loan you cannot afford to lose is a gift you cannot afford.'),
    num('You lend $200 a month for 3 months from money you can lose. How much have you lent?', 600,
        '$200 × 3 = $600.'),
    mc('What makes a loan different from a gift, on paper?',
       ['A written amount and a date you expect it back', 'A handshake and a good feeling', 'Posting about it'], 0,
       'The writing is what you can point to later. It does not guarantee you are paid.'),
    tf('The emergency fund is a good source for a friend’s loan.', False,
       'That fund is for your job loss and your urgent repair. Lending it spends the cushion.'),
])

prenup = lesson('rl-prenup', 'A Prenup, at a High Level', 'A legal paper about what stays separate. Not advice for your wedding.', [
    info('What it is, and what this is not',
         'A [[prenup|prenuptial-agreement]] is an agreement before marriage about what stays separate. A house or a business one person already owns is a common reason.\n\nIt is a legal document. This lesson is not legal advice. A lawyer in your state is.'),
    mc('Which situation is a common reason people look at a prenup?',
       ['One person already owns a house or a business', 'They want the caterer to cost less', 'They have no assets and no debts'], 0,
       'The paper is about property that already exists, or debts one person does not want to share.'),
    tf('This course can tell you whether you should sign a prenup.', False,
       'That is legal advice, and it depends on your state and your facts. A lawyer can. A lesson cannot.'),
    mc('What is a prenup, in one line?',
       ['An agreement before marriage about what stays separate', 'A joint checking account', 'A replacement for a marriage license'], 0,
       'It sorts property. It is not the wedding and it is not a budget.'),
    fill('A prenup is signed ___ the marriage.',
         ['before', 'after', 'instead of'], 0,
         'The “pre” is the point. After the wedding, a different paper does that job.'),
])

pair_story = {
    'title': 'Alex and Jordan',
    'character': 'Alex, 28',
    'body': 'Alex is 28 and earns **$4,000**. Jordan is 27 and earns **$2,000**. The rent is **$1,800**, so they split it **$1,200** and **$600**.\n\nThey also want a **$3,000** trip in **10** months. That is **$300** a month, split **$200** and **$100**.\n\nAlex’s month for those two things is **$1,400**. Jordan’s is **$700**. They wrote both numbers down before they signed the [[lease]].',
}
pair = lesson('rl-pair', 'Alex and Jordan', 'The split follows the pay, and it is written down.', [
    num('What is Alex’s rent share?', 1200, '$1,800 × 2/3 = $1,200.'),
    num('What is Jordan’s rent share?', 600, '$1,800 × 1/3 = $600.'),
    num('Alex also puts $200 toward the trip. What is Alex’s total for rent plus the trip?', 1400,
        '$1,200 + $200 = $1,400.'),
    num('Jordan’s rent share plus $100 for the trip is how much?', 700,
        '$600 + $100 = $700.'),
    num('Do the two totals cover the $1,800 rent and the $300 trip?', 2100,
        '$1,400 + $700 = $2,100, and $1,800 + $300 = $2,100.'),
], fmt='story', story=pair_story)

trial_steps = [
    mc('Pay is $3,000 and $1,000. Rent is $1,600. What is the fairer first step?',
       ['Split the rent by income, not automatically in half', 'The higher earner pays nothing, because they worked for it', 'Hide the incomes and split the rent evenly'], 0,
       'Half of $1,600 is $800, which is most of the $1,000 paycheck. Income is the fairer base.'),
    tf('A hidden debt on a shared account is a small thing if the rent was still paid.', False,
       'The secret is the breach. The other person cannot plan around a debt they cannot see.'),
    num('A $2,400 goal in 8 months. What is the monthly save?', 300, '$2,400 ÷ 8 = $300.'),
    mc('Which setup gives you a shared bills account and a private one?',
       ['Both', 'Joint only', 'No accounts at all'], 0,
       'Both is the mix. Joint is one pot. Separate is two, with no shared pot.'),
]

lessons = [early, accounts, split, goals, flags, lend, prenup, pair,
           review('rl'), trial('rl', 'Money & Relationships', trial_steps)]
write_unit('07-relationships.json', 'relationships', 7, 'Money & Relationships',
           'The talk, the accounts, a fair split, and the secrets that break a budget.',
           'Agree on the split before you agree on the couch.', terms, lessons, section=S)
