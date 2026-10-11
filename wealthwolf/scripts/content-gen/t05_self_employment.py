from lib import *

S = 'taxes'
terms = {
    'self-employment-tax': term('Self-employment tax',
                                'The Social Security and Medicare tax a self-employed person pays on net earnings. The common case is 15.3% of 92.35% of the net, which is both the employee half and the employer half.',
                                'A $10,000 self-employment base is taxed at 15.3%, which is $1,530.'),
}

both = lesson('se-both', 'Both Halves of FICA', 'An employee pays one half. You pay both.', [
    info('The common case',
         '[[Self-employment tax]] is both halves of [[FICA]]. In the common case, under the Social Security wage base, it is **15.3%** of **92.35%** of net self-employment earnings.\n\nOn a **$20,000** net, the base is **$18,470**. On a round **$10,000** base, 15.3% is **$1,530**. An employee’s half of FICA on $10,000 of wages is **7.65%**, or **$765**. The extra 0.9% Medicare tax is a high-income exception. This lesson does not grade that threshold.'),
    num('Net self-employment earnings are $20,000. What is 92.35% of that?', 18470,
        '$20,000 × 0.9235 = $18,470.'),
    num('The self-employment base in front of you is $10,000. What is 15.3% of it?', 1530,
        '$10,000 × 0.153 = $1,530.'),
    num('What is the employee half, 7.65%, on $10,000 of wages?', 765,
        '$10,000 × 0.0765 = $765.'),
    num('How much more is the $1,530 self-employment tax than that employee half?', 765,
        '$1,530 − $765 = $765. That gap is the employer half, which a self-employed person also pays.'),
])

sched = doc('statement', 'Schedule C, simplified', [
    ('gross', 'Gross receipts', 40000),
    ('supplies', 'Supplies', -2000),
    ('help', 'Contract help', -3000),
], subtitle='One freelance business', totals=[('Net profit', 35000, True)])
assert 40000 - 2000 - 3000 == 35000

page = lesson('se-sched', 'A Schedule C', 'Profit is receipts minus the costs you can deduct.', [
    info('The bottom line',
         'Schedule C is the high-level picture of one business. Gross receipts are **$40,000**. Supplies are **$2,000**. Contract help is **$3,000**. Net profit is **$35,000**.\n\nA personal grocery trip is not a line here. A [[business expense]] has to belong to the work.'),
    num('What is the net profit on this page?', 35000,
        '$40,000 − $2,000 − $3,000 = $35,000.', doc=sched),
    num('Supplies and contract help together are how much?', 5000,
        '$2,000 + $3,000 = $5,000.', doc=sched),
    mc('Which cost belongs on this Schedule C?',
       ['Software you bought only for client work', 'Your household groceries', 'A vacation that included one work email'], 0,
       'The software is a business expense. The groceries and the vacation are personal.'),
    tf('Net profit is the gross receipts, with no costs taken off.', False,
       'Net profit is what remains. Here that is $35,000, not $40,000.'),
], fmt='document')

office = lesson('se-office', 'Expenses and a Home Office', 'The space has to be for the work, regularly and only.', [
    info('Exclusive means exclusive',
         'Ordinary [[business expense]] items, like the supplies on the Schedule C, come off the receipts.\n\nA home office usually has to be used regularly and only for the business. A desk in the living room, or a spare room that is also the guest room, usually fails that test. This lesson does not assign a dollar deduction for the room. The IRS page for the year is the method, simplified or actual.'),
    mc('Which space usually qualifies?',
       ['A room used only for the business, regularly', 'The kitchen table, also used for dinner', 'A guest room with a laptop in the corner'], 0,
       'Only, and regularly. Shared family space usually does not qualify.'),
    tf('A personal grocery bill becomes a business expense because you thought about work while shopping.', False,
       'The cost has to be for the business. Thinking about work does not convert a personal bill.'),
    num('Gross receipts are $35,000. A real business expense is $5,000. What is left before any home-office method?', 30000,
        '$35,000 − $5,000 = $30,000. The home office is a separate question, not an automatic extra.'),
    fill('A home office usually must be used regularly and ___ for the business.',
         ['only', 'socially', 'never'], 0,
         'Only. A mixed-use room usually stays personal.'),
])

miles = lesson('se-miles', 'Mileage in 2026', 'The rate changed on July 1. Use the half you drove.', [
    info('Two rates, one year',
         'For 2026, the business standard mileage rate is **72.5 cents** a mile from January through June, and **76 cents** from July through December.\n\nIt is for business miles of a self-employed person, not for an employee’s commute to a regular workplace. **1,000** miles in the second half are **$760**. The same 1,000 miles in the first half are **$725**. Both halves are **$1,485**. Do not use one rate for the whole year.'),
    num('What is 1,000 business miles in July through December 2026, at 76 cents?', 760,
        '1,000 × $0.76 = $760.'),
    num('What is 1,000 business miles in January through June 2026, at 72.5 cents?', 725,
        '1,000 × $0.725 = $725.'),
    num('You drove 1,000 business miles in each half. What is the deduction?', 1485,
        '$760 + $725 = $1,485.'),
    tf('The drive from home to a regular W-2 office is a business mile at these rates.', False,
       'These rates are the self-employed business deduction. A commute to your job is personal.'),
])

