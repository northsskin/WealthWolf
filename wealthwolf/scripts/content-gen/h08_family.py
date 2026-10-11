from lib import *

S = 'home-life'
terms = {
    'dependent-care-fsa': term('Dependent Care FSA',
                               'A work account for childcare or care of a qualifying dependent. In 2026 the federal exclusion is up to $7,500 per household, or $3,750 if you are married filing separately, and only if your plan offers that limit.',
                               'Childcare of $9,600. A plan that offers the full 2026 limit can cover $7,500 of it.'),
    'child-tax-credit': term('Child tax credit',
                             'A federal credit of up to $2,200 per qualifying child for 2026. It starts to shrink above $200,000 of income, or $400,000 if you are married filing jointly.',
                             'Two qualifying children, and income under the 2026 line: up to $2,200 × 2 = $4,400.'),
    '529-plan': term('529 plan',
                     'A savings plan for education. Qualified withdrawals are tax-free at the federal level. The balance can go down, and this course does not promise a return.',
                     'You put in $100 a month. What it is worth later depends on the investments, not on a guaranteed rate.'),
}

baby_doc = doc('statement', 'A baby’s first year, before childcare', [
    ('gear', 'Crib and gear', 600),
    ('diapers', 'Diapers and wipes', 960),
    ('formula', 'Formula', 1200),
    ('copay', 'Checkup copays', 240),
], note='Childcare is not on this page.', totals=[('Before childcare', 3000, True)])
assert 600 + 960 + 1200 + 240 == 3000 and 80 * 12 == 960 and 100 * 12 == 1200

baby = lesson('fc-baby', 'The First Year', 'This page stops before childcare. That bill is its own lesson.', [
    info('Four lines, not the whole story',
         'Gear **$600**. Diapers and wipes **$80** a month, which is **$960**. Formula **$100** a month, which is **$1,200**. Checkup copays **$240**.\n\nThe total is **$3,000**, and childcare is not in it.'),
    num('What is this first-year page, before childcare?', 3000,
        '$600 + $960 + $1,200 + $240 = $3,000.', doc=baby_doc),
    num('Diapers are $80 a month. What is that for 12 months?', 960, '$80 × 12 = $960.', doc=baby_doc),
    num('Formula is $100 a month. What is the year?', 1200, '$100 × 12 = $1,200.', doc=baby_doc),
    tf('This $3,000 page is the full cost of a baby’s first year.', False,
       'It leaves out childcare, which can be larger than all four lines combined.'),
], fmt='document')

center = doc('statement', 'Childcare center', [
    ('month', 'Monthly tuition', 1200),
], subtitle='One child')
home_care = doc('statement', 'Home day care', [
    ('month', 'Monthly tuition', 800),
], subtitle='One child')
assert 1200 * 12 == 14400 and 800 * 12 == 9600 and 14400 - 9600 == 4800 and 1200 - 800 == 400

care = lesson('fc-care', 'Childcare', 'The monthly tuition is the number that moves the budget.', [
    num('What does the center cost in a year?', 14400,
        '$1,200 × 12 = $14,400.', docs=[center, home_care]),
    num('What does the home day care cost in a year?', 9600,
        '$800 × 12 = $9,600.', docs=[center, home_care]),
    num('How much more is the center per year?', 4800,
        '$14,400 − $9,600 = $4,800.', docs=[center, home_care]),
    num('How much more is the center per month?', 400,
        '$1,200 − $800 = $400.', docs=[center, home_care]),
    mc('You need care five days a week and the $400 gap is the whole difference you care about. Which page costs less?',
       ['Home day care', 'The center', 'They cost the same per year'], 0,
       'Home day care is $9,600. The center is $14,400. Price is not the only reason to choose, but it is the gap on these pages.',
       docs=[center, home_care]),
], fmt='call')

