from lib import *

S = 'taxes'
terms = {
    'tax-deduction': term('Tax deduction',
                          'An amount that lowers the income the tax is figured on. In a 12% bracket, a $1,000 deduction saves $120. It does not save $1,000.',
                          'A $1,000 deduction in the 12% bracket cuts the tax by $120.'),
    'tax-credit': term('Tax credit',
                       'An amount that lowers the tax itself, dollar for dollar. A $1,000 credit saves $1,000, up to the rules for that credit.',
                       'The same $1,000 as a credit saves the whole $1,000, which is $880 more than the deduction.'),
    'itemized-deduction': term('Itemized deduction',
                               'The added-up list of allowed expenses, such as some taxes, mortgage interest, and gifts, used instead of the standard deduction when the list is larger.',
                               'A list that adds to $13,000 loses to the 2026 single standard deduction of $16,100.'),
}

versus = lesson('dd-versus', 'A Deduction or a Credit', 'Same $1,000. Two very different savings.', [
    info('Dollars off the income, or dollars off the tax',
         'A [[tax deduction]] lowers taxable income. In the 12% bracket, **$1,000** of deduction saves **$120**.\n\nA [[tax credit]] lowers the tax. The same **$1,000** credit saves **$1,000**. The credit saves **$880** more.'),
    num('A $1,000 deduction sits in the 12% bracket. How much tax does it save?', 120,
        '$1,000 × 0.12 = $120.'),
    num('A $1,000 credit saves how much tax, before any cap on that credit?', 1000,
        'A credit cuts the tax dollar for dollar. $1,000.'),
    num('How much more does the credit save than the deduction?', 880,
        '$1,000 − $120 = $880.'),
    tf('A $1,000 deduction and a $1,000 credit save the same tax in the 12% bracket.', False,
       'The deduction saves $120. The credit saves $1,000.'),
])

std_doc = doc('statement', '2026 standard deduction, single', [
    ('std', 'Standard deduction', 16100),
])
item_doc = doc('statement', 'Itemized list in this example', [
    ('state', 'State income tax you may count', 5000),
    ('mort', 'Mortgage interest', 6000),
    ('gift', 'Gifts to charity', 2000),
], totals=[('Itemized deductions', 13000, True)])
assert 5000 + 6000 + 2000 == 13000 and 16100 - 13000 == 3100

choose = lesson('dd-choose', 'Standard or Itemized', 'Take the larger one. This list loses.', [
    num('What do the itemized lines add up to?', 13000,
        '$5,000 + $6,000 + $2,000 = $13,000.',
        context='You take the [[standard deduction]] or your [[itemized deduction|itemized-deduction]] list, whichever is larger. These amounts are the ones this example is allowed to count.',
        docs=[std_doc, item_doc]),
    num('How much larger is the 2026 single standard deduction than this list?', 3100,
        '$16,100 − $13,000 = $3,100.', docs=[std_doc, item_doc]),
    mc('Which one lowers taxable income more, on these two pages?',
       ['The $16,100 standard deduction', 'The $13,000 itemized list', 'They lower it by the same amount'], 0,
       'The standard deduction is $3,100 larger.',
       why=['$16,100 beats $13,000.', 'The list is real, and it is still smaller.', 'They differ by $3,100.'],
       docs=[std_doc, item_doc]),
    tf('You add the standard deduction on top of this itemized list.', False,
       'You choose one. Adding both would deduct twice.'),
    fill('Take the standard deduction when it is ___ than the itemized list.',
         ['larger', 'smaller', 'the same tax credit'], 0,
         'Larger. The point of comparing is to keep the bigger subtraction.'),
], fmt='call')

