from lib import *

S = 'protecting'
terms = {
    'disability-insurance': term('Disability insurance',
                                 'Insurance that replaces part of your income if an illness or injury keeps you from working.',
                                 'You earn $5,000 a month. A policy that pays 60% would pay $3,000 a month while you qualify.'),
    'umbrella-policy': term('Umbrella policy',
                            'Extra liability coverage that sits on top of your auto or home liability limits when a lawsuit blows past them.',
                            'Auto liability stops at $250,000. A lawsuit is $900,000. An umbrella can cover the $650,000 gap, up to its own limit.'),
}

what = lesson('du-what', 'Income Insurance', 'Your paycheck is the asset. This policy protects it.', [
    mc('What does disability insurance replace?',
       ['Part of your income if you cannot work', 'The market value of your car', 'A life insurance death benefit'], 0,
       'The loss is the paycheck that stops.',
       context='[[Disability insurance]] is income insurance. Work sometimes offers a short version. It is not the same as life insurance, which pays after you die.'),
    tf('If you do not work, disability insurance has a paycheck to replace.', False,
       'No earned income, nothing for this policy to replace.'),
    mc('Why do people skip this and then regret it?',
       ['A long illness is more common than they think, and the paycheck stops anyway', 'The policy pays their rent in cash even when they are healthy', 'It is illegal to buy'], 0,
       'The premium looks optional until the paychecks stop.'),
    num('You earn $4,000 a month. You miss three months of work with no disability coverage and no paid leave. How much pay is missing?', 12000,
        '$4,000 × 3 = $12,000.'),
    fill('Disability insurance protects your ___.',
         ['income', 'luggage', 'credit score'], 0,
         'The bills stay. The paycheck is what this policy stands in for.'),
])

length = lesson('du-length', 'Short Term and Long Term', 'One covers weeks. The other covers the year you did not plan.', [
    mc('Short-term disability is built for:',
       ['A few weeks or months away from work', 'The rest of your life only', 'A cracked phone screen'], 0,
       'It is the bridge. It is not the whole road.',
       context='Short-term coverage often runs for a few months. Long-term coverage can run for years. A job’s plan may offer one, both, or neither.'),
    mc('Long-term disability is built for:',
       ['An illness or injury that keeps you out for a long stretch', 'A three-day cold', 'A parking ticket'], 0,
       'That is the policy that matters if you cannot return this year.'),
    tf('Short-term coverage makes long-term coverage unnecessary.', False,
       'The short policy ends. The long one is what is left.'),
    mc('Your job offers short-term disability at 60% of pay for 12 weeks, and nothing after. What is the hole?',
       ['Any illness that lasts longer than those 12 weeks', 'The first day of a cold', 'Your life insurance beneficiary'], 0,
       'Week 13 is the hole.'),
    num('Short-term pays $600 a week for 12 weeks. What is the most it will pay?', 7200,
        '$600 × 12 = $7,200.'),
])

math = lesson('du-math', 'How Much It Pays', 'It replaces a percent, not the whole paycheck.', [
    num('You earn $5,000 a month. The policy pays 60%. What is the monthly benefit?', 3000,
        '$5,000 × 0.60 = $3,000.',
        context='Read the percent and whose definition of disability the policy uses. Some pay only if you cannot do any job. Others pay if you cannot do your own.'),
    num('What is that benefit for a year?', 36000, '$3,000 × 12 = $36,000.'),
    num('Your old pay for a year was $60,000. How much pay is not replaced?', 24000,
        '$60,000 − $36,000 = $24,000.'),
    tf('A 60% policy pays your full salary.', False,
       'Sixty percent is sixty percent. The other forty still has to come from somewhere.'),
    mc('Why might a policy that covers “your own job” pay when a stricter one would not?',
       ['You cannot do your work, even if you could do some other work', 'It ignores injuries', 'It pays only after you retire'], 0,
       'The definition of disability is the gate. Read it.'),
])

doc_lines = [
    ('benefit', 'Monthly benefit if you qualify', 3000),
    ('prem', 'Premium per month', 45),
]
DOC = doc('statement', 'Disability policy summary', doc_lines, subtitle='Long-term',
          meta=[('Pays', '60% of pay'), ('Waiting period', '90 days'), ('Covers', 'Your own occupation')])
