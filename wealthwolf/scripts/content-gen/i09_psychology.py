from lib import *

S = 'investing'
terms = {
    'recency-bias': term('Recency bias',
                         'Treating the latest stretch as the way things always go. A great year feels permanent. A crash feels permanent too.',
                         'Last year was down, so you conclude stocks are finished.'),
    'survivorship-bias': term('Survivorship bias',
                              'Noticing only the investments that made it, and forgetting the ones that died. A list of winners is not the list you could have picked from in advance.',
                              'A “best stocks of the decade” list leaves out the companies that went to zero.'),
}

crash_doc = doc('statement', 'An example 50% drop',
                [('then', 'Value before the drop', 10000), ('now', 'Value after a 50% drop', 5000)],
                totals=[('Dollars missing', -5000)],
                subtitle='A round number, so the math is visible',
                note='From the October 2007 peak to March 2009, the S&P 500 fell about 57%. It regained that old peak in 2013.')

crash = lesson('ip-crash', 'A Real Crash', 'The drop was real. So was the recovery.', [
    info('2007 to 2009, then 2013',
         'From its October 2007 peak to March 2009, the S&P 500 fell about 57%. Someone who sold at the bottom locked that loss in. The index regained its old peak in 2013. Holding was miserable, and it was how a holder of that index got the old price back. This is history, not a promise that the next drop will rhyme.\n\nThe page uses a round 50% so the next lesson’s math is clean. The historical drop was about 57%.'),
    num('On the example page, a $10,000 portfolio falls 50%. How many dollars are left?', 5000,
        doc=crash_doc,
        explain='$10,000 × 0.50 = $5,000 left. The historical S&P 500 drop was about 57%, which is harsher than this round example.'),
    num('Using the course’s round figure of about 57%, how many dollars does a $10,000 investment lose?', 5700,
        'About 57% of $10,000 is $5,700. About $4,300 would be left. “About” matters. The real peak-to-bottom figure was roughly that.'),
    tf('Because the S&P 500 later regained its 2007 peak, every future crash will recover on the same calendar.', False,
       '2013 is a fact about that decline. It is not a schedule you can count on next time.'),
    mc('What did selling at the March 2009 bottom do?',
       ['It avoided a loss that had not happened yet', 'It locked the drop in, and the holder missed the later recovery', 'It is what SIPC is for'], 1,
       'The loss becomes permanent when you sell. The people who held the index were the ones still there in 2013.'),
], fmt='document')

back = lesson('ip-back', 'Getting Back to Even', 'A 50% drop asks for a 100% gain.', [
    info('The hill is steeper',
         'The example portfolio fell from $10,000 to $5,000. Getting back to $10,000 means the $5,000 has to double. That is a 100% gain, not a 50% gain. This is why panic-selling at the bottom is so expensive, and why the percent down is not the percent required to recover.'),
    num('A $10,000 portfolio falls 50%. How many dollars is it worth?', 5000,
        '$10,000 − $5,000 = $5,000.'),
    num('What percent gain turns $5,000 back into $10,000?', 100, unit='%',
        explain='$5,000 × 2 = $10,000. That is a 100% gain. A 50% gain would only reach $7,500.'),
    num('A 50% gain on the $5,000 would reach how many dollars?', 7500,
        '$5,000 × 1.50 = $7,500. Still $2,500 short of where you started.'),
    tf('After a 50% drop, a 50% rise gets you back to even.', False,
       'Fifty percent of the smaller number is not fifty percent of the original. You need a 100% gain.'),
])

timing = lesson('ip-timing', 'Timing the Market', 'Out at the bottom, gone for the rebound.', [
    info('The expensive part',
         'Timing means jumping out and back in. In the example, you sell at $5,000 and sit in cash. The recovery to $10,000 happens without you. You still have $5,000. The person who held has their $10,000 back. Historically, on average, the rebounds have been bunched into short stretches. Missing them is the cost of waiting for “calm.”'),
    num('You sell at $5,000 and the held portfolio recovers to $10,000. How many dollars behind is the cash?', 5000,
        '$10,000 − $5,000 = $5,000. That gap is the rebound you were not in for.'),
    tf('Waiting for a calm market has been a free way to keep the gains and skip the drops.', False,
       'The drops and the rebounds are mixed together. Sitting out to feel calm often skips the rebound too.'),
    mc('Your goal is 25 years away and prices just fell. What matches “time in the market”?',
       ['Sell and wait for a headline that says it is safe', 'Stay invested and keep the schedule', 'Move everything into one stock that fell less'], 1,
       'The schedule is the plan. The headline is not.'),
    fill('Jumping in and out is called ___ the market.',
         ['timing', 'diversifying', 'vesting'], 0,
         'Timing. Time in the market is the opposite habit: stay in.'),
])

