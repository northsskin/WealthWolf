from lib import *

S = 'taxes'
terms = {
    'adjusted-gross-income': term('Adjusted gross income',
                                  'Gross income minus a short list of adjustments, such as some retirement contributions. The standard deduction comes off after this, not before.',
                                  'Wages of $40,000 and a $1,000 adjustment leave an adjusted gross income of $39,000.'),
    'standard-deduction': term('Standard deduction',
                               'A set amount the IRS lets you subtract from income before the tax is figured. For 2026 it is $16,100 if you are single.',
                               'Wages of $40,000 minus the $16,100 standard deduction leave $23,900 of taxable income.'),
    'tax-bracket': term('Tax bracket',
                        'A bucket for a slice of taxable income. Each slice has its own rate. A higher bracket does not re-tax the earlier slices.',
                        'In 2026, a single filer’s first $12,400 of taxable income is taxed at 10%. The next dollars, up to $50,400, are taxed at 12%.'),
}

path = lesson('tx-path', 'From Pay to Taxable Income', 'Three stops. The tax is figured on the last one.', [
    info('Not tax advice',
         'This unit teaches how the federal income tax is built. It is education, not advice for your return. For free help, start at IRS Free File and VITA on irs.gov.\n\nGross income is the top. Adjustments come off next. What remains is [[adjusted gross income]]. Then the [[standard deduction]] comes off. What remains is taxable income.'),
    order('Put the path in order.',
          ['Start with gross income',
           'Subtract adjustments to get adjusted gross income',
           'Subtract the standard deduction or itemized deductions',
           'The result is taxable income'],
          'The deduction comes after adjusted gross income. The tax is figured on taxable income, not on the gross pay.'),
    num('Wages are $40,000 and there are no adjustments. Adjusted gross income is the same $40,000. The 2026 standard deduction for a single filer is $16,100. What is taxable income?', 23900,
        '$40,000 − $16,100 = $23,900.'),
    mc('Which amount is the tax actually figured on, in this path?',
       ['Taxable income', 'Gross income', 'The standard deduction'], 0,
       'Gross income is the start. Taxable income is the end, after the deduction.'),
    tf('The standard deduction is subtracted before adjusted gross income.', False,
       'Adjustments come first. The standard deduction comes off adjusted gross income.'),
])

deduction = lesson('tx-deduction', 'The 2026 Standard Deduction', 'One number, labeled by filing status.', [
    info('Single, for this course',
         'For 2026, the [[standard deduction]] is **$16,100** if you are single or married filing separately, **$32,200** if you are married filing jointly, and **$24,150** if you are head of household.\n\nThe worked examples here are a single filer. Itemizing is a later unit.'),
    num('What is the 2026 standard deduction for a single filer?', 16100,
        '$16,100. That is the 2026 amount for single filers and for married filing separately.'),
    num('A single filer’s adjusted gross income is $50,000. What is taxable income after the $16,100 deduction?', 33900,
        '$50,000 − $16,100 = $33,900.'),
    num('What is the 2026 standard deduction for a married couple filing jointly?', 32200,
        '$32,200 for 2026.'),
    tf('The 2026 single standard deduction is $16,100 for every filing status.', False,
       'Joint filers get $32,200 in 2026. Heads of household get $24,150.'),
])

brackets = lesson('tx-brackets', 'Brackets Are Buckets', 'Only the dollars in a bucket pay that bucket’s rate.', [
    info('2026, single',
         'A [[tax bracket]] is a bucket. For a single filer in 2026, the first **$12,400** of taxable income is taxed at **10%**. That is **$1,240**.\n\nThe next dollars, until taxable income reaches **$50,400**, are taxed at **12%**. The 22% bucket starts above $50,400. It does not reach back.'),
    num('What is 10% of the first $12,400 of taxable income?', 1240, '$12,400 × 0.10 = $1,240.'),
    num('A $1,000 slice sits in the 12% bucket. How much tax does that slice add?', 120, '$1,000 × 0.12 = $120.'),
    tf('The 22% bracket taxes your first dollar of taxable income at 22%.', False,
       'The first $12,400 is still in the 10% bucket. The 22% rate starts above $50,400 of taxable income.'),
    fill('A bracket taxes the dollars ___ that bucket, not the dollars in the earlier ones.',
         ['inside', 'above', 'before'], 0,
         'Inside the bucket. Earlier dollars keep their own rates.'),
])

