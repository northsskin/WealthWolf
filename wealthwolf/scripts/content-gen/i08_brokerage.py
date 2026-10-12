from lib import *

S = 'investing'
terms = {
    'market-order': term('Market order',
                         'An order to buy or sell now, at the best price currently available. You do not set a ceiling.',
                         'Buying at whatever the latest trade is, near $50.'),
    'limit-order': term('Limit order',
                        'An order that only trades at your price or better. A buy limit at $48 will not pay $50.',
                        '“Buy if the price is $48 or less.”'),
    'margin': term('Margin',
                   'Borrowing from the brokerage to buy more investments. Losses can be larger than the cash you put in.',
                   'Putting in $1,000 and borrowing $1,000 to buy $2,000 of stock.'),
    'dollar-cost-averaging': term('Dollar-cost averaging',
                                  'Investing the same number of dollars on a schedule, so you buy more shares when the price is lower and fewer when it is higher.',
                                  '$120 a month, whatever the price is that day.'),
    'sipc': term('SIPC',
                 'The Securities Investor Protection Corporation. If your brokerage fails, it protects up to $500,000 of securities per customer, including up to $250,000 of cash. It does not protect you from the market falling.',
                 'A brokerage goes under. The market dropping 20% is not an SIPC event.'),
}

opened = lesson('br-open', 'Opening the Account', 'The container, then the cash, then the buy.', [
    info('A brokerage is the shop',
         'A brokerage account is where you buy [[stock]]s, [[bond]]s, and [[fund]]s outside a workplace plan. You prove who you are, link a bank, and send cash. The cash sits there until you place a trade. This unit stays with cash. [[Margin]] comes next, as the thing to skip.'),
    order('Put a first account in order.',
          ['Open the brokerage and verify your identity',
           'Link your bank',
           'Transfer cash in',
           'Place a buy with that cash'],
          'No cash, no trade. The buy is last.'),
    tf('Money you transfer in is invested automatically, the moment it arrives, in a stock the brokerage picks.', False,
       'A transfer is cash. You still choose the investment, unless you separately set up an automatic buy.'),
    mc('Which account is this lesson about?',
       ['A workplace 401(k)', 'A brokerage account you open yourself', 'A savings account at 4% APY'], 1,
       'The 401(k) is the job. This is the account at a brokerage.'),
    num('You transfer $500 and the trade costs $200. How many dollars of cash are left in the account after the trade?', 300,
        '$500 − $200 = $300 still in cash. It is not invested until you buy something with it.'),
])

margin = lesson('br-margin', 'Cash, Not Margin', 'Borrowed shares can wipe out more than you brought.', [
    info('Skip the loan',
         'A cash account spends your money. A [[margin]] account borrows from the brokerage so you can buy more. If the investment falls, you can lose the cash you put in and still owe the loan. Beginners stay on cash.'),
    num('You put in $1,000 and borrow $1,000 to buy $2,000 of stock. The stock falls 50%, to $1,000. How many dollars do you still owe?', 1000,
        'The loan does not shrink with the stock. You owe $1,000, and the stock is now worth $1,000, so your equity is $0.'),
    num('After that drop, how many dollars of your own $1,000 are left as equity?', 0,
        '$1,000 of stock minus the $1,000 you owe is $0. The whole cash stake is gone. A deeper drop would leave you owing more than the stock is worth.'),
    tf('Margin losses stop at the cash you deposited.', False,
       'The loan stays. A hard drop can leave you owing more than the investment is worth.'),
    mc('What should a beginner use?',
       ['A margin account, to buy twice as much', 'A cash account', 'A loan from the 401(k) to fund the brokerage'], 1,
       'Cash. The extra shares are not worth the chance of owing money.'),
])

mkt = doc('statement', 'Market order',
          [('est', 'Last price you are seeing', 50)],
          subtitle='Buy now, at the available price',
          note='The fill can differ a little from the last price you saw.')
lim = doc('statement', 'Limit order at $48',
          [('cap', 'Most you will pay', 48)],
          subtitle='No trade if the price stays above $48')