page = lesson('du-page', 'The Benefit Summary', 'Percent, waiting period, and the job test.', [
    num('What is the monthly benefit on this page?', 3000, 'That line says $3,000.',
        context='The waiting period is 90 days. The policy pays nothing during the wait.', doc=DOC),
    num('The premium is $45 a month. What is that per year?', 540, '$45 × 12 = $540.', doc=DOC),
    mc('You are hurt on day 1. When does this summary say benefits can start?',
       ['After the 90-day waiting period', 'The same afternoon', 'After 90 years'], 0,
       'The wait is part of the price. Savings have to cover it.'),
    tf('“Your own occupation” means the policy only pays if every job on earth is impossible.', False,
       'It means your own job. A stricter policy says any job.'),
    num('Three months of waiting, and your pay is $5,000 a month. How much pay is missing before benefits start, if you have no other leave?', 15000,
        '$5,000 × 3 = $15,000.'),
], fmt='document')

umbrella = lesson('du-umbrella', 'Umbrella Coverage', 'When a lawsuit is taller than the policy underneath.', [
    mc('What is an umbrella policy?',
       ['Extra liability coverage above your auto or home limits', 'A policy that replaces health insurance', 'A warranty for umbrellas'], 0,
       'It starts where the other liability limit stops.',
       context='An [[umbrella policy]] needs enough [[liability coverage|liability-coverage]] underneath it. Insurers usually require that floor.'),
    num('Auto liability stops at $250,000. The lawsuit is $900,000. How much is above the auto limit?', 650000,
        '$900,000 − $250,000 = $650,000.'),
    mc('Who looks at an umbrella?',
       ['Someone whose savings or home could be reached by a large lawsuit', 'Someone who wants a cheaper oil change', 'Someone with no car, no home, and no savings'], 0,
       'The umbrella protects what a judgment could take.'),
    tf('An umbrella replaces the need for any auto liability coverage.', False,
       'It sits on top. The insurer will ask for a solid policy underneath.'),
    num('In this example the umbrella premium is $300 a year. Over 10 years, what is that premium?', 3000,
        '$300 × 10 = $3,000. A real quote can differ. The shape is a small premium under a large limit.'),
])

checklist = lesson('du-checklist', 'An Insurance Checklist', 'Name the hole before the year names it for you.', [
    sort('Solid enough for now, or worth a look?',
         ['Solid enough for now', 'Worth a look'],
         [('Health plan in force, and you know the deductible', 0),
          ('Renters or home policy, and you know if flood is excluded', 0),
          ('Auto liability at the state minimum only', 1),
          ('No disability coverage, and you live on your paycheck', 1),
          ('Life insurance through work equal to one year of pay, with a new baby at home', 1)],
         'A minimum, a missing income policy, and a thin life benefit are the looks. A plan you understand can sit.'),
    mc('Why is “auto liability at the state minimum only” worth a look?',
       ['The legal floor is often too small for a serious injury', 'State minimums are the maximum the law allows', 'Minimum policies include umbrella coverage free'], 0,
       'Legal and enough are still different words.'),
    tf('A checklist replaces reading the policy.', False,
       'The checklist tells you which policy to open.'),
    mc('You rent, and you have no renters policy. Where does that land?',
       ['Worth a look. The landlord’s policy is not yours', 'Solid. Renters are covered by the building', 'Solid, if you own a car'], 0,
       'Your belongings and your liability are uninsured until you buy the policy.'),
    fill('The point of the list is to find the ___ before a loss does.',
         ['hole', 'logo', 'slogan'], 0,
         'A named hole can be priced. A surprise cannot.'),
], fmt='sort')

