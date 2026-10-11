from lib import *

S = 'earning'
terms = {
    'gig-work': term('Gig work', 'Short jobs, one at a time, often through an app: delivery, rideshare, task apps.', 'Delivering food through an app on weekends.'),
    'independent-contractor': term('Independent contractor', 'Someone paid for work as their own small business, not as an employee. No employer benefits, and no taxes taken out.',
                                   'A rideshare driver who sets their own hours and pays for their own gas.'),
    'form-1099': term('Form 1099', 'A tax form showing what a business paid you as a contractor. Nothing was taken out for taxes.',
                      'A delivery app sends you a 1099 showing $9,400 paid last year.'),
    'side-hustle': term('Side hustle', 'Paid work you do alongside your main job.', 'Tutoring math two evenings a week.'),
}

what = lesson('gw-what', 'What Gig Work Is', 'Freedom to choose your hours, and everything that comes with it.', [
    mc('Which is gig work?', ['Delivering food through an app', 'A salaried office job', 'A pension'], 0, 'One short job at a time, through an app.',
       context='[[Gig work]] is short jobs, one at a time, often through an app: delivery, rideshare, task apps.'),
    mc('As an independent contractor, who pays for your health insurance?', ['You do', 'The app', 'The government, always'], 0, 'No employer means no employer benefits.',
       context='Gig workers are usually [[independent contractors|independent-contractor]], not employees. Nobody sets your hours, but nobody gives you benefits either.'),
    sort('Employee or independent contractor?', ['Employee', 'Contractor'],
         [('Gets a W-2 each January', 0), ('Sets their own hours on a delivery app', 1), ('Gets a 401(k) match', 0),
          ('Pays both halves of Social Security and Medicare', 1), ('Gets overtime past 40 hours', 0), ('Pays for their own gas', 1)]),
    tf('Gig apps usually take taxes out of your pay.', False, 'Contractors get paid in full and owe the taxes themselves. More on that soon.'),
    mc('What’s the biggest upside of gig work?', ['Flexibility: work when you want', 'Guaranteed income', 'Free health insurance'], 0, 'You’re the boss of your schedule.'),
    mc('What’s the biggest downside?', ['Income goes up and down, with no benefits', 'Too many benefits', 'Fixed hours'], 0, 'Freedom comes with uncertainty.'),
], fmt='sort')

real = lesson('gw-real-pay', 'Your Real Hourly Pay', 'What the app shows isn’t what you earn.', [
    num('You earned $160 in 8 hours of driving. What’s that per hour, before costs?', 20, '$160 ÷ 8 = $20.',
        context='Apps show what you earned per job. Your real hourly pay is earnings minus costs, divided by every hour you were working, including waiting.'),
    num('Gas and wear on your car cost $48. What’s left?', 112, '$160 − $48 = $112.'),
    num('So what’s your real pay per hour over those 8 hours?', 14, '$112 ÷ 8 = $14.'),
    num('You also spent 2 unpaid hours waiting for orders. What’s your real pay per hour over all 10 hours?', 11.20, '$112 ÷ 10 = $11.20.'),
    mc('What matters most when choosing a gig?', ['Pay per hour after costs', 'Pay per order', 'How fun the app looks'], 0, 'The number that pays your rent.'),
    tf('Earning $25 per order always beats $18 an hour.', False, 'Not if each order takes two hours of driving.'),
])

sum_lines = [('earn', 'Delivery earnings', 412.00), ('tips', 'Tips', 96.50), ('gas', 'Gas', -71.20), ('wash', 'Car wash', -12.00), ('data', 'Phone data, work share', -10.00)]
SUM = doc('statement', 'Your driving week', sum_lines, subtitle='Self-made summary · Mon–Sun', meta=[['Hours online', '26'], ['Miles driven', '310']])
assert total([412, 96.50]) == 508.50 and total([71.20, 12, 10]) == 93.20 and total(l[2] for l in sum_lines) == 415.30
car = lesson('gw-car-costs', 'What Driving Really Costs', 'One week of a driver’s numbers, the honest way.', [
    num('How much did you earn, counting tips?', 508.50, '$412.00 + $96.50 = $508.50.', doc=SUM),
    num('What were the costs?', 93.20, '$71.20 + $12.00 + $10.00 = $93.20.', doc=SUM),
    num('What’s left after costs?', 415.30, '$508.50 − $93.20 = $415.30.', doc=SUM),
    num('Per hour, over 26 hours online? Round to the cent.', 15.97, '$415.30 ÷ 26 = $15.97.', doc=SUM),
    mc('Which hidden cost isn’t on this summary?', ['Wear and tear on the car', 'Gas', 'Tips'], 0,
       'Every mile costs tires, oil, repairs and value. It’s real money, just paid later.',
       context='Driving costs more than gas: tires, oil, repairs and the car losing value with every mile. The IRS lets drivers deduct a set amount per business mile because those costs are real.',
       doc=SUM),
    tf('Keeping a mileage log can lower the taxes you owe on gig income.', True, 'Business miles can be deducted. No log, no deduction.'),
], fmt='document')

