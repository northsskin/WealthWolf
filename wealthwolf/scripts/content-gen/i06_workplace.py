from lib import *

S = 'investing'
terms = {
    'roth-401k': term('Roth 401(k)',
                      'A 401(k) you fund with pay that has already been taxed. Qualified withdrawals in retirement are tax-free. It is not a Roth IRA, and it does not use the Roth IRA income limit.',
                      'Choosing the Roth option inside the workplace plan for $1,000 of pay.'),
}

rate = lesson('wr-rate', 'The Contribution Rate', 'A percent of pay, every paycheck.', [
    info('The percent',
         'The contribution rate is the slice of pay that goes into the [[401(k)|401k]] before you see it. Jamie, from the earning section, earns $52,000 and currently sends 4%. This employer matches 50 cents per dollar you put in, up to 6% of pay. That match is this plan’s rule, not a law.'),
    num('Jamie earns $52,000 and contributes 4%. How many dollars a year is that?', 2080,
        '0.04 × $52,000 = $2,080.'),
    num('The match is 50% of what Jamie puts in, and 4% is under the 6% cap. How many match dollars is that?', 1040,
        '0.50 × $2,080 = $1,040. The plan will not match past 6% of pay.'),
    num('To get the full match, Jamie needs to contribute 6%. How many dollars a year is 6% of $52,000?', 3120,
        '0.06 × $52,000 = $3,120. The match on that would be half, $1,560.'),
    tf('The employer match is required by law to be 50% up to 6%.', False,
       'This lesson uses one plan’s rule. Another employer can match more, less, or nothing. Read your plan.'),
])

trad_page = doc('statement', 'Traditional 401(k)',
                [('in', 'Contribution', 1000), ('save', 'Tax saved this year in the 12% bracket', 120)],
                subtitle='Pre-tax. Taxable pay falls by $1,000.',
                note='The withdrawal in retirement is taxed.')
roth_page = doc('statement', 'Roth 401(k)',
                [('in', 'Contribution', 1000), ('save', 'Tax saved this year', 0)],
                subtitle='After-tax. No break this year.',
                note='Qualified withdrawals in retirement are tax-free.')

which = lesson('wr-which', 'Traditional or Roth 401(k)', 'The tax break now, or the tax break later.', [
    info('Same plan, two tax doors',
         'A traditional [[401(k)|401k]] contribution is a [[pre-tax deduction|pre-tax-deduction]]. In the 12% bracket, $1,000 contributed saves $120 of tax this year. A [[Roth 401(k)|roth-401k]] uses pay that was already taxed, so this year saves $0. Qualified Roth withdrawals later are tax-free. Neither door is a Roth IRA.'),
    mc('Which page lowers this year’s taxable pay?',
         [trad_page['title'], roth_page['title']], 0,
         docs=(trad_page, roth_page),
         explain='The traditional page is the pre-tax one. $1,000 × 0.12 = $120 saved this year. The Roth page takes the tax break later, if the withdrawal is qualified.'),
    num('In the 12% bracket, how many dollars of tax does a $1,000 traditional contribution save this year?', 120,
        '$1,000 × 0.12 = $120. A $1,000 Roth contribution saves $0 this year.'),
    tf('A Roth 401(k) uses the same income limit as a Roth IRA.', False,
       'The Roth IRA income limit is for the IRA. A Roth 401(k), if your plan offers it, does not use that limit.'),
    mc('You expect a higher tax bracket in retirement than the 12% you pay now. Which door takes the tax at today’s lower rate?',
       ['Traditional, which delays the tax', 'Roth, which pays the tax now', 'Neither, because 401(k) money is never taxed'], 1,
       'Roth pays now, at the current rate, and a qualified withdrawal later is tax-free. Traditional does the reverse. This is a sketch, not advice for your bracket.'),
], fmt='call')

menu = doc('statement', 'Plan menu, fees on $10,000',
           [('us', 'US stock index fund, yearly fee', 4),
            ('intl', 'International stock index fund, yearly fee', 6),
            ('bond', 'Bond index fund, yearly fee', 5),
            ('co', 'Your employer’s own stock, yearly fee', 0)],
           subtitle='Four choices. The $0 fee is not the safe one.',
           note='Fees are the expense ratio turned into dollars on $10,000.')

