from lib import *

S = 'home-life'
terms = {}

steps = lesson('le-steps', 'When the Event Hits', 'The event changes. The order of the money work does not.', [
    info('Four beats',
         'A move, a wedding, a divorce, a baby, a lost job, or a death all hit the same list.\n\nName the bills that changed. Update the [[beneficiary]] names and the insurance. Set the cash plan. Tell the people who share the money.'),
    order('Put the money work in order.',
          ['List the bills that changed',
           'Update beneficiaries and insurance',
           'Set the cash plan',
           'Tell the people who share the money'],
          'You cannot plan a bill you have not listed. The papers and the cash come before the announcement.'),
    mc('Why do the papers come before you spend the savings?',
       ['An old beneficiary can send the money to the wrong person', 'The bank requires a party first', 'Insurance updates itself'], 0,
       'A wedding, a divorce, or a death is exactly when the old name becomes the wrong name.'),
    tf('You can skip the list if the event is a happy one.', False,
       'A wedding and a baby add bills too. Happy is not the same as cheap.'),
    fill('First, list the bills that ___.',
         ['changed', 'vanished', 'doubled themselves'], 0,
         'The list is the start. Guessing is how a bill gets missed.'),
])

events = lesson('le-events', 'Each Event’s Job', 'Match the moment to the money move.', [
    info('Six moments, four cards',
         'Moving cities needs a deposit and a truck. Getting married needs a talk and new beneficiaries. A baby needs childcare and insurance. A lost job needs a cut in bills and the [[emergency fund]].\n\nDivorce and a death get their own lessons. They are not missing. They are next.'),
    match('Match the event to the money job.',
          [('Moving cities', 'Deposits, a truck, and first month’s rent'),
           ('Getting married', 'A money talk and updated beneficiaries'),
           ('A new baby', 'Childcare and insurance'),
           ('Losing a job', 'Cut bills and use the emergency fund')],
          'Each event has a job. The match is the job, not a slogan.'),
    mc('You are moving cities. Which pile of cash is the one to plan first?',
       ['Deposits, a truck, and the first month', 'A college fund', 'A HELOC on a house you do not own yet'], 0,
       'The move has a due date. The other piles do not.'),
    tf('Losing a job is the moment to raise every subscription.', False,
       'It is the moment to cut. The emergency fund is for the gap, and it is finite.'),
    fill('A new baby adds ___ to the monthly plan.',
         ['childcare', 'a truck rental', 'a wedding venue'], 0,
         'Childcare is the line that shows up and stays.'),
])

old = doc('statement', 'After the divorce', [
    ('rent', 'Rent', 1500),
    ('car', 'Car insurance', 140),
    ('life', 'Life insurance premium', 30),
    ('old', 'Automatic transfer to an account only your former spouse can open', 400),
])
papers = lesson('le-papers', 'Update the Papers', 'A divorce, a marriage, or a death leaves old names in place until you change them.', [
    info('The transfer does not notice the decree',
         'Accounts and policies keep the old instructions until you change them. This statement still sends **$400** a month to an account only a former spouse can open.\n\nThe [[beneficiary]] on a life policy can be just as stale. Update it. Tell the insurer. Do not assume the divorce did the paperwork.'),
    spot('Which line should have stopped?', old, 'old',
         'The $400 transfer still feeds an account that is no longer yours to share.'),
    num('How much is that leftover transfer per year?', 4800, '$400 × 12 = $4,800.', doc=old),
    mc('You just married. What happens to a life policy that still names a parent, if you wanted your spouse?',
       ['Nothing, until you file a beneficiary change', 'It updates on the wedding day', 'The court picks a new name'], 0,
       'The form is the update. The wedding is not.'),
    tf('A divorce automatically removes an ex from every beneficiary line.', False,
       'You have to change each account and each policy. The decree does not log in for you.'),
], fmt='spot')

wedding = lesson('le-wedding', 'A Wedding Budget', 'Give the day a total before the vendors do.', [
    info('Eight thousand dollars',
         'The cap is **$8,000**. The venue needs at least **$3,000**. Food needs at least **$2,000**. Photos need at least **$1,000**.\n\nWhat remains is a buffer. A wedding without a buffer spends the [[emergency fund]] the first time a vendor adds a fee.'),
    alloc('Assign $8,000. The venue needs at least $3,000, food at least $2,000, and photos at least $1,000.', 8000, 100,
          [{'label': 'Venue', 'min': 3000}, {'label': 'Food', 'min': 2000}, {'label': 'Photos', 'min': 1000}, {'label': 'Buffer'}],
          'Those three minimums are $6,000. The buffer gets a job too, and all $8,000 is assigned.'),
    num('Venue $3,000, food $2,000, and photos $1,000. How much of the $8,000 is still unassigned?', 2000,
        '$8,000 − $3,000 − $2,000 − $1,000 = $2,000.'),
    num('A vendor adds a $400 fee. The buffer is $2,000. How much buffer is left?', 1600,
        '$2,000 − $400 = $1,600.'),
    tf('If the wedding runs over, the emergency fund is the right next account.', False,
       'The buffer is for the wedding. The emergency fund is for a job loss or an urgent repair.'),
])

big = lesson('le-big', 'A Big Expense', 'Divide it by the months you actually have.', [
    info('A move with a date',
         'The move will cost **$6,000**, and you have **10** months. That is **$600** a month.\n\nWaiting and putting it on a card adds [[interest]]. The plan is the $600, set aside on purpose.'),
    num('A $6,000 move in 10 months. How much do you set aside each month?', 600,
        '$6,000 ÷ 10 = $600.'),
    num('You actually save $600 for 6 months, then the date moves up. How much have you saved?', 3600,
        '$600 × 6 = $3,600.'),
    num('The move still costs $6,000. How short are you?', 2400,
        '$6,000 − $3,600 = $2,400.'),
    mc('What is the better fix for that $2,400 gap?',
       ['Cut the move or earn the gap, instead of quietly charging it', 'Put it on a card and call it a plan', 'Skip the next month of rent'], 0,
       'A card is a loan. Name it as one, or shrink the expense.'),
])