fomo = lesson('ip-fomo', 'FOMO and Hype', 'A big recent gain is not an invitation.', [
    info('The feeling',
         'FOMO is the fear of missing out. A stock, a coin, or a fund doubles, and the stories arrive. Buying because the price already ran is a feeling, not a plan. The person who bought earlier is not proof that buying now works. This course will not name a hot investment.'),
    mc('A stock rose 80% last month and your group chat is loud. What is the solid reading?',
       ['It has to rise another 80%', 'The rise already happened, and it is not a forecast', 'SIPC covers the next drop'], 1,
       'Past rise, past. The chat is not research.'),
    tf('If everyone you know is buying it, the risk is gone.', False,
       'A crowd can be early or late. Popularity is not a margin of safety.'),
    num('You put $500 into a hyped idea and it falls 60%. How many dollars are left?', 200,
        '$500 × 0.40 = $200. The story did not change the math.'),
    mc('What belongs in the plan instead of the group chat?',
       ['The goal, the date, and the mix you already wrote', 'Whichever ticker is loudest today', 'A loan, so you can buy more of the hype'], 0,
       'The written plan. Hype is a feeling with a price.'),
])

bias = lesson('ip-bias', 'Two Tricks of Memory', 'The latest year, and the winners you can see.', [
    info('What your brain keeps',
         '[[Recency bias]] treats the latest stretch as destiny. [[Survivorship bias]] stares at the winners and forgets the investments that went to zero. A bad year is a bad year. A list of successes is not the menu you actually had.'),
    sort('What kind of thinking is this?',
         ['Recency bias', 'Survivorship bias', 'A real change of plan'],
         [('Last year was awful, so stocks are finished forever', 0),
          ('A list of the decade’s winners, with the dead companies left off', 1),
          ('You now need the money in 2 years, not 30', 2),
          ('The last 12 months were great, so every year will be', 0)],
         'The latest year is recency. The edited winner list is survivorship. A new date for the money is an actual change.'),
    tf('A “best of the decade” list shows every company you could have bought at the start.', False,
       'The failures are usually missing. That is survivorship bias.'),
    mc('A 30% drop this year convinces you that stocks never recover. Which bias is that?',
       ['Recency bias', 'A margin call', 'Vesting'], 0,
       'One bad stretch, treated as the whole future. History includes recoveries and also long slumps. One year is not either story by itself.'),
    fill('Ignoring the investments that failed is ___ bias.',
         ['survivorship', 'coupon', 'ticker'], 0,
         'Survivorship. The graveyard is part of the real menu.'),
], fmt='sort')

often = lesson('ip-check', 'Checking Too Often', 'A daily price is a bad boss.', [
    info('The app is not the plan',
         'A 30-year [[portfolio]] does not need a daily vote. Checking every hour turns a normal down day into a decision. The decision was already made when you picked the mix and the schedule. Look on a schedule you wrote in advance, not when you are bored or scared.'),
    mc('Your retirement money is for age 65 and you are 30. How often does that goal need a trade?',
       ['Every time the app sends a red number', 'On the schedule you wrote, unless the goal itself changed', 'Whenever a friend texts a screenshot'], 1,
       'The schedule. A red day is not a new goal.'),
    tf('Watching the price more often makes the long-term result more accurate.', False,
       'It makes the feelings louder. The result still comes from the mix, the fees, and the years.'),
    num('You check a $10,000 fund and it is down $150 today, which is 1.5%. How many dollars is that one-day move?', 150,
        'The move is $150. On a 30-year goal it is noise. Selling would turn the noise into a trade.'),
    mc('When is a look at the account actually useful?',
       ['To rebalance on the date you planned', 'To react to one afternoon', 'To copy a stranger’s trade'], 0,
       'A planned look. The afternoon can wait.'),
])

