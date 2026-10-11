from lib import *

S = 'earning'
terms = {
    'hourly-wage': term('Hourly wage', 'Pay for every hour you work. More hours, more pay.', '$18 an hour × 40 hours = $720 for the week.'),
    'salary': term('Salary', 'A fixed yearly amount, split across your paychecks, no matter how many hours you work.', '$52,000 a year, paid as 26 paychecks of $2,000.'),
    'minimum-wage': term('Minimum wage', 'The lowest hourly pay allowed by law. The federal minimum is $7.25, and many states and cities set a higher one.',
                         'A state minimum of $15 an hour beats the federal $7.25.'),
    'overtime': term('Overtime', 'Extra pay for hours past 40 in a workweek. Under federal law most hourly workers get 1.5 times their usual rate.',
                     'At $20 an hour, overtime pays $30 an hour.'),
    'fica': term('FICA', 'The two payroll taxes on every paycheck: Social Security (6.2%) and Medicare (1.45%).', '7.65% of $1,680 is $128.52 of FICA.'),
    'pre-tax-deduction': term('Pre-tax deduction', 'Money taken from your pay before income tax is worked out, so you’re taxed on less.',
                              'A traditional 401(k) contribution or a work health insurance premium.'),
    'year-to-date': term('Year-to-date', 'Totals since January 1 of this year, often shown as YTD on a pay stub.', 'YTD gross pay through June: $21,840.'),
    'w-2': term('W-2', 'The yearly summary of your pay and the taxes taken out, sent by your employer each January, used to file your taxes.',
                'Your W-2 shows $43,680 of wages and the federal tax withheld from them.'),
}

hourly = lesson('pc-hourly-salary', 'Hourly vs. Salary', 'Two ways to get paid, and how to compare them.', [
    mc('Which kind of pay changes when you work more hours?', ['Hourly', 'Salary'], 0, 'Hourly pay counts every hour. A salary stays the same.',
       context='An [[hourly wage]] pays you for every hour you work. A [[salary]] is a fixed yearly amount, split across your paychecks, no matter how many hours you put in.'),
    num('You earn $18 an hour and work 40 hours a week. What’s your weekly pay before deductions?', 720, '$18 × 40 = $720.'),
    num('$18 an hour, 40 hours a week, 52 weeks. What’s that for a year?', 37440, '$18 × 40 × 52 = $37,440.',
        context='To turn hourly pay into a yearly number, multiply by hours a week, then by 52 weeks.'),
    num('A salary of $52,000. What’s that per hour at 40 hours a week? Divide by 2,080 hours.', 25, '$52,000 ÷ 2,080 = $25 an hour.'),
    mc('You’re salaried at $52,000 and work 50 hours one week. What usually happens to your pay?',
       ['Nothing: a salary stays the same', 'It goes up 25%', 'It goes down'], 0, 'Many salaried jobs don’t pay for extra hours. The next lesson explains why.'),
    tf('Your state can require a higher minimum wage than the federal $7.25.', True, 'Many states and cities do. The higher one wins.',
       context='The federal [[minimum wage]] is $7.25 an hour, and many states and cities set a higher one.'),
    mc('What’s a perk of hourly pay?', ['Every extra hour you work gets paid', 'Your pay never changes', 'No taxes'], 0, 'Extra shifts mean extra money.'),
])

overtime = lesson('pc-overtime', 'Overtime', 'Hours past 40 pay more. Here’s how much.', [
    mc('You earn $20 an hour. What’s your overtime rate?', ['$30 an hour', '$20 an hour', '$40 an hour'], 0, '$20 × 1.5 = $30.',
       context='[[Overtime]] is extra pay for hours past 40 in a workweek. Under federal law, most hourly workers get 1.5 times their usual rate for those hours.'),
    num('At $20 an hour, you work 46 hours this week. How many overtime hours?', 6, '46 − 40 = 6 hours.', unit='hours'),
    num('What’s your pay for the week? 40 hours at $20, plus 6 hours at $30.', 980, '$800 + $180 = $980.'),
    tf('Overtime counts hours in a single workweek, not across two weeks.', True,
       '50 hours one week and 30 the next still means 10 overtime hours in the first week.'),
    mc('Many salaried workers are “exempt.” What does that usually mean?', ['They aren’t paid extra for hours over 40', 'They pay no taxes', 'They can’t be fired'], 0,
       'Exempt from overtime rules. Some salaried workers do still get overtime, so check.'),
    num('$16 an hour, 44 hours this week. What’s the weekly pay?', 736, '40 × $16 = $640, plus 4 × $24 = $96. $736.'),
    fill('Overtime under federal law pays ___ times your usual rate.', ['1.5', '2', '1.25'], 0, 'Time and a half.'),
])

