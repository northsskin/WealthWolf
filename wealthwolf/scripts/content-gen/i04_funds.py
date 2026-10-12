from lib import *

S = 'investing'
terms = {
    'fund': term('Fund',
                 'A pool of money from lots of people, invested in many things at once. You buy a slice of the pot.',
                 'One purchase that holds hundreds of stocks.'),
    'index': term('Index',
                  'A list that tracks a group of investments, such as a country’s 500 biggest companies.',
                  'A list of the 500 largest US companies.'),
    'index-fund': term('Index fund',
                       'A fund that simply buys everything on an index. No one is picking winners.',
                       'A fund that holds all 500 companies on a big-company list.'),
    'expense-ratio': term('Expense ratio',
                          'The yearly fee a fund charges, as a percent of what you have invested.',
                          'A 0.1% expense ratio on $10,000 is $10 a year.'),
    'mutual-fund': term('Mutual fund',
                        'A fund whose price is set once a day, after the market closes.',
                        'You place an order in the afternoon and get the end-of-day price.'),
    'etf': term('ETF',
                'An exchange-traded fund. A fund that trades through the day, like a stock.',
                'Buying an ETF at 11am at the price buyers and sellers are trading then.'),
    'target-date-fund': term('Target-date fund',
                             'A fund with a year in its name. It starts out heavier in stocks and shifts toward bonds as that year gets closer. The year is a target, not a guarantee.',
                             'A 2060 fund is built for someone hoping to retire around 2060.'),
}

index_funds = lesson('iv-index-funds', 'Index Funds', 'Buy the whole haystack instead of hunting for the needle.', [
    mc('Why do people buy funds?',
       ['To own lots of investments with one purchase', 'To make sure they never lose money', 'To borrow money'], 0,
       'One purchase, many investments. A [[fund]] is the pot. You own a slice.',
       context='A [[fund]] pools money from lots of people and invests it in many things at once. You buy a slice of the pot.'),
    mc('What does an index fund do?',
       ['Picks the single best stock', 'Buys every company on a list', 'Promises a profit'], 1,
       'No guessing which company wins. An [[index fund]] owns the list.',
       context='An [[index]] is a list that tracks a group of companies, like a country’s 500 biggest. An [[index fund]] simply buys everything on that list.'),
    mc('Two funds own the same things. One’s expense ratio is 1%, the other’s is 0.1%. Which leaves you more money?',
       ['The 1% fund', 'The 0.1% fund', 'No difference'], 1,
       'A lower [[expense ratio]] leaves more for you. On the same investments, the fee is the difference.',
       context='Every fund charges a yearly fee called the [[expense ratio]], a percentage of what you’ve invested. Index funds are usually cheap.'),
    num('You have $50,000 in a fund with a 1% expense ratio. What’s the fee each year?', 500,
        '$50,000 × 0.01 = $500, every single year.'),
    num('Same $50,000 in a fund with a 0.1% expense ratio. What’s the fee each year?', 50,
        '$50,000 × 0.001 = $50. You keep the other $450.'),
    tf('Paying an expert to pick stocks usually beats an index fund over the long run.', False,
       'Most fall behind after fees. That’s why index funds are so popular.'),
])

kinds = lesson('fe-kinds', 'Mutual Fund or ETF', 'Two wrappers. The insides can match.', [
    info('Same pot, different door',
         'A [[mutual fund]] is priced once a day, after the close. An [[ETF]] trades through the day like a [[stock]]. Either one can be an [[index fund]]. The wrapper is not what makes it cheap or expensive. The [[expense ratio]] and what it holds are.'),
    sort('Where does each fact belong?',
         ['Mutual fund', 'ETF', 'Either one'],
         [('Priced once, after the market closes', 0),
          ('Trades through the day like a stock', 1),
          ('Can be an index fund', 2),
          ('Charges an expense ratio', 2)],
         'The once-a-day price is the mutual fund. The all-day trading is the ETF. Index tracking and fees can be either.'),
    tf('An ETF is automatically cheaper than a mutual fund.', False,
       'Either wrapper can be cheap or expensive. Read the expense ratio.'),
    mc('You want to buy in the middle of the day at the price people are trading right then. Which wrapper does that?',
       ['A mutual fund, at the end-of-day price', 'An ETF', 'A CD'], 1,
       'The ETF trades through the day. The mutual fund waits for the closing price.'),
    fill('A fund that trades through the day like a stock is an ___.',
         ['ETF', 'I bond', 'coupon'], 0,
         'ETF is the short name for an exchange-traded fund.'),
], fmt='sort')

