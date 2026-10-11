from lib import *

S = 'protecting'
terms = {
    'term-life': term('Term life insurance',
                      'Life insurance that pays if you die during a set period, such as 20 years. It is insurance, not an investment account.',
                      'A 20-year term policy for $500,000 might cost $25 a month. If you outlive the term, it does not pay.'),
    'whole-life': term('Whole life insurance',
                       'Life insurance meant to last your whole life, with a savings piece inside. The premium is much higher than term for the same death benefit.',
                       'The same $500,000 might cost $220 a month as whole life. Most of the extra premium is the savings piece and the lifetime promise.'),
    'beneficiary': term('Beneficiary',
                        'The person, or people, who receive the life insurance money if you die.',
                        'You name your sister. If you die while the policy is in force, she receives the death benefit, not your email provider.'),
}

who = lesson('li-who', 'Who Needs Life Insurance', 'Insure the paycheck someone else depends on.', [
    mc('Who has the clearest reason to buy life insurance?',
       ['A parent whose income pays the rent', 'A single adult no one relies on for money', 'A person who wants a fancy savings slogan'], 0,
       'The question is who would be short of money if you died.',
       context='Life insurance pays a death benefit to the people who lose your income. [[Term life insurance|term-life]] is the usual way to buy a large benefit for a set number of years.'),
    tf('Life insurance is a good fit when no person and no debt depends on your income.', False,
       'If nobody is harmed financially by your death, the premium has little to protect.'),
    mc('A stay-at-home parent provides childcare that would cost money to replace. Do they have a reason to be insured?',
       ['Yes. Replacing that care costs real money', 'No. Only paychecks count', 'No. Children cannot be beneficiaries'], 0,
       'The loss is the cost of replacing the care, not only a W-2.'),
    mc('What is the death benefit?',
       ['The amount paid if you die while the policy is in force', 'The monthly premium', 'A bonus for staying healthy'], 0,
       'That check is the point of the policy.'),
    fill('Buy life insurance to protect people who ___ your income or your care.',
         ['depend on', 'compete with', 'insure'], 0,
         'No dependent, no job for this policy.'),
])

term_lines = [
    ('ben', 'Death benefit', 500000),
    ('prem', 'Premium per month', 25),
]
whole_lines = [
    ('ben', 'Death benefit', 500000),
    ('prem', 'Premium per month', 220),
]
assert 25 * 12 == 300 and 220 * 12 == 2640 and 2640 - 300 == 2340
TERM = doc('statement', 'Term quote', term_lines, subtitle='20 years')
WHOLE = doc('statement', 'Whole life quote', whole_lines, subtitle='Lifetime, with a savings piece')
compare = lesson('li-compare', 'Term or Whole Life', 'Same death benefit. A very different price.', [
    num('What is the term quote per year?', 300, '$25 × 12 = $300.',
        context='[[Term life insurance|term-life]] covers a period. [[Whole life insurance|whole-life]] is priced to last, and to carry savings.',
        docs=[TERM, WHOLE]),
    num('What is the whole life quote per year?', 2640, '$220 × 12 = $2,640.', docs=[TERM, WHOLE]),
    num('How much more is whole life per year, for the same $500,000?', 2340,
        '$2,640 − $300 = $2,340.', docs=[TERM, WHOLE]),
    mc('You want a large benefit while your kids are growing up, and you will invest the rest yourself. Which quote fits?',
       ['The term quote', 'The whole life quote', 'Neither. The benefits differ'], 0,
       'Term buys the $500,000 for $300 a year. The extra $2,340 is not more death benefit.',
       why=['Same $500,000, far less premium.', 'Whole life costs $2,340 more for the same benefit.', 'Both quotes say $500,000.']),
    tf('Whole life is more expensive because it pays a larger death benefit in this pair of quotes.', False,
       'Both say $500,000. The price difference is the lifetime design and the savings piece.'),
], fmt='call')

