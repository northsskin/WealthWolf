from lib import *

S = 'earning'
terms = {
    'employee-benefits': term('Employee benefits', 'Everything a job gives you besides your paycheck: health insurance, retirement money, paid time off and more.',
                              'An employer paying $500 a month toward your health insurance.'),
    'premium': term('Premium', 'What you pay to keep insurance active, whether or not you use it.', '$65 a paycheck for your work health plan.'),
    '401k': term('401(k)', 'A retirement account you get through work. Money goes in straight from your paycheck and is invested until you retire.',
                 'Putting 5% of each paycheck into your company’s 401(k).'),
    'employer-match': term('Employer match', 'Money your employer adds to your 401(k) when you put money in yourself.',
                           '50 cents for every dollar you save, up to 6% of your pay.'),
    'vesting': term('Vesting', 'Earning full ownership of your employer’s match over time. Leave too early and you may lose part of it.',
                    '25% of the match becomes yours for each full year you stay.'),
    'paid-time-off': term('Paid time off', 'Days you’re paid for without working: vacation, sick days and holidays. Often shortened to PTO.',
                          '15 PTO days a year at $200 a day is worth $3,000.'),
    'open-enrollment': term('Open enrollment', 'The window each year, usually a few weeks, when you can choose or change your work benefits.',
                            'Every November, pick next year’s health plan and 401(k) rate.'),
}

what = lesson('jb-what', 'What Benefits Are Worth', 'Your pay is more than your paycheck.', [
    info('Pay is more than the paycheck',
         '[[Employee benefits|employee-benefits]] are everything a job gives you besides your paycheck: health insurance, retirement money, paid time off and more.\n\n'
         'They’re worth real money, often thousands of dollars a year. Two jobs with the same salary can be worlds apart.'),
    sort('Benefit or not?', ['Benefit', 'Not a benefit'],
         [('Health insurance the company helps pay for', 0), ('Paid vacation days', 0), ('A 401(k) match', 0),
          ('Your regular paycheck', 1), ('Overtime pay', 1), ('A tip from a customer', 1)]),
    num('Your employer pays $500 a month toward your health insurance. What’s that worth over a year?', 6000, '$500 × 12 = $6,000.'),
    mc('Two jobs pay $50,000. One includes health insurance, the other doesn’t. Which really pays more?', ['The one with health insurance', 'They’re the same'], 0,
       'Thousands of dollars of coverage is real pay, just not in your bank account.'),
    tf('Benefits can be worth thousands of dollars a year.', True, 'Health insurance alone often is.'),
    mc('Where do you find a job’s benefits?', ['The offer letter and the benefits guide', 'Your bank statement', 'The company’s social media'], 0,
       'Ask for the benefits guide before you accept.'),
])

health = lesson('jb-health', 'Health Insurance at Work', 'What it costs you, and what your employer chips in.', [
    mc('What’s a premium?', ['What you pay to keep insurance, used or not', 'A bonus', 'A doctor’s bill'], 0,
       'You pay it every month, whether or not you see a doctor.',
       context='A [[premium]] is what you pay to keep insurance active. At work it usually comes out of each paycheck, and your employer often pays a big share too.'),
    num('Your health premium is $65 a paycheck, 26 paychecks a year. What’s the yearly cost to you?', 1690, '$65 × 26 = $1,690.'),
    num('The full plan costs $7,800 a year and you pay $1,690. How much does your employer pay?', 6110, '$7,800 − $1,690 = $6,110.'),
    tf('Work health insurance premiums are usually taken out before tax.', True, 'Another reason work coverage is a good deal.'),
    mc('Adding a spouse or kids to your plan usually…', ['raises your premium', 'lowers it', 'doesn’t change it'], 0, 'More people covered, higher premium.'),
    mc('You’re young and healthy. Should you skip work health insurance to keep the $65?',
       ['No: one accident can cost far more than a year of premiums', 'Yes, always', 'Only in summer'], 0,
       'A broken leg can cost tens of thousands of dollars without insurance.'),
])