eitc = lesson('dd-eitc', 'The Earned Income Tax Credit', 'A maximum is not your credit.', [
    info('2026, and a warning',
         'For 2026, the maximum [[tax credit|tax-credit]] called the Earned Income Tax Credit is **$8,231** for a taxpayer with three or more qualifying children. Smaller families have smaller maximums. The credit phases out as income rises.\n\nDo not treat $8,231 as the credit for one child, or for every income. The IRS EITC assistant is the way to check a real household.'),
    num('What is the 2026 maximum EITC for three or more qualifying children?', 8231,
        '$8,231. That maximum is not the amount for one child.'),
    mc('Jamal has one qualifying child. What is $8,231 to him?',
       ['The published maximum for a larger family, not a number this lesson assigns him', 'His credit, automatically', 'His standard deduction'], 0,
       'One child is not three or more. He uses the IRS assistant.'),
    tf('Every worker receives the $8,231 maximum in 2026.', False,
       'The maximum is for a specific family size, and income can phase the credit down to nothing.'),
    fill('The tool that checks a real EITC amount is the IRS ___ assistant.',
         ['EITC', 'mileage', 'W-4'], 0,
         'EITC assistant. A lesson should not invent the phaseout.'),
])

ctc = doc('statement', 'One qualifying child, 2026', [
    ('tax', 'Tax before this credit', 2620),
    ('credit', 'Child tax credit at the full amount', 2200),
], subtitle='Income under the 2026 phaseout', note='This page is not the Child and Dependent Care Credit.')
assert 2620 - 2200 == 420

child = lesson('dd-ctc', 'The Child Tax Credit', 'The Section 5 number, still for 2026.', [
    info('Up to $2,200',
         'The [[child tax credit]] is up to **$2,200** per qualifying child for 2026. It starts to shrink above **$200,000** of income, or **$400,000** if married filing jointly.\n\nThis page is a single filer under that line, so the full **$2,200** is in play. It is not the Child and Dependent Care Credit, and it is not a dependent-care FSA.'),
    num('What is the child tax credit on this page?', 2200,
        'The full 2026 amount for one qualifying child, because this income is under the phaseout.', doc=ctc),
    num('Tax before the credit is $2,620. What is the tax after this $2,200 credit?', 420,
        '$2,620 − $2,200 = $420.', doc=ctc),
    tf('This $2,200 is the medical FSA limit.', False,
       'The medical FSA is a different account, with a different limit. This line is the child tax credit.'),
    mc('Whose income, in 2026, is past the start of the phaseout for a single filer?',
       ['Income above $200,000', 'Income of $40,000', 'Income of $85,000'], 0,
       'The shrink starts above $200,000 for a single filer. $40,000 and $85,000 are under it.'),
], fmt='document')

school = lesson('dd-school', 'Education Credits', 'The full American Opportunity amount is $2,500, if you qualify.', [
    info('2026, Form 8863',
         'The American Opportunity Tax Credit is up to **$2,500** per eligible student: **100%** of the first **$2,000** of qualified expenses and **25%** of the next **$2,000**.\n\nFor 2026, the full credit is for modified adjusted gross income of **$80,000** or less if you are single, and it is gone above **$90,000**. Joint filers use **$160,000** and **$180,000**. This lesson does not compute a partial phaseout. The Lifetime Learning Credit is a different credit, up to **$2,000** per return.'),
    num('Qualified expenses are $4,000 and you qualify for the full credit. What is 100% of the first $2,000?', 2000,
        'The first $2,000 counts in full.'),
    num('What is 25% of the next $2,000?', 500, '$2,000 × 0.25 = $500.'),
    num('What is the full American Opportunity credit from those two pieces?', 2500,
        '$2,000 + $500 = $2,500.'),
    tf('A single filer with modified adjusted gross income of $40,000 is over the 2026 line where this credit disappears.', False,
       'It disappears above $90,000 for a single filer. $40,000 is under the $80,000 line for the full credit.'),
])

refundable = lesson('dd-refund', 'Refundable or Not', 'A credit can stop at the tax, or it can pay you past it.', [
    info('Two endings',
         'A nonrefundable credit can cut the tax to zero and then stop. The leftover does not come back.\n\nTax of **$400** and a **$1,000** nonrefundable credit uses **$400**. The other **$600** is lost. A refundable credit of **$1,000** against the same **$400** tax can send that **$600** back. The child tax credit is partly refundable. Do not treat every credit as cash.'),
    num('Tax is $400 and the nonrefundable credit is $1,000. How much of the credit is used?', 400,
        'It can only erase the $400 of tax.'),
    num('How much of that nonrefundable credit does not come back?', 600,
        '$1,000 − $400 = $600.'),
    num('The credit is refundable instead. How much can come back after the $400 tax is erased?', 600,
        '$1,000 − $400 = $600.'),
    tf('Every credit is refundable.', False,
       'A nonrefundable credit stops at the tax. Read the credit before you count on cash back.'),
])

