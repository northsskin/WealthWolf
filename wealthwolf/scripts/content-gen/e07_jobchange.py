from lib import *

S = 'earning'
terms = {
    'notice-period': term('Notice period', 'The time between telling your employer you’re leaving and your last day, usually two weeks in the US.',
                          'Resigning on the 1st with your last day on the 15th.'),
    'layoff': term('Layoff', 'Losing your job because the company is cutting jobs, not because of anything you did.', 'A warehouse closes and 80 people are laid off.'),
    'severance': term('Severance', 'Money some employers pay when they let you go, often a few weeks of pay per year worked, usually with an agreement to sign.',
                      'Four weeks of pay in exchange for signing a release.'),
    'cobra': term('COBRA', 'A law that lets you keep your work health plan after leaving, usually up to 18 months, but you pay the full premium yourself.',
                  'Your $640 a month plan, now all paid by you.'),
    'rollover': term('Rollover', 'Moving retirement money from one account to another, like an old 401(k) into an IRA, without cashing it out.',
                     'Moving $8,000 from your old job’s 401(k) into your new job’s plan.'),
}

before = lesson('jc-before-quit', 'Before You Quit', 'Line up the money before you hand in the letter.', [
    mc('What should you have before quitting?', ['A signed offer, or savings to cover the gap', 'Just a good feeling', 'A new phone'], 0, 'Never leap without a net.'),
    num('Your essentials cost $2,200 a month and you expect 3 months between jobs. How much should you have saved?', 6600, '$2,200 × 3 = $6,600.'),
    mc('What else should you check before leaving?', ['When your health insurance ends and the new one starts', 'Nothing', 'The office plants'], 0,
       'Gaps in health coverage are expensive.'),
    tf('Some benefits, like health insurance, can end on your last day or at the end of that month.', True, 'Ask HR for the exact date.'),
    mc('Unused vacation days when you leave…', ['may be paid out, depending on your state and company', 'always vanish', 'always pay double'], 0,
       'Check your state’s rules and your company policy.'),
    order('Put a smart job switch in order.', ['Get the new offer in writing', 'Check when benefits end and start', 'Give notice', 'Leave on good terms'],
          'Secure it, check it, announce it, exit well.'),
])

notice = lesson('jc-notice', 'Leaving Well', 'Notice, final pay, and not burning bridges.', [
    mc('What’s the usual notice period in the US?', ['Two weeks', 'Two days', 'Six months'], 0, 'Two weeks is the norm.',
       context='Your [[notice period]] is the time between telling your employer you’re leaving and your last day.'),
    tf('In most US states, you aren’t legally required to give notice.', True,
       'Most jobs are “at will.” Notice is about goodwill and references, unless your contract says otherwise.'),
    mc('What’s the best way to resign?', ['A short, polite letter with your last day', 'Just not showing up', 'An angry email to everyone'], 0, 'Short and kind.'),
    num('Final paycheck: 6 days at $160 a day, plus 4 unused vacation days paid out at $160. Total before deductions?', 1600, '10 × $160 = $1,600.'),
    mc('Your boss offers more money to stay. What should you weigh?', ['Why you wanted to leave in the first place, not just the pay', 'Only the money', 'Nothing'], 0,
       'If money wasn’t the reason, more money won’t fix it.'),
    tf('Leaving on good terms can matter for future references.', True, 'Industries are smaller than they look.'),
])

gap = lesson('jc-gap', 'The Gap Between Jobs', 'The first new paycheck can be weeks away.', [
    mc('You start a new job on the 1st. When might your first paycheck arrive?', ['Two to four weeks later', 'On the 1st', 'After a year'], 0,
       'Payroll runs on its own schedule.'),
    num('Your last paycheck lands Mar 15. Your new job starts Apr 1 and first pays Apr 19. How many days with no income?', 35,
        '16 days left in March plus 19 days in April = 35 days.', unit='days'),
    num('Your essentials cost about $70 a day. What does that gap cost?', 2450, '35 × $70 = $2,450.'),
    mc('What’s the best way to cover it?', ['Savings set aside before switching', 'A credit card at 24%', 'Hope'], 0, 'Plan the gap before you jump.'),
    tf('Your new job’s benefits may have a waiting period before they start.', True, 'Some start on day one, some after 30 or 60 days.'),
    mc('During the gap, which costs do you cut first?', ['Wants', 'Rent', 'Food'], 0, 'Wants pause. Needs don’t.'),
])

