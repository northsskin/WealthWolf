from lib import *

S = 'investing'
terms = {
    'diversification': term('Diversification',
                            'Spreading your money across lots of different investments, so one bad one cannot sink you.',
                            'An index fund that holds hundreds of companies.'),
    'concentration-risk': term('Concentration risk',
                               'Having too much money in one place. If that one thing fails, you lose a lot.',
                               'All your savings in the company you work for.'),
    'asset-allocation': term('Asset allocation',
                             'How you split a portfolio among types of investments, such as stocks and bonds. The split follows the timeline.',
                             '80% stocks and 20% bonds for a goal that is decades away.'),
    'rebalancing': term('Rebalancing',
                        'Putting the split back to its target after markets move it. You sell some of what grew and buy some of what lagged.',
                        'Stocks grew to 90% of a portfolio whose target is 80%. Selling the extra 10% is rebalancing.'),
}

spread = lesson('iv-diversification', 'Diversification', 'Don’t let one bad bet sink the pack.', [
    mc('Which portfolio is more diversified?',
       ['All your money in one company', 'An index fund holding hundreds of companies', 'Three companies in the same industry'], 1,
       'Hundreds of companies means no single one can wipe you out. That spread is [[diversification]].',
       context='[[Diversification]] means spreading your money across lots of different investments, so one bad one can’t sink you.'),
    mc('Which of these has the most concentration risk?',
       ['A global index fund', 'A mix of stocks and bonds', 'All your savings in the company you work for'], 2,
       '[[Concentration risk]] is the pile in one place. If that company struggles, the job and the savings can fail together.',
       context='Having too much money in one place is called [[concentration risk]]. If that one thing fails, you lose big.'),
    tf('A diversified portfolio can never lose money.', False,
       'When everything falls, it falls too. Just less painfully than one bad bet.'),
    match('Match each way to diversify with an example.', [
        ['Companies', 'Hundreds of businesses, not one'],
        ['Industries', 'Tech, healthcare and energy'],
        ['Countries', 'Your home country plus others'],
        ['Investment types', 'Stocks and bonds'],
    ]),
    mc('Why mix stocks and bonds in one portfolio?',
       ['They often move differently, which smooths out the ride', 'Bonds always beat stocks', 'It removes all risk'], 0,
       'When one dips, the other often holds steadier. The mix is not a promise.'),
    fill('Spreading your money across many investments is called ___.',
         ['concentration', 'diversification', 'budgeting'], 1,
         'Spread out so no single hit takes you down.'),
])

dee = lesson('aa-horizon', 'Allocation and Time', 'The years pick the mix.', [
    info('Meet Dee',
         'Dee is 29 and a dental hygienist. She has two piles, $5,000 each. One is a house down payment in 3 years. The other is retirement in about 35 years.\n\n[[Asset allocation]] is the split. The 3-year pile wants to stay mostly cash. The 35-year pile can hold mostly [[stock]]s, with some [[bond]]s.'),
    mc('Which pile can hold mostly stocks?',
       ['The house money she needs in 3 years', 'The retirement money she will not use for about 35 years', 'Both, because stocks cannot fall for 3 years'], 1,
       'Decades can ride out drops. Three years cannot.'),
    num('Dee’s house pile is $5,000 and she keeps it in cash. How many dollars of that pile are not in stocks?', 5000,
        'All $5,000 stays out of stocks. The timeline is too short.'),
    tf('The same split fits every goal, no matter when you need the money.', False,
       'Asset allocation follows the timeline. Soon money and later money are different jobs.'),
    mc('What is asset allocation?',
       ['The split among types of investments', 'The ticker of one stock', 'The tax on a dividend'], 0,
       'Stocks, bonds, and cash, in proportions that match when you need the money.'),
], fmt='story', story={
    'title': 'Two piles',
    'character': 'Dee, 29, dental hygienist',
    'body': 'Dee has two piles of **$5,000**. One is a house down payment in **3 years**. The other is retirement in about **35 years**.\n\nThe 3-year pile stays mostly cash. The 35-year pile can be mostly stocks.',
})