k401 = lesson('jb-401k', 'The 401(k)', 'Retirement saving, straight from your paycheck.', [
    mc('Where does 401(k) money come from?', ['Straight from your paycheck', 'Your savings account', 'The government'], 0,
       'It’s taken out before you ever see it.',
       context='A [[401(k)|401k]] is a retirement account you get through work. Money goes in straight from your paycheck, and it’s invested to grow until you retire.'),
    tf('Money in a traditional 401(k) goes in before income tax.', True, 'That lowers your tax bill today.'),
    num('You put in 5% of a $50,000 salary. How much is that a year?', 2500, '$50,000 × 0.05 = $2,500.'),
    mc('In 2026, what’s the most you can put into a 401(k) yourself (under age 50)?', ['$24,500', '$2,450', '$245,000'], 0,
       'The IRS sets the limit each year. For 2026 it’s $24,500.'),
    mc('Why start a 401(k) in your twenties instead of your forties?', ['Twenty extra years of growth', 'It’s required', 'Taxes are lower in your forties'], 0,
       'Time is the biggest ingredient in growth.'),
    tf('Taking money out of a 401(k) before age 59½ usually means taxes plus a 10% penalty.', True, 'It’s built for retirement, and the rules enforce it.'),
    fill('A 401(k) is a ___ account you get through work.', ['retirement', 'checking', 'credit'], 0, 'Retirement.'),
])

match_ = lesson('jb-match', 'The Employer Match', 'Free money. Here’s how not to leave it on the table.', [
    mc('What’s an employer match?', ['Money your employer adds when you save', 'A team sport', 'A tax'], 0, 'It’s extra pay, delivered to your retirement account.',
       context='Many employers add money to your 401(k) when you do. That’s an [[employer match]]. A common one: 50 cents for every dollar you put in, up to 6% of your pay.'),
    num('Salary $50,000. You put in 6% ($3,000), and your employer matches 50% of that. How much do they add?', 1500, '$3,000 × 0.50 = $1,500.'),
    num('If you only put in 2% ($1,000), how much would they add?', 500, '$1,000 × 0.50 = $500.'),
    num('How much free money do you leave on the table by putting in 2% instead of 6%?', 1000, '$1,500 − $500 = $1,000 a year.'),
    mc('Best move when there’s a match?', ['Put in at least enough to get the full match', 'Skip it while you’re young', 'Put in 1%'], 0,
       'An instant return you can’t get anywhere else.'),
    tf('A 100% match on your first 4% doubles that money instantly.', True, 'Put in $100, and $200 lands in the account.'),
])

lee_story = {
    'title': 'Leaving money behind',
    'character': 'Lee, 27, logistics coordinator',
    'body': 'Lee put **$6,000** of pay into the company 401(k) over two years. The employer added **$3,000** in matching money.\n\n'
            'But the match comes with [[vesting]]: Lee only fully owns it after a set time. This company vests **25%** of the match for every full year worked.\n\n'
            'Lee has a new job offer paying **$2,000** a year more, and would leave after exactly **2** years.',
}
lee = lesson('jb-vesting', 'Lee Leaves Early', 'Your match might not be all yours yet. Do the math before you go.', [
    num('How much of Lee’s own $6,000 can Lee keep?', 6000, 'All of it. Your own contributions are always yours.'),
    num('What percent of the match is vested after 2 full years?', 50, '25% × 2 years = 50%.', unit='%'),
    num('How much of the $3,000 match can Lee take?', 1500, '50% of $3,000 = $1,500.'),
    num('What’s the total Lee leaves with?', 7500, '$6,000 + $1,500 = $7,500.'),
    mc('Staying 2 more years would vest the other $1,500. Is leaving still worth it?',
       ['Probably: $2,000 more a year beats a one-time $1,500', 'Never leave before vesting', 'Only if the new job has no match'], 0,
       '$4,000 more pay over two years beats $1,500 of match. Just know the trade-off.'),
    tf('Your own 401(k) contributions are always 100% yours.', True, 'Vesting only applies to the employer’s money.'),
], fmt='story', story=lee_story)

pto = lesson('jb-pto', 'Paid Time Off', 'Days off you’re paid for are worth real money.', [
    mc('What does PTO mean?', ['Days you’re paid for without working', 'Unpaid leave', 'Overtime'], 0, 'Vacation, sick days and holidays, paid.',
       context='[[Paid time off|paid-time-off]] (PTO) is days you’re paid for without working: vacation, sick days and holidays.'),
    num('You earn $25 an hour. One PTO day is 8 hours. What’s it worth?', 200, '$25 × 8 = $200.'),
    num('15 PTO days a year at $200 each. What are they worth?', 3000, '15 × $200 = $3,000.'),
    mc('Your company is use-it-or-lose-it, and you have 5 days left in December. Smart move?', ['Use them', 'Let them disappear', 'Ask to be paid less'], 0,
       'Unused days under that rule are just lost pay.', context='Some companies have “use it or lose it” rules: unused days vanish at the end of the year.'),
    tf('Every US employer must give paid vacation.', False, 'No federal law requires paid vacation. That’s why it’s worth comparing between offers.'),
    mc('Same pay. Job A gives 10 PTO days, Job B gives 20. Job B is worth roughly…', ['10 extra paid days off a year', 'Nothing extra', 'Less'], 0,
       'Two extra weeks off, paid.'),
])

