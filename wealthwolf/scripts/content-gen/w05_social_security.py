from lib import *

S = 'building-wealth'
terms = {
    'work-credit': term('Work credit',
                        'A unit of work that counts toward Social Security. In 2026, one credit is $1,890 of covered earnings. You can earn at most four credits a year.',
                        'Four credits in 2026 take $7,560 of earnings. A 40-credit record is the usual retirement gate.'),
    'full-retirement-age': term('Full retirement age',
                                'The age Social Security calls full. For people born in 1960 or later, it is 67. Medicare stays at 65.',
                                'Claiming at 62 pays less than the full benefit. Waiting until 70 pays more.'),
    'medicare': term('Medicare',
                     'The federal health insurance people usually join at 65. Part A is hospital care, Part B is doctors and outpatient care, and Part D is prescriptions. Medicare Advantage is a private plan that can bundle them.',
                     'The initial signup window is 7 months around the month you turn 65.'),
}

credits = lesson('so-credits', 'Work Credits', 'Forty of them, and the year they were earned.', [
    info('The 2026 credit',
         'Social Security retirement benefits are earned with [[work credit]]s. In 2026, one credit is $1,890 of covered earnings, and you can earn at most four in a year, which is $7,560. Anyone born in 1929 or later needs 40 credits, about 10 years of work. Credits decide whether you qualify. They do not set the size of the check.'),
    num('In 2026, how many dollars of earnings buy one work credit?', 1890,
        'The 2026 amount is $1,890. It rises when average wages rise.'),
    num('How many dollars buy the maximum four credits in 2026?', 7560,
        '4 × $1,890 = $7,560. Earnings above that do not buy a fifth credit.'),
    num('How many credits does a retirement benefit usually require?', 40, unit=None,
        explain='40 credits, about 10 years. The size of the check comes from your earnings record, not from piling past 40.'),
    tf('Earning $20,000 in 2026 buys more than four work credits.', False,
       'Four is the yearly cap. $20,000 still buys four, once you have passed $7,560.'),
])

claim = lesson('so-claim', '62, 67, or 70', 'Same record. Three different checks.', [
    info('The ages',
         'You can claim as early as 62. [[Full retirement age]] is 67 for someone born in 1960 or later. Waiting past 67 adds about 8% a year until 70. On a $2,000 full monthly benefit, 62 pays about 70%, which is $1,400. Age 70 pays about 124%, which is $2,480. These are the SSA shapes for a full retirement age of 67. Your own record can differ.'),
    num('What is 70% of a $2,000 full monthly benefit?', 1400,
        '$2,000 × 0.70 = $1,400. That is the about-62 check in this example.'),
    num('What is 124% of that $2,000 full monthly benefit?', 2480,
        '$2,000 × 1.24 = $2,480. Three years past 67, at about 8% a year, is the 24% add-on.'),
    num('How many dollars a month separate the age-70 check from the age-62 check in this example?', 1080,
        '$2,480 − $1,400 = $1,080. Waiting pays more each month and starts later. Needing the money at 62 is a real reason to take the smaller check.'),
    tf('Medicare also waits until full retirement age.', False,
       'Medicare stays at 65. Full retirement age for this group is 67. They are different clocks.'),
])

statement = doc('statement', 'A teaching Social Security sketch',
                [('full', 'Monthly benefit at full retirement age', 2000)],
                meta=[('Full retirement age on this sketch', '67'),
                      ('About 70% if claimed at 62', '$1,400'),
                      ('About 124% if claimed at 70', '$2,480')],
                subtitle='One record, three ages',
                note='A real statement uses your earnings. This page uses a round $2,000 so the ages are easy to see.')

read = lesson('so-statement', 'Reading a Statement', 'Find the age before you memorize the dollar.', [
    info('The row that matches an age',
         'A Social Security statement estimates the check at different ages. This teaching page shows $2,000 at [[full retirement age]] of 67. The early and late figures are the same percents as the last lesson. A real statement is yours. This one is a sketch.'),
    num('What monthly benefit does this page show at full retirement age?', 2000,
        doc=statement,
        explain='The full-retirement-age line is $2,000 a month.'),
    num('How many dollars a year is that $2,000 month?', 24000,
        '12 × $2,000 = $24,000. Monthly figures hide the year if you do not multiply.'),
    tf('The $2,000 on a teaching page is the check every worker gets.', False,
       'It is a round example. Your statement uses your earnings record.'),
    mc('What should you match before you trust a dollar on the statement?',
       ['The age the dollar belongs to', 'A friend’s check', 'The federal funds rate'], 0,
       'A $1,400 and a $2,480 can both be “your” benefit. They are different ages.'),
], fmt='document')