taxes = lesson('gw-taxes', 'Taxes Nobody Takes Out', 'Contractors get paid in full, then owe the tax themselves.', [
    mc('What does a Form 1099 show?', ['What a business paid you as a contractor', 'Your bank balance', 'Your credit score'], 0, 'Your contractor income, with nothing taken out.',
       context='Apps and clients send you a [[Form 1099]] showing what they paid you. Nothing was taken out for taxes, so you owe them yourself.'),
    tf('If you don’t get a 1099, the income isn’t taxable.', False, 'All income counts, form or no form.'),
    num('You make $1,200 of profit this month. Set aside 25% for taxes. How much?', 300, '$1,200 × 0.25 = $300.',
        context='A common rule of thumb: set aside 25–30% of gig profit for taxes.'),
    mc('Where should tax money live?', ['A separate savings account you don’t touch', 'Your checking account with everything else', 'Spend it now, sort it out in April'], 0,
       'Out of sight, out of your budget.'),
    tf('Contractors pay both halves of Social Security and Medicare, about 15.3% in total.', True,
       'Employees pay 7.65% and their employer pays 7.65%. When you’re the business, you pay both.'),
    mc('Contractors who owe enough usually pay their taxes…', ['four times a year, in quarterly payments', 'never', 'once every five years'], 0,
       'You’ll see exactly how in Freelancing.'),
])

hustle = lesson('gw-side-hustle', 'Picking a Side Hustle', 'Skills, time and real hourly pay.', [
    mc('Which is a side hustle?', ['Tutoring math two evenings a week', 'Your full-time job', 'Your savings account'], 0, 'Paid work on the side.',
       context='A [[side hustle]] is paid work you do alongside your main job: dog walking, tutoring, reselling, freelancing.'),
    sort('Low or high cost to start?', ['Low cost to start', 'High cost to start'],
         [('Dog walking', 0), ('Tutoring', 0), ('A food truck', 1), ('Babysitting', 0), ('Opening a café', 1), ('Reselling clothes you already own', 0)]),
    mc('What matters most when picking one?', ['Your skills, your free time, and real pay per hour', 'What’s trending', 'What a friend does'], 0, 'Fit beats hype.'),
    num('Tutoring at $30 an hour, 4 hours a week, for 4 weeks. Monthly earnings?', 480, '$30 × 4 × 4 = $480.'),
    tf('A side hustle can burn you out if it eats all your free time.', True, 'Rest is part of the plan.'),
    mc('Your hustle earns $480 this month. What happens first?', ['Set aside taxes, then give the rest a job', 'Spend it', 'Quit your day job'], 0,
       'Taxes first, then the plan.'),
], fmt='sort')

pay_lines = [('jacket', 'Sale: denim jacket', 45.00), ('sneakers', 'Sale: sneakers', 80.00), ('sell', 'Selling fee, 10%', -12.50),
             ('proc', 'Payment processing, 3%', -3.75), ('instant', 'Instant payout fee', -5.00)]