rules = lesson('ip-rules', 'Write the Rules First', 'Decide before the drop, not during it.', [
    info('A page you can reread',
         'Write the rules on a calm day. The goal, the date, the mix, and one sentence: you will not sell only because prices fell. When a crash shows up, you follow the page. You do not hold a meeting with your fear.'),
    order('Put the rules in the order you write them.',
          ['Name the goal and the date',
           'Choose the mix that fits that date',
           'Write that you will not sell only because of a drop',
           'Pick a calm date to look again'],
          'The date picks the mix. The “do not sell on a drop” line is what you reread later. The look-again date keeps you from living in the app.'),
    tf('The right time to invent your sell rule is in the middle of a crash.', False,
       'That is the worst time. The rule belongs to the calm day, when the goal is clear.'),
    mc('Prices fall 20% and your written rule says not to sell on a drop. The goal date has not changed. What do you do?',
       ['Follow the rule', 'Delete the rule because today feels different', 'Borrow on margin to “buy the fear”'], 0,
       'The rule was for this exact day. Follow it. Margin is still the thing to skip.'),
    fill('You write the rules on a ___ day, before you need them.',
         ['calm', 'panic', 'hype'], 0,
         'Calm. Panic will not negotiate fairly.'),
])

ray = lesson('ip-ray', 'Ray Sells at the Bottom', 'March 2009, in cash.', [
    info('Meet Ray',
         'Ray is 44 and a hotel manager. He owned an S&P 500 index fund. Using this course’s round figure, a drop of about 57% took it from $10,000 to $4,300. In March 2009 he sold, because he could not stand the screen.\n\nThe index regained its October 2007 peak in 2013. Ray’s sold shares were not there for that climb. This is his history lesson, not a forecast with his name on it.'),
    num('Using the round 57% figure, how many dollars were left of Ray’s $10,000 when he sold?', 4300,
        '$10,000 − $5,700 = $4,300. Selling took that price. The later recovery happened without those shares.'),
    tf('Ray’s sale was protected by SIPC, because the market had fallen.', False,
       'SIPC is a failed brokerage. A falling index is market risk, and the sale made the lower price his.'),
    mc('What did Ray give up by selling?',
       ['The chance to be invested for the recovery that followed', 'A guaranteed 57% profit', 'His emergency fund rules'], 0,
       'He locked in about $4,300. Holders of the index were the ones who got the old peak back in 2013.'),
    mc('What should Ray’s written rule have said?',
       ['Sell when the screen is unbearable', 'Do not sell a long-term fund only because it dropped', 'Switch to whichever coin is popular'], 1,
       'The rule is for the unbearable day. The fund was for a long timeline. The drop was not a new timeline.'),
], fmt='story', story={
    'title': 'Sold in March 2009',
    'character': 'Ray, 44, hotel manager',
    'body': 'Ray’s S&P 500 index fund fell about **57%**, from **$10,000** to about **$4,300**. In March 2009 he sold.\n\nThe index regained its 2007 peak in **2013**. The shares he sold were not invested for that climb.',
})

write_unit('09-psychology.json', 'psychology', 9, 'Investor Psychology',
           'Crashes, biases, and the rules you write before you need them.',
           'The screen is loud. The written rule is the plan.',
           terms, [crash, back, timing, fomo, bias, often, rules, ray, review('ip'), trial('ip', 'Investor Psychology', [
               num('A $8,000 fund falls 50%. How many dollars is it worth?', 4000,
                   '$8,000 × 0.50 = $4,000. Getting back to $8,000 would take a 100% gain.'),
               tf('A list of famous winning stocks includes the companies that failed along the way.', False,
                  'That edited list is survivorship bias. The failures are the part you do not see.'),
               mc('From the 2007 peak to March 2009, the S&P 500 fell about how much?',
                  ['About 5%', 'About 57%', 'It rose'], 1,
                  'About 57%. The old peak was regained in 2013. That history is not a promise for the next drop.'),
               tf('Checking a 30-year portfolio every hour improves the result.', False,
                  'It turns noise into the urge to trade. Look on a date you chose in advance.'),
           ])],
           section=S)