spouse = lesson('so-spouse', 'A Spouse’s Benefit', 'Up to half, at the spouse’s own full age.', [
    info('Half of the full benefit',
         'A spouse can receive up to 50% of the worker’s full retirement benefit, if the spouse claims at the spouse’s own [[full retirement age]]. On a $2,000 full benefit, that is up to $1,000. It does not cut the worker’s own check. Claiming the spousal benefit early reduces it. This lesson grades the full-age half, not the early reduction.'),
    num('The worker’s full benefit is $2,000 a month. What is 50% of it?', 1000,
        '$2,000 × 0.50 = $1,000. That is the “up to” figure at the spouse’s full retirement age.'),
    tf('Paying the spouse $1,000 reduces the worker’s $2,000 check.', False,
       'The worker keeps the worker’s benefit. The spousal benefit is additional, up to that half.'),
    mc('When is the “up to 50%” figure for?',
       ['When the spouse claims at their own full retirement age', 'When the spouse claims at 62, with no reduction', 'When the spouse skips Medicare'], 0,
       'Full retirement age for the spouse. Earlier claiming reduces the spousal benefit.'),
    num('How many dollars a year is that $1,000 monthly spousal benefit?', 12000,
        '12 × $1,000 = $12,000. Still a sketch, and only at the full age.'),
])

parts = lesson('so-parts', 'Medicare’s Parts', 'Hospital, doctors, drugs, and a private bundle.', [
    info('Four names',
         '[[Medicare]] at 65 is not one product. Part A is hospital care. Part B is doctors and outpatient care. Part D is prescriptions. Medicare Advantage, sometimes called Part C, is a private plan that can bundle those jobs. Part A is often premium-free if you have 40 work credits. Part B has a premium. This lesson does not grade this year’s premium.'),
    sort('Which part is this care?',
         ['Part A', 'Part B', 'Part D'],
         [('A hospital stay', 0),
          ('A visit to the doctor', 1),
          ('A prescription you fill at a pharmacy', 2),
          ('Outpatient surgery', 1)],
         'Hospital is Part A. The doctor and outpatient surgery are Part B. The prescription is Part D.'),
    mc('What is Medicare Advantage?',
       ['A private plan that can bundle hospital, doctor, and drug coverage', 'A bonus that raises your Social Security check', 'The same thing as a 401(k)'], 0,
       'A private bundle. It is still Medicare, with the plan’s own network and rules.'),
    tf('Part B is free for everyone because Part A can be.', False,
       'Part A is often premium-free with enough work credits. Part B has a premium. Do not treat them as the same bill.'),
    fill('Prescription coverage is Medicare Part ___.',
         ['D', 'A', 'match'], 0,
         'Part D. Part A is the hospital. Part B is the doctor.'),
], fmt='sort')

window = lesson('so-window', 'When You Sign Up', 'Seven months around 65.', [
    info('Do not wait for 67',
         'The Initial Enrollment Period for [[Medicare]] is 7 months. It starts 3 months before the month you turn 65, includes that month, and runs 3 months after. Full retirement age can be 67. Medicare does not wait for it. If you have qualifying job coverage you may be able to delay Part B. Missing Part B without that coverage can raise the premium later. This lesson grades the window, not a personal penalty.'),
    num('How many months long is the Initial Enrollment Period?', 7, unit='months',
        explain='3 months before, the birthday month, and 3 months after: 3 + 1 + 3 = 7.'),
    tf('You should wait until full retirement age of 67 to first look at Medicare.', False,
       'Medicare’s window is around 65. Full retirement age is a Social Security clock, not the Medicare clock.'),
    mc('The 7 months start when?',
       ['3 months before the month you turn 65', 'On your 67th birthday only', 'When you claim Social Security, whatever age that is'], 0,
       'Three months before the birthday month. Claiming Social Security is a separate decision.'),
    mc('What is a solid reason to look at delaying Part B?',
       ['Qualifying health coverage from a job', 'A headline about the Fed', 'Because Part A and Part B are the same premium'], 0,
       'Job coverage can change the deadline. A headline does not. The premiums are not the same.'),
])