PAY = doc('statement', 'ResellHub', pay_lines, subtitle='Payout summary · March')
assert total([12.5, 3.75, 5]) == 21.25 and total(l[2] for l in pay_lines) == 103.75
fees = lesson('gw-platform-fees', 'Platform Fees', 'Read the payout, not just the sale price.', [
    spot('Which fee could you have skipped by waiting a few days for your payout?', PAY, 'instant', 'Standard payouts are usually free. Instant costs extra.',
         context='Platforms take their cut in fees. Read the payout, not just the sale price.'),
    num('Add up the sales.', 125, '$45 + $80 = $125.', doc=PAY),
    num('What were the total fees?', 21.25, '$12.50 + $3.75 + $5.00 = $21.25.', doc=PAY),
    num('What did you actually get paid?', 103.75, '$125.00 − $21.25 = $103.75.', doc=PAY),
    num('What percent of your sales went to fees?', 17, '$21.25 ÷ $125 = 0.17, which is 17%.', unit='%'),
    tf('Comparing platforms’ fees can make the same sale worth more.', True, 'A 5% platform instead of 10% keeps $6.25 more here.'),
], fmt='spot')

casey_story = {
    'title': 'Weekend wheels',
    'character': 'Casey, 21, student',
    'body': 'Casey delivers food on weekends to save for a **$2,000** laptop.\n\n'
            'This weekend: **6** hours on Saturday for **$118**, and **5** hours on Sunday for **$97**. Gas cost **$38**.\n\n'
            'Casey puts **25%** of every weekend’s profit aside for taxes.',
}
assert 118 + 97 == 215 and 215 - 38 == 177 and round(177 / 11, 2) == 16.09 and 177 * 0.25 == 44.25
casey = lesson('gw-casey', 'Casey’s Weekend Hustle', 'One weekend of deliveries, start to finish.', [
    num('What did Casey earn this weekend?', 215, '$118 + $97 = $215.'),
    num('What’s left after gas?', 177, '$215 − $38 = $177.'),
    num('What’s Casey’s real pay per hour over 11 hours? Round to the cent.', 16.09, '$177 ÷ 11 = $16.09.'),
    num('How much goes aside for taxes at 25%?', 44.25, '$177 × 0.25 = $44.25.'),
    num('What can Casey actually put toward the laptop?', 132.75, '$177.00 − $44.25 = $132.75.'),
    mc('At $132.75 a weekend, about how many weekends until the $2,000 laptop?', ['About 15', 'About 5', 'About 50'], 0, '$2,000 ÷ $132.75 = 15.1 weekends.'),
], fmt='story', story=casey_story)

DOG = doc('bill', 'Dog walking', [('pay', '4 walks at $20', 80.00), ('cost', 'Costs', 0.00)], subtitle='Saturday morning, 3 hours')
RIDE = doc('bill', 'Rideshare', [('pay', 'Fares and tips', 95.00), ('gas', 'Gas', -22.00)], subtitle='Friday evening, 4 hours')
worth = lesson('gw-worth-it', 'Is It Worth It?', 'Compare two hustles the way that counts.', [
    mc('Which pays more per hour after costs?', ['Dog walking', 'Rideshare'], 0, 'Dog walking: $26.67 an hour. Rideshare: $18.25.', docs=[DOG, RIDE]),
    num('Dog walking per hour? Round to the cent.', 26.67, '$80 ÷ 3 = $26.67.', docs=[DOG, RIDE]),
    num('Rideshare per hour, after gas?', 18.25, '($95 − $22) ÷ 4 = $18.25.', docs=[DOG, RIDE]),
    mc('What else should you weigh?', ['Wear on your car, safety, and whether you enjoy it', 'Nothing else', 'Only the app rating'], 0,
       'The hourly number is the start, not the end.'),
    tf('The hustle with the bigger total isn’t always the better one.', True, 'Rideshare made more in total, but less per hour.'),
], fmt='call')

trial_steps = [
    num('$150 of gig profit. Set aside 25% for taxes. How much?', 37.50, '$150 × 0.25 = $37.50.'),
    tf('Independent contractors get overtime pay.', False, 'Overtime rules cover employees, not contractors.'),
    mc('What’s a Form 1099?', ['A record of what a business paid you as a contractor', 'A pay stub', 'A bank statement'], 0, 'And nothing was taken out for taxes.'),
    num('You earned $90 in 5 hours and spent $15 on gas. What’s your real hourly pay?', 15, '($90 − $15) ÷ 5 = $15.'),
]

lessons = [what, real, car, taxes, hustle, fees, casey, worth, review('gw'), trial('gw', 'Gig Work', trial_steps)]
write_unit('05-gig-work.json', 'gig-work', 5, 'Gig Work & Side Hustles', 'App gigs and side hustles: what they really pay after costs and taxes.',
           'Count every hour, including the ones you spend waiting.', terms, lessons, section=S)
