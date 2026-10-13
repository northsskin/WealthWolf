from lib import *

S = 'building-wealth'
terms = {
    'consumer-price-index': term('Consumer price index',
                                 'A measure of inflation. It prices a basket of ordinary things, then sees how that basket’s cost changes.',
                                 'A basket that cost $100 last year and $103 this year rose 3%.'),
    'unemployment-rate': term('Unemployment rate',
                              'The share of people in the labor force who want a job, are looking, and do not have one. It is not a grade of the whole country.',
                              'An example rate of 5% means 5 of every 100 people in the labor force are looking for work.'),
    'recession': term('Recession',
                      'A serious slowdown in the economy. Jobs get harder to find and spending pulls back. A common description is a long stretch of falling output.',
                      'Hours get cut at work, and the emergency fund is what covers groceries.'),
}

cpi = lesson('ec-cpi', 'How Inflation Is Measured', 'A basket, priced twice.', [
    info('The basket',
         '[[Inflation]] is prices rising, so the same money buys less. The [[consumer price index]] prices a basket of ordinary things and compares it with last year. This course will not grade this month’s reading. The method is the lesson.'),
    num('The basket cost $100 last year and $103 this year. By how many dollars did it rise?', 3,
        '$103 − $100 = $3.'),
    num('That $3 rise on a $100 basket is what percent?', 3, unit='%',
        explain='$3 ÷ $100 = 0.03, which is 3% inflation in this example.'),
    tf('The consumer price index is a promise of what prices will do next year.', False,
       'It describes the basket that already happened. Next year is not in the number.'),
    mc('What is inside the idea of the index?',
       ['One company’s stock', 'A basket of ordinary prices', 'Your savings account balance'], 1,
       'Ordinary prices, gathered into one basket. Not a stock and not your bank balance.'),
])

buys = lesson('ec-buys', 'What $100 Buys', 'A higher price is a smaller bag.', [
    info('The same bill',
         'If prices rise 25% in this example, the old $100 basket costs $125. The $100 bill now covers $100 ÷ $125 of that basket. That is $80 of the old stuff. [[Inflation]] did not take the bill. It took what the bill can carry.'),
    num('Prices rise 25%. What does the old $100 basket cost now?', 125,
        '$100 × 1.25 = $125.'),
    num('How many dollars of the old basket does $100 buy after that 25% rise?', 80,
        '$100 ÷ 1.25 = $80. You still hold $100. It buys less.'),
    tf('A 25% rise in prices means your $100 bill became a $75 bill.', False,
       'The bill is still $100. What changed is the basket. It now buys $80 of the old basket, not $75.'),
    mc('Which sentence matches the math?',
       ['The cash shrank', 'The cash buys a smaller basket', 'Prices fell'], 1,
       '$100 still says $100. The basket got more expensive, so the bag is smaller.'),
])

wages = lesson('ec-wages', 'Wages and Prices', 'A raise can still lose the race.', [
    info('Two percent signs',
         'A raise only moves you forward if it beats [[inflation]]. In this example pay rises 2% and prices rise 4%. The paycheck is bigger. The basket got bigger faster.'),
    num('Pay is $50,000 and it rises 2%. How many dollars is the raise?', 1000,
        '$50,000 × 0.02 = $1,000. The new pay is $51,000.'),
    num('A $50,000 lifestyle costs 4% more. How many extra dollars does that lifestyle take?', 2000,
        '$50,000 × 0.04 = $2,000.'),
    num('How many dollars short of the price rise is that $1,000 raise?', 1000,
        '$2,000 − $1,000 = $1,000. The raise was real, and prices still won.'),
    tf('Any raise means you can buy more than last year.', False,
       'Only a raise that beats inflation buys more. A smaller raise can still leave you behind.'),
])

slow = lesson('ec-slow', 'Recessions', 'The slowdown shows up as missing hours.', [
    info('What the word is for',
         'A [[recession]] is a serious slowdown. People spend less, and employers cut hours or jobs. Your long-term [[index fund]] can fall in the same season. The [[emergency fund]] is the pile for the grocery bill, not the fund you hoped to leave until retirement.'),
    mc('What does a recession usually mean for jobs?',
       ['Everyone gets a bonus', 'Hours and jobs get harder to hold', 'Prices are required to fall to zero'], 1,
       'A slowdown is when work gets scarce. That is why the cash pile exists.'),
    tf('A recession is the signal to sell a retirement fund you will not need for 30 years.', False,
       'The long fund can wait. Selling turns a downturn into a finished loss. The emergency fund is what you spend.'),
    mc('Which pile is for a cut in hours?',
       ['The emergency fund', 'A retirement fund dated for age 65', 'A coin you cannot afford to lose'], 0,
       'Cash for a surprise. The retirement date did not move just because the economy slowed.'),
    fill('A serious economic slowdown is called a ___.',
         ['recession', 'coupon', 'ticker'], 0,
         'Recession. It is a slowdown, not a new plan.'),
])

jobless = lesson('ec-rate', 'The Unemployment Rate', 'Looking, and not working.', [
    info('Who is counted',
         'The [[unemployment rate]] is the share of the labor force that wants a job, is looking, and does not have one. People who are not looking are not in that share. An example rate of 5% is 5 out of 100 in the labor force. It is an example, not this month’s reading.'),
    num('In an example labor force of 200 people, a 5% unemployment rate is how many people?', 10, unit=None,
        explain='200 × 0.05 = 10 people looking for work.'),
    tf('The unemployment rate counts every adult, including people who are not looking for a job.', False,
       'It counts the labor force: people working or looking. Someone who is not looking is outside that rate.'),
    mc('A rising unemployment rate in a recession usually means what nearby?',
       ['Jobs are easier', 'More people who want work cannot find it', 'Inflation is cancelled'], 1,
       'The rate is the looking-and-not-working share. Up means the search got harder.'),
    num('An example rate of 4% on a labor force of 1,000 is how many people?', 40, unit=None,
        explain='1,000 × 0.04 = 40.'),
])

