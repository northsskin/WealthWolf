from lib import *

# "Credit card" is defined in the Credit & Debt section; this unit is where the path first teaches it.
terms = {
    'peer-to-peer-payment': term('Peer-to-peer payment', 'Sending money straight from one person to another with an app like Venmo, Zelle or Cash App.',
                                 'Paying a friend back $12 for pizza from your phone.'),
    'sales-tax': term('Sales tax', 'A tax added to the price at the register. In most US states the shelf price doesn’t include it.',
                      'A $40 jacket with 7% sales tax costs $42.80.'),
    'foreign-transaction-fee': term('Foreign transaction fee', 'An extra charge, often 3%, when you pay in another currency or with a store based abroad.',
                                    'Spend $500 on a trip and a 3% fee adds $15.'),
}

ways = lesson('pm-ways-to-pay', 'Ways to Pay', 'Cash, debit, credit and apps all move money. Differently.', [
    info('Four ways to pay',
         'Cash, debit cards, credit cards and payment apps all move money, but they work differently: whose money it is, how fast it moves, '
         'and what protection you get if something goes wrong.'),
    mc('You pay $50 with a credit card. Whose money paid the store?',
       ['The card company’s, and now you owe it back', 'Yours, straight from checking', 'Nobody’s'], 0,
       'A credit card is a loan you pay back when the bill comes.',
       context='A [[credit card]] lets you buy now and pay later. The money is borrowed from the card company, and you get a bill each month.'),
    sort('Whose money is it?', ['Your money, right now', 'Borrowed, paid back later'],
         [('Cash', 0), ('Debit card', 0), ('Credit card', 1), ('Payment app linked to your bank account', 0)]),
    tf('Paying with a credit card always costs the same as paying with a debit card.', False,
       'Not if you leave part of the bill unpaid. Then you pay interest on top.'),
    mc('Which way of paying leaves no record unless you write it down?', ['Cash', 'Debit card', 'Credit card'], 0, 'Cash leaves no trail.'),
    match('Match each way to pay.', [
        ('Cash', 'Paper money, gone when it’s spent'),
        ('Debit card', 'Spends from your checking account'),
        ('Credit card', 'Borrowed money, billed monthly'),
        ('Payment app', 'Sends money between people from your phone'),
    ]),
])

dvc = lesson('pm-debit-vs-credit', 'Debit vs. Credit', 'Same plastic, very different rules.', [
    mc('A thief spends $500 with your stolen card. With which card is your own money missing while the bank investigates?', ['Debit', 'Credit'], 0,
       'Debit fraud takes your real cash until it’s sorted out. Credit card fraud is the card company’s money.'),
    tf('If you pay your credit card bill in full every month, you pay no interest.', True, 'Pay in full, and the borrowing is free.'),
    num('You leave $500 unpaid on a card charging about 24% a year. Roughly how much interest is that over a year?', 120,
        '$500 × 0.24 = $120.', context='If you don’t pay the bill in full, the card charges interest on what’s left. Rates around 24% a year are common.'),
    mc('Which habit is safest for a beginner?',
       ['Only put on credit what you could pay with cash today, then pay in full', 'Use credit for things you can’t afford yet', 'Pay just the minimum each month'], 0,
       'Treat it like a debit card that sends one bill.'),
    mc('Which card builds a credit history?', ['A credit card', 'A debit card'], 0,
       'Credit history comes from borrowing and paying back on time. More on that in the Credit & Debt section.'),
    fill('With a ___ card, the money comes straight out of your checking account.', ['debit', 'credit', 'gift'], 0, 'Debit means your own money.'),
], fmt='call')

apps = lesson('pm-apps', 'Payment Apps', 'Instant and easy. Also instant and final.', [
    mc('What’s a payment app best for?', ['Paying back a friend you know', 'Buying from a stranger online', 'Paying someone who says you won a prize'], 0,
       'Use it with people you know and trust.',
       context='A [[peer-to-peer payment]] app (like Venmo, Zelle or Cash App) sends money from one person to another in seconds.'),
    tf('If you send money to the wrong person on a payment app, you can always get it back.', False,
       'Payments are often instant and final. Check the name and number before you hit send.'),
    mc('Before sending $60 to a friend, what should you check?', ['Their exact name or number, and the amount', 'Their favorite color', 'Nothing'], 0,
       'One wrong digit sends your money to a stranger.'),
    mc('A stranger “accidentally” sends you $200 and asks you to send it back. What’s going on?',
       ['Probably a scam: their $200 may vanish later, and yours won’t come back', 'An honest mistake', 'A refund you were owed'], 0,
       'Tell them to ask their bank to reverse it. Don’t send your own money.'),
    num('An instant transfer to your bank costs 1.75%. How much is that on $400?', 7, '$400 × 0.0175 = $7.'),
    tf('Money sitting in a payment app balance may not have FDIC insurance.', True,
       'Many app balances aren’t bank deposits. Move larger amounts to your insured account.'),
])

