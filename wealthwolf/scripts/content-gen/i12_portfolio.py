from lib import *

S = 'investing'
terms = {
    'three-fund-portfolio': term('Three-fund portfolio',
                       'A portfolio of three cheap index funds: a US stock fund, an international stock fund, and a bond fund. The split follows your timeline.',
                       'A $10,000 retirement pile with $5,000 in US stocks, $2,000 international, and $3,000 in bonds.'),
}

three = lesson('pf-three', 'The Three Funds', 'Home stocks, the rest of the world, and bonds.', [
    info('A complete boring mix',
         'A [[three-fund portfolio]] is three cheap [[index fund]]s. One holds US stocks. One holds stocks from other countries. One holds [[bond]]s. You already know each piece. The portfolio is the split, plus the [[expense ratio]]s, plus the years you leave it alone. Nothing here is a promise of a return.'),
    mc('Which three does this lesson mean?',
       ['A US stock index fund, an international stock index fund, and a bond index fund',
        'Three individual stocks from one industry',
        'A coin, a meme stock, and an option'], 0,
       'Those three funds cover home stocks, other countries’ stocks, and bonds. The coin and the meme stock are speculation.'),
    tf('The three-fund portfolio is three copies of the same US stock fund.', False,
       'Two of the funds are stocks, and they are different lists: the US, and the rest of the world. The third is bonds.'),
    num('A $10,000 three-fund pile has $6,000 in the US stock fund and $2,000 in the international fund. How many dollars are in the bond fund?', 2000,
        '$10,000 − $6,000 − $2,000 = $2,000.'),
    mc('What does the bond fund’s job stay?',
       ['To triple the stocks', 'To be the steadier slice', 'To replace the emergency fund'], 1,
       'Steadier, not magic. The emergency fund is still cash, outside this pile.'),
])

enough = lesson('pf-enough', 'Three Is Enough', 'More names often means the same stocks twice.', [
    info('Overlap',
         'Five US stock funds can own the same giant companies five times. That is not more [[diversification]]. It is the same bet with more [[expense ratio]]s. Three broad funds already cover the US, other countries, and bonds. Add a fund when it adds a job you do not already have.'),
    mc('You already own a total US stock index fund. What does a second US large-company fund mostly add?',
       ['Hundreds of new companies', 'Overlap, plus another fee', 'A bond cushion'], 1,
       'The big companies are already in the total market fund. The second fund repeats them.'),
    tf('Twelve funds are always more diversified than three broad ones.', False,
       'Diversification is different bets. Twelve overlapping funds are still one bet, with a longer fee list.'),
    num('Two overlapping funds each charge $15 a year. A single broad fund would charge $5. How many extra dollars a year do the two funds cost?', 25,
        '$15 + $15 = $30. $30 − $5 = $25 extra.'),
    fill('Owning the same companies in several funds is called ___.',
         ['overlap', 'a coupon', 'vesting'], 0,
         'Overlap. A new fund should add a job, not a second copy.'),
])

mix = lesson('pf-mix', 'A Mix for the Years', 'Assign the $10,000.', [
    info('Minimums, not a single correct life',
         'This check is a 25-year-old’s $10,000 retirement pile, decades away. Put at least $5,000 in the US stock fund, at least $2,000 in the international fund, and at least $2,000 in the bond fund. Every dollar gets assigned. A heavier stock mix would also fit this timeline. The minimums are the floor for this exercise, not a required life.'),
    alloc('Assign all $10,000. Meet each minimum.', 10000, 100,
          [{'label': 'US stock index fund', 'min': 5000},
           {'label': 'International stock index fund', 'min': 2000},
           {'label': 'Bond index fund', 'min': 2000}],
          'The floors are $5,000, $2,000, and $2,000, which already add to $9,000. The last $1,000 can sit in any fund. The bond line in a simple fill ends at $3,000. Decades away can also hold more stocks. This is an exercise, not a personal plan.'),
    num('The three minimums are $5,000, $2,000, and $2,000. How many dollars is that before the last $1,000?', 9000,
        '$5,000 + $2,000 + $2,000 = $9,000. The pile is $10,000, so $1,000 is still free to place.'),
    tf('This exercise is the only legal mix for a 25-year-old.', False,
       'The minimums keep every job on the page. More stocks would still fit a decades-long goal.'),
    mc('Where does the emergency fund sit relative to this $10,000?',
       ['Inside the bond fund', 'Outside, in cash', 'In a coin'], 1,
       'The emergency fund stays cash. This pile is money that can wait.'),
])