above = lesson('dd-above', 'Without Itemizing', 'Some subtractions happen before the standard deduction.', [
    info('Adjustments',
         'Some [[tax deduction|tax-deduction]] amounts, often called adjustments, come off income before adjusted gross income. You can take them and still take the [[standard deduction]].\n\nIn this example, wages are **$40,000** and a **$1,000** adjustment is allowed. Adjusted gross income is **$39,000**. Taxable income is **$39,000** minus **$16,100**, which is **$22,900**. That is **$1,000** less taxable income than with no adjustment.'),
    num('Wages are $40,000 and the adjustment is $1,000. What is adjusted gross income?', 39000,
        '$40,000 − $1,000 = $39,000.'),
    num('What is taxable income after the $16,100 standard deduction?', 22900,
        '$39,000 − $16,100 = $22,900.'),
    num('Without the adjustment, taxable income was $23,900. How much lower is it now?', 1000,
        '$23,900 − $22,900 = $1,000. The adjustment and the standard deduction both happened.'),
    tf('An adjustment means you must itemize.', False,
       'That is the point of an adjustment. The standard deduction can still come off afterward.'),
])

jamal_story = {
    'title': 'Jamal checks the EITC',
    'character': 'Jamal, 29',
    'body': 'Jamal is 29 and a warehouse lead. He is single. His wages are **$28,000**, and he has one qualifying child.\n\nThe 2026 standard deduction leaves taxable income of **$11,900**. That is inside the 10% bucket, so the income tax before credits is **$1,190**. A **$1,000** [[tax deduction]] would save him **$100**. A **$1,000** [[tax credit]] would save him **$1,000**.\n\nThe **$8,231** EITC maximum is for three or more children. Jamal does not write that number on his return. He uses the IRS EITC assistant.',
}
jamal = lesson('dd-jamal', 'Jamal and the EITC', 'His bracket is 10%. The $8,231 figure is not his.', [
    num('What is Jamal’s taxable income?', 11900, '$28,000 − $16,100 = $11,900.'),
    num('What is 10% of that $11,900, the tax before credits?', 1190, '$11,900 × 0.10 = $1,190.'),
    num('A $1,000 deduction in his 10% bucket saves how much?', 100, '$1,000 × 0.10 = $100.'),
    mc('What should Jamal do with the EITC?',
       ['Use the IRS EITC assistant', 'Claim the $8,231 maximum for three or more children', 'Skip it because he is in the 10% bracket'], 0,
       'One child is not the three-child maximum. The assistant handles the phaseout.'),
    tf('Jamal’s $11,900 of taxable income has reached the 12% bracket.', False,
       'The 12% bracket starts above $12,400. He is $500 under that line. $12,400 − $11,900 = $500.'),
], fmt='story', story=jamal_story)

trial_steps = [
    num('A $2,000 deduction is in the 22% bracket. How much tax does it save?', 440, '$2,000 × 0.22 = $440.'),
    num('Itemized deductions in an example are $9,000. The 2026 single standard deduction is $16,100. How much larger is the standard deduction?', 7100,
        '$16,100 − $9,000 = $7,100.'),
    tf('The 2026 child tax credit maximum in this course is $2,200 per qualifying child.', True,
       'That is the 2026 amount, and it shrinks above the income lines you already learned.'),
    mc('A $500 nonrefundable credit meets a $200 tax. How much of the credit can be refunded?',
       ['$0', '$300', '$500'], 0,
       'Nonrefundable means the leftover $300 does not come back. The credit used is $200.'),
]

lessons = [versus, choose, eitc, child, school, refundable, above, jamal,
           review('dd'), trial('dd', 'Deductions & Credits', trial_steps)]
write_unit('04-deductions-credits.json', 'deductions-credits', 4, 'Deductions & Credits',
           'A deduction shrinks income. A credit shrinks the tax. The larger subtraction wins.',
           'A credit is not a deduction with a nicer name.', terms, lessons, section=S)