freq = lesson('pc-pay-frequency', 'How Often You’re Paid', 'Weekly, every two weeks, twice a month: same salary, different checks.', [
    info('Four common pay schedules',
         'Weekly means 52 paychecks a year. Every two weeks means 26. Twice a month (like the 15th and the last day) means 24. Monthly means 12.\n\n'
         'Same salary, different-sized checks. Your budget needs the per-paycheck number.'),
    match('Match each schedule to its paychecks a year.', [('Weekly', '52'), ('Every two weeks', '26'), ('Twice a month', '24'), ('Monthly', '12')]),
    num('A $45,500 salary paid every two weeks. What’s each gross paycheck?', 1750, '$45,500 ÷ 26 = $1,750.'),
    num('The same salary paid twice a month (24 paychecks). What’s each gross paycheck?', 1895.83, '$45,500 ÷ 24 = $1,895.83.'),
    mc('Why are every-two-weeks paychecks smaller than twice-a-month ones on the same salary?',
       ['The year is split into 26 checks instead of 24', 'Every-two-weeks pays less overall', 'More taxes'], 0, 'Same yearly total, cut into more pieces.'),
    tf('On the same salary, every-two-weeks and twice-a-month pay add up to the same yearly total.', True, 'Only the slicing is different.'),
])

stub_lines = [
    ('gross', 'Regular pay, 80 hrs × $21.00', 1680.00, {'section': 'Earnings'}),
    ('fed', 'Federal income tax', -126.00, {'section': 'Deductions'}),
    ('state', 'State income tax', -50.40, {'section': 'Deductions'}),
    ('ss', 'Social Security', -104.16, {'section': 'Deductions'}),
    ('med', 'Medicare', -24.36, {'section': 'Deductions'}),
]
assert money(1680 * 0.062) == 104.16 and money(1680 * 0.0145) == 24.36
net = total(l[2] for l in stub_lines)
assert net == 1375.08
STUB = doc('paystub', 'Riverside Hardware', stub_lines, subtitle='Pay stub · Employee: You',
           meta=[['Pay period', 'Mar 1–14'], ['Pay date', 'Mar 20']], totals=[('Gross pay', 1680.00)])
fica = lesson('pc-fica', 'Social Security & Medicare', 'The 7.65% on every pay stub, and what it buys you.', [
    mc('Which two lines are FICA?', ['Social Security and Medicare', 'Federal and state income tax', 'Gross pay and net pay'], 0,
       'FICA is Social Security plus Medicare.',
       context='[[FICA]] is the name for two taxes on your pay: Social Security (6.2%) and Medicare (1.45%). They fund retirement and health coverage for older Americans, and you’ll collect from them later yourself.',
       doc=STUB),
    num('Check the Social Security line: 6.2% of $1,680.', 104.16, '$1,680 × 0.062 = $104.16.', doc=STUB),
    num('Check Medicare: 1.45% of $1,680.', 24.36, '$1,680 × 0.0145 = $24.36.', doc=STUB),
    num('How much FICA in total on this paycheck?', 128.52, '$104.16 + $24.36 = $128.52, which is 7.65% of $1,680.', doc=STUB),
    num('What’s the net pay?', net, '$1,680.00 − $126.00 − $50.40 − $104.16 − $24.36 = $1,375.08.', doc=STUB),
    tf('Your employer pays a matching 7.65% on top of your pay.', True,
       'Employers match your Social Security and Medicare. If you work for yourself, you pay both halves.'),
    mc('Who collects Social Security later?', ['You do, when you retire or if you become disabled', 'Only your employer', 'Nobody'], 0,
       'It’s insurance you pay into now and draw on later.'),
], fmt='document')