layoff = lesson('jc-layoff', 'Laid Off: The First Week', 'What to do, in what order.', [
    mc('Laid off vs. fired: what’s the difference?', ['A layoff is about the company. Firing is about your performance or conduct', 'No difference', 'Fired is better'], 0,
       'Being laid off says nothing bad about you.',
       context='A [[layoff]] means losing your job because the company is cutting jobs, not because of anything you did.'),
    order('Laid off. Put the first week in order.',
          ['Get everything in writing: last day, final pay, severance, benefits', 'Apply for unemployment benefits', 'Cut your budget to essentials', 'Start the job search'],
          'Facts, benefits, budget, search.'),
    tf('Apply for unemployment right away, not after your savings run out.', True, 'Waiting can cost you weeks of benefits.'),
    num('Your emergency fund is $6,000 and essentials cost $2,000 a month. How many months does it cover?', 3, '$6,000 ÷ $2,000 = 3 months.', unit='months'),
    mc('What should you not do in week one?', ['Cash out your 401(k)', 'Make a bare-bones budget', 'Update your résumé'], 0,
       'Cashing out costs taxes plus a penalty. More on that soon.'),
    tf('Being laid off says nothing bad about your skills.', True, 'Companies cut jobs, not people’s worth.'),
])

SEV = doc('bill', 'Northwind Logistics', [('sev', 'Severance pay, 4 weeks', 4000.00), ('pto', 'Unused PTO payout, 6 days', 1200.00),
                                           ('health', 'Health insurance continued through Jun 30', 0.00)],
          subtitle='Severance agreement', meta=[['Last day', 'Apr 30'], ['Sign by', 'May 14']],
          totals=[('Total cash, before taxes', 5200.00, True)],
          note='By signing, you agree not to sue the company over your employment.')
sev = lesson('jc-severance', 'Reading a Severance Offer', 'What you get, and what you give up by signing.', [
    num('How much cash does this offer include, before taxes?', 5200, '$4,000 + $1,200 = $5,200.',
        context='[[Severance]] is money some employers pay when they let you go, often a few weeks of pay per year worked. It usually comes with an agreement to sign.',
        doc=SEV),
    mc('What do you give up by signing?', ['The right to sue the company over your job', 'Your unemployment benefits', 'Your next job'], 0,
       'Read the note at the bottom. That’s the trade.', doc=SEV),
    tf('You can ask for more time to read a severance agreement, or have a lawyer look at it.', True, 'Never sign something big on the spot.'),
    mc('Severance pay is…', ['taxed like regular pay', 'tax-free', 'a loan'], 0, 'It shows up on your W-2.'),
    num('4 weeks of severance on a $52,000 salary. How much?', 4000, '$52,000 ÷ 52 = $1,000 a week. × 4 = $4,000.'),
    mc('What’s the best use of severance?', ['Covering essentials while you job hunt', 'A vacation', 'Spending it fast'], 0, 'It’s a bridge, not a bonus.'),
], fmt='document')

COBRA_DOC = doc('bill', 'COBRA', [('prem', 'Monthly premium, same plan as before', 640.00)], subtitle='Keep your old work plan', note='Same doctors. Up to 18 months.')
MARKET = doc('bill', 'Marketplace plan', [('prem', 'Monthly premium, after discount', 310.00)], subtitle='HealthCare.gov', note='New plan. Check your doctors are covered.')
cobra = lesson('jc-cobra', 'Keeping Health Insurance', 'Two ways to stay covered between jobs.', [
    mc('What’s the catch with COBRA?', ['You pay the full premium your employer used to share', 'It’s free', 'It lasts forever'], 0, 'Same plan, much bigger bill.',
       context='[[COBRA]] lets you keep your work health plan after you leave, usually for up to 18 months, but you pay the whole premium yourself, plus a small fee.'),
    mc('Which costs less per month?', ['The Marketplace plan', 'COBRA'], 0, '$310 vs. $640.', docs=[COBRA_DOC, MARKET]),
    num('Over 3 months, how much does the Marketplace plan save?', 990, '($640 − $310) × 3 = $990.', docs=[COBRA_DOC, MARKET]),
    tf('Losing job-based coverage lets you sign up on the Marketplace outside the usual enrollment window.', True,
       'You usually have 60 days to pick a plan.'),
    mc('When might COBRA make sense anyway?', ['When you’re mid-treatment with doctors you need to keep', 'Never', 'Always'], 0,
       'Sometimes keeping your doctors is worth the price.'),
    tf('Going without health insurance between jobs is a smart way to save.', False, 'One emergency can cost more than years of premiums.'),
], fmt='call')