orders = lesson('br-orders', 'Market or Limit', 'Now, or only at your price.', [
    info('Two instructions',
         'A [[market order]] says buy now, at the best price on offer. A [[limit order]] says buy only at your price or better. A limit protects the price and can mean you get no shares.'),
    mc('You want the shares today and you accept the current price. Which order is that?',
         [mkt['title'], lim['title']], 0,
         docs=(mkt, lim),
         explain='The market order takes the available price. The $48 limit waits, and it may never fill while the price is $50.'),
    num('Your limit is $48 and the only shares on offer are at $50. How many shares does that limit order buy?', 0, unit=None,
        explain='A buy limit at $48 will not pay $50. Zero shares. That is the order doing its job.'),
    tf('A market order guarantees the last price shown on the screen.', False,
       'It takes the best available price, which can be a bit different by the time the order arrives.'),
    mc('You will not pay more than $48. Which order says that?',
       ['Market order', 'Limit order at $48', 'Margin'], 1,
       'The limit is the ceiling. The market order has no ceiling.'),
], fmt='call')

frac = lesson('br-frac', 'Fractional Shares', 'A slice, when one whole share is a lot.', [
    info('Part of a share',
         'A fractional share is a piece of one share. If a share costs $200 and you invest $50, you own 0.25 of a share. You still own a slice of that one company, with that one company’s risk. It is a way to fit a budget. It is not diversification.'),
    num('A share costs $200. How many dollars buy one quarter of it?', 50,
        '0.25 × $200 = $50.'),
    num('You invest $25 in a share that costs $100. How many shares do you own? Enter 0.25 if you own a quarter.', 0.25, unit=None,
        explain='$25 ÷ $100 = 0.25 of a share.'),
    tf('Owning 0.25 of one company’s share is the same as owning an index fund.', False,
       'It is still one company. The fraction only changes how much of it you bought.'),
    mc('Why do brokerages offer fractional shares?',
       ['So a $50 deposit can buy part of a $200 share', 'So one company becomes hundreds of companies', 'So margin is required'], 0,
       'The fraction fits the deposit. The risk is still the company’s risk.'),
])

confirm = doc('statement', 'Trade confirmation',
              [('trade', '4 shares at $50', 200), ('fee', 'Commission', 5)],
              totals=[('You paid', 205, True)],
              subtitle='WOLF, a made-up ticker',
              note='The share cost and the commission are separate lines.')

conf = lesson('br-confirm', 'The Confirmation', 'Shares, price, and the fee beside them.', [
    info('Read it before you forget',
         'A confirmation is the receipt. It shows what you bought, the price, and any commission. This one is 4 shares of the made-up ticker WOLF at $50, plus a $5 commission.'),
    num('How many dollars did the shares themselves cost?', 200,
        doc=confirm,
        explain='4 × $50 = $200. That line is the shares, not the fee.'),
    num('How many dollars did you pay in total, shares plus commission?', 205,
        doc=confirm,
        explain='$200 + $5 = $205.'),
    tf('The commission is part of the share price, so the shares really cost $51.25 each and the fee line is optional.', False,
       'The shares cost $200. The $5 is a separate fee. Ignoring the fee line understates what left your cash.'),
    mc('What is WOLF in this confirmation?',
       ['A real company this course wants you to buy', 'A made-up ticker so the receipt can have a name', 'A type of bond'], 1,
       'The lesson needs a name on the receipt. It is not a recommendation.'),
], fmt='document')

protect = lesson('br-sipc', 'If the Brokerage Fails', 'SIPC is not a market refund.', [
    info('What is protected',
         '[[SIPC]] steps in if your brokerage fails and your securities are missing, up to $500,000 per customer, including up to $250,000 of cash. If your stocks fall because the market fell, SIPC does not pay you back. A drop is not a failed brokerage.'),
    num('SIPC’s securities protection is up to how many dollars per customer?', 500000,
        'The cap is $500,000, and no more than $250,000 of that can be cash.'),
    num('You hold $600,000 of securities at one brokerage and it fails. How many dollars of that are above the $500,000 SIPC cap?', 100000,
        '$600,000 − $500,000 = $100,000 above the cap.'),
    tf('SIPC replaces losses when the stock market drops.', False,
       'SIPC is about a failed brokerage, not a fallen price.'),
    mc('Which event is an SIPC kind of problem?',
       ['Your index fund falls 15% in a month', 'The brokerage fails and customer securities are missing', 'You sell at a loss'], 1,
       'A failed brokerage. The 15% drop is market risk, and selling is your trade.'),
])

