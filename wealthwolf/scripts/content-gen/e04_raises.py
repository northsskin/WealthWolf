from lib import *

S = 'earning'
terms = {
    'inflation': term('Inflation', 'Prices rising over time, so the same money buys a little less each year.', 'Groceries that cost $400 cost $420 after 5% inflation.'),
    'cost-of-living-adjustment': term('Cost-of-living adjustment', 'A raise meant to keep up with rising prices, not to reward performance. Often called a COLA.',
                                      'Everyone gets 3% in January because prices rose 3%.'),
    'merit-raise': term('Merit raise', 'A raise that rewards how well you did your job.', 'A 5% raise for beating your targets, when the average was 3%.'),
    'performance-review': term('Performance review', 'A regular meeting, often yearly, where your manager rates your work. Raises are often decided there.',
                               'Your December review: “exceeds expectations,” plus a 5% raise.'),
}

mathl = lesson('rp-math', 'Raise Math', 'Percent raises, in dollars.', [
    num('$50,000 with a 4% raise. What’s the new salary?', 52000, '$50,000 × 1.04 = $52,000.',
        context='Raises are usually a percent. To get the new pay, multiply by 1 plus the percent: a 4% raise is × 1.04.'),
    num('$20 an hour with a 5% raise. What’s the new rate?', 21, '$20 × 1.05 = $21.'),
    num('From $40,000 to $42,000. What percent raise is that?', 5, '$2,000 ÷ $40,000 = 0.05, which is 5%.', unit='%'),
    num('A 3% raise on $48,000 adds how much per year?', 1440, '$48,000 × 0.03 = $1,440.'),
    num('Paid every two weeks, how much more is that per paycheck, before deductions?', 55.38, '$1,440 ÷ 26 = $55.38.'),
    tf('A 3% raise on $60,000 is bigger in dollars than a 4% raise on $40,000.', True, '$1,800 vs. $1,600.'),
])

infl = lesson('rp-inflation', 'Raises vs. Rising Prices', 'A raise only counts if it beats rising prices.', [
    mc('Prices rose 3% this year. Your raise was 3%. Can you buy more than last year?', ['About the same', 'More', 'Less'], 0,
       'Your pay and your prices moved together.',
       context='[[Inflation]] is prices rising over time. If prices rise 3% a year, the same groceries cost 3% more next year.'),
    mc('Your raise was 2% and prices rose 4%. What happened to your buying power?', ['It shrank', 'It grew', 'No change'], 0,
       'Your pay went up less than your costs.'),
    num('A real raise is roughly your raise minus inflation. 5% raise, 3% inflation?', 2, '5% − 3% = about 2% more buying power.', unit='%'),
    mc('Your company gives everyone 3% to match rising prices. What is it?', ['A cost-of-living adjustment', 'A promotion', 'A bonus'], 0,
       'It keeps you level. It’s not a reward.',
       context='A [[cost-of-living adjustment]] (COLA) is a raise meant to keep up with rising prices, not to reward you.'),
    tf('A raise that only matches inflation leaves you no richer.', True, 'Same buying power as before.'),
    num('Groceries cost $400 a month. Prices rise 5%. What’s the new monthly cost?', 420, '$400 × 1.05 = $420.'),
])

types = lesson('rp-types', 'Kinds of Raises', 'Merit, cost-of-living and promotion: what each one means.', [
    mc('What decides a merit raise?', ['How well you did your job', 'Rising prices', 'Only the time of year'], 0, 'Performance, not the calendar.',
       context='A [[merit raise]] rewards how well you did. It’s often decided at your [[performance review]], a regular meeting about your work.'),
    sort('What kind of raise is it?', ['Merit raise', 'Cost-of-living', 'Promotion'],
         [('3% for everyone because prices rose', 1), ('A bigger raise for top performers', 0), ('New title, new duties, new pay', 2),
          ('An inflation adjustment in January', 1), ('A reward for beating your sales goals', 0), ('Moving from cashier to shift lead', 2)]),
    mc('Which usually brings the biggest jump in pay?', ['A promotion', 'A cost-of-living adjustment', 'Neither'], 0, 'New role, new pay band.'),
    tf('Switching jobs can bring a bigger raise than staying put.', True, 'Job changers often get bigger jumps, though it’s never guaranteed.'),
    num('Promoted from $46,000 to $53,000. What percent raise is that? Round to the nearest whole percent.', 15,
        '$7,000 ÷ $46,000 = 0.152, about 15%.', unit='%'),
    mc('Your review says “meets expectations” and you get 2%. Prices rose 3%. Best response?',
       ['Ask what it takes to earn more next time, and track it', 'Quit on the spot', 'Never mention it'], 0, 'Turn a weak raise into a plan.'),
], fmt='sort')