k401 = lesson('jc-401k', 'Your 401(k) When You Leave', 'Roll it, don’t cash it.', [
    mc('What’s a rollover?', ['Moving retirement money to another retirement account', 'Cashing it out', 'A gymnastics move'], 0, 'The money stays invested and untaxed.',
       context='When you leave a job, your 401(k) stays yours. You can usually leave it, move it to your new job’s plan, or do a [[rollover]] into an IRA, an account you open yourself.'),
    tf('Cashing out a 401(k) before age 59½ usually means income tax plus a 10% penalty.', True, 'And the money stops growing.'),
    num('You cash out $10,000. What’s the 10% penalty?', 1000, '$10,000 × 0.10 = $1,000.'),
    num('Add about 22% income tax. What do the tax and penalty come to together?', 3200, '$1,000 + $2,200 = $3,200.'),
    num('What’s left of the $10,000?', 6800, '$10,000 − $3,200 = $6,800.'),
    mc('What’s usually the best move with an old 401(k)?', ['Roll it into your new plan or an IRA', 'Cash it out for a trip', 'Forget about it'], 0,
       'Keep it growing, tax-free, for future you.'),
])

theo_story = {
    'title': 'The warehouse closes',
    'character': 'Theo, 34, warehouse supervisor',
    'body': 'Theo was laid off on Friday when his warehouse closed. He got **$6,600** in severance after taxes and has **$5,400** in his emergency fund.\n\n'
            'His bare-bones costs (rent, food, car, phone, utilities) are **$2,400** a month. He’s approved for unemployment of about **$1,800** a month, '
            'which in his state lasts up to **6** months.',
}
theo = lesson('jc-theo', 'Theo Gets Laid Off', 'Severance, savings and unemployment: how far do they stretch?', [
    num('Severance plus emergency fund: how much does Theo have?', 12000, '$6,600 + $5,400 = $12,000.'),
    num('Unemployment covers $1,800 of his $2,400 a month. How much must come from savings each month?', 600, '$2,400 − $1,800 = $600.'),
    num('After 6 months of unemployment, how much savings is left?', 8400, '$12,000 − 6 × $600 = $8,400.'),
    num('After that, savings cover the full $2,400. How many more full months? Round down.', 3, '$8,400 ÷ $2,400 = 3.5, so 3 full months.', unit='months'),
    mc('What’s Theo’s smartest move this week?', ['Apply for jobs and keep the budget bare-bones', 'Take a long vacation first', 'Cash out his 401(k)'], 0,
       'About 9 months of runway. Use it well.'),
    tf('Theo’s emergency fund turned a crisis into a hard but manageable stretch.', True, 'That’s exactly what it was for.'),
], fmt='story', story=theo_story)

trial_steps = [
    num('You cash out $5,000 from a 401(k) before age 59½. What’s the 10% penalty?', 500, '$5,000 × 0.10 = $500.'),
    mc('Why does COBRA usually cost so much more than your old paycheck deduction?', ['Your employer no longer pays its share of the premium', 'It covers less', 'It has a sign-up fee'], 0, 'Same plan, full price.'),
    tf('In most states, the law requires you to give two weeks’ notice.', False, 'It’s a custom, not a law, in most states.'),
    num('Essentials cost $1,800 a month. Savings needed for a 4-month gap?', 7200, '$1,800 × 4 = $7,200.'),
]

lessons = [before, notice, gap, layoff, sev, cobra, k401, theo, review('jc'), trial('jc', 'Changing Jobs', trial_steps)]
write_unit('07-job-change.json', 'job-change', 7, 'Changing Jobs & Job Loss', 'Quitting well, getting laid off, and protecting your money in between.',
           'Every wolf changes territory. The smart ones carry food.', terms, lessons, section=S)