thin_lines = [
    ('health', 'Health premium per month', 90),
    ('rent', 'Renters premium per year', 0),
]
# $0 renters means they don't have it - avoid $0. Use two real sketches differently.
a_lines = [
    ('health', 'Health premium, per year', 1080),
    ('auto', 'Auto liability', 25000),
]
b_lines = [
    ('health', 'Health premium, per year', 1080),
    ('auto', 'Auto liability limit', 250000),
    ('dis', 'Disability benefit, per month', 2400),
]
# Don't compare unequal line counts as if totals match. Call can still show both docs.
SKETCH_A = doc('statement', 'Sketch A', a_lines, subtitle='Health, and a thin auto limit')
SKETCH_B = doc('statement', 'Sketch B', [
    ('health', 'Health premium, per year', 1080),
    ('auto', 'Auto liability limit', 250000),
    ('dis', 'Disability benefit per month', 2400),
], subtitle='Health, higher auto limit, disability')
together = lesson('du-together', 'Putting It Together', 'Look for the hole, not the matching premium.', [
    mc('Both sketches pay $1,080 a year for health insurance. What is Sketch A missing that Sketch B has?',
       ['A higher auto liability limit and a disability benefit', 'A cheaper health premium', 'A life insurance slogan'], 0,
       'The health line matches. The protection does not.',
       context='Same health premium. The rest of the sketch is the decision.',
       docs=[SKETCH_A, SKETCH_B]),
    num('How much higher is Sketch B’s auto liability limit than Sketch A’s $25,000?', 225000,
        '$250,000 − $25,000 = $225,000.', docs=[SKETCH_A, SKETCH_B]),
    mc('You live on your paycheck and Sketch A has no disability benefit. What is the exposed piece?',
       ['Your income if you cannot work', 'The health premium, which is unpaid', 'A death benefit'], 0,
       'The health plan pays doctors. It does not replace the paycheck.'),
    tf('Matching health premiums means the two sketches protect you equally.', False,
       'The auto limit and the disability line are the difference.'),
    mc('Which sketch is the sturdier starting point?',
       ['Sketch B', 'Sketch A', 'They are the same stack'], 0,
       'B raised the liability ceiling and insured the paycheck.',
       why=['Higher liability, plus income coverage.', 'A’s $25,000 limit is the thin one.', 'The health premiums match. The rest does not.']),
], fmt='call')

elena_story = {
    'title': 'The afternoon she reads the stack',
    'character': 'Elena, 38, high school counselor',
    'body': 'Once a year, after her raise, Elena reads the stack. She earns **$60,000**. Her long-term disability policy would pay **60%**, which is **$36,000** a year, or **$3,000** a month, after a **90**-day wait.\n\nHer auto liability limit is **$100,000**. She owns a small condo and has **$40,000** in savings. A serious crash could reach past that limit. She prices an umbrella and writes the date of this review on the folder.',
}
elena = lesson('du-elena', 'Elena’s Yearly Review', 'A raise is a reason to reread the stack.', [
    num('What is 60% of Elena’s $60,000 salary?', 36000, '$60,000 × 0.60 = $36,000.'),
    num('What is that benefit per month?', 3000, '$36,000 ÷ 12 = $3,000.'),
    num('The waiting period is 90 days. About how many months is that?', 3,
        '90 ÷ 30 = 3 months. She needs savings for the wait.', unit='months'),
    mc('Why is a $100,000 auto limit worth a look, given the condo and the savings?',
       ['A lawsuit could reach past $100,000 and into what she owns', 'Condo insurance cancels auto liability', 'Savings make liability unnecessary'], 0,
       'The limit is the ceiling on the insurer. Her condo sits above it.'),
    tf('She can skip the review next year because she did it once.', False,
       'A raise, a baby, a move, or a new car changes the stack.'),
], fmt='story', story=elena_story)

trial_steps = [
    num('Pay is $3,000 a month. Disability pays 50%. What is the monthly benefit?', 1500,
        '$3,000 × 0.50 = $1,500.'),
    mc('An umbrella policy sits where?',
       ['Above the liability limits you already have', 'Instead of health insurance', 'Inside a term life premium'], 0,
       'It is extra liability coverage, not a replacement for the policy under it.'),
    tf('Short-term disability that ends at 12 weeks covers a two-year illness.', False,
       'The short policy ends. The rest needs long-term coverage or savings.'),
    mc('Which gap deserves a look this year?',
       ['No income coverage, and your paycheck pays the rent', 'A health plan whose deductible you already know', 'A renters policy you reread in January'], 0,
       'The missing paycheck is the hole. A plan you understand is not.'),
]

lessons = [what, length, math, page, umbrella, checklist, together, elena,
           review('du'), trial('du', 'Disability & Umbrella', trial_steps)]
write_unit('09-disability-umbrella.json', 'disability-umbrella', 9, 'Disability & Umbrella Coverage',
           'The paycheck if you cannot work, and extra liability if a lawsuit runs past the limit.',
           'Insure the income. Then look at what a lawsuit could reach.', terms, lessons, section=S)