fsa = lesson('fc-fsa', 'The Care Account and the Credit', 'Two different 2026 benefits. Do not add them into one bucket.', [
    info('2026, from the IRS',
         'A [[Dependent Care FSA|dependent-care-fsa]] is a work account. For 2026 the federal exclusion is up to **$7,500** per household, or **$3,750** if you are married filing separately. Your employer has to offer that limit. Many plans used to stop at $5,000.\n\nThe [[child tax credit]] is separate. For 2026 it is up to **$2,200** per qualifying child, and it starts to shrink above **$200,000** of income, or **$400,000** if you are married filing jointly. This lesson does not cover the Child and Dependent Care Credit. That is a third thing.'),
    num('Childcare is $9,600 and your plan offers the full $7,500. How much childcare is left outside the FSA?', 2100,
        '$9,600 − $7,500 = $2,100.'),
    num('You are married filing separately, so the 2026 FSA limit is $3,750. Childcare is $9,600. How much is outside the FSA?', 5850,
        '$9,600 − $3,750 = $5,850.'),
    num('One qualifying child, and your income is under the 2026 phaseout. What is the child tax credit, at the full amount?', 2200,
        'Up to $2,200 for that child. Income under $200,000, or under $400,000 if married filing jointly, is what keeps the full amount in play.'),
    tf('The $7,500 dependent-care limit and the $2,200 child tax credit are the same benefit counted twice.', False,
       'One is a work account for care expenses. The other is a tax credit per qualifying child. They are different, and a third credit exists that this lesson does not teach.'),
])

college = lesson('fc-529', 'A 529 Plan', 'Money for school. Not a promised return.', [
    info('Tax-free if you use it for school',
         'A [[529 plan]] is for education. Qualified withdrawals are tax-free at the federal level. The investments inside can fall.\n\n**$100** a month is **$1,200** a year of contributions. That is the part you control. The balance later is not a rate this course will invent.'),
    num('You contribute $100 a month. How much is that in a year?', 1200, '$100 × 12 = $1,200.'),
    num('You contribute $100 a month for 5 years. How much have you put in, before any investment change?', 6000,
        '$1,200 × 5 = $6,000.'),
    mc('What can you say for sure about a 529?',
       ['Qualified education withdrawals are tax-free at the federal level', 'The balance will rise by a set percent every year', 'The state must match what you put in'], 0,
       'The tax treatment of qualified withdrawals is the rule. The return is not.'),
    tf('A 529 is the same account as a dependent care FSA.', False,
       'The FSA pays this year’s care, up to the plan limit. A 529 is savings for education later.'),
])

kids = lesson('fc-kids', 'Teaching Kids', 'Three jars: spend, save, give.', [
    info('A small paycheck they can see',
         'A simple sketch is three jars. Spend, save, give.\n\nA **$10** gift becomes **$5** to spend, **$3** to save, and **$2** to give. The amounts matter less than the habit of splitting the money on purpose.'),
    num('The gift is $10. Spend $5, save $3, give $2. Do the three jars use the whole gift?', 10,
        '$5 + $3 + $2 = $10.'),
    num('She gets $10 a week and saves $3 each time. How much is in the save jar after 8 weeks?', 24,
        '$3 × 8 = $24.'),
    mc('What is the point of the three jars?',
       ['To practice choosing, before the amounts are large', 'To hide money from the household budget', 'To replace a college plan'], 0,
       'The habit is the lesson. A 529 can still exist beside it.'),
    tf('Kids should only see the spend jar, so saving stays an adult topic.', False,
       'The save jar is how saving becomes visible.'),
])

life = lesson('fc-life', 'Once Someone Depends on You', 'The policy from the protecting section now has a reason.', [
    info('A dependent changes the question',
         '[[Term life insurance|term-life]] pays if you die during the term. The [[beneficiary]] is who receives it.\n\nBefore anyone depended on your income, the policy had no job. A child who needs your paycheck is the job. Name the beneficiary on purpose, and check it when the family changes.'),
    mc('Who is the beneficiary?',
       ['The person you name to receive the money if you die', 'The insurance company', 'The child-care center'], 0,
       'You choose them. If you do not, the policy’s default may not be who you think.'),
    mc('Why does a new child change the life-insurance question?',
       ['Someone now depends on your income', 'Term life becomes a savings account', 'The premium is no longer owed'], 0,
       'The need is the dependent. The product is still term life, not a new kind of account.'),
    tf('A term policy pays the beneficiary every year, like a paycheck, while you are alive.', False,
       'It pays if you die during the term. It is not income while you are living.'),
    fill('The person who receives the life insurance is the ___.',
         ['beneficiary', 'landlord', 'lender'], 0,
         'Name them, and update the name when life changes.'),
])

