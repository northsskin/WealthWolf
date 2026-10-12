from lib import *

S = 'investing'
terms = {
    'ticker': term('Ticker',
                   'The short code a stock uses on an exchange, so you can find that company and not a different one.',
                   'A made-up company that trades as WOLF.'),
    'market-cap': term('Market cap',
                       'What the whole company is priced at: the share price times the number of shares.',
                       'A $40 share and 2,000,000 shares is a market cap of $80,000,000.'),
    'price-to-earnings': term('Price-to-earnings',
                              'The share price divided by the company’s yearly earnings per share. It says how many dollars you pay for each dollar of those earnings. It is not a buy signal.',
                              'A $30 share with $2 of yearly earnings per share has a price-to-earnings of 15.'),
    'dividend-yield': term('Dividend yield',
                           'The yearly dividend divided by the share price, as a percent.',
                           'A $1 yearly dividend on a $50 share is a 2% dividend yield.'),
}

share = lesson('sk-share', 'What a Share Is', 'One share is one piece, not the whole company.', [
    info('A piece, with a price',
         'A [[stock]] is a piece of a company. One share is one of those pieces. The price is what buyers and sellers agreed to most recently. It is not a promise of what the company is “really” worth.'),
    mc('You buy 10 shares at $40. What do you own?',
       ['The whole company', '10 pieces of the company', 'A loan to the company'], 1,
       '10 shares are 10 pieces. The other shares belong to other owners.'),
    num('Those 10 shares cost $40 each. How many dollars did you pay?', 400,
        '10 × $40 = $400.'),
    tf('The share price is a promise of what the company will be worth next year.', False,
       'The price is the latest trade. Next year it can be higher or lower.'),
    mc('A share of stock is closest to which idea?',
       ['A slice of ownership', 'A savings account at a bank', 'A bill you owe'], 0,
       'Ownership. A [[bond]] is the loan. A share is a piece of the company.'),
])

ticker = lesson('sk-ticker', 'Exchanges and Tickers', 'The marketplace, and the short code.', [
    info('Where a share trades',
         'An exchange is the marketplace where shares are bought and sold. A [[ticker]] is the short code for one company on that marketplace. This course uses a made-up ticker, WOLF, so it is never a tip to buy a real company.'),
    mc('What is a ticker?',
       ['The yearly dividend', 'The short code that finds one company’s stock', 'The fee to trade'], 1,
       'The ticker is the code. The price and the dividend are different facts.'),
    mc('What is an exchange?',
       ['The marketplace where the shares trade', 'A tax form', 'The company’s profit'], 0,
       'Buyers and sellers meet there. The latest trade sets the price you see.'),
    tf('Two different companies can be the right one to buy just because their names look similar.', False,
       'Names can be close. The ticker is how you check you have the company you meant.'),
    fill('The short code for a stock is called its ___.',
         ['ticker', 'coupon', 'premium'], 0,
         'Ticker. Check it before you buy, so a similar name does not send you to the wrong company.'),
])

nina = lesson('sk-nina', 'Why Prices Move', 'A headline changes what people will pay.', [
    info('Meet Nina',
         'Nina is 28 and a warehouse supervisor. She owns 10 shares of a made-up company, ticker WOLF, at $40. That is $400.\n\nA news story says a big customer might leave. Buyers will not pay $40 anymore. The price falls to $32.'),
    num('Nina’s 10 shares fall from $40 to $32. How many dollars did she lose?', 80,
        'The drop is $8 a share. 10 × $8 = $80. Her $400 is now $320.'),
    num('What are the 10 shares worth at $32?', 320,
        '10 × $32 = $320.'),
    mc('Why did the price fall?',
       ['The exchange changed her ticker', 'Buyers changed what they would pay after the news', 'Dividends are illegal'], 1,
       'The price is the latest agreement. Bad news can make that agreement a lower number.'),
    tf('A falling price means Nina did something wrong.', False,
       'Prices move because the crowd changes its mind. One owner cannot hold the old price in place.'),
], fmt='story', story={
    'title': 'The headline',
    'character': 'Nina, 28, warehouse supervisor',
    'body': 'Nina owns **10** shares of a made-up company at **$40**, so **$400**. A news story says a big customer might leave.\n\nBuyers will not pay $40 anymore. The price falls to **$32**.',
})

cap = lesson('sk-cap', 'Market Cap', 'Price times every share.', [
    info('The whole price tag',
         '[[Market cap]] is the share price times the number of shares. A $40 price on a giant company is not “cheaper” than a $20 price on a tiny one. The whole price tag is the market cap.'),
    num('WOLF has 2,000,000 shares at $40. What is the market cap in dollars?', 80000000,
        '2,000,000 × $40 = $80,000,000.'),
    mc('Company A is $20 a share. Company B is $40 a share. Which must be the bigger company?',
       ['Company B, because $40 is more', 'You cannot tell from the share price alone', 'Company A, because a low price means a giant'], 1,
       'Share price is one share. Market cap is the whole company. You need the number of shares too.'),
    tf('A $10 stock is automatically a better deal than a $100 stock.', False,
       'The price is per share. A $10 stock can be a tiny company or a giant one with many shares.'),
    num('A company has a market cap of $80,000,000 and 2,000,000 shares. What is the price of one share?', 40,
        '$80,000,000 ÷ 2,000,000 = $40.'),
])