mixes = lesson('aa-mixes', 'Mixes and Swings', 'More stocks, a wider year.', [
    info('Two familiar mixes',
         'A mix that is 90% [[stock]]s and 10% [[bond]]s will usually swing more in a bad year than a mix that is 60% stocks and 40% bonds. Historically, on average, the stock-heavier mix has also grown more over many decades. That is the trade. It is not a forecast for next year.'),
    mc('Which mix usually swings more in a single bad year?',
       ['90% stocks and 10% bonds', '60% stocks and 40% bonds', 'They are required to fall the same amount'], 0,
       'More stocks, wider swings. The bonds are the calmer slice.'),
    num('A $10,000 portfolio is 60% stocks. How many dollars are in stocks?', 6000,
        '0.60 × $10,000 = $6,000. The other $4,000 is the bond slice.'),
    num('The same $10,000 is 90% stocks. How many dollars are in stocks?', 9000,
        '0.90 × $10,000 = $9,000.'),
    tf('The calmer mix is always the better one.', False,
       'Calmer fits a nearer goal. A far-off goal can accept the wider swing for the chance of more growth.'),
])

rebalance = lesson('aa-rebalance', 'Rebalancing', 'Put the split back.', [
    info('The target drifted',
         'Your target [[asset allocation]] is 80% stocks and 20% bonds, on $10,000. Stocks had a big year. You now have $9,000 in stocks and $1,000 in bonds. Stocks are 90% of the pile. [[Rebalancing]] sells some of what grew and buys some of what lagged, back to the target.'),
    num('On $10,000, how many dollars of stocks is an 80% target?', 8000,
        '0.80 × $10,000 = $8,000.'),
    num('You have $9,000 in stocks and the target is $8,000. How many dollars of stocks do you sell?', 1000,
        '$9,000 − $8,000 = $1,000.'),
    num('Bonds are $1,000 and the 20% target on $10,000 is $2,000. How many dollars of bonds do you buy?', 1000,
        '$2,000 − $1,000 = $1,000. The sale of stocks pays for the bonds.'),
    tf('Rebalancing means chasing whatever rose the most and buying more of it.', False,
       'It does the opposite. You trim what grew past the target and top up what fell behind.'),
])

world = lesson('aa-world', 'Other Countries', 'Home is not the whole list.', [
    info('Beyond one country',
         'A fund of US companies is [[diversification]] across those companies. It is not diversification across the world. Other countries have other companies, other currencies, and other bad years. Adding them does not promise a higher return. It means one country’s slump is not your entire stock pile.'),
    mc('A fund that holds only US companies is diversified across what?',
       ['Many US companies, and not the rest of the world', 'Every stock market on earth', 'Stocks and bonds in equal parts'], 0,
       'Many companies, one country. International funds are the other countries.'),
    tf('Adding international stocks guarantees a smoother year.', False,
       'Other markets fall too, sometimes in the same year. The point is that they are not the same bet.'),
    mc('Why include countries besides your own?',
       ['Because foreign stocks cannot fall', 'So one country’s bad decade is not the whole stock pile', 'Because a US fund is illegal'], 1,
       'The world is a bigger list. It is still stocks, with stock risk.'),
    num('A $10,000 stock pile is 70% US and 30% international. How many dollars are international?', 3000,
        '0.30 × $10,000 = $3,000.'),
])

tolerance = lesson('aa-tolerance', 'Risk Tolerance', 'The timeline, and whether you can sleep.', [
    info('Two questions',
         'Risk tolerance is how much of a drop you can hold through. The timeline still comes first. A 30-year goal can use a wide swing even if a bad month feels awful. A 2-year goal cannot, no matter how calm you feel today.'),
    sort('Which timeline is this money on?',
         ['Need it soon', 'Can leave it for decades'],
         [('A house down payment in 2 years', 0),
          ('Retirement about 30 years away', 1),
          ('Tuition due next semester', 0),
          ('Money you will not touch until your 60s', 1)],
         'Soon money stays steady. Decades can take the stock swings.'),
    mc('You feel brave, and you need the money in 18 months. What wins?',
       ['The brave feeling', 'The 18-month timeline', 'Last year’s best stock'], 1,
       'Feeling brave does not make a short timeline long. The bill still arrives.'),
    tf('A long timeline means a crash will not bother you.', False,
       'It can bother you. The long timeline means you do not have to sell during it.'),
    fill('How much of a drop you can hold through is called risk ___.',
         ['tolerance', 'yield', 'ticker'], 0,
         'Tolerance. It sits next to the timeline. It does not replace it.'),
], fmt='sort')

