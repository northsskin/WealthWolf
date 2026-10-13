from lib import *

S = 'building-wealth'
terms = {}

need_doc = doc('statement', 'A retirement sketch',
                 [('pay', 'Pay today', 80000), ('spend', 'Spending target at 75%', 60000)],
                 subtitle='Rules of thumb, not a bill',
                 note='The portfolio sketch is 25 times the spending target, which is $1,500,000.')

need = lesson('rt-need', 'How Much You Might Need', 'A sketch, then a pile.', [
    info('Two rules of thumb, stacked',
         'One common sketch says a retirement might replace 70% to 80% of pay, because you stop saving and some costs fall. Another is the [[FI number|fi-number]]: about 25 times the spending you still have. On $80,000 of pay, 75% is $60,000 of spending. Twenty-five times that is $1,500,000. Both figures are rules of thumb, not a bill.'),
    num('What is the spending target on this page, in dollars?', 60000,
        doc=need_doc,
        explain='$80,000 × 0.75 = $60,000.'),
    num('What is 25 times that $60,000 spending target?', 1500000,
        '25 × $60,000 = $1,500,000. That is the portfolio sketch, not a balance you are required to have on a date.'),
    tf('Replacing 75% of pay is a law.', False,
       'It is a rule of thumb. A paid-off house, a pension, or a more expensive city can move the percent.'),
    mc('What does the $1,500,000 represent here?',
       ['A guaranteed account balance', 'About 25 times the $60,000 spending sketch', 'The federal funds rate'], 1,
       'Twenty-five times spending. Social Security, if you have it, can cover part of the spending so the portfolio does less.'),
], fmt='document')

band = lesson('rt-band', '70% to 80%', 'The band is the spending, not a score.', [
    info('Why not 100%',
         'You may not need the whole paycheck. You stop the [[savings rate|savings-rate]], and you may drop commuting and payroll taxes. You still eat. The 70% to 80% band is the usual sketch. Run your own spending. Do not borrow a stranger’s percent.'),
    num('At the low end, 70% of $80,000 is how many dollars?', 56000,
        '$80,000 × 0.70 = $56,000.'),
    num('At the high end, 80% of $80,000 is how many dollars?', 64000,
        '$80,000 × 0.80 = $64,000.'),
    num('How wide is that band, in dollars?', 8000,
        '$64,000 − $56,000 = $8,000. The band is a range, which is why a calculator asks for your spending, not a slogan.'),
    tf('You should always target 100% of your paycheck, because the band is too narrow to matter.', False,
       'The band is $8,000 wide on this pay, and the real input is your spending. One hundred percent ignores the costs that stop.'),
])

early = lesson('rt-early', 'Starting at 25 or at 35', 'The extra decade is deposits, before any growth.', [
    info('Ten quiet years',
         'Two people invest $200 a month. One starts at 25, the other at 35. By 35 the first person has already deposited 10 years of contributions. Growth, if it comes, is extra. This lesson grades the deposits, not a promised balance.'),
    num('How many dollars is $200 a month for one year?', 2400,
        '12 × $200 = $2,400.'),
    num('How many dollars does the 25-year-old deposit in the 10 years before the other person starts?', 24000,
        '10 × $2,400 = $24,000. That money also has 10 extra years to compound. The $24,000 is only the deposits.'),
    tf('Starting at 35 deposits the same dollars by age 35 as starting at 25.', False,
       'The later start has deposited $0 of this plan by 35. The earlier start has deposited $24,000.'),
    mc('What is the part this lesson will not pretend to know?',
       ['The deposits', 'The future return', 'That 12 months make a year'], 1,
       'The return is a guess. The deposits are arithmetic.'),
])

calc = lesson('rt-calc', 'Retirement Calculators', 'A machine that multiplies your guesses.', [
    info('Inputs, then a picture',
         'A retirement calculator needs spending, how many years the money has, and a return you type in. Change the return and the picture changes. The picture is not a promise. Use it to see which input matters. Do not use it as a date the market owes you.'),
    mc('Which input is a guess, not a fact?',
       ['The return you type in', 'The number of months in a year', 'A savings deposit you already made'], 0,
       'The return is the guess. The calculator will honor whatever you type, including a fantasy.'),
    tf('Two calculators must agree if you give them different return guesses.', False,
       'The guess is the engine. Different guesses, different pictures.'),
    mc('What is the honest use of the tool?',
       ['To see how spending and time move the sketch', 'To lock in a balance the market must deliver', 'To replace an emergency fund'], 0,
       'A sketch of your inputs. The emergency fund is still cash, outside the picture.'),
    fill('The return you type into a calculator is a ___.',
         ['guess', 'coupon', 'will'], 0,
         'A guess. Treat the output with the same humility.'),
])

order_accounts = lesson('rt-order', 'Which Account, in What Order', 'A common line. Not the only life.', [
    info('The usual queue',
         'A common order: take the full [[employer match|employer-match]] first, because it is pay. Then a [[health savings account|health-savings-account]] if you have a qualifying health plan. Then an [[IRA|traditional-ira]] or [[Roth IRA|roth-ira]] if you are allowed one. Then fill more of the [[401(k)|401k]]. A taxable brokerage is the pile after the tax-favored ones. High-interest debt can jump the line. This is a common order, not a personal instruction.'),
    order('Put this common queue in order. Leave the taxable brokerage last.',
          ['Take the full employer match',
           'Use an HSA if you qualify',
           'Contribute to an IRA if you are allowed',
           'Fill more of the 401(k)',
           'Use a taxable brokerage for what is left'],
          'The match is first because it is extra pay. The brokerage is last because the others are tax-favored.'),
    tf('Skipping the match to buy a single stock in a brokerage is the common order.', False,
       'The match comes first. A single stock is not the queue.'),
    mc('Why is the match usually first?',
       ['Because it is extra pay on top of what you put in', 'Because a 401(k) cannot hold a fund', 'Because IRAs are illegal if you match'], 0,
       'The match is part of the job. Leaving it is leaving pay.'),
    mc('When might high-interest debt jump ahead of extra investing?',
       ['When the debt’s interest is the more expensive leak', 'Never, because investing is always first', 'Only if a headline says so'], 0,
       'A very expensive debt can outrank extra investing. The match is still hard to beat, because it is an instant return.'),
])