pick = lesson('wr-menu', 'The Plan Menu', 'A short list. Read the fee and the bet.', [
    info('You do not need all four',
         'A 401(k) menu is a list the plan picked. A broad [[index fund]] with a tiny [[expense ratio]] is usually the workhorse. Your employer’s own stock can show a $0 fee and still be [[concentration risk]], because your paycheck already depends on that company.'),
    num('On $10,000, how many dollars a year does the US stock index fund cost?', 4,
        doc=menu,
        explain='The US stock index line is $4. That is a 0.04% expense ratio on $10,000.'),
    mc('Which line is a single company, even though the fee is $0?',
       ['US stock index fund', 'Bond index fund', 'Your employer’s own stock'], 2,
       'A $0 fee does not fix concentration. The job and the stock are the same company.'),
    tf('You should buy every fund on the menu so none of them feel left out.', False,
       'The menu is a list of options. A few broad, cheap funds can cover the mix. More names is not more of a plan.'),
    num('How many more dollars a year is the international index fund than the US stock index fund, on this $10,000?', 2,
        '$6 − $4 = $2. Both are cheap. The employer stock is the odd line, not the $2.'),
], fmt='document')

auto = lesson('wr-auto', 'Auto-Escalation', 'One percent, once a year.', [
    info('The slow raise',
         'Auto-escalation raises your contribution rate a little each year, often 1 percentage point, until you hit a cap you chose. Jamie is at 4%. A 1-point raise makes it 5%. On $52,000 that is $520 more of Jamie’s money, plus more match.'),
    num('Jamie goes from 4% to 5% of $52,000. How many more dollars a year does Jamie contribute?', 520,
        '1% of $52,000 = $520. The new contribution is $2,600.'),
    num('The match is 50% and 5% is still under the 6% match cap. How many extra match dollars does that $520 bring?', 260,
        '0.50 × $520 = $260.'),
    num('How many new dollars, Jamie’s plus the match, go in because of that one-point raise?', 780,
        '$520 + $260 = $780.'),
    tf('Auto-escalation means the plan invests 100% of your pay next year.', False,
       'It nudges the rate, often by 1 point a year. You can usually opt out or pick the cap.'),
])

limits = lesson('wr-limits', 'The 2026 Limits', 'The employee cap, then the age add-on.', [
    info('Whose limit',
         'In 2026 the employee [[401(k)|401k]] deferral limit is $24,500. That is your money, not the match. At age 50 the catch-up is $8,000 more, for a total of $32,500. At ages 60 through 63 the catch-up is $11,250, for a total of $35,750. Jamie is 23, so Jamie gets the $24,500 cap and not the catch-up. These are IRS figures for 2026.'),
    num('What is the 2026 employee 401(k) deferral limit, in dollars, before any catch-up?', 24500,
        'The 2026 employee cap is $24,500. The match can sit on top. Jamie’s $2,080 is under the cap.'),
    num('At age 50 in 2026, what is the total employee deferral including the $8,000 catch-up?', 32500,
        '$24,500 + $8,000 = $32,500.'),
    num('At age 61 in 2026, what is the total employee deferral including the $11,250 catch-up?', 35750,
        '$24,500 + $11,250 = $35,750. That higher catch-up is only for ages 60 through 63.'),
    tf('Jamie, at 23, can use the age-50 catch-up.', False,
       'The catch-up is an age rule. 23 gets the $24,500 base limit only.'),
])

loan = lesson('wr-loan', 'A Loan from the Plan', 'Your money leaves the market, and the job can call it due.', [
    info('Borrowing from yourself',
         'Some plans let you borrow from the [[401(k)|401k]]. A $5,000 loan is $5,000 that is not invested while you repay it. Leave the job and the loan often comes due quickly. Miss that, and it can be treated as a withdrawal: income tax, plus the usual 10% penalty if you are under 59½. It is a last resort, not a clever trick.'),
    num('How many dollars are out of the market during a $5,000 plan loan?', 5000,
        'The $5,000 is no longer invested. Repayments put money back over time. The missed growth is the quiet cost.'),
    tf('Quitting the job usually leaves a 401(k) loan quietly in place for decades.', False,
       'Leaving often makes the loan due. Unpaid, it can become a taxable withdrawal, with a penalty if you are under 59½.'),
    mc('What is the strongest reason to avoid a 401(k) loan for a want, not an emergency?',
       ['The money stays invested the whole time', 'The money leaves the market, and the job can turn the loan into a taxable withdrawal', 'Loans raise your employer match'], 1,
       'Two costs: time out of the market, and a bill that can show up when you leave.'),
    mc('The 10% early-withdrawal penalty, if the unpaid loan is treated as a withdrawal, generally applies before what age?',
       ['59½', '23', '65, with no exceptions ever'], 0,
       'Before 59½, an early withdrawal from a traditional 401(k) is usually tax plus a 10% penalty. Some exceptions exist. Do not plan on them.'),
])