pretax = lesson('pc-pretax', 'Before Tax or After?', 'Some deductions shrink your tax bill. Here’s which.', [
    mc('$100 goes into a pre-tax 401(k). What happens to the pay you’re taxed on?', ['It drops by $100', 'It stays the same', 'It rises by $100'], 0,
       'You’re taxed as if you earned $100 less.',
       context='A [[pre-tax deduction]] comes out of your pay before income tax is worked out, so you’re taxed on less. A traditional 401(k) and most work health insurance are pre-tax.'),
    num('Gross pay is $2,000. Pre-tax deductions: $120 to a 401(k) and $80 for health insurance. What pay is income tax worked out on?', 1800,
        '$2,000 − $120 − $80 = $1,800.'),
    num('At a 12% income tax rate, how much tax do those $200 of pre-tax deductions save each paycheck?', 24, '$200 × 0.12 = $24.'),
    sort('Usually pre-tax or after-tax?', ['Usually pre-tax', 'Usually after-tax'],
         [('Traditional 401(k)', 0), ('Work health insurance premium', 0), ('Health savings account through work', 0),
          ('Roth 401(k)', 1), ('Paying back a loan from your 401(k)', 1), ('Charity gifts through payroll', 1)]),
    tf('A Roth 401(k) is taxed now, so the money comes out tax-free in retirement.', True, 'Pay the tax today, skip it later.'),
    mc('$100 of pre-tax deductions shrinks your take-home pay by…', ['Less than $100', 'Exactly $100', 'More than $100'], 0,
       'At 12% tax, $100 pre-tax only costs you $88 of take-home, because $12 of tax disappears too.'),
], fmt='sort')

ytd_lines = [
    ('gross', 'Gross pay, YTD', 21840.00), ('fed', 'Federal income tax, YTD', -1638.00), ('state', 'State income tax, YTD', -655.20),
    ('ss', 'Social Security, YTD', -1354.08), ('med', 'Medicare, YTD', -316.68),
]
assert money(21840 * 0.062) == 1354.08 and money(21840 * 0.0145) == 316.68
YTD = doc('paystub', 'Riverside Hardware', ytd_lines, subtitle='Year-to-date totals · through Jun 30')
assert total([1638, 655.20, 1354.08, 316.68]) == 3963.96
ytd = lesson('pc-ytd', 'Year-to-Date & Your W-2', 'The running totals on your stub, and the form they become.', [
    mc('How much has this person earned before deductions so far this year?', ['$21,840.00', '$17,876.04', '$1,638.00'], 0, 'The gross pay YTD line.',
       context='[[Year-to-date]] (YTD) totals add up everything since January 1. Most pay stubs show them next to the current paycheck.', doc=YTD),
    num('How much federal income tax have they paid so far this year?', 1638, 'The federal line: $1,638.00.', doc=YTD),
    num('Add up all the deductions so far this year.', 3963.96, '$1,638.00 + $655.20 + $1,354.08 + $316.68 = $3,963.96.', doc=YTD),
    num('If the second half of the year matches the first, about what will they earn before deductions for the full year?', 43680,
        '$21,840 × 2 = $43,680.', doc=YTD),
    mc('What’s a W-2 for?', ['Filing your taxes', 'Applying for a job', 'Opening a bank account'], 0, 'It’s the official record of your year’s pay and tax.',
       context='Every January your employer sends a [[W-2]]: the yearly summary of your pay and the taxes taken out, used to file your tax return.'),
    tf('Your last pay stub of the year should roughly match your W-2.', True, 'If they’re far apart, ask payroll why.'),
], fmt='document')

