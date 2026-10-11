from lib import *

S = 'protecting'
terms = {
    'in-network': term('In network',
                       'A doctor, hospital, or pharmacy that has a price deal with your health plan. Care there costs you less.',
                       'An in-network MRI is priced at $600 for your plan. The same scan out of network is billed at $1,900.'),
    'hmo': term('HMO',
                'A health plan that asks you to use its network and pick a primary doctor, who refers you to specialists. Premiums are often lower.',
                'Your HMO covers the dermatologist after your primary doctor sends a referral.'),
    'ppo': term('PPO',
                'A health plan with a larger network that lets you see specialists without a referral, and pays some out-of-network care. Premiums are often higher.',
                'With a PPO you book the dermatologist yourself, no referral needed.'),
    'copay': term('Copay',
                  'A fixed amount you pay for a visit or a prescription. The plan pays the rest of its allowed price.',
                  'A $40 copay at the clinic. The visit’s allowed price is $180. You pay $40.'),
    'coinsurance': term('Coinsurance',
                        'Your share of a covered bill, as a percent, after the deductible is met.',
                        'The deductible is met. The bill left is $1,000. At 20% coinsurance you pay $200.'),
    'out-of-pocket-maximum': term('Out-of-pocket maximum',
                                  'The most you pay in a year for covered, in-network care. After that, the plan pays 100% of covered costs.',
                                  'A $5,000 maximum. Once you have paid $5,000 of deductibles, copays, and coinsurance, covered care costs you $0 for the rest of the year.'),
    'special-enrollment': term('Special enrollment',
                               'A limited window, generally 60 days, to buy or change health coverage after a qualifying event such as losing other coverage, moving, marrying, or having a baby.',
                               'You lose a job’s health plan on March 1. You generally have 60 days to enroll, instead of waiting for the yearly window.'),
}

price = lesson('hl-price', 'Premium and Deductible', 'One is the yearly ticket. The other is the first part of a bill.', [
    mc('On a health plan, the premium is:',
       ['What you pay to keep the plan active', 'The first part of each hospital bill', 'A percent of every bill after the deductible'], 0,
       'You pay it in quiet months too.',
       context='A health [[premium]] keeps the plan on. The [[deductible]] is what you pay on covered care before the plan shares the bill.'),
    num('The premium is $150 a month. What is that for a year?', 1800, '$150 × 12 = $1,800.'),
    num('Your deductible is $1,500 and you have paid $400 of it. How much deductible is left?', 1100,
        '$1,500 − $400 = $1,100.'),
    tf('A year with no doctor visits refunds the premium.', False,
       'The premium bought the plan. It is not a deposit.'),
    fill('The deductible is the part of a covered bill you pay ___.',
         ['first', 'last', 'every month'], 0,
         'Then coinsurance or a copay can take a turn.'),
])

share = lesson('hl-share', 'Copay and Coinsurance', 'One is a flat fee. The other is a percent.', [
    mc('What is a copay?',
       ['A fixed dollar amount for a visit or a prescription', 'A percent of the hospital bill', 'The yearly premium'], 0,
       'The number does not change with the size of that visit.',
       context='A [[copay]] is flat. [[Coinsurance]] is a percent after the deductible.'),
    num('The clinic’s allowed price is $180. Your copay is $40. How much do you pay for that visit?', 40,
        'A copay is the fixed $40, not a slice of the $180.'),
    num('The deductible is already met. Coinsurance is 20% of $1,000. How much do you pay?', 200,
        '$1,000 × 0.20 = $200.'),
    num('How much does the plan pay of that $1,000?', 800, '$1,000 − $200 = $800.'),
    tf('Coinsurance is a second premium you pay every month.', False,
       'It shows up on a bill, after the deductible, not on the monthly premium.'),
])

er = lesson('hl-er', 'One ER Visit', 'Deductible first. Then the percent. Then the yearly cap.', [
    info('The bill, in order',
         'This plan’s ER has no copay. The deductible is **$1,500** and none of it is met. Coinsurance is **20%** after that. The out-of-pocket maximum is **$5,000**.\n\nThe bill is **$2,500**.'),
    num('How much of the $2,500 goes to the deductible?', 1500,
        'The whole $1,500 deductible is still open.',
        context='An [[out-of-pocket maximum]] caps what you pay in a year for covered, in-network care.'),
    num('Coinsurance applies to the other $1,000. At 20%, how much is that?', 200,
        '$1,000 × 0.20 = $200.'),
    num('How much do you pay in total for this visit?', 1700, '$1,500 + $200 = $1,700.'),
    num('The out-of-pocket maximum is $5,000. After this $1,700, how much room is left before the plan pays covered care in full?', 3300,
        '$5,000 − $1,700 = $3,300.'),
    tf('Once you hit the out-of-pocket maximum, the plan pays 100% of covered in-network care for the rest of that year.', True,
       'That is the cap. It does not include the premium, and it does not include care the plan never covered.'),
])