ask = lesson('rp-asking', 'Asking for a Raise', 'Raises go to people who ask, with proof.', [
    info('Build your case',
         'Raises usually go to people who ask, and back it up. Keep a running list of wins: problems solved, money saved, praise from customers. '
         'Then look up what your role pays elsewhere.'),
    order('Put asking for a raise in order.',
          ['Collect your wins and pay research', 'Ask your manager for a meeting', 'Make your case with a specific number', 'Agree on next steps and a date'],
          'Prepare, ask, propose, follow up.'),
    mc('When’s the best time to ask?', ['A few weeks before budgets or reviews are set', 'The day after a big mistake', 'During company layoffs'], 0,
       'Ask while the money is still being divided up.'),
    mc('What’s the strongest reason for a raise?', ['What you’ve achieved, and what the role pays elsewhere', 'Your rent went up', 'A coworker earns more'], 0,
       'Your value to them is the argument that works.',
       why=['', 'True, but it’s your problem, not their reason to pay more.', 'Risky, and it makes it about someone else.']),
    tf('If the answer is no, it’s fine to ask what would make it a yes later.', True, 'Get the goals in writing.'),
    num('You ask for 8% on $45,000. What number do you say?', 48600, '$45,000 × 1.08 = $48,600.'),
])

review_day = lesson('rp-review-day', 'Review Day', 'Your manager offers a number. What do you say?', [
    mc('Your manager offers 3%. Your research says the role pays 10% more elsewhere. Best response?',
       ['Thank them, share your research, and ask if 6% is possible', 'Accept quietly', 'Threaten to quit'], 0,
       'Calm, specific and backed by numbers.',
       why=['', 'You leave money on the table without even asking.', 'Only threaten what you’re ready to do.']),
    mc('They say the budget is frozen until summer. Next move?', ['Ask to revisit it in summer, in writing', 'Give up for good', 'Complain to coworkers'], 0,
       'A date in writing is a promise you can come back to.'),
    mc('They offer a better title but no raise. What do you ask?', ['When the pay for that title will follow', 'Nothing', 'For a new chair'], 0,
       'Titles are nice. Pay is nicer.'),
    tf('Getting your goals agreed in writing makes the next raise conversation easier.', True, 'Hit the goals, point to the email.'),
    num('You negotiate from 3% to 5% on $50,000. How much more per year is that?', 1000, '2% of $50,000 = $1,000.'),
    mc('Your raise comes through. First thought?', ['Give the extra money a job before it disappears', 'Upgrade everything', 'Nothing'], 0,
       'That’s the last lesson in this unit.'),
], fmt='call')

stack = lesson('rp-stacking', 'Raises Stack Up', 'Every raise builds on the last one.', [
    num('$40,000 with a 5% raise this year and 5% again next year. What’s the pay after two years?', 44100,
        '$40,000 × 1.05 = $42,000. $42,000 × 1.05 = $44,100.',
        context='Raises build on each other: next year’s raise is a percent of this year’s bigger pay.'),
    num('Compare: two raises of $2,000 each. Pay after two years?', 44000, '$40,000 + $2,000 + $2,000 = $44,000.'),
    mc('Why is the percent version a bit higher?', ['The second raise is 5% of a bigger number', 'Luck', 'Taxes'], 0, '5% of $42,000 beats 5% of $40,000.'),
    num('Starting at $48,000 vs. $45,000, both with a 3% raise. How far apart are they after one year?', 3090,
        '$49,440 − $46,350 = $3,090. The gap grows with every raise.'),
    tf('Your starting salary matters because every future raise builds on it.', True, 'That’s why negotiating it is worth it.'),
    mc('Which helps most over a career?', ['Higher starting pay plus regular raises', 'One big bonus', 'Never changing jobs'], 0, 'Growth on top of a good base.'),
])