active = lesson('fe-active', 'Active or Passive', 'Picking winners, or owning the list.', [
    info('Two jobs',
         'A passive fund, such as an [[index fund]], buys the list and holds it. An active fund pays people to pick what they think will win. Those people cost money, so the [[expense ratio]] is usually higher. Over long periods, most active funds have ended up behind a simple index once the higher fees are counted.'),
    mc('Which fund is passive?',
       ['A fund that buys every company on an index', 'A fund whose manager trades in and out, hunting for winners', 'A fund that promises to beat the market'], 0,
       'Buying the list is passive. Hunting is active.'),
    tf('A higher fee is worth it whenever a person is picking the stocks.', False,
       'Most of those funds have lagged a cheap index after fees. A higher fee is a hurdle, not a medal.'),
    mc('Two funds hold the same index. One charges 0.05% and one charges 0.80% because it calls itself active. Which is the odd one?',
       ['The 0.05% fund, because cheap means bad', 'The 0.80% fund, because you are paying active prices for a list', 'They are the same deal'], 1,
       'If it owns the list, you want the small fee. The label “active” does not change the holdings.'),
    num('On $10,000, what is a 0.80% yearly fee, in dollars?', 80,
        '$10,000 × 0.008 = $80 a year. A 0.05% fee on the same pile is $5.'),
])

drag = lesson('fe-drag', 'Fees Over 30 Years', 'A small percent, many times.', [
    info('Hold the balance still',
         'This sketch pretends a $10,000 balance never changes, so you can see the fee by itself. A 1% [[expense ratio]] is $100 a year. A 0.1% expense ratio is $10 a year. Real life is harsher when the balance grows, because the fee is a percent of a bigger pile. These are not promised returns.'),
    num('At 1% a year on a steady $10,000, how many dollars of fees is that over 30 years?', 3000,
        '$100 × 30 = $3,000.'),
    num('At 0.1% a year on the same steady $10,000, how many dollars of fees is that over 30 years?', 300,
        '$10 × 30 = $300.'),
    num('How many more dollars does the 1% fund take over those 30 years, in this steady sketch?', 2700,
        '$3,000 − $300 = $2,700. Same investments, different fee.'),
    tf('Because the sketch held the balance still, the real fee on a growing balance would be smaller.', False,
       'A percent of a larger balance is more dollars. The still sketch understates the fee, it does not overstate it.'),
])

sheet = doc('statement', 'Fact sheet: Total US Market',
            [('held', 'You invested', 10000), ('fee', 'Yearly fee at 0.05%', 5)],
            meta=[('What it holds', 'The broad US stock market'), ('Expense ratio', '0.05%')],
            subtitle='A teaching fund, not a recommendation',
            note='The fee line is $10,000 × 0.0005.')

fact = lesson('fe-sheet', 'A Fund Fact Sheet', 'Holdings, fee, and no forecast.', [
    info('What to read',
         'A fact sheet says what the [[fund]] owns and what it charges. It does not say what the fund will earn next year. On this teaching sheet the fund owns the broad US stock market and charges 0.05%.'),
    num('How many dollars is the yearly fee on this sheet?', 5,
        doc=sheet,
        explain='$10,000 × 0.0005 = $5.'),
    mc('What does this fund hold, according to the sheet?',
       ['One company’s stock', 'The broad US stock market', 'Only bonds'], 1,
       'The sheet says the broad US stock market. That is an index-style holding, not a single stock.'),
    tf('A fact sheet’s past return is a promise for next year.', False,
       'The past is a record. Next year can be higher or lower. Read the holdings and the fee.'),
    num('If the expense ratio were 1% instead of 0.05%, how many dollars would the yearly fee be on this $10,000?', 100,
        '$10,000 × 0.01 = $100. That is $95 more than the $5 on the sheet.'),
], fmt='document')

target = lesson('fe-target', 'Target-Date Funds', 'A year on the label, and a mix that shifts.', [
    info('The year is a target',
         'A [[target-date fund]] has a year in its name, like 2060. It starts heavier in [[stock]]s and shifts toward [[bond]]s as that year gets closer. The year is when you hope to use the money. It is not a promise you will have enough, and it is not the year the fund closes.'),
    mc('A 2060 target-date fund is built for someone who hopes to retire around when?',
       ['2060', 'This year', 'Whenever the market peaks'], 0,
       'The year is the target. Far-off targets stay heavier in stocks.'),
    tf('A target-date fund guarantees you can retire in the year on the label.', False,
       'The mix shifts. The result still depends on what markets do and how much you put in.'),
    mc('As the target year gets closer, what does the mix usually do?',
       ['It shifts toward bonds', 'It shifts into a single stock', 'It stops charging an expense ratio'], 0,
       'Closer to the year, the fund usually takes less stock risk. You still check the fee.'),
    num('You are 25 in 2026 and you hope to retire at 65. Which target year matches that hope?', 2066, unit=None,
        explain='2026 + 40 = 2066. The fund year is a target around then, not a promise.'),
])