tips_tax = lesson('pm-tips-tax', 'Tips & Sales Tax', 'The price on the tag isn’t the price you pay.', [
    num('A $40 jacket with 7% sales tax. What do you pay?', 42.80, '$40 × 0.07 = $2.80 tax. $40 + $2.80 = $42.80.',
        context='[[Sales tax]] is added at the register in most US states. The price on the tag usually doesn’t include it.'),
    num('8.25% sales tax on a $200 purchase. How much is the tax?', 16.50, '$200 × 0.0825 = $16.50.'),
    mc('Where do US prices usually include sales tax already?', ['Hardly anywhere, so add it in your head', 'Everywhere', 'Only online'], 0,
       'Expect the register total to be a bit higher than the tag.'),
    num('What’s a 20% tip on a $45 meal?', 9, '$45 × 0.20 = $9.', context='To work out a tip, multiply. 20% is the same as × 0.20.'),
    num('What’s a 15% tip on $60?', 9, '$60 × 0.15 = $9.'),
    tf('A quick way to find 20%: find 10% by moving the decimal point one place left, then double it.', True,
       '10% of $45 is $4.50. Double it: $9.'),
])

bill_lines = [('pizza', 'Margherita pizza', 16.00), ('lasagna', 'Lasagna', 19.50), ('salad', 'Caesar salad', 12.00),
              ('tiramisu', 'Tiramisu', 9.00), ('drinks', 'Lemonade', 18.00, {'qty': 4})]
subtotal = total(l[2] for l in bill_lines)
tax = money(subtotal * 0.08)
bill_total = total([subtotal, tax])
assert subtotal == 74.50 and tax == 5.96 and bill_total == 80.46
LUIGI = doc('receipt', 'Luigi’s Trattoria', bill_lines, subtitle='Table 6 · Fri 8:05 PM',
            totals=[('Subtotal', subtotal), ('Sales tax, 8%', tax), ('Total', bill_total, True)], note='Tip not included.')
tip = money(subtotal * 0.20)
assert tip == 14.90
split = lesson('pm-split', 'Splitting the Bill', 'Dinner for two: tax, tip and who owes what.', [
    num('What’s the total before tip?', bill_total, 'It’s printed at the bottom: $80.46.', doc=LUIGI),
    num('A 20% tip on the $74.50 subtotal?', tip, '$74.50 × 0.20 = $14.90.', doc=LUIGI,
        context='Tip is usually worked out on the total before tax, often 18–20%.'),
    num('You split the total plus tip evenly between 2 friends. What does each pay?', 47.68,
        '$80.46 + $14.90 = $95.36. $95.36 ÷ 2 = $47.68.', doc=LUIGI),
    mc('You had the salad and one lemonade. Your friend had everything else. What’s the fairest split?',
       ['Each pays for what they ordered', 'Split it 50/50', 'Whoever picked the restaurant pays'], 0,
       'Even splits are easy, but item-by-item is fair when orders are lopsided.', doc=LUIGI),
    num('Your items: the salad and one $4.50 lemonade. What’s your subtotal?', 16.50, '$12.00 + $4.50 = $16.50.', doc=LUIGI),
    tf('When you split by item, tax and tip should be shared in the same proportion.', True,
       'You ordered about 22% of the food, so you cover about 22% of the tax and tip.'),
], fmt='document')

cash = lesson('pm-cash', 'Cash Still Counts', 'Why paper money still has a place.', [
    mc('Why do some people budget with cash?', ['It’s harder to overspend money you can see', 'Cash earns interest', 'Every store gives a cash discount'], 0,
       'Watching the bills leave your hand makes spending feel real.',
       context='Paying with cash feels different. Handing over real bills makes spending more noticeable, so many people spend less.'),
    tf('Some stores and gas stations charge less if you pay with cash.', True, 'Card fees cost them money, so some pass the saving on.'),
    mc('You need $40 in cash. Cheapest way?', ['Cash back at the grocery register with your debit card', 'An out-of-network ATM with two fees', 'Borrowing from a payday lender'], 0,
       'Many stores give cash back with a debit purchase for free.',
       context='At many stores you can ask for cash back at the register when you pay with debit, usually with no fee.'),
    num('Your weekly cash budget is $80. You’ve spent $23, $18 and $27. How much is left?', 12, '$80 − $23 − $18 − $27 = $12.'),
    mc('What’s the downside of cash?', ['If it’s lost or stolen, it’s gone', 'It’s too slow', 'It’s illegal in some stores'], 0,
       'No fraud protection, no getting it back.'),
    order('A cash week: put it in order.',
          ['Decide the week’s cash amount', 'Take it out once, fee-free', 'Spend only what’s in your wallet', 'Note what’s left at the end of the week'],
          'Plan, withdraw, spend, review.'),
])