ty_story = {
    'title': 'Promotion or pay cut?',
    'character': 'Ty, 29, cashier',
    'body': 'Ty earns **$17.50** an hour and works about **38** hours a week.\n\n'
            'The store offers Ty a promotion to shift lead: a salary of **$41,000** a year. The catch: shift leads work about **45** hours a week, '
            'and as a salaried manager Ty wouldn’t get overtime.',
}
assert 17.5 * 38 * 52 == 34580 and 45 * 52 == 2340 and round(41000 / 2340, 2) == 17.52
ty = lesson('rp-promotion', 'Ty’s Promotion', 'A bigger number can hide a smaller hourly rate.', [
    num('What does Ty earn now in a year? $17.50 × 38 hours × 52 weeks.', 34580, '$17.50 × 38 × 52 = $34,580.'),
    num('How much more a year is the salaried offer?', 6420, '$41,000 − $34,580 = $6,420.'),
    num('At 45 hours a week, how many hours a year is the new job?', 2340, '45 × 52 = 2,340 hours.', unit='hours'),
    num('What does the new job pay per hour? $41,000 ÷ 2,340, rounded to the cent.', 17.52, '$41,000 ÷ 2,340 = $17.52.'),
    mc('So is it a raise per hour?', ['Barely: 2 cents more an hour, for 7 more hours a week', 'Yes, a big one', 'No, it’s a pay cut'], 0,
       'More money, but almost all of it is from working more.'),
    mc('What could make the promotion worth it anyway?', ['The title and experience lead to bigger raises later', 'Nothing', 'The new uniform'], 0,
       'Sometimes the next step pays off at the step after.'),
], fmt='story', story=ty_story)

job = lesson('rp-give-raise-a-job', 'Give Your Raise a Job', 'Catch the raise before lifestyle creep does.', [
    mc('Your take-home rose $200 a month. Six months later you have no more saved. What happened?', ['Lifestyle creep ate it', 'Taxes', 'Only inflation'], 0,
       'The extra money quietly turned into extra spending.',
       context='When pay goes up, spending tends to drift up too. That’s [[lifestyle creep]], and it eats raises.'),
    mc('What’s a simple rule many people use for raises?', ['Save at least half of every raise', 'Spend all of it', 'Save none of it'], 0,
       'Half for future you, half to enjoy.'),
    alloc('Your take-home went up $300 a month. Plan it: at least half goes to savings and goals.', 300, 10,
          [{'label': 'Savings & goals', 'min': 150}, {'label': 'Fun & treats'}, {'label': 'Bills that went up'}],
          'Savings got at least $150 and every dollar has a job.'),
    num('Saving $150 a month from a raise for a year adds up to?', 1800, '$150 × 12 = $1,800.'),
    tf('Raising your 401(k) contribution by 1% with each raise is an easy habit.', True, 'You never miss money you never got used to.'),
    order('Raise day: put it in order.', ['Check your new take-home pay', 'Increase your savings first', 'Update your budget', 'Enjoy the rest guilt-free'],
          'Know it, save it, plan it, enjoy it.'),
], fmt='sort')

trial_steps = [
    num('$52,000 with a 3% raise. What’s the new salary?', 53560, '$52,000 × 1.03 = $53,560.'),
    mc('Your raise was 3% and prices rose 4%. Your buying power…', ['shrank', 'grew', 'stayed exactly the same'], 0, 'Prices beat your raise.'),
    tf('A promotion usually brings a bigger jump than a cost-of-living adjustment.', True, 'New role, new pay band.'),
    num('From $30.00 to $31.50 an hour. What percent raise is that?', 5, '$1.50 ÷ $30 = 0.05, which is 5%.', unit='%'),
]

lessons = [mathl, infl, types, ask, review_day, stack, ty, job, review('rp'), trial('rp', 'Raises & Promotions', trial_steps)]
write_unit('04-raises.json', 'raises', 4, 'Raises & Promotions', 'Raise math, rising prices, and how to ask for more.',
           'Nobody hands the meat to the wolf who waits by the door.', terms, lessons, section=S)