cost_doc = doc('statement', 'Fees on $10,000 a year',
               [('cheap', 'Three-fund mix, yearly fees', 8),
                ('pricey', 'Similar mix, yearly fees', 120)],
               subtitle='Same jobs, different bill')

cost = lesson('pf-cost', 'The Cost Check', 'The mix is not done until you see the fee.', [
    info('Add the three fees',
         'Each [[fund]] has an [[expense ratio]]. On $10,000, a cheap three-fund mix in this example costs $8 a year. A similar mix of pricey funds costs $120. The jobs match. The bill does not.'),
    spot('Which yearly fee should you walk away from?', cost_doc, 'pricey',
         '$120 a year for the same kind of mix is the line to leave. The $8 mix is the cheap one.'),
    num('How many more dollars a year is the pricey mix?', 112,
        '$120 − $8 = $112 a year, on the same $10,000, in this example.'),
    tf('A higher fee means the pricey mix is safer.', False,
       'The fee is money out. Safety comes from the mix and the timeline, not from paying more.'),
    num('Over 10 years, if the $112 gap stayed the same, how many extra dollars would the pricey mix take?', 1120,
        '10 × $112 = $1,120. This sketch holds the fee gap still. A growing balance would make a percent fee larger.'),
], fmt='spot')

auto = lesson('pf-auto', 'Automate It', 'Payday does the work.', [
    info('Take yourself out of it',
         'The [[three-fund portfolio]] survives if you do not have to decide every payday. The transfer happens, the buy happens, and you look again on a date you already wrote. That is the same habit as [[dollar-cost averaging]], pointed at the three funds.'),
    order('Put the automation in order.',
          ['Get paid',
           'Automatic transfer to the IRA or brokerage',
           'Automatic buy of the three funds',
           'Look again only on the date you wrote'],
          'Cash arrives, the transfer leaves, the funds get bought, and the app does not get a daily vote.'),
    num('Morgan can send $100 a month. How many dollars is that in a year?', 1200,
        '12 × $100 = $1,200. The mix, not the month, is the decision.'),
    tf('An automatic plan means you never look at it again, even when the goal date changes.', False,
       'You look on the written date, and you look when the goal itself changes. You do not look because today was red.'),
    mc('What should the automatic buy purchase?',
       ['Whatever is up the most today', 'The three funds in the split you chose', 'A new coin each month'], 1,
       'The split you already chose. The automation is not permission to chase.'),
])

fell = doc('statement', 'A bad month',
           [('then', 'Value last month', 10000), ('now', 'Value today', 8500)],
           subtitle='The goal is still 30 years away',
           note='A 15% drop. The date did not change.')
soon = doc('statement', 'A new date',
           [('stock', 'Still in stocks', 8000), ('bond', 'Still in bonds', 2000)],
           subtitle='You now need the money in 3 years, not 30',
           note='The investments did not change. The timeline did.')

change = lesson('pf-change', 'When to Change the Plan', 'A new date. Not a red month.', [
    info('Two pages',
         'One page is a 15% drop, from $10,000 to $8,500, and the goal is still 30 years away. The other page is the same kind of mix, except you now need the money in 3 years. Only the second page is a reason to change the [[asset allocation]]. The drop is the reason you wrote the rule.'),
    mc('Which page is a reason to change the mix?',
       [fell['title'], soon['title']], 1,
       docs=(fell, soon),
       explain='The new date is the change. Three years cannot wear a 30-year stock mix. The 15% drop, with the date unchanged, is the moment you follow the old rule.'),
    num('On the bad-month page, how many dollars did the $10,000 fall?', 1500,
        doc=fell,
        explain='$10,000 − $8,500 = $1,500. That is 15%. It is not a new goal.'),
    tf('A 15% drop means the three-fund portfolio was the wrong idea.', False,
       'A drop is part of owning stocks. The idea is wrong when the timeline changes, or the fees are wild, not when a year is red.'),
    mc('You will need the money in 3 years. What should the mix do?',
       ['Shift toward cash and bonds', 'Shift into one meme stock to catch up', 'Stay 100% in the riskiest fund because you are behind'], 0,
       'A near date wants less swing. Catching up with a bet is how people lock in the shortfall.'),
], fmt='call')