harbor = lesson('se-harbor', 'Quarterly Estimates', 'A safe harbor is a target, not a guess.', [
    info('Match last year, or come close to this one',
         '[[Estimated taxes]] are how you pay during the year when no employer is withholding. You already know the quarterly dates.\n\nA common safe harbor is **100%** of last year’s tax, or **110%** if your adjusted gross income was over **$150,000**. Another path is **90%** of this year’s tax. Last year’s tax of **$4,000** makes the 100% target **$4,000**, or **$1,000** a quarter. The 110% target is **$4,400**, or **$1,100** a quarter.'),
    num('Last year’s tax was $4,000. What is 100% of it?', 4000, 'The common safe harbor is the whole $4,000.'),
    num('Split that $4,000 into four equal quarterly payments. What is each one?', 1000,
        '$4,000 ÷ 4 = $1,000.'),
    num('Your adjusted gross income was over $150,000, so you use 110% of the $4,000. What is the target?', 4400,
        '$4,000 × 1.10 = $4,400.'),
    tf('The quarterly dates replace the need to pay.', False,
       'The dates are when the estimates are due. A safe harbor is how much. You already learned the dates.'),
])

records = lesson('se-records', 'Keep the Records', 'No receipt, no easy deduction.', [
    info('The file is the deduction',
         'Keep the invoice, the receipt, and a mileage log written at the time. A number you reconstruct in April is a weak record.\n\nPersonal bills do not go in the business folder just because the folder is nearby.'),
    sort('Sort each paper.',
         ['Keep for the business', 'Personal'],
         [('An invoice you sent a client', 0),
          ('A log of miles driven to that client', 0),
          ('A receipt for software used only for the work', 0),
          ('The household streaming bill', 1)],
         'Client income, client miles, and work software stay. The streaming bill is personal.'),
    mc('When should the mileage log be written?',
       ['When you drive the miles', 'The night before you file', 'Only if you are audited'], 0,
       'A log from the day is a record. A log from memory is a story.'),
    tf('A personal streaming bill is a business expense if it is in the same drawer as the invoices.', False,
       'The drawer does not change what the bill paid for.'),
    fill('Write the mileage down when you ___ it.',
         ['drive', 'file', 'forget'], 0,
         'Drive. April is too late to invent the log.'),
], fmt='sort')

emp = doc('statement', 'Employee half on $10,000', [
    ('fica', 'FICA you pay', 765),
], subtitle='The employer pays the other half')
self_doc = doc('statement', 'Self-employed on a $10,000 base', [
    ('se', 'Self-employment tax', 1530),
], subtitle='Both halves')
assert 1530 - 765 == 765

call = lesson('se-call', 'One Half or Both', 'Same $10,000 base. Twice the FICA.', [
    num('What does the employee pay in FICA on this page?', 765,
        '7.65% of $10,000 is $765.', docs=[emp, self_doc]),
    num('What is the self-employment tax on the $10,000 base?', 1530,
        '15.3% of $10,000 is $1,530.', docs=[emp, self_doc]),
    num('How much more is the self-employed page?', 765,
        '$1,530 − $765 = $765.', docs=[emp, self_doc]),
    mc('Who pays both halves on these two pages?',
       ['The self-employed person', 'The employee', 'Neither. FICA is optional'], 0,
       'The employee page is one half. The self-employed page is both.',
       why=['$1,530 is both halves.', 'The employee pays $765.', 'FICA is not optional.'],
       docs=[emp, self_doc]),
    tf('The self-employed tax on this page is smaller because there is no employer.', False,
       'There is no employer to pay the other half, so the self-employed person pays both. The page is larger, not smaller.'),
], fmt='call')

rosa_story = {
    'title': 'Rosa’s second year',
    'character': 'Rosa, 38',
    'body': 'Rosa is 38 and a freelance designer. Her second year’s net profit, before the mileage, is **$20,000**. The self-employment base is 92.35% of that, which is **$18,470**.\n\nShe also drove **1,000** miles to clients in July through December 2026. At **76 cents**, that deduction is **$760**. She does not use the January rate for those miles.\n\nShe already knows the quarterly dates. Last year’s tax was **$4,000**, and her income was under **$150,000**, so her 100% safe harbor is **$4,000**. She keeps the invoices and the mileage log as she goes.',
}
rosa = lesson('se-rosa', 'Rosa’s Second Year', 'The base, the miles, and a harbor she can name.', [
    num('What is 92.35% of Rosa’s $20,000 net?', 18470, '$20,000 × 0.9235 = $18,470.'),
    num('What is her mileage deduction for those 1,000 second-half miles?', 760,
        '1,000 × $0.76 = $760.'),
    num('What is her 100% safe-harbor target?', 4000, '100% of last year’s $4,000 tax is $4,000.'),
    num('What is each of four equal payments toward that $4,000?', 1000, '$4,000 ÷ 4 = $1,000.'),
    tf('Rosa should use 72.5 cents for the miles she drove in November.', False,
       'November is in the second half of 2026. Those miles are 76 cents.'),
], fmt='story', story=rosa_story)

trial_steps = [
    num('Net self-employment earnings are $10,000. What is 92.35% of that?', 9235,
        '$10,000 × 0.9235 = $9,235.'),
    num('A $8,000 self-employment base is taxed at 15.3%. What is the tax?', 1224,
        '$8,000 × 0.153 = $1,224.'),
    mc('Which miles use the 76-cent rate in 2026?',
       ['Business miles driven from July through December', 'January miles', 'The commute to a W-2 job'], 0,
       'July through December is the 76-cent half. January is 72.5 cents. The commute is not this deduction.'),
    tf('A guest room that relatives still sleep in is a clean home office.', False,
       'The space usually has to be used only for the business.'),
]

lessons = [both, page, office, miles, harbor, records, call, rosa,
           review('se'), trial('se', 'Self-Employment Taxes', trial_steps)]
write_unit('05-self-employment-tax.json', 'self-employment-tax', 5, 'Self-Employment Taxes',
           'Both halves of FICA, a Schedule C, and the 2026 mileage rates that split in July.',
           'No employer is paying the other half. That half is still due.', terms, lessons, section=S)