err_lines = [
    ('reg', 'Regular pay, 72 hrs × $19.00', 1368.00, {'section': 'Earnings'}),
    ('fed', 'Federal income tax', -102.60, {'section': 'Deductions'}),
    ('ss', 'Social Security', -84.82, {'section': 'Deductions'}),
    ('med', 'Medicare', -19.84, {'section': 'Deductions'}),
]
assert money(1368 * 0.062) == 84.82 and money(1368 * 0.0145) == 19.84
ERR = doc('paystub', 'Lakeview Grocery', err_lines, subtitle='Pay stub · Employee: You', meta=[['Pay period', 'Apr 1–14']])
ded_lines = [
    ('reg', 'Regular pay, 80 hrs × $19.00', 1520.00, {'section': 'Earnings'}),
    ('fed', 'Federal income tax', -114.00, {'section': 'Deductions'}),
    ('ss', 'Social Security', -94.24, {'section': 'Deductions'}),
    ('med', 'Medicare', -22.04, {'section': 'Deductions'}),
    ('park', 'Employee parking permit', -25.00, {'section': 'Deductions'}),
]
assert money(1520 * 0.062) == 94.24 and money(1520 * 0.0145) == 22.04
DED = doc('paystub', 'Lakeview Grocery', ded_lines, subtitle='Pay stub · Employee: You', meta=[['Pay period', 'Apr 15–28']])
errors = lesson('pc-stub-errors', 'Check Your Pay Stub', 'Payroll makes mistakes. Catch them.', [
    spot('Your timesheet says you worked 80 hours this pay period. Tap the line that’s wrong.', ERR, 'reg',
         'It only paid 72 hours. You’re owed 8 more.', context='Payroll mistakes happen. Compare every stub with your own record of hours.'),
    num('How much pay is missing? 8 hours at $19.', 152, '8 × $19 = $152, before deductions.'),
    spot('You take the bus and never park at work. Which deduction shouldn’t be there?', DED, 'park', 'A $25 parking permit you never asked for.'),
    order('You find a mistake on your stub. Put the fix in order.',
          ['Compare the stub with your own hours', 'Tell your manager or payroll in writing', 'Keep copies of your timesheet and stub', 'Check the next stub to confirm the fix'],
          'Check, report, document, confirm.'),
    tf('If payroll underpays you, it’s up to you to notice and speak up.', True, 'Nobody watches your pay as closely as you do.'),
    mc('What’s the best habit with pay stubs?', ['Check hours, rate and deductions every payday', 'Never read them', 'Only read the net pay'], 0,
       'Two minutes every payday.'),
], fmt='spot')

jamie_story = {
    'title': 'The first real paycheck',
    'character': 'Jamie, 23, first salaried job',
    'body': 'Jamie just started a first salaried job: **$52,000** a year, paid every two weeks (26 paychecks).\n\n'
            'Jamie signed up for the 401(k) at **4%** of pay, and work health insurance costs **$60** a paycheck. Each paycheck also loses **$160** '
            'to federal income tax, **$60** to state income tax, and **7.65%** to Social Security and Medicare.',
}
assert 52000 / 26 == 2000 and 2000 * 0.0765 == 153 and 2000 - 80 - 60 - 153 - 160 - 60 == 1487
jamie = lesson('pc-jamie', 'Jamie’s First Salary', 'From $52,000 a year to what actually lands every other Friday.', [
    num('What’s Jamie’s gross pay per paycheck? ($52,000 ÷ 26)', 2000, '$52,000 ÷ 26 = $2,000.'),
    num('Social Security and Medicare take 7.65% of gross. How much is that per paycheck?', 153, '$2,000 × 0.0765 = $153.'),
    num('4% of gross goes to the 401(k). How much per paycheck?', 80, '$2,000 × 0.04 = $80.'),
    num('Add up every deduction: 401(k), health insurance, Social Security and Medicare, federal tax and state tax.', 513,
        '$80 + $60 + $153 + $160 + $60 = $513.'),
    num('What lands in Jamie’s account each paycheck?', 1487, '$2,000 − $513 = $1,487.'),
    mc('Jamie budgets with $52,000 ÷ 12 = $4,333 a month. What’s wrong with that?',
       ['That’s before deductions. Budget take-home pay instead', 'Nothing', 'Jamie should divide by 52'], 0,
       'Budget the $1,487s, not the $52,000.'),
    num('Planning on two paychecks a month, how much take-home does Jamie budget per month?', 2974, '$1,487 × 2 = $2,974.'),
], fmt='story', story=jamie_story)

trial_steps = [
    num('$22 an hour, 45 hours this week. What’s the weekly pay?', 1045, '40 × $22 = $880, plus 5 × $33 = $165. $1,045.'),
    mc('Which two taxes make up FICA?', ['Social Security and Medicare', 'Federal and state income tax', 'Sales tax and property tax'], 0, '6.2% plus 1.45%.'),
    num('A $39,000 salary paid every two weeks. What’s each gross paycheck?', 1500, '$39,000 ÷ 26 = $1,500.'),
    tf('Pre-tax deductions lower the pay that income tax is worked out on.', True, 'That’s what pre-tax means.'),
]

lessons = [hourly, overtime, freq, fica, pretax, ytd, errors, jamie, review('pc'), trial('pc', 'Your Paycheck', trial_steps)]
write_unit('01-paycheck.json', 'paycheck', 1, 'Your Paycheck', 'Hourly, salary, overtime, and every line on your pay stub.',
           'Read the stub. Every line is either yours or someone’s excuse.', terms, lessons, section=S)