much = lesson('li-much', 'How Much', 'A plain estimate: years of income the household would lose.', [
    info('A rough replacement',
         'A common starting point is several years of the income your household would lose. Ten years is a simple sketch, not a personal plan.\n\nIf you earn **$50,000** a year, ten years is **$500,000**. Debts, a partner’s income, and savings move that number.'),
    num('Ten years of a $50,000 income. What is that sketch?', 500000, '$50,000 × 10 = $500,000.'),
    num('You earn $40,000. Ten years. What is the sketch?', 400000, '$40,000 × 10 = $400,000.'),
    num('The sketch is $400,000 and you already have $50,000 in life insurance through work. How much is the gap?', 350000,
        '$400,000 − $50,000 = $350,000.'),
    tf('The ten-year sketch is a personal order you must follow.', False,
       'It is a starting sketch. A partner’s paycheck or a paid-off home can shrink it.'),
])

page_lines = [
    ('ben', 'Death benefit', 500000),
    ('years', 'Term length, shown as the premium for 20 years at $300 a year', 300),
    ('prem', 'Premium for the year', 300),
]
# Avoid a fake "years" money line. Redo.
page_lines = [
    ('ben', 'Death benefit', 500000),
    ('prem', 'Premium for the year', 300),
]
PAGE = doc('statement', 'Term policy', page_lines, subtitle='20-year term',
           meta=[('Beneficiary', 'Your sister'), ('Term', '20 years')])
page = lesson('li-page', 'The Policy Page', 'Benefit, price, term, and the name of the person who is paid.', [
    num('What death benefit does this policy page list?', 500000, 'That line is $500,000.',
        context='The page should name the [[beneficiary]]: the person who receives the money.', doc=PAGE),
    num('What yearly premium does this policy page list?', 300, 'That line is $300.', doc=PAGE),
    mc('Who receives the money if you die while this policy is in force?',
       ['The beneficiary named on the policy', 'Whoever finds the paper', 'The insurer’s shareholders'], 0,
       'The name on the policy is the instruction.'),
    tf('A 20-year term pays the death benefit if you die in year 25.', False,
       'The term ended. Outliving it means no payout, which is what you hope for.'),
    mc('Why write the beneficiary down instead of assuming the family will sort it out?',
       ['The policy pays the name it has, not the argument that follows', 'Insurers ignore the form', 'A will always overrides every beneficiary'], 0,
       'The form is the instruction the insurer follows.'),
], fmt='document')

ben = lesson('li-beneficiary', 'Beneficiaries', 'The form is the will for this one check.', [
    mc('What is a beneficiary?',
       ['The person you name to receive the death benefit', 'The agent who sold the policy', 'The hospital'], 0,
       'No name, and the money waits on a process your family did not need.',
       context='Keep the [[beneficiary]] current. A divorce, a baby, or a death can make the old name wrong.'),
    tf('Naming your beneficiary once, at age 22, is enough for life.', False,
       'Life changes. The form does not update itself.'),
    mc('You have a baby and the beneficiary is still a parent who has died. What do you do?',
       ['Update the form', 'Wait for the insurer to notice', 'Cancel the policy'], 0,
       'A dead beneficiary sends the money into a slower process.'),
    mc('You want your partner and your sibling to split the benefit. What does the form need?',
       ['Both names, and the share each one gets', 'Only a nickname', 'The word family'], 0,
       'Shares should add to the whole. Write the percents.'),
    num('You leave 60% to your partner and 40% to your sibling. What do the shares add up to?', 100,
        '60% + 40% = 100%.', unit='%'),
])

work = lesson('li-work', 'Coverage Through Work', 'It is a start. It leaves when the job does.', [
    mc('What is the usual limit of life insurance you get at work?',
       ['It often ends when the job ends, and the benefit can be small', 'It follows you for life at the same price', 'It replaces a term policy dollar for dollar, always'], 0,
       'A job change can take the coverage with it.',
       context='Work coverage is often one or two times your salary. [[COBRA|cobra]] is about health insurance after a job ends, not a promise that the life policy stays.'),
    num('Your salary is $50,000. Work life insurance is one times salary. What is the benefit?', 50000,
        '$50,000 × 1 = $50,000.'),
    num('Your ten-year sketch is $500,000. How much of that sketch is missing?', 450000,
        '$500,000 − $50,000 = $450,000.'),
    tf('Quitting the job keeps that work policy in force at no cost.', False,
       'The policy belonged to the job. Ask what, if anything, you can take with you, and at what price.'),
    mc('Why not rely on the work policy alone while you have young kids?',
       ['The benefit is often only a year or two of pay, and it can end with the job', 'Work policies are illegal', 'Kids cannot be protected by any policy'], 0,
       'One year of pay is a thin bridge.'),
])