pe = lesson('sk-pe', 'Price and Earnings', 'How many dollars for one dollar of earnings.', [
    info('A beginner ratio',
         '[[Price-to-earnings]] is the share price divided by the company’s yearly earnings per share. A result of 15 means you are paying $15 for each $1 of those earnings. It is a description, not a signal to buy or sell.'),
    num('A share costs $30 and the company earned $2 per share this year. What is the price-to-earnings?', 15, unit=None,
        explain='$30 ÷ $2 = 15. You are paying $15 for each $1 of that year’s earnings.'),
    mc('What does a price-to-earnings of 15 tell you by itself?',
       ['That you should buy the stock', 'That you pay $15 for each $1 of those yearly earnings', 'That the stock cannot fall'], 1,
       'It is a ratio. It is not a recommendation, and it does not remove risk.'),
    tf('A low price-to-earnings guarantees the stock will rise.', False,
       'Cheap on a ratio can still be a weak company. The ratio does not promise a return.'),
    num('You pay $15 for each $1 of yearly earnings. On $2 of earnings per share, what share price does that describe?', 30,
        '15 × $2 = $30.'),
])

dyield = lesson('sk-yield', 'Dividends and Yield', 'The cash, then the percent.', [
    info('Cash, as a percent of the price',
         'A [[dividend]] is cash some companies pay their owners. [[Dividend yield]] is that yearly cash divided by the share price. A $1 dividend on a $50 share is 2%. A high yield can also be a falling price, so it is not automatically good.'),
    num('A share pays a $1 dividend and costs $50. What is the dividend yield, in percent?', 2, unit='%',
        explain='$1 ÷ $50 = 0.02, which is 2%.'),
    num('You own 20 of those $50 shares. How many dollars of dividends do you get in a year at $1 a share?', 20,
        '20 × $1 = $20. The yield is still 2%.'),
    mc('A dividend yield jumps from 2% to 6% because the share price fell and the dividend stayed $1. What happened?',
       ['The company doubled the dividend', 'The price drop made the same $1 look bigger', 'The yield is a fee you pay'], 1,
       'Yield is dividend ÷ price. A lower price raises the yield even when the cash did not change.'),
    tf('Every stock pays a dividend.', False,
       'Some companies pay none and keep the profits in the business. No dividend is not the same as a broken stock.'),
])

quote = doc('statement', 'Quote for WOLF',
            [('last', 'Last price', 50), ('div', 'Dividend per year', 1)],
            subtitle='A made-up company, not a tip',
            note='Dividend yield is the yearly dividend divided by the last price.')

read_quote = lesson('sk-quote', 'Reading a Quote', 'Two numbers, and what they are not.', [
    info('The quote',
         'A quote is a snapshot. The last price is the latest trade. The dividend line is the cash the company pays in a year, if it pays one. Neither line is a prediction.'),
    num('What is the last price on this quote, in dollars?', 50,
        doc=quote,
        explain='The last price is $50. That is the latest trade, not a forecast.'),
    num('What is the dividend yield on this quote, in percent?', 2, unit='%',
        doc=quote,
        explain='$1 ÷ $50 = 0.02, which is 2%.'),
    tf('The last price on a quote is the price the company promises to buy the share back for.', False,
       'It is the latest trade between buyers and sellers. The company is not promising that price.'),
    mc('This quote is for a made-up ticker. Why does the course use one?',
       ['So the lesson is a tip to buy a real company', 'So you can practice the numbers without a buy recommendation', 'Because real companies do not have tickers'], 1,
       'WOLF is a teaching name. A real quote uses the same kind of lines, and this course still will not name a stock to buy.'),
], fmt='document')

one_page = doc('statement', 'One company',
               [('shares', '10 shares of WOLF', 400)],
               subtitle='All $400 is in one stock')
many_page = doc('statement', 'Hundreds of companies',
                [('fund', 'A fund that owns hundreds of stocks', 400)],
                subtitle='The same $400, spread out')

one_or_many = lesson('sk-one', 'One Stock or the Market', 'A single headline can hit one company.', [
    info('The same dollars, two shapes',
         'Owning one [[stock]] means one company’s news is your news. A fund that holds hundreds of companies still rises and falls, but one failed product is a small piece of it. A later unit names that kind of fund. This lesson is only the contrast.'),
    mc('A single bad headline hits one company. Which page takes the full hit?',
         [one_page['title'], many_page['title']], 0,
         docs=(one_page, many_page),
         explain='The one-company page has nowhere else for the loss to hide. The fund still moves, but one company is a slice, not the whole $400.'),
    num('Both pages start at $400. The one stock falls 20%. How many dollars is that page worth?', 320,
        '$400 × 0.80 = $320. The whole page took the drop.'),
    tf('A fund of hundreds of companies cannot lose money.', False,
       'The whole market can fall. Spreading out avoids one company’s disaster. It does not avoid every drop.'),
    mc('Why might a beginner use a broad fund instead of picking one company?',
       ['Because one company cannot fall', 'Because one company’s bad year is not the whole account', 'Because funds are guaranteed'], 1,
       'The point of the many is that one failure is a piece. Nothing here is guaranteed.'),
], fmt='call')

write_unit('02-stock-market.json', 'stock-market', 2, 'The Stock Market',
           'Shares, prices, and why one company is a different bet from the whole market.',
           'A price is the latest trade, not a promise.',
           terms, [share, ticker, nina, cap, pe, dyield, read_quote, one_or_many, review('sk'), trial('sk', 'The Stock Market', [
               num('You own 8 shares at $25. How many dollars did they cost?', 200,
                   '8 × $25 = $200.'),
               num('A share pays $2 a year and costs $40. What is the dividend yield, in percent?', 5, unit='%',
                   explain='$2 ÷ $40 = 0.05, which is 5%.'),
               tf('Market cap is the share price alone.', False,
                  '[[Market cap]] is the price times the number of shares.'),
               mc('A price-to-earnings ratio is best read as what?',
                  ['A promise the price will rise', 'The dollars you pay per dollar of those earnings', 'The dividend'], 1,
                  'It describes the price against earnings. It is not a buy signal.'),
           ])],
           section=S)