gap = lesson('so-gap', 'Not the Whole Plan', 'The check covers a slice of the spending.', [
    info('Subtract it',
         'A $2,000 monthly Social Security check is $24,000 a year. If the spending sketch is $40,000, the portfolio and any other income have to cover the other $16,000. Social Security is a base. It is not the [[FI number|fi-number]].'),
    num('How many dollars a year is a $2,000 monthly benefit?', 24000,
        '12 × $2,000 = $24,000.'),
    num('Spending is $40,000 and Social Security is $24,000. How many dollars are still uncovered?', 16000,
        '$40,000 − $24,000 = $16,000. That gap is what the portfolio is for, in this sketch.'),
    tf('A Social Security estimate means you can ignore the retirement accounts.', False,
       'The estimate is one slice. Spending minus that slice is still a bill.'),
    mc('What is the right job for the $24,000 in this sketch?',
       ['The entire spending plan', 'A base, with the portfolio covering the gap', 'A replacement for Medicare'], 1,
       'A base. The $16,000 gap is the rest of the plan.'),
])

rita = lesson('so-rita', 'Rita’s Three Ages', 'She can wait, so she prices the wait.', [
    info('Meet Rita',
         'Rita is 61 and a high school librarian. Her teaching statement shows a $2,000 monthly benefit at 67. She is still working and does not need the check at 62.\n\nShe writes down $1,400 at 62, $2,000 at 67, and $2,480 at 70. Waiting is available to her because the job covers her. Someone who needs income at 62 is in a different story. She also puts a note on the calendar: Medicare at 65, not at 67.',
         ),
    num('If Rita claims at 62 in this example, what is the monthly check?', 1400,
        '70% of $2,000 is $1,400.'),
    num('If she waits until 70, what is the monthly check in this example?', 2480,
        '124% of $2,000 is $2,480.'),
    tf('Rita should delay Medicare until 70 because she might delay Social Security.', False,
       'The Medicare window is around 65. The claiming age is a separate choice.'),
    mc('Why is waiting even a choice for Rita?',
       ['She is still working and does not need the check at 62', 'Waiting is required by law', 'Her full retirement age is 62'], 0,
       'Need comes first. Her full retirement age in this lesson is 67, and the job is paying her now.'),
], fmt='story', story={
    'title': 'Three numbers on one page',
    'character': 'Rita, 61, high school librarian',
    'body': 'Rita’s teaching statement shows **$2,000** a month at **67**. She is still working.\n\nShe writes **$1,400** at 62, **$2,000** at 67, and **$2,480** at 70. Medicare goes on the calendar at **65**, not at 67.',
})

write_unit('05-social-security.json', 'social-security', 5, 'Social Security & Medicare',
           'Credits, claiming ages, and the health-insurance clock that stays at 65.',
           'The check depends on the age. Medicare does not wait for 67.',
           terms, [credits, claim, read, spouse, parts, window, gap, rita, review('so'), trial('so', 'Social Security & Medicare', [
               num('In 2026, four work credits cost how many dollars of earnings?', 7560,
                   '4 × $1,890 = $7,560.'),
               num('A full benefit of $1,500 a month is claimed at 62, at about 70%. What is the monthly check?', 1050,
                   '$1,500 × 0.70 = $1,050.'),
               tf('Medicare’s initial window waits until full retirement age.', False,
                  'The 7-month window is around 65. Full retirement age for people born in 1960 or later is 67.'),
               mc('A spouse at their own full retirement age can receive up to what share of the worker’s full benefit?',
                  ['10%', '50%', 'The whole check, instead of the worker'], 1,
                  'Up to half, and it does not reduce the worker’s own benefit. Claiming earlier reduces the spousal amount.'),
           ])],
           section=S)