sum_lines = [
    ('prem', 'Premium for the year', 2400),
    ('ded', 'Deductible', 1500),
    ('oop', 'Out-of-pocket maximum', 5000),
    ('copay', 'Office-visit copay', 40),
]
SUM = doc('statement', 'Health plan summary', sum_lines, subtitle='In-network',
          meta=[('Coinsurance', '20% after deductible'), ('Network', 'In-network figures only')])
summary = lesson('hl-summary', 'A Plan Summary', 'Four numbers. Do not mix them up.', [
    num('What is the yearly premium?', 2400, 'That line is $2,400.',
        context='The summary is the cover. The network note matters as much as the dollars.', doc=SUM),
    num('What is the office-visit copay?', 40, 'That line is $40.', doc=SUM),
    num('What is the out-of-pocket maximum?', 5000, 'That line is $5,000.', doc=SUM),
    mc('Which number do you pay even if you never see a doctor?',
       ['The $2,400 premium', 'The $40 copay', 'The $5,000 maximum'], 0,
       'The premium is the ticket. The copay is a visit. The maximum is the yearly cap.'),
    tf('These dollar figures apply to every out-of-network doctor automatically.', False,
       'The page says in-network. Out of network is a different, usually worse, set of numbers.'),
], fmt='document')

network = lesson('hl-network', 'In Network or Out', 'The same doctor can be a bargain or a surprise.', [
    mc('What does in-network mean?',
       ['The doctor or hospital has a deal with your plan', 'The doctor is the closest one to your house', 'The visit is free'], 0,
       'The deal is why the allowed price is lower.',
       context='[[In-network|in-network]] care uses the plan’s prices. Out-of-network care often costs you more, and it may not count toward the [[out-of-pocket maximum]].'),
    tf('Going out of network usually costs the same as staying in.', False,
       'The plan’s deal stops at the edge of the network.'),
    mc('You need a specialist. What do you check before the visit?',
       ['That they are in network for this plan', 'That they have good online reviews', 'That their office is close to home'], 0,
       'A great doctor can still be an out-of-network bill.'),
    mc('Before a planned surgery at an in-network hospital, you are handed a form agreeing to pay out-of-network prices for one doctor. What does signing it do?',
       ['It can give up your protection from a surprise out-of-network bill', 'Nothing. In-network hospitals can never bill out-of-network prices', 'It lowers your deductible for the surgery'], 0,
       'Since 2022, the No Surprises Act protects you from most surprise out-of-network bills at in-network hospitals, and in emergencies. Signing that form can waive it.',
       why=['', 'They can, if you agree in writing. That is what the form is for.', 'The form is about price, not your deductible.']),
    fill('Care with a doctor who has a deal with your plan is ___.',
         ['in network', 'a deductible', 'a premium'], 0,
         'That deal is the discount.'),
])

plansort = lesson('hl-sort', 'HMO or PPO', 'One plan wants a home base. The other lets you roam.', [
    sort('Which setup is this?',
         ['HMO', 'PPO'],
         [('You pick a primary doctor and get referrals to specialists', 0),
          ('You can see a specialist without a referral', 1),
          ('The network is usually smaller and the premium often lower', 0),
          ('The network is usually larger and the premium often higher', 1),
          ('Out-of-network care is rarely covered, except emergencies', 0)],
         'An HMO is a tighter list and a home doctor. A PPO costs more and lets you move around.',
         context='An [[HMO]] wants a home doctor and a tighter network. A [[PPO]] costs more and lets you roam. Emergencies are covered either way.'),
    mc('You want to see a dermatologist without asking a primary doctor first. Which shape fits?',
       ['PPO', 'HMO', 'Either. Both need a referral'], 0,
       'The PPO is the one that skips the referral.'),
    tf('An HMO and a PPO always charge the same premium.', False,
       'The PPO’s extra freedom is usually not free.'),
    mc('You rarely leave one clinic and you want a lower premium. Which shape is built for that?',
       ['HMO', 'PPO', 'A policy with no network at all'], 0,
       'A smaller list is the HMO’s bargain.'),
    fill('An HMO usually asks you to start with a ___ doctor.',
         ['primary', 'specialist', 'out-of-network'], 0,
         'That doctor is the front door.'),
], fmt='sort')