stay = lesson('pf-stay', 'Stay the Course', 'The rule was written for this month.', [
    info('Do not take the meeting',
         'Staying the course means you keep the [[three-fund portfolio]] and the automatic buy when the screen is red, as long as the goal date is the same. Selling the $8,500 locks the $1,500 drop in. The next recovery, if it comes, happens to the people who still hold the funds. This is the habit. It is not a promise that every drop recovers on a schedule.'),
    num('You sell at $8,500 after the drop from $10,000. How many dollars of the drop did you lock in?', 1500,
        '$10,000 − $8,500 = $1,500. The sale makes that the result.'),
    tf('Staying the course means never changing the mix, even if you need the money next year.', False,
       'A new date is a real change. A red month is not. The course you stay is the one that still matches the date.'),
    mc('The goal is still 30 years away and the funds are down 15%. What is the move?',
       ['Sell all three funds', 'Keep the funds and let the next automatic buy happen', 'Borrow on margin to get even faster'], 1,
       'The buy happens. The rule holds. Margin is still a skip.'),
    fill('Keeping the plan through a drop is called staying the ___.',
         ['course', 'hype', 'margin'], 0,
         'The course. You set it on a calm day so a loud day cannot edit it.'),
])

morgan = lesson('pf-morgan', 'Morgan Builds a Plan', 'The emergency fund is done. The $100 has a job.', [
    info('Meet Morgan, later',
         'Morgan is 25 and a dental assistant, the same Morgan who mapped a starter emergency fund. That cash fund is now in place. Take-home pay is still about $3,000 a month.\n\nMorgan will send $100 a month into a Roth IRA and buy the three cheap index funds: US stocks, international stocks, and a bond fund. The look-again date is her birthday, not tomorrow morning.',
         ),
    num('How many dollars a year is Morgan’s $100 a month?', 1200,
        '12 × $100 = $1,200. That is under the 2026 IRA limit of $7,500.'),
    tf('Morgan should invest the emergency fund too, so the account looks serious.', False,
       'The cash fund stays cash. The $100 is the investing pile.'),
    mc('When does Morgan reread the plan?',
       ['Every time a fund is red', 'On her birthday, unless the goal date changes', 'When a video names a coin'], 1,
       'A written date. A red day is not a meeting.'),
    order('Put Morgan’s plan in order.',
          ['Keep the emergency fund in cash',
           'Send $100 a month to the Roth IRA',
           'Buy the three cheap index funds',
           'Look again on her birthday'],
          'Cash first, then the automatic dollars, then the three funds, then a calm date to look.'),
], fmt='story', story={
    'title': 'A hundred dollars',
    'character': 'Morgan, 25, dental assistant',
    'body': 'Morgan’s starter emergency fund is now in place. She takes home about **$3,000** a month.\n\nShe will send **$100** a month to a Roth IRA and buy three cheap index funds: US stocks, international stocks, and bonds. She looks again on her birthday.',
})

sim = {
    'id': 'iv-sim',
    'type': 'sim',
    'title': 'Portfolio Simulator',
    'summary': 'Build a portfolio and fast-forward 30 years.',
    'xp': 20,
    'steps': [],
}

write_unit('12-portfolio.json', 'portfolio', 12, 'Building Your Portfolio',
           'Three cheap funds, an automatic transfer, and a rule for red months.',
           'Build it once. Automate it. Then leave it alone.',
           terms, [three, enough, mix, cost, auto, change, stay, morgan, sim, review('pf'), trial('pf', 'Building Your Portfolio', [
               num('A $9,000 portfolio is $6,000 US stocks and $2,000 international stocks. How many dollars are in bonds?', 1000,
                   '$9,000 − $6,000 − $2,000 = $1,000.'),
               tf('A 15% drop, with the goal still decades away, is a reason to scrap the three-fund mix.', False,
                  'The drop is why the rule exists. Change the mix when the date changes, not when the month is red.'),
               mc('Which set is the three-fund portfolio?',
                  ['US stock index, international stock index, bond index', 'Three coins', 'One employer’s stock, three times'], 0,
                  'Home stocks, the rest of the world, and bonds. Cheap funds, then you leave them.'),
               num('The cheap mix costs $8 a year and the pricey mix costs $120. How many dollars a year do you keep by choosing the cheap one?', 112,
                   '$120 − $8 = $112 a year in this example.'),
           ])],
           section=S)