family = lesson('fc-budget', 'A Family Month', 'Childcare gets the first claim. Then the rest of the $2,000.', [
    info('Two thousand dollars',
         'This month has **$2,000** for the new family costs. Childcare needs at least **$1,200**. Diapers and food need at least **$200**.\n\nWhat remains can go to a college jar. Assign every dollar.'),
    alloc('Assign $2,000. Childcare needs at least $1,200, and diapers and food need at least $200.', 2000, 50,
          [{'label': 'Childcare', 'min': 1200}, {'label': 'Diapers and food', 'min': 200}, {'label': 'College jar'}],
          'Childcare is at least $1,200, diapers and food at least $200, and all $2,000 is assigned.'),
    num('Childcare takes $1,200 and diapers take $200. How much is left of the $2,000?', 600,
        '$2,000 − $1,200 − $200 = $600.'),
    num('That leftover $600 goes to the college jar every month. How much is that in a year?', 7200,
        '$600 × 12 = $7,200.'),
    tf('The college jar should be filled before the childcare bill.', False,
       'Care is due this month. The college jar is what is left after the bills that cannot wait.'),
])

maria_story = {
    'title': 'Maria’s twins',
    'character': 'Maria, 34',
    'body': 'Maria is 34. She is having twins, and her income is **$85,000**, under the 2026 line where the [[child tax credit]] starts to shrink.\n\nAt the full amount, two qualifying children are **$2,200** × 2, which is **$4,400**. Childcare is **$1,000** a child each month, so **$2,000** a month, or **$24,000** a year.\n\nHer plan offers the 2026 [[Dependent Care FSA|dependent-care-fsa]] limit of **$7,500**. That covers part of the childcare. It does not cover the year.',
}
maria = lesson('fc-maria', 'Maria’s Twins', 'Two credits are not two childcare bills paid.', [
    num('At the full 2026 amount, what is the child tax credit for Maria’s two children?', 4400,
        '$2,200 × 2 = $4,400. Her $85,000 income is under the $200,000 phaseout.'),
    num('Childcare is $1,000 per child per month. What is a month for both?', 2000,
        '$1,000 × 2 = $2,000.'),
    num('What is that childcare for a year?', 24000, '$2,000 × 12 = $24,000.'),
    num('The FSA covers $7,500. How much of the $24,000 is still outside it?', 16500,
        '$24,000 − $7,500 = $16,500.'),
    tf('The $4,400 child tax credit pays the $24,000 childcare bill.', False,
       'The credit is $4,400 at the full amount. Childcare is $24,000. They are not the same pile of money.'),
], fmt='story', story=maria_story)

trial_steps = [
    num('Formula is $90 a month. What is the year?', 1080, '$90 × 12 = $1,080.'),
    num('A 2026 child tax credit at the full amount, for one qualifying child, is how much?', 2200,
        'Up to $2,200, if income is under the phaseout.'),
    mc('Which account is the 2026 work benefit for childcare, up to $7,500 if the plan offers it?',
       ['A dependent care FSA', 'A 529 plan', 'A mortgage escrow'], 0,
       'The FSA is for this year’s care. A 529 is for education later. Escrow pays tax and insurance.'),
    tf('Once you have a child, term life insurance is a savings plan you can spend.', False,
       'It pays a beneficiary if you die during the term.'),
]

lessons = [baby, care, fsa, college, kids, life, family, maria,
           review('fc'), trial('fc', 'Kids & Family Costs', trial_steps)]
write_unit('08-family-costs.json', 'family-costs', 8, 'Kids & Family Costs',
           'The first year, childcare, two 2026 tax benefits, and a policy once someone depends on you.',
           'The credit is not the childcare bill. Count them apart.', terms, lessons, section=S)