a_lines = [
    ('prem', 'Premium per month', 240),
    ('ded', 'Deductible', 500),
]
b_lines = [
    ('prem', 'Premium per month', 90),
    ('ded', 'Deductible', 3000),
]
assert 240 * 12 == 2880 and 90 * 12 == 1080 and 2880 - 1080 == 1800
PLAN_A = doc('statement', 'Plan A', a_lines, subtitle='Lower deductible')
PLAN_B = doc('statement', 'Plan B', b_lines, subtitle='Lower premium')
choose = lesson('hl-choose', 'Two Plans', 'A quiet year and a sick year pick different winners.', [
    num('What is Plan A’s premium for a year?', 2880, '$240 × 12 = $2,880.',
        context='Same coinsurance. The premium and the deductible are the contrast.',
        docs=[PLAN_A, PLAN_B]),
    num('What is Plan B’s premium for a year?', 1080, '$90 × 12 = $1,080.', docs=[PLAN_A, PLAN_B]),
    num('How much more premium does Plan A cost per year?', 1800, '$2,880 − $1,080 = $1,800.',
        docs=[PLAN_A, PLAN_B]),
    mc('You expect almost no care. Which plan costs less if that comes true?',
       ['Plan B', 'Plan A', 'They match'], 0,
       'With no bills you pay the premium. $1,080 is less than $2,880.'),
    mc('You expect a large bill and you want the smaller deductible. Which plan is that?',
       ['Plan A', 'Plan B', 'Neither has a deductible'], 0,
       'A’s deductible is $500. B’s is $3,000.',
       why=['$500 against $3,000.', 'B is the cheap premium, not the small deductible.', 'Both lists show a deductible.']),
    tf('The lower premium is the better plan for every person.', False,
       'It wins a quiet year. A big bill can make the low deductible worth the extra premium.'),
], fmt='call')

luis_story = {
    'title': 'The window and the discount',
    'character': 'Luis, 26, barista',
    'body': 'Luis’s café does not offer health insurance. He has been uninsured since he turned 26 and left a parent’s plan. The yearly [[open enrollment|open-enrollment]] window for work benefits is not his door. His door is HealthCare.gov, and he should check that site for this year’s dates.\n\nIn this example a plan’s premium is **$180** a month. An income-based discount brings his example premium to **$70**. He also learns that losing coverage, moving, marrying, or having a baby can open a special enrollment period of generally **60** days.',
}
luis = lesson('hl-luis', 'Luis on the Marketplace', 'The yearly window is posted. A life change can open a shorter one.', [
    num('In the example, how much less is the discounted premium per month?', 110,
        '$180 − $70 = $110.',
        context='[[Special enrollment]] is the extra window, generally 60 days, after a qualifying event. Income-based Marketplace discounts are real, and the dollar amount depends on the year and the household.'),
    num('How much is that example discount over 12 months?', 1320, '$110 × 12 = $1,320.'),
    num('A special enrollment period is generally how many days?', 60,
        'About 60 days after the qualifying event. Check HealthCare.gov for the rule that applies to you.',
        unit='days'),
    mc('Luis loses no job coverage, does not move, and does not have a baby. He simply waited. What is true?',
       ['He uses the yearly window posted on HealthCare.gov, not a special enrollment period', 'He can enroll any day, since he has no coverage', 'Turning 26 last year still counts as a qualifying event'], 0,
       'Special enrollment needs a recent qualifying event, generally within 60 days. The yearly window is the ordinary door.'),
    tf('An income-based discount is the same dollar amount for every shopper.', False,
       'It depends on income, household, and the year’s rules.'),
], fmt='story', story=luis_story)

trial_steps = [
    num('Premium $200 a month. What is the yearly premium?', 2400, '$200 × 12 = $2,400.'),
    mc('The deductible is met. You owe 20% of a $500 covered bill. What is that share called?',
       ['Coinsurance', 'The premium', 'A copay'], 0,
       'A percent after the deductible is coinsurance.'),
    tf('Out-of-network care usually costs the same as in-network care.', False,
       'The plan’s prices stop at the network.'),
    num('Out-of-pocket maximum $4,000. You have paid $2,500. How much room is left?', 1500,
        '$4,000 − $2,500 = $1,500.'),
]

lessons = [price, share, er, summary, network, plansort, choose, luis,
           review('hl'), trial('hl', 'Health Insurance', trial_steps)]
write_unit('06-health-insurance.json', 'health-insurance', 6, 'Health Insurance',
           'Premium, deductible, copay, coinsurance, and the network that changes the bill.',
           'The monthly price is not the bill. Read both.', terms, lessons, section=S)