rates = lesson('tx-rates', 'Marginal and Effective', 'The last dollar’s rate is not the rate on the whole pile.', [
    info('Two different rates',
         'The marginal rate is the rate on your next dollar. In the single example, taxable income is **$23,900**, so the next dollar is in the **12%** bucket.\n\nThe tax is not 12% of the whole $23,900. The first **$12,400** is taxed at 10% (**$1,240**). The other **$11,500** is taxed at 12% (**$1,380**). The bill is **$2,620**.'),
    num('Taxable income is $23,900. How much of it is above the $12,400 bucket?', 11500,
        '$23,900 − $12,400 = $11,500.'),
    num('What is 12% of that $11,500?', 1380, '$11,500 × 0.12 = $1,380.'),
    num('Add the $1,240 from the 10% bucket. What is the federal income tax?', 2620,
        '$1,240 + $1,380 = $2,620.'),
    num('12% of the whole $23,900 would be $2,868. How much more is that than the real $2,620?', 248,
        '$2,868 − $2,620 = $248. The real bill is lower because the first bucket is 10%.'),
])

myth = lesson('tx-myth', 'A Raise and a Bracket', 'The bracket does not take the raise back. A credit phaseout can.', [
    info('The myth, cut in half',
         'Moving into a higher [[tax bracket]] does not tax your old dollars at the new rate. A **$1,000** raise that stays in the 12% bucket adds **$120** of federal income tax, and **$880** is still yours.\n\nThat is only the bracket. A credit that shrinks as income rises can still cut a refund. The bracket did not do that. The phaseout did.'),
    tf('Moving into the 12% bracket taxes all $23,900 of taxable income at 12%.', False,
       'Only the dollars above $12,400 are taxed at 12%. The first bucket stays at 10%.'),
    num('A $1,000 raise stays in the 12% bucket. How much federal income tax does that $1,000 add?', 120,
        '$1,000 × 0.12 = $120.'),
    num('How much of that $1,000 is left after that $120 of federal income tax?', 880,
        '$1,000 − $120 = $880.'),
    tf('A credit that phases out can shrink a refund even when the bracket taxed only the new dollars.', True,
       'The bracket and the phaseout are different. This lesson’s “no” is about the bracket alone.'),
])

which = lesson('tx-which', 'Federal, State, FICA', 'Three different taxes can leave the same paycheck.', [
    info('Do not mix the jars',
         'Federal income tax uses the brackets and the [[standard deduction]]. A state may charge its own tax on wages. [[FICA]] is Social Security and Medicare.\n\nA refund of federal income tax does not refund the FICA.'),
    sort('Sort each tax.',
         ['Federal income tax', 'State income tax', 'FICA'],
         [('The brackets and the standard deduction', 0),
          ('A tax your state may charge on wages', 1),
          ('Social Security and Medicare', 2),
          ('The income tax on Form 1040', 0)],
         'Form 1040 is the federal income tax. FICA is the payroll tax. The state is a third bill.'),
    mc('You get a federal income-tax refund. What does that refund not return?',
       ['The FICA that was withheld', 'Any federal income tax that was over-withheld', 'Money the IRS owes you from that income tax'], 0,
       'FICA is a different tax. The refund is about the income tax.'),
    tf('FICA uses the same brackets as the federal income tax.', False,
       'FICA is a payroll tax. The brackets belong to the income tax.'),
    fill('Social Security and Medicare are ___.',
         ['FICA', 'the standard deduction', 'a state tax'], 0,
         'FICA. You already met it on the paycheck.'),
], fmt='sort')

