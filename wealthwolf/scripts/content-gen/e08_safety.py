from lib import *

S = 'earning'
terms = {
    'unemployment-insurance': term('Unemployment insurance', 'State-run payments that replace part of your wages for a while if you lose your job through no fault of your own.',
                                   'About half your old weekly pay, up to a state maximum, for up to 26 weeks in many states.'),
    'snap': term('SNAP', 'A government program, often called food stamps, that gives people with low income monthly money for groceries on a card.',
                 '$250 a month loaded onto a card for groceries.'),
    'medicaid': term('Medicaid', 'Free or low-cost health coverage for people with low income. Rules differ by state.', 'Coverage after a job loss drops your income.'),
    'hardship-program': term('Hardship program', 'Lower or paused payments a company offers when you’ve lost income. You usually have to ask.',
                             'Your phone company pausing half your bill for two months after a layoff.'),
}

ui = lesson('sn-ui', 'Unemployment Insurance', 'What it is, who gets it, and how long it lasts.', [
    mc('Who usually qualifies?', ['People laid off through no fault of their own', 'Anyone who quits for any reason', 'Only people over 65'], 0,
       'It’s for losing work you didn’t choose to lose.',
       context='[[Unemployment insurance]] pays part of your old wages for a while if you lose your job through no fault of your own. Each state runs its own program.'),
    tf('Unemployment is run by your state, so rules and amounts differ from state to state.', True, 'Check your state’s labor department website.'),
    mc('In many states, benefits last up to about…', ['26 weeks', '26 days', '26 years'], 0, 'About six months in many states. Some offer less.'),
    tf('Unemployment benefits count as taxable income.', True, 'You can ask to have tax withheld, so April isn’t a surprise.'),
    mc('To keep getting benefits, you usually must…', ['Certify every week or two and look for work', 'Do nothing', 'Move to another state'], 0, 'Benefits come with a job search.'),
    mc('Fired for serious misconduct. Unemployment?', ['Often not eligible', 'Always eligible', 'Paid double'], 0, 'It’s built for losing work through no fault of your own.'),
])

ui_math = lesson('sn-ui-math', 'How Much You’d Get', 'Usually helpful, rarely enough on its own.', [
    num('Your old pay was $900 a week. Half of that?', 450, '$900 ÷ 2 = $450.',
        context='Many states pay roughly half your old weekly wage, up to a state maximum. These numbers are an example; check your own state.'),
    num('Your state’s maximum is $400 a week. What would you actually get?', 400, 'The cap wins: $400.'),
    num('Over 26 weeks at $400?', 10400, '$400 × 26 = $10,400.'),
    num('Your essentials cost about $510 a week. What’s the weekly shortfall at $400?', 110, '$510 − $400 = $110.'),
    mc('So unemployment alone…', ['helps, but usually isn’t enough by itself', 'replaces your full pay', 'covers everything with extra'], 0, 'Plan to combine it with savings and cuts.'),
    tf('An emergency fund plus unemployment carries you much further than either alone.', True, 'Together they buy you months.'),
])

apply_ = lesson('sn-apply', 'Applying for Benefits', 'File early, report honestly, keep certifying.', [
    order('Put applying in order.', ['Apply on your state’s unemployment website right after losing your job', 'Answer questions about why you left',
                                    'Certify every week or two', 'Report any work or pay you get'],
          'File, explain, certify, report.'),
    mc('What do you usually need to apply?', ['ID, Social Security number, and your recent employers and dates', 'A doctor’s note', 'Your credit score'], 0,
       'Gather it before you start.'),
    tf('If your claim is denied, you can usually appeal.', True, 'Read the letter for the deadline.'),
    mc('You pick up a one-day job while on unemployment. What do you do?', ['Report it when you certify', 'Hide it', 'Stop certifying'], 0,
       'Unreported pay can mean paying benefits back, plus penalties.'),
    mc('Many states have a “waiting week.” What does that mean?', ['The first week often isn’t paid', 'You wait a year', 'You’re paid twice'], 0,
       'Another reason to apply right away.'),
    tf('Applying late can cost you weeks of benefits.', True, 'Benefits usually start from when you apply, not when you lost the job.'),
])