vest = lesson('wr-vest', 'When the Match Is Yours', 'Your dollars are yours. Theirs may have a clock.', [
    info('A clock on their money',
         '[[Vesting]] is earning the [[employer match]] over time. Your own contributions are yours from day one. This example plan vests 25% of the match for each full year you stay. That schedule is an example, like the one in the earning section. Your plan document is the real one.'),
    num('The match so far is $2,000 and you are 50% vested. How many match dollars are yours?', 1000,
        '0.50 × $2,000 = $1,000. The other $1,000 goes back if you leave now.'),
    num('You contributed $4,000 of your own pay. How many of those dollars are yours, vesting aside?', 4000,
        'Your contributions are not on the vesting clock. All $4,000 is yours.'),
    mc('You leave after the example plan has vested 25% of a $2,000 match. How many match dollars do you keep?',
       ['$2,000', '$500', '$0, because matches are never yours'], 1,
       '25% of $2,000 is $500. Your own contributions still leave with you.'),
    tf('Vesting applies to the money you put in yourself.', False,
       'Vesting is about the employer’s money. Yours is yours.'),
])

jamie = lesson('wr-jamie', 'Jamie Turns It Up', 'One point a year, toward the full match.', [
    info('Meet Jamie, a year along',
         'Jamie is 23, in that first salaried job at $52,000. The 401(k) is at 4%, which is $2,080, and the match on it is $1,040. The plan matches 50% up to 6% of pay, so the full match is $1,560.\n\nJamie turns on a 1% auto-escalation. Next year the rate is 5%, if the pay stays $52,000.'),
    num('How many match dollars is Jamie missing by contributing 4% instead of 6%?', 520,
        'The full match is $1,560. Jamie is getting $1,040. $1,560 − $1,040 = $520 left on the table.'),
    num('After the one-point raise, Jamie contributes 5%. How many dollars a year is that?', 2600,
        '0.05 × $52,000 = $2,600.'),
    tf('Jamie should skip the match to pick individual stocks in the plan.', False,
       'The match is part of pay. The menu’s broad, cheap funds can hold it. Single stocks are the concentration.'),
    order('Put Jamie’s raise in order.',
          ['Get the plan’s match rule in writing',
           'Raise the rate by 1 point, from 4% to 5%',
           'Let the next year’s raise move it toward 6%',
           'Leave the investments in broad, cheap funds'],
          'The match rule first, then the slow raise, then the fund choice. 6% is where this plan’s match stops growing.'),
], fmt='story', story={
    'title': 'One point',
    'character': 'Jamie, 23, first salaried job',
    'body': 'Jamie earns **$52,000** and puts **4%** into the 401(k), which is **$2,080**. This plan matches 50% up to 6% of pay, so the full match would be **$1,560**. Jamie is getting **$1,040**.\n\nA 1% auto-escalation makes next year’s rate **5%**.',
})

write_unit('06-workplace.json', 'workplace', 6, '401(k)s & the Employer Match',
           'The percent of pay, the tax door, and the match you do not want to skip.',
           'The match is pay. Raise the rate until you have all of it.',
           terms, [rate, which, pick, auto, limits, loan, vest, jamie, review('wr'), trial('wr', '401(k)s & the Employer Match', [
               num('In 2026, what is the employee 401(k) deferral limit before any age catch-up?', 24500,
                   'The 2026 employee cap is $24,500. Catch-up amounts are extra, and only at the ages the IRS names.'),
               num('A plan matches 50% up to 6% of a $40,000 salary. The worker contributes 6%. How many match dollars is that?', 1200,
                   '6% of $40,000 is $2,400. Half of that is $1,200.'),
               tf('Your own 401(k) contributions vest on the same clock as the employer match.', False,
                  'Your contributions are yours. Vesting is the clock on the match.'),
               mc('A Roth 401(k) contribution does what to this year’s taxable pay?',
                  ['Lowers it, like a traditional contribution', 'Does not lower it, because the money was already taxed', 'Erases the employer match'], 1,
                  'Roth is the after-tax door. The traditional door is the one that lowers taxable pay now.'),
           ])],
           section=S)