menu = lesson('jb-menu', 'The Benefits Menu', 'What each benefit does for you, and what to grab first.', [
    sort('What does each benefit do for you?', ['Saves money now', 'Builds future wealth', 'Protects you'],
         [('Commuter pass paid before tax', 0), ('401(k) match', 1), ('Life insurance', 2), ('Gym discount', 0),
          ('Disability insurance', 2), ('Company stock purchase plan', 1)]),
    mc('Which benefit should almost everyone take first?', ['Enough 401(k) to get the full match', 'The gym discount', 'Pet insurance'], 0,
       'Free money comes first.'),
    tf('Under 26, you can usually stay on a parent’s health plan instead of your job’s.', True, 'Compare the costs. Either one can be cheaper.'),
    num('A commuter benefit lets you pay your $150 monthly transit pass before tax. At a 22% tax rate, how much does that save a month?', 33,
        '$150 × 0.22 = $33.'),
    mc('A benefit you’ll never use (pet insurance, and you have no pet) is worth…', ['Nothing to you, so skip it', 'Its full price', 'More than cash'], 0,
       'Only pick what you’ll use.'),
], fmt='sort')

guide_lines = [('health', 'Health insurance, employer share', 6400.00), ('match', '401(k) match: 100% of the first 4% you save', 1920.00),
               ('life', 'Life insurance, 1× salary', 180.00), ('commute', 'Commuter pass', 900.00)]
GUIDE = doc('bill', 'Northwind Logistics', guide_lines, subtitle='Benefits summary · What we pay each year',
            meta=[['Salary', '$48,000'], ['Paid time off', '15 days']])
assert total(l[2] for l in guide_lines) == 9400 and 48000 * 0.04 == 1920
guide = lesson('jb-benefits-guide', 'Read a Benefits Summary', 'Add up what an employer really pays you.', [
    num('Add up what the employer pays toward benefits each year.', 9400, '$6,400 + $1,920 + $180 + $900 = $9,400.', doc=GUIDE),
    num('Salary plus benefits: what’s the total yearly value?', 57400, '$48,000 + $9,400 = $57,400.', doc=GUIDE),
    mc('Which benefit do you only get if you put in money yourself?', ['The 401(k) match', 'The health insurance share', 'The life insurance'], 0,
       'No saving from you, no match.', doc=GUIDE),
    num('If you only put in 2% of your $48,000, how much match would you get?', 960, '$48,000 × 0.02 = $960.', doc=GUIDE),
    mc('You miss open enrollment. What usually happens?', ['You wait until next year, unless a big life event happens', 'You get every benefit automatically', 'You lose your job'], 0,
       'Marriage, a baby or losing other coverage can open a special window. Otherwise, mark the dates.',
       context='[[Open enrollment]] is the window each year, usually a few weeks, when you choose or change your benefits.'),
    tf('Most of these benefits aren’t taxed as part of your pay.', True, 'Which makes each dollar of benefits worth even more.'),
], fmt='document')

trial_steps = [
    num('Salary $60,000. Your employer matches 50% of what you put in, up to 6%. You put in 6%. What’s the match?', 1800, '$3,600 × 0.50 = $1,800.'),
    tf('Your own 401(k) money is always fully yours, even if you leave early.', True, 'Vesting only applies to the employer’s share.'),
    mc('What’s an insurance premium?', ['What you pay to keep the coverage', 'A bonus for being healthy', 'A doctor’s fee'], 0, 'Paid whether or not you use it.'),
    num('12 PTO days at $160 a day. What are they worth?', 1920, '12 × $160 = $1,920.'),
]

lessons = [what, health, k401, match_, lee, pto, menu, guide, review('jb'), trial('jb', 'Job Benefits', trial_steps)]
write_unit('02-job-benefits.json', 'job-benefits', 2, 'Job Benefits', 'Health insurance, the 401(k) match and paid time off: the pay you don’t see.',
           'Free money on the table is still on the table. Take it.', terms, lessons, section=S)