whyterm = lesson('li-why-term', 'Why Most People Choose Term', 'Buy the protection. Invest the difference on purpose.', [
    mc('Why do many people choose term instead of whole life?',
       ['Term buys a large benefit for a small premium during the years people depend on you', 'Term pays a larger death benefit for the same premium in the quotes we used', 'Whole life is illegal'], 0,
       'The expensive years are the years with kids or a big debt. Term covers those years.'),
    num('Term is $300 a year. Whole life is $2,640. How much is left each year if you buy term instead?', 2340,
        '$2,640 − $300 = $2,340.'),
    tf('That $2,340 is automatically a better investment if you spend it.', False,
       'The difference only helps if you actually save or invest it. Spending it buys neither insurance nor savings.'),
    mc('You have no dependents and no co-signed debt. What is a reasonable conclusion?',
       ['You may not need life insurance right now', 'You must buy whole life', 'You must buy the largest term sold'], 0,
       'The product protects a person. No person, no purchase required.'),
    fill('Term covers a ___ of years, not your whole life by default.',
         ['set number', 'random', 'secret'], 0,
         'When the term ends, so does the coverage.'),
])

aisha_story = {
    'title': 'A paycheck and a new baby',
    'character': 'Aisha, 31, clinic receptionist',
    'body': 'Aisha’s baby is three months old. She earns **$4,000** a month, **$48,000** a year. Her partner works too, but the rent still needs her paycheck. Work gives her life insurance equal to one year of pay, **$48,000**.\n\nA ten-year sketch of her income is **$480,000**. A 20-year term quote for that amount is **$28** a month.',
}
aisha = lesson('li-aisha', 'Aisha and Her New Baby', 'One year of pay is not ten.', [
    num('What is ten years of Aisha’s $48,000 income?', 480000, '$48,000 × 10 = $480,000.'),
    num('How much of that sketch does the work policy already cover?', 48000,
        'One year of pay is $48,000.'),
    num('How big is the gap?', 432000, '$480,000 − $48,000 = $432,000.'),
    num('The term quote is $28 a month. What is that per year?', 336, '$28 × 12 = $336.'),
    mc('What is the sensible shape of her next step?',
       ['Price a term policy for the gap, and name the baby’s other parent as beneficiary', 'Buy whole life because a baby means the expensive product', 'Drop the work policy and stay uninsured'], 0,
       'The gap is the uncovered years. Term is built for a gap with an end date.'),
], fmt='story', story=aisha_story)

trial_steps = [
    mc('Life insurance is most useful when:',
       ['Someone depends on your income', 'You want a logo on a folder', 'You have no dependents and no shared debts'], 0,
       'The benefit replaces what those people would lose.'),
    num('Term premium $40 a month. What is the yearly premium?', 480, '$40 × 12 = $480.'),
    tf('A work life policy of one times salary usually equals a ten-year income sketch.', False,
       'One times salary is one year, not ten.'),
    mc('Who should you name on the policy?',
       ['The beneficiary who should receive the money', 'Whoever sold it', 'No one. The form is optional'], 0,
       'The name is the instruction.'),
]

lessons = [who, compare, much, page, ben, work, whyterm, aisha,
           review('li'), trial('li', 'Life Insurance', trial_steps)]
write_unit('08-life-insurance.json', 'life-insurance', 8, 'Life Insurance',
           'Term, whole life, and the years of income a household would lose.',
           'Insure the paycheck. Do not insure a slogan.', terms, lessons, section=S)