soon = doc('statement', 'Goal in two years',
           [('cash', 'Savings', 10000), ('stock', 'Stocks', 0)],
           subtitle='The money has a near date')
later = doc('statement', 'Goal in thirty years',
            [('stock', 'Stocks', 8000), ('bond', 'Bonds', 2000)],
            subtitle='The money can wait')

choose = lesson('aa-goal', 'A Mix for a Goal', 'Pick the page that matches the date.', [
    info('Match the date',
         'The two-year page is cash, because a drop would hit the goal. The thirty-year page is 80% stocks and 20% bonds. Same person can own both. The goals are different.'),
    mc('Which page fits a house down payment in two years?',
         [soon['title'], later['title']], 0,
         docs=(soon, later),
         explain='Two years wants the cash page. The stock-heavy page is for the goal that can wait thirty years.'),
    num('On the thirty-year page, how many dollars are in bonds?', 2000,
        doc=later,
        explain='The bond slice is $2,000, which is 20% of $10,000.'),
    tf('The thirty-year mix is also the right mix for the house.', False,
       'The house date is two years. That page stays in savings.'),
    mc('What changed between the pages?',
       ['The person', 'When the money is needed', 'The ticker of a single stock'], 1,
       'Asset allocation follows the date. One person, two dates, two mixes.'),
], fmt='call')

ben_doc = doc('statement', 'Ben’s portfolio',
              [('job', 'Stock in the company that employs him', 8000),
               ('fund', 'Broad stock fund', 2000)],
              totals=[('Total', 10000)],
              subtitle='Most of it rides on one employer')

ben = lesson('aa-ben', 'Ben’s Lopsided Portfolio', 'The job and the stock are the same bet.', [
    info('One employer, twice',
         'Ben is 31 and an electrician. $8,000 of his $10,000 portfolio is stock in the company that pays him. If that company stumbles, he can lose the job and the $8,000 together. That is [[concentration risk]].'),
    spot('Which line is the concentration?', ben_doc, 'job',
         'The $8,000 employer stock is the pile in one place. The broad fund is the smaller, spread-out line.'),
    num('What percent of Ben’s $10,000 is the employer stock?', 80, unit='%',
        explain='$8,000 ÷ $10,000 = 0.80, which is 80%.'),
    mc('What is the danger in that 80%?',
       ['The broad fund might be boring', 'A bad year for the employer can hit his paycheck and his portfolio', 'Bonds pay coupons'], 1,
       'The job and the stock are the same company. Diversification wants them unlinked.'),
    tf('Ben is diversified because he also owns $2,000 of a broad fund.', False,
       'The $2,000 helps a little. $8,000 in one employer is still the concentrated pile.'),
], fmt='spot')

write_unit('05-allocation.json', 'allocation', 5, 'Diversification & Asset Allocation',
           'Spread out, then match the mix to the date you need the money.',
           'One company is a bet. A mix is a plan.',
           terms, [spread, dee, mixes, rebalance, world, tolerance, choose, ben, review('aa'), trial('aa', 'Diversification & Asset Allocation', [
               num('A $20,000 portfolio targets 70% stocks. How many dollars of stocks is that?', 14000,
                   '0.70 × $20,000 = $14,000.'),
               tf('Rebalancing means buying more of whatever just went up.', False,
                  'You trim what grew past the target and add to what fell behind it.'),
               mc('Which is the clearest concentration risk?',
                  ['A global stock fund', '90% of your portfolio in your employer’s stock', 'A mix of stocks and bonds'], 1,
                  'One employer can take the job and the savings in the same bad year.'),
               num('Stocks drifted to $9,000 of a $10,000 portfolio. The target is $7,500. How many dollars of stocks do you sell to get back?', 1500,
                   '$9,000 − $7,500 = $1,500.'),
           ])],
           section=S)