app_lines = [
    ('jamie', 'From Jamie: pizza', 12.00, {'date': 'Nov 3'}),
    ('prize', 'Request from “Prize Center”: release fee', -49.99, {'date': 'Nov 4'}),
    ('mom', 'To Mom: phone bill', -35.00, {'date': 'Nov 5'}),
    ('chris', 'From Chris: concert tickets', 40.00, {'date': 'Nov 6'}),
]
APP = doc('statement', 'QuickPay', app_lines, subtitle='Activity and requests')
scam = lesson('pm-scam', 'Request or Scam?', 'Payment apps are a scammer’s favorite tool. Spot the setup.', [
    spot('Tap the request you should decline.', APP, 'prize', 'A real prize never charges a fee to “release” it.',
         context='Scammers love payment apps because money moves instantly and is hard to get back.'),
    mc('Why is a “release fee” for a prize a red flag?', ['Real prizes don’t make you pay to collect them', 'Fees are normal for prizes', 'It isn’t a red flag'], 0,
       'If you have to pay to win, you didn’t win.'),
    tf('Payment app scammers often pretend to be your bank, a store, or someone you know.', True, 'Check by calling the real person or company yourself.'),
    mc('Someone selling concert tickets online wants payment through an app. What’s safer?',
       ['Buy through a platform with buyer protection, or pay by credit card', 'Pay first, they seem nice', 'Send extra to be sure'], 0,
       'Payment apps rarely protect purchases from strangers.'),
    order('You think you’ve been scammed on an app. Put it in order.',
          ['Report it in the app', 'Call your bank', 'Change your password', 'Report it to the FTC'],
          'Fast reports give you the best chance of getting money back.'),
    mc('Who should you send money to with a payment app?', ['People you know and trust', 'Anyone who asks politely', 'Sellers you just met online'], 0,
       'Treat it like handing over cash.'),
], fmt='spot')

abroad = lesson('pm-abroad', 'Paying Online & Abroad', 'Hidden fees on trips and risky checkouts.', [
    num('You spend $500 abroad on a card with a 3% foreign transaction fee. How much is the fee?', 15, '$500 × 0.03 = $15.',
        context='A [[foreign transaction fee]] is an extra charge, often 3%, when you pay in another currency or with a store based abroad.'),
    mc('A card machine abroad asks: pay in dollars or local currency?', ['Local currency, to avoid the machine’s worse exchange rate', 'Dollars, always', 'It makes no difference'], 0,
       'Paying in dollars lets the shop pick the exchange rate, and it’s rarely a good one.'),
    mc('Shopping online, what makes a site safer?', ['A store you know, a secure checkout, and paying by credit card', 'A pop-up saying you won', 'Everything 90% off'], 0,
       'Too-good deals and pop-ups are classic warning signs.'),
    tf('Saving your card on lots of small websites is low risk.', False, 'Every site that stores your card is another place it can leak.'),
    num('A trip costs $1,200 on a card with a 3% foreign transaction fee. What’s the fee?', 36, '$1,200 × 0.03 = $36.'),
    mc('Which card is best for travel?', ['One with no foreign transaction fee', 'The one with the nicest design', 'A debit card with ATM fees'], 0,
       'Many cards charge 0%. Check before you go.'),
])

trial_steps = [
    num('What’s a 20% tip on a $35 meal?', 7, '$35 × 0.20 = $7.'),
    mc('Your card is stolen and used. Which card keeps your own cash safe while the bank investigates?', ['Credit', 'Debit'], 0,
       'With credit, it’s the card company’s money on the line.'),
    tf('Payments sent on a peer-to-peer app are easy to reverse.', False, 'They’re usually instant and final.'),
    num('6% sales tax on a $150 purchase. How much is the tax?', 9, '$150 × 0.06 = $9.'),
]

lessons = [ways, dvc, apps, tips_tax, split, cash, scam, abroad,
           review('pm'), trial('pm', 'Ways to Pay', trial_steps)]
write_unit('09-payments.json', 'payments', 9, 'Cash, Cards & Payment Apps',
           'Cash, debit, credit and payment apps: which to use, and how not to get burned.',
           'Money moves fast now. Make sure it’s going where you meant.', terms, lessons)