bill = doc('statement', 'Federal income tax, single, 2026', [
    ('ten', 'Tax on the first $12,400 at 10%', 1240),
    ('twelve', 'Tax on the next $11,500 at 12%', 1380),
], subtitle='Taxable income $23,900', meta=['Wages $40,000', 'Standard deduction $16,100'],
   totals=[('Federal income tax', 2620, True)])
assert 1240 + 1380 == 2620 and 40000 - 16100 == 23900 and 23900 - 12400 == 11500

page = lesson('tx-bill', 'The Bill on One Page', 'Two slices. One tax.', [
    info('Read the slices',
         'This page is the single-filer example. Wages **$40,000**. The 2026 [[standard deduction]] is **$16,100**. Taxable income is **$23,900**.\n\nThe tax is the two slices added together.'),
    num('What is the federal income tax on this page?', 2620,
        '$1,240 + $1,380 = $2,620.', doc=bill),
    num('Withholding on this return is $3,000. How much is the refund?', 380,
        '$3,000 − $2,620 = $380.', doc=bill),
    mc('Why is the tax not 12% of the whole $23,900?',
       ['The first $12,400 was taxed at 10%', 'The IRS waives the first bracket', 'Withholding replaces the brackets'], 0,
       'The 12% slice is only the $11,500 above $12,400.'),
    tf('The $380 refund means the taxable income was wrong.', False,
       'The tax is $2,620. Withholding was $3,000. The extra $380 comes back.'),
], fmt='document')

ana_story = {
    'title': 'Ana’s first bill',
    'character': 'Ana, 27',
    'body': 'Ana is 27. She is a medical receptionist, single, and her [[W-2|w-2]] wages are **$40,000**. She takes the 2026 [[standard deduction]] of **$16,100**.\n\nTaxable income is **$23,900**. The first **$12,400** is taxed at 10%, which is **$1,240**. The other **$11,500** is taxed at 12%, which is **$1,380**. The bill is **$2,620**.\n\nHer employer withheld **$3,000** of federal income tax. The refund is **$380**. This is a lesson, not a return. If she wants free help, she starts at IRS Free File or VITA.',
}
ana = lesson('tx-ana', 'Ana’s First Bill', 'The refund is the withholding minus the tax.', [
    num('What is Ana’s 2026 taxable income?', 23900, '$40,000 − $16,100 = $23,900.'),
    num('What is her federal income tax?', 2620, '$1,240 + $1,380 = $2,620.'),
    num('Withholding is $3,000. What is her refund?', 380, '$3,000 − $2,620 = $380.'),
    mc('Her next dollar of taxable income is taxed at which rate?',
       ['12%', '10%', '22%'], 0,
       'Taxable income of $23,900 is above $12,400 and below $50,400, so the next dollar is in the 12% bucket.'),
    tf('The $380 refund means her whole $40,000 was taxed at 12%.', False,
       'The tax was $2,620, built from a 10% slice and a 12% slice. The refund is extra withholding.'),
], fmt='story', story=ana_story)

trial_steps = [
    num('A single filer’s adjusted gross income is $30,000. The 2026 standard deduction is $16,100. What is taxable income?', 13900,
        '$30,000 − $16,100 = $13,900.'),
    mc('Which rate applies to a single filer’s first $12,400 of taxable income in 2026?',
       ['10%', '12%', '22%'], 0,
       'The first bucket is 10%. The 12% bucket starts after that.'),
    tf('A higher bracket re-taxes every earlier dollar at the new rate.', False,
       'Each bucket keeps its own rate.'),
    num('Tax is $2,000 and federal income tax withheld is $2,450. What is the refund?', 450,
        '$2,450 − $2,000 = $450.'),
]

lessons = [path, deduction, brackets, rates, myth, which, page, ana,
           review('tx'), trial('tx', 'How Income Tax Works', trial_steps)]
write_unit('01-income-tax.json', 'income-tax', 1, 'How Income Tax Works',
           'Gross income, the 2026 standard deduction, and brackets that do not reach backward.',
           'The bracket taxes the next dollar. It does not reopen the earlier ones.', terms, lessons, section=S)