food = lesson('sn-food', 'Help With Food', 'SNAP, food banks, and the number 2-1-1.', [
    mc('What can SNAP pay for?', ['Groceries', 'Rent', 'Phone bills'], 0, 'Food from grocery stores.',
       context='[[SNAP]], often called food stamps, gives people with low income monthly money for groceries on a card.'),
    tf('Losing your job can make you eligible for SNAP, even if you never were before.', True, 'Eligibility is based on current income.'),
    mc('Where else can you get food help fast?', ['Food banks and pantries', 'Payday loans', 'Nowhere'], 0, 'Often same-day help.'),
    mc('Dialing 2-1-1 in most of the US connects you to…', ['Local help with food, housing and bills', 'The police', 'Your bank'], 0,
       'A free line to local programs.'),
    tf('Using SNAP or a food bank during a hard stretch is exactly what they’re for.', True, 'No shame in using a safety net.'),
    num('SNAP covers $280 of your $400 grocery budget. How much does that free up for other bills?', 280, 'The $280 you’d have spent on food can go elsewhere.'),
])

health = lesson('sn-health', 'Health Coverage When Money Is Tight', 'Medicaid, CHIP and Marketplace discounts.', [
    mc('When might you qualify for Medicaid?', ['When your income drops, like after a job loss', 'Only if you’re wealthy', 'Never'], 0, 'It’s based on current income.',
       context='[[Medicaid]] is free or low-cost health coverage for people with low income. Rules differ by state.'),
    tf('Kids may qualify for low-cost coverage through CHIP, even if their parents don’t.', True, 'CHIP covers kids in families that earn too much for Medicaid.'),
    mc('Where do you check Medicaid and Marketplace options?', ['HealthCare.gov or your state’s site', 'A random ad', 'Your gym'], 0, 'Start at the official sites.'),
    tf('Marketplace plans can come with discounts based on your income.', True, 'Lower income, bigger discount.'),
    mc('Your income drops to zero mid-year. Smart move?', ['Check Medicaid and the Marketplace right away', 'Go without insurance', 'Wait a year'], 0, 'Losing income can open the door.'),
    mc('Which usually costs least for someone with very low income?', ['Medicaid', 'COBRA', 'Paying full price'], 0, 'Often free.'),
])

lenders = lesson('sn-lenders', 'Talking to Landlords and Lenders', 'Call before you miss a payment, not after.', [
    mc('When should you call?', ['Before you miss a payment', 'After three missed payments', 'Never'], 0, 'You have more options before you fall behind.',
       context='Many companies have [[hardship programs|hardship-program]]: lower or paused payments when you’ve lost income. You usually have to ask.'),
    mc('Rent is due in 10 days and you were just laid off. Best move?', ['Talk to your landlord now and propose a payment plan in writing', 'Say nothing and hope', 'Move out tonight'], 0,
       'Landlords prefer a plan to a surprise.'),
    tf('Utility companies often have payment plans or assistance programs.', True, 'Ask before the shut-off notice.'),
    mc('When money is short, which bills come first?', ['Housing, utilities, food and getting to work', 'Streaming', 'Shopping'], 0, 'Keep a roof, the lights and food.'),
    sort('Pay first, or can it wait?', ['Pay first', 'Can wait or pause'],
         [('Rent', 0), ('Electricity', 0), ('Streaming subscription', 1), ('Groceries', 0), ('Gym membership', 1), ('Car insurance, if you need the car', 0)]),
    tf('A payment plan agreed in writing protects you better than a promise on the phone.', True, 'Get it in an email at least.'),
], fmt='call')