cash = doc('statement', 'Pay from savings', [
    ('pay', 'You pay', 8000),
], subtitle='No loan')
loan = doc('statement', 'Pay with a loan', [
    ('pay', 'Payments over 12 months', 9000),
], subtitle='$750 a month')
assert 750 * 12 == 9000 and 9000 - 8000 == 1000

ways = lesson('le-ways', 'Cash or a Loan', 'The loan costs $1,000 more for the same day.', [
    num('The loan is $750 a month for 12 months. What do you pay in all?', 9000,
        '$750 × 12 = $9,000.', docs=[cash, loan]),
    num('Paying from savings costs $8,000. How much more is the loan?', 1000,
        '$9,000 − $8,000 = $1,000.', docs=[cash, loan]),
    mc('You have the $8,000, and it is not your emergency fund. Which page costs less?',
       ['Pay from savings', 'The 12-month loan', 'They cost the same'], 0,
       'Savings costs $8,000. The loan costs $9,000.',
       why=['$8,000 is the lower total.', 'The loan adds $1,000.', 'The pages differ by $1,000.'],
       docs=[cash, loan]),
    tf('The loan is cheaper because you pay it in small pieces.', False,
       'The pieces add up to $9,000. Small is not the same as less.'),
    fill('The extra $1,000 on the loan is the cost of ___.',
         ['borrowing', 'the venue', 'the photos'], 0,
         'Same wedding. The extra thousand is interest and fees, not a better party.'),
], fmt='call')

death = lesson('le-death', 'A Death in the Family', 'The papers matter more than the casserole schedule.', [
    info('What to touch first',
         'Ask for the death certificates you will need. Find the will, the [[beneficiary]] forms, and the bills that were on autopay.\n\nA funeral here is budgeted at **$8,000**. If **$3,000** was set aside, the gap is **$5,000**. Do not fill that gap from a credit card before you know what insurance or the estate will pay.'),
    num('The funeral budget is $8,000 and $3,000 was set aside. How large is the gap?', 5000,
        '$8,000 − $3,000 = $5,000.'),
    mc('Which paper tells the insurer who is paid?',
       ['The beneficiary form', 'The funeral program', 'The last grocery receipt'], 0,
       'The beneficiary form is the instruction. The other two are not.'),
    tf('Autopay stops on its own when someone dies.', False,
       'Bills keep drafting until a person stops them. Find the list.'),
    fill('The gap in this funeral budget is ___.',
         ['$5,000', '$8,000', '$3,000'], 0,
         '$8,000 − $3,000 = $5,000. Know the gap before you borrow it.'),
])

tom_story = {
    'title': 'Tom’s year',
    'character': 'Tom, 32',
    'body': 'Tom is 32. He moves cities, and the truck, the deposit, and the first month cost **$3,500**. His [[emergency fund]] was **$10,000**, so **$6,500** is left.\n\nThe wedding he wants is **$8,000**. Paying it in cash from what remains would leave him **$1,500** short, and it would spend the cushion he has left.\n\nHe gets married anyway, on a smaller plan, and he updates his [[beneficiary]]. When a layoff rumor starts in the fall, the remaining savings are still there.',
}
tom = lesson('le-tom', 'Tom’s Year', 'The move was affordable. The wedding, on top of it, was not.', [
    num('The emergency fund was $10,000 and the move cost $3,500. How much is left?', 6500,
        '$10,000 − $3,500 = $6,500.'),
    num('The wedding he first wanted is $8,000. How short is the $6,500?', 1500,
        '$8,000 − $6,500 = $1,500.'),
    mc('What keeps a cushion for the layoff rumor?',
       ['A smaller wedding, so the $6,500 is not spent', 'The $8,000 wedding, paid from the cushion', 'Skipping the beneficiary update to save a stamp'], 0,
       'The $1,500 gap means the original wedding spends the cushion and still comes up short.'),
    tf('Tom’s marriage automatically made his spouse the beneficiary.', False,
       'He had to send the form. The wedding did not.'),
    num('If he keeps the $6,500 and a layoff cuts $2,000 of income, how much of the cushion is left after covering that $2,000?', 4500,
        '$6,500 − $2,000 = $4,500.'),
], fmt='story', story=tom_story)

trial_steps = [
    mc('You divorced last month. A policy still names your ex. What actually changes it?',
       ['A beneficiary form you file', 'The divorce decree, by itself', 'Waiting a calendar year'], 0,
       'Each policy keeps its old name until you change that policy.'),
    num('A $4,800 expense over 8 months. How much do you set aside each month?', 600,
        '$4,800 ÷ 8 = $600.'),
    num('A loan costs $6,600 over the year. Cash costs $6,000. How much more is the loan?', 600,
        '$6,600 − $6,000 = $600.'),
    tf('A happy event, like a wedding, has no money checklist.', False,
       'It has a budget, a beneficiary update, and a line it must not steal from the emergency fund.'),
]

lessons = [steps, events, papers, wedding, big, ways, death, tom,
           review('le'), trial('le', 'Big Life Events', trial_steps)]
write_unit('09-life-events.json', 'life-events', 9, 'Big Life Events',
           'The same checklist for a move, a marriage, a split, a baby, a lost job, or a death.',
           'The event is loud. The checklist is quiet, and it is the part that saves you.', terms, lessons, section=S)