fee_doc = doc('statement', 'Two funds, same $10,000',
              [('cheap', 'Broad market fund, yearly fee', 5),
               ('pricey', 'Similar holdings, yearly fee', 120)],
              subtitle='Spot the fee that does not belong',
              note='Similar holdings should not cost $120 when $5 buys the same kind of list.')

spot_fee = lesson('fe-spot', 'Spot the High Fee', 'Same kind of list, very different bill.', [
    info('The line that hurts',
         'Both funds hold a broad stock market. One charges about 0.05%, which is $5 on $10,000. The other charges 1.2%, which is $120. The holdings are the reason to compare them. The fee is the reason to walk away from the second.'),
    spot('Which line is the high fee?', fee_doc, 'pricey',
         '$120 is 1.2% of $10,000. The $5 line is the cheap fund. Similar list, much smaller bill.'),
    num('How many more dollars a year does the pricey fund charge on this $10,000?', 115,
        '$120 − $5 = $115 a year, before any growth.'),
    tf('The pricey fund must be better because the fee is higher.', False,
       'On similar holdings the higher fee is money you do not get to keep.'),
    mc('What should you compare before you pick the pricey fund?',
       ['Only last year’s return', 'Whether the holdings are actually different, and what the fee is', 'The fund’s ticker length'], 1,
       'A different job can justify a different fund. The same job does not justify $115 more.'),
], fmt='spot')

omar = lesson('fe-omar', 'Omar’s First Fund', 'Cheap, broad, and boring on purpose.', [
    info('Meet Omar',
         'Omar is 26 and a bike mechanic. His [[emergency fund]] is already in cash. He has $2,000 he will not need for decades. He wants one [[fund]], not a pile of single stocks.\n\nHe compares two funds that both hold the broad US market. One has an [[expense ratio]] of 0.05%. The other charges 1%.'),
    num('On Omar’s $2,000, how many dollars a year is the 1% fee?', 20,
        '$2,000 × 0.01 = $20.'),
    num('On the same $2,000, how many dollars a year is the 0.05% fee?', 1,
        '$2,000 × 0.0005 = $1.'),
    mc('Which fund does Omar pick, and why?',
       ['The 1% fund, because a higher fee means more help', 'The 0.05% fund, because the holdings match and the fee is smaller', 'Neither, because funds are only for experts'], 1,
       'Same kind of list. He keeps the fee at $1 instead of $20 in this first year, if the balance stays $2,000.'),
    tf('Omar’s pick is a promise that the $2,000 will grow.', False,
       'The low fee means less drag. It does not promise a return. He still leaves the money alone for years.'),
], fmt='story', story={
    'title': 'The boring pick',
    'character': 'Omar, 26, bike mechanic',
    'body': 'Omar’s emergency fund is already cash. He has **$2,000** he will not need for decades.\n\nTwo funds both hold the broad US market. One charges **0.05%**. The other charges **1%**. He wants the smaller fee.',
})

write_unit('04-funds.json', 'funds', 4, 'Funds, ETFs & Index Investing',
           'One purchase, many investments, and a fee you can actually read.',
           'Own the list. Then check what the list costs.',
           terms, [index_funds, kinds, active, drag, fact, target, spot_fee, omar, review('fe'), trial('fe', 'Funds, ETFs & Index Investing', [
               num('A fund charges 0.2% a year on $20,000. How many dollars is the fee this year?', 40,
                   '$20,000 × 0.002 = $40.'),
               mc('An index fund’s job is to…',
                  ['Pick next year’s winner', 'Buy the investments on a list', 'Avoid every down year'], 1,
                  'It owns the [[index]]. It does not promise a profit.'),
               tf('A mutual fund and an ETF can both be index funds.', True,
                  'The wrapper differs. Either one can hold the list.'),
               mc('A target-date fund’s year means what?',
                  ['The year the fund guarantees a result', 'The year you are aiming to use the money', 'The year the fee disappears'], 1,
                  'The year is a target. The mix usually shifts toward bonds as it gets closer.'),
           ])],
           section=S)