bare = lesson('sn-bare-bones', 'The Bare-Bones Budget', 'Survival mode, on purpose.', [
    info('Survival mode, on purpose',
         'A bare-bones budget covers only what keeps you housed, fed, healthy and able to find work. Everything else pauses until income is back.'),
    sort('Keep or pause in a bare-bones month?', ['Keep', 'Pause'],
         [('Rent', 0), ('Groceries', 0), ('Phone, needed for job hunting', 0), ('Takeout', 1), ('New clothes', 1), ('Streaming services', 1)]),
    alloc('Plan a bare-bones month on $2,000 from unemployment and savings. Rent is fixed at $1,100.', 2000, 50,
          [{'label': 'Rent', 'fixed': 1100}, {'label': 'Groceries', 'min': 300}, {'label': 'Utilities & phone', 'min': 150},
           {'label': 'Transport', 'min': 100}, {'label': 'Job search & other'}],
          'Essentials first, and every dollar has a job.'),
    num('Your normal month costs $3,100. Bare-bones costs $2,000. How much less is that?', 1100, '$3,100 − $2,000 = $1,100 a month.'),
    num('With $8,800 of savings covering bare-bones spending, how many full months does it last?', 4, '$8,800 ÷ $2,000 = 4.4, so 4 full months.', unit='months'),
    tf('Cutting to bare-bones early stretches savings the furthest.', True, 'Every early dollar saved buys time later.'),
], fmt='sort')

ana_story = {
    'title': 'Three lean months',
    'character': 'Ana, 27, call center agent',
    'body': 'Ana’s call center closed in March. She applied for unemployment the same week and gets **$380** a week. She also qualified for **$250** a month in SNAP.\n\n'
            'Her bare-bones costs come to **$2,300** a month, and she has **$3,000** saved.',
}
assert 380 * 4 == 1520 and 1520 + 250 == 1770 and 2300 - 1770 == 530 and 3000 // 530 == 5
ana = lesson('sn-ana', 'Ana’s Lean Months', 'Benefits plus savings plus a plan.', [
    num('Unemployment for 4 weeks?', 1520, '$380 × 4 = $1,520.'),
    num('Add SNAP. How much help comes in a month?', 1770, '$1,520 + $250 = $1,770.'),
    num('What’s the monthly shortfall against her $2,300 of costs?', 530, '$2,300 − $1,770 = $530.'),
    num('How many full months can her $3,000 cover that shortfall? Round down.', 5, '$3,000 ÷ $530 = 5.7, so 5 full months.', unit='months'),
    mc('What else could stretch Ana’s money?', ['Asking her phone company and utilities about hardship programs', 'Signing up for new subscriptions', 'A payday loan'], 0,
       'Every bill lowered adds time.'),
    tf('Ana’s plan works partly because she applied for help early.', True, 'Applying the same week meant no lost weeks of benefits.'),
], fmt='story', story=ana_story)

trial_steps = [
    num('Your old pay was $800 a week. Your state pays half, up to $375. What’s your weekly benefit?', 375, 'Half would be $400, but the $375 cap wins.'),
    tf('Unemployment benefits are taxable income.', True, 'Have tax withheld, or set some aside.'),
    mc('What does SNAP pay for?', ['Groceries', 'Rent', 'Car payments'], 0, 'Food.'),
    mc('When should you call a lender about a hardship program?', ['Before you miss a payment', 'After a few missed payments', 'Never'], 0, 'Early calls open more doors.'),
]

lessons = [ui, ui_math, apply_, food, health, lenders, bare, ana, review('sn'), trial('sn', 'Safety Nets', trial_steps)]
write_unit('08-safety-nets.json', 'safety-nets', 8, 'Unemployment & Safety Nets', 'The help that exists when income stops, and how to use it.',
           'Even the strongest wolf leans on the pack sometimes.', terms, lessons, section=S)