catch = lesson('rt-catch', 'Catching Up Later', 'The age add-on is real. It is not magic.', [
    info('The 2026 add-on',
         'In 2026 the employee [[401(k)|401k]] limit is $24,500, plus an $8,000 catch-up at age 50, for $32,500. The IRA limit is $7,500, plus $1,100 at 50, for $8,600. The catch-up is an age rule. It does not replace the years you did not contribute. A 45-year-old does not get it yet.'),
    num('At age 50 in 2026, what is the total employee 401(k) deferral including the $8,000 catch-up?', 32500,
        '$24,500 + $8,000 = $32,500.'),
    num('At age 50 in 2026, what is the total IRA limit including the catch-up?', 8600,
        '$7,500 + $1,100 = $8,600.'),
    tf('A 45-year-old can use the age-50 catch-up in 2026.', False,
       'The catch-up starts at 50. Forty-five gets the base limits only.'),
    mc('What can the catch-up not do?',
       ['Raise the limit at the ages the IRS names', 'Replace a decade of missing deposits', 'Sit on top of the base limit'], 1,
       'It adds room later. It does not rewind the years.'),
])

checklist = lesson('rt-list', 'A Retirement Checklist', 'Write it while the date is still far.', [
    info('One page, in order',
         'A plan you can reread: the spending guess, the accounts in the common order, the mix that matches the date, and a day each year to look. The look is not a daily vote on red numbers.'),
    order('Put the checklist in the order you would write it.',
          ['Write the yearly spending you are actually aiming at',
           'Take the employer match, then the rest of the account order',
           'Pick a mix that matches when you need the money',
           'Choose a calm date each year to look again'],
          'Spending first, because it sets the target. The mix follows the date. The yearly look keeps you out of the daily app.'),
    tf('The checklist is finished when you pick a stock from a headline.', False,
       'A headline stock is not on the list. The list is spending, the match, the mix, and a date to look.'),
    mc('Why does spending come before the funds?',
       ['Because the target is a multiple of spending', 'Because funds do not charge fees', 'Because Social Security sets your rent'], 0,
       'Twenty-five times spending, or 70% to 80% of pay, both start with a spending number.'),
    fill('Look at the plan on a calm date, not on a ___ day.',
         ['red', 'match', 'credit'], 0,
         'A red day is noise if the date you need the money has not changed.'),
])

marcus = lesson('rt-marcus', 'Marcus at 45', 'Twenty years, and the catch-up is not here yet.', [
    info('Meet Marcus',
         'Marcus is 45 and an electrician. He can invest $500 a month. He is five years short of the age-50 catch-up, so 2026’s extra room is not his yet. He takes his job’s match first.\n\nTwenty years of $500 a month, before any growth, is $120,000 of deposits. He is later than a 25-year-old. He is not at zero.',
         ),
    num('How many dollars a year is Marcus’s $500 a month?', 6000,
        '12 × $500 = $6,000.'),
    num('Over 20 years, how many dollars does he deposit before growth?', 120000,
        '20 × $6,000 = $120,000.'),
    tf('Marcus can add the 2026 age-50 catch-up this year.', False,
       'He is 45. The catch-up is an age rule, and 50 has not arrived.'),
    mc('What does he do before he buys anything fancy in a brokerage?',
       ['Takes the employer match', 'Skips the match to pick one stock', 'Empties the emergency fund'], 0,
       'The match is first. The $500 is the investing pile, not the cash pile.'),
], fmt='story', story={
    'title': 'Twenty years from 45',
    'character': 'Marcus, 45, electrician',
    'body': 'Marcus can invest **$500** a month. He is **45**, so the age-50 catch-up is not his yet. He takes the match first.\n\nTwenty years of deposits, before growth, are **$120,000**.',
})

write_unit('04-retirement-planning.json', 'retirement-planning', 4, 'Planning for Retirement',
           'A spending sketch, the account order, and the years you still have.',
           'The target is a multiple of spending. The match still comes first.',
           terms, [need, band, early, calc, order_accounts, catch, checklist, marcus, review('rt'), trial('rt', 'Planning for Retirement', [
               num('80% of $50,000 pay is how many dollars of yearly spending?', 40000,
                   '$50,000 × 0.80 = $40,000.'),
               num('$300 a month for 10 years is how many dollars of deposits, before growth?', 36000,
                   '12 × $300 = $3,600, and 10 × $3,600 = $36,000.'),
               tf('The age-50 catch-up is available at 45.', False,
                  'The 2026 catch-up starts at 50. Forty-five uses the base limit.'),
               mc('In the common account order, what usually comes first?',
                  ['A taxable brokerage full of one stock', 'The full employer match', 'A coin'], 1,
                  'The match is extra pay. The brokerage is the pile after the tax-favored accounts.'),
           ])],
           section=S)