fee_doc = doc('statement', 'A tiny trade',
              [('buy', 'Shares', 100), ('comm', 'Commission', 40)],
              totals=[('Cash out', 140)],
              subtitle='The fee is the problem line')

fees = lesson('br-fees', 'Fees to Watch', 'A $40 fee on a $100 trade is the whole story.', [
    info('The line that eats the trade',
         'Commissions, fund [[expense ratio]]s, and account fees all leave with your money. On a $100 trade, a $40 commission is 40% gone before the investment does anything. Many brokerages now charge $0 to trade shares. A $40 commission is a reason to look at a different brokerage.'),
    spot('Which line is the fee that does not belong on a $100 trade?', fee_doc, 'comm',
         'The $40 commission is 40% of the $100 trade. The shares line is the investment. The fee is the problem.'),
    num('What percent of the $100 share purchase is that $40 commission?', 40, unit='%',
        explain='$40 ÷ $100 = 0.40, which is 40%.'),
    tf('A zero-commission trade means the fund inside it has no expense ratio.', False,
       'The trade can be free and the fund can still charge a yearly percent. Read both.'),
    mc('Which fee keeps charging after the trade is done?',
       ['A one-time commission', 'A fund’s expense ratio, every year', 'SIPC'], 1,
       'The expense ratio is yearly. A commission, if there is one, is the trade itself.'),
], fmt='spot')

luis = lesson('br-luis', 'The Automatic $120', 'Same dollars, different prices.', [
    info('Meet Luis',
         'Luis is 27 and a line cook. On payday he invests $120 into one broad [[fund]], automatically. That habit is [[dollar-cost averaging]]. Over three months the price is $10, then $8, then $12.\n\nHe buys 12 shares, then 15, then 10. He did not pick the prices. The schedule did.'),
    num('At $10 a share, how many shares does $120 buy?', 12, unit=None,
        explain='$120 ÷ $10 = 12 shares.'),
    num('At $8 a share, how many shares does the next $120 buy?', 15, unit=None,
        explain='$120 ÷ $8 = 15 shares. The lower price bought more shares.'),
    num('The third month is $12 a share, so 10 shares. How many shares does Luis own after all three months?', 37, unit=None,
        explain='12 + 15 + 10 = 37 shares. He spent 3 × $120 = $360.'),
    tf('Dollar-cost averaging promises you will beat someone who invested the whole amount on day one.', False,
       'It is a habit. It buys more shares at lower prices. It is not a promise of a higher return than investing a lump sum.'),
], fmt='story', story={
    'title': 'Payday, every payday',
    'character': 'Luis, 27, line cook',
    'body': 'Luis invests **$120** on payday into one broad fund. Over three months the price is **$10**, then **$8**, then **$12**.\n\nHe buys **12** shares, then **15**, then **10**. The schedule did the buying.',
})

write_unit('08-brokerage.json', 'brokerage', 8, 'Brokerage Accounts & Placing Trades',
           'Cash accounts, order types, and the fees sitting on the receipt.',
           'Use cash. Read the confirmation. Then automate it.',
           terms, [opened, margin, orders, frac, conf, protect, fees, luis, review('br'), trial('br', 'Brokerage Accounts & Placing Trades', [
               num('You buy $60 of a share that costs $240. What fraction of a share is that? Enter 0.25 for a quarter.', 0.25, unit=None,
                   explain='$60 ÷ $240 = 0.25 of a share.'),
               tf('SIPC pays you back when your fund drops.', False,
                  'SIPC covers a failed brokerage, up to its caps. A market drop is not that event.'),
               mc('A buy limit at $30, when the price is $36, does what?',
                  ['Buys immediately at $36', 'Waits, and does not pay more than $30', 'Borrows the $6 difference'], 1,
                  'The limit is the ceiling. No fill while the price is above it.'),
               num('Three automatic deposits of $100 buy shares at $10, $5, and $20. How many shares is that in total?', 35, unit=None,
                   explain='$100 ÷ $10 = 10, $100 ÷ $5 = 20, and $100 ÷ $20 = 5. 10 + 20 + 5 = 35 shares.'),
           ])],
           section=S)