cash_page = doc('statement', 'Emergency fund',
                [('cash', 'Cash set aside', 5000)],
                subtitle='For a cut in hours')
fund_page = doc('statement', 'Retirement fund',
                [('fund', 'Stock index fund', 20000)],
                subtitle='Not needed until about age 65')

protect = lesson('ec-protect', 'Your Plan in a Downturn', 'Spend the pile that was built for this.', [
    info('Two piles, one slowdown',
         'A [[recession]] can cut your hours and drop a stock fund in the same month. The plan you already wrote still applies. Cash pays the bills. The long fund stays put unless the date you need it has changed.'),
    mc('Your hours get cut. Which page pays the grocery bill?',
       [cash_page['title'], fund_page['title']], 0,
       docs=(cash_page, fund_page),
       explain='The emergency fund is the grocery pile. The $20,000 fund is for a date decades away. Selling it would lock in the downturn.'),
    num('How many dollars are on the page you spend first?', 5000,
        doc=cash_page,
        explain='The cash page is $5,000. That is the pile for a lost month of work.'),
    tf('A falling retirement fund means the emergency fund failed.', False,
       'They have different jobs. The fund can fall. The cash is what you spend.'),
    mc('When would the retirement page become the one you change?',
       ['Because the headline is scary', 'Because you now need that money in two years, not at 65', 'Because a friend sold'], 1,
       'A new date is a real change. A headline is not.'),
], fmt='call')

headline = doc('statement', 'A headline, in numbers',
               [('then', 'Price basket a year ago', 100), ('now', 'Same basket now', 103)],
               meta=[('Example unemployment rate', '5%')],
               subtitle='An example, not this morning’s news',
               note='Inflation here is the basket’s percent rise. The 5% is an example rate, not a live one.')

news = lesson('ec-headline', 'Reading a Headline', 'The number, then the claim.', [
    info('Separate the figure from the fear',
         'A headline can be true and still be a bad order. This page says the basket went from $100 to $103, and it mentions an example [[unemployment rate]] of 5%. Neither figure tells you to sell a 30-year fund.'),
    num('What percent did the basket rise?', 3, unit='%',
        doc=headline,
        explain='$103 − $100 = $3, and $3 ÷ $100 = 3%.'),
    tf('The 5% on this page is this morning’s official unemployment rate.', False,
       'The page labels it as an example. A real rate changes, and this lesson does not grade the live one.'),
    mc('What is a fair reading of the 3% basket rise?',
       ['Prices in the example rose 3%', 'Your personal raise was 3%', 'Stocks must fall 3%'], 0,
       'The basket rose 3%. Your raise, and the stock market, are different measurements.'),
    num('How many dollars more is the basket than last year?', 3,
        doc=headline,
        explain='$103 − $100 = $3.'),
], fmt='document')

earl = lesson('ec-earl', 'Earl’s Dollar Ticket', 'The ticket changed. The dollar bill did not.', [
    info('Meet Earl',
         'Earl is 78 and a retired bus driver. When he was young, a movie ticket in this story cost $1. The same kind of ticket is $12 in the lesson’s example.\n\nHis $1 bill from back then would not buy the ticket now. [[Inflation]] is that gap. The numbers are a teaching example, not a claim about one exact year.',
         ),
    num('How many times higher is the $12 ticket than the $1 ticket?', 12, unit=None,
        explain='$12 ÷ $1 = 12. The ticket costs 12 times what it did in the story.'),
    num('How many of today’s $12 tickets does $100 buy? Ignore the leftover dollars.', 8, unit=None,
        explain='$100 ÷ $12 = 8 tickets, with $4 left over. The question asks for the 8.'),
    tf('Earl’s story means a movie will cost $12 forever.', False,
       'It is an example of prices drifting. The next ticket can be higher or, less often, lower.'),
    mc('What should Earl’s grandchildren take from the $1 ticket?',
       ['Cash loses buying power when prices rise', 'Old prices come back if you wait', 'A dollar is required to buy a ticket'], 0,
       'The bill still says $1. The ticket moved. That is inflation, in one story.'),
], fmt='story', story={
    'title': 'A dollar at the window',
    'character': 'Earl, 78, retired bus driver',
    'body': 'When Earl was young, a movie ticket in this story cost **$1**. The same kind of ticket is **$12** in this example.\n\nA dollar bill from back then does not buy the ticket now. Inflation is that gap.',
})

write_unit('01-economy.json', 'economy', 1, 'Inflation & the Economy',
           'Prices, jobs, and which pile you spend when the slowdown arrives.',
           'The headline is loud. The emergency fund is the plan.',
           terms, [cpi, buys, wages, slow, jobless, protect, news, earl, review('ec'), trial('ec', 'Inflation & the Economy', [
               num('A basket goes from $200 to $210. What percent is that rise?', 5, unit='%',
                   explain='$10 ÷ $200 = 0.05, which is 5%.'),
               num('Prices rise 25% and you still hold $200. How many dollars of the old basket does it buy?', 160,
                   '$200 ÷ 1.25 = $160.'),
               tf('A recession is a reason to empty a 30-year stock fund for groceries.', False,
                  'Groceries come from the emergency fund. The long fund stays unless the date you need it changed.'),
               mc('The unemployment rate describes which group?',
                  ['Every retired person', 'People in the labor force who are looking and do not have a job', 'Everyone who owns a fund'], 1,
                  'Looking, and not working. People who are not looking are not in that share.'),
           ])],
           section=S)
