from lib import *

S = 'building-wealth'
terms = {
    'federal-reserve': term('Federal Reserve',
                            'The central bank of the United States. It sets a target for the short-term rate banks charge each other, and that target ripples out to loans and savings.',
                            'A Fed move does not rewrite a fixed mortgage you already locked.'),
    'federal-funds-rate': term('Federal funds rate',
                               'The rate banks charge one another for overnight loans. The Federal Reserve sets a target for it. Your savings rate and a new loan rate are related, but they are not this number itself.',
                               'When the target rises, new loans tend to cost more.'),
}

fed = lesson('fd-fed', 'What the Fed Does', 'A target for short-term rates. Not your landlord.', [
    info('The short rate',
         'The [[Federal Reserve]] is the central bank. Its famous lever is the [[federal funds rate]], the overnight rate banks charge each other. When that target moves, savings yields and new loan rates tend to follow. The Fed does not set your grocery bill, and it does not edit a fixed mortgage you already signed.'),
    mc('What is the Federal Reserve?',
       ['The central bank that targets short-term rates', 'Your employer', 'The company that insures bank deposits'], 0,
       'The central bank. Deposit insurance is a different agency. Your employer is neither.'),
    tf('The Fed’s target rate is the same number as the APY on your savings account.', False,
       'The target is what banks charge each other overnight. Your APY is related, and it is set by your bank.'),
    mc('Which rate is the Fed actually targeting?',
       ['The federal funds rate', 'The price of a movie ticket', 'Your credit card balance'], 0,
       'The overnight rate between banks. The rest of the rates tend to react.'),
    fill('The central bank of the United States is the Federal ___.',
         ['Reserve', 'fund', 'coupon'], 0,
         'Federal Reserve. Often just called the Fed.'),
])

funds = lesson('fd-rate', 'The Federal Funds Rate', 'Banks, overnight, then everyone else.', [
    info('One night, between banks',
         'The [[federal funds rate]] is an overnight loan between banks. You will never pay it directly. You feel it because a bank that pays more to borrow tends to charge more on a new loan, and to offer more on savings when it wants deposits. This lesson does not grade today’s target. It moves.'),
    tf('You pay the federal funds rate on your mortgage.', False,
       'Your mortgage has its own rate. The funds rate is between banks. A new mortgage offer can move when the target moves.'),
    mc('Why does a saver care about a rate that banks charge each other?',
       ['Because savings offers tend to move the same direction', 'Because the Fed deposits your paycheck', 'Because the rate is your dividend'], 0,
       'Same direction, not the same number. When the target rises, savings offers often rise too.'),
    mc('What will this course not ask you to memorize?',
       ['The direction of the ripple', 'Today’s exact target', 'That a fixed loan you already have stays fixed'], 1,
       'The exact target changes. The lesson is the ripple, and what does not move.'),
    fill('The overnight rate between banks is the federal ___ rate.',
         ['funds', 'ticket', 'cap'], 0,
         'Funds rate. Your own loan is a different contract.'),
])

ripple = lesson('fd-ripple', 'Where a Rate Move Lands', 'Some prices rise. An old contract does not.', [
    info('Three different objects',
         'When the [[Federal Reserve]] raises its target, new loans and savings offers tend to pay or cost more. The price of an existing [[bond]] tends to fall, so its yield can compete. A fixed mortgage you already locked does not get a new payment.'),
    sort('When the Fed raises its target, what usually happens?',
         ['Tends to rise', 'Tends to fall', 'Stays as signed'],
         [('The APY a bank offers on new savings', 0),
          ('The rate on a brand-new mortgage', 0),
          ('The price of a bond you already hold', 1),
          ('The payment on a fixed mortgage you already locked', 2)],
         'New offers move up. An old bond’s price tends to fall. A signed fixed payment stays signed.'),
    tf('Your locked fixed mortgage payment rises automatically when the Fed raises rates.', False,
       'Fixed means the payment you signed. A new buyer’s offer can be higher. Yours does not rewrite itself.'),
    mc('Why can an existing bond’s price fall when rates rise?',
       ['Because the coupon has to compete with new, higher rates', 'Because the Fed buys your bond at a discount by law', 'Because dividends replace coupons'], 0,
       'Buyers will not pay the old price for an old coupon when new bonds pay more. The price does the adjusting.'),
    num('A new one-year CD example moves from 3% to 4% on $10,000. How many more dollars of interest is that for the year?', 100,
        '4% is $400. 3% is $300. The difference is $100. This is an example rate, not a live offer.'),
], fmt='sort')

markets = lesson('fd-markets', 'Rates, Stocks, and Bonds', 'Bonds have a mechanical link. Stocks do not owe you one.', [
    info('Two reactions',
         '[[Bond]] prices and rates move like a seesaw: rates up, existing bond prices down. [[Stock]]s have no such lever. Higher rates can pressure stock prices, because borrowing costs more and future profits are discounted harder. They do not have to. A rate day is not a forecast.'),
    tf('Existing bond prices generally rise when interest rates rise.', False,
       'They generally fall. The old coupon has to compete, and the price is how it competes.'),
    mc('What is the honest line about stocks and a rate hike?',
       ['Stocks are required to fall by the size of the hike', 'Stocks can fall, and they are not required to', 'Stocks turn into bonds'], 1,
       'Pressure is not a law. The bond seesaw is the reliable relationship. Stocks are the maybe.'),
    num('You hold a bond with a $40 coupon. Buyers will now pay $800. What yield, in percent, does that price offer them?', 5, unit='%',
        explain='$40 ÷ $800 = 0.05, which is 5%. The price fell so the yield could rise.'),
    mc('Which relationship is the one you can count on directionally?',
       ['Rate up, existing bond price down', 'Rate up, every stock down by the same percent', 'Rate up, your fixed mortgage payment up'], 0,
       'The bond seesaw. The stock market and your signed mortgage are different stories.'),
])

fixed = lesson('fd-fixed', 'The Rate You Already Signed', 'A lock is a lock.', [
    info('The contract does not watch the news',
         'A fixed mortgage payment is the one in the note you signed. A later move by the [[Federal Reserve]] changes offers for new borrowers. It does not send you a new bill. An adjustable loan is the kind that can reset. This lesson is about the fixed one.'),
    num('Your fixed payment is $1,400 a month. The Fed raises rates and new buyers are offered more. What is your payment next month, in dollars?', 1400,
        'Still $1,400. The news changed the offer for the next person, not the note you signed.'),
    tf('Refinancing is automatic when rates fall.', False,
       'A refinance is a new loan you choose. The old payment stays until you replace it, and a new loan has its own costs.'),
    mc('Who feels a Fed hike first on a mortgage?',
       ['Someone shopping for a new loan', 'Someone who already locked a fixed payment', 'Someone holding only cash in a drawer'], 0,
       'The shopper sees a new offer. The locked payment stays. Cash in a drawer has no mortgage at all.'),
    fill('A mortgage whose payment does not change with the news is called ___.',
         ['fixed', 'a dividend', 'a ticker'], 0,
         'Fixed. Adjustable is the other kind, and it can reset.'),
])

after = doc('statement', 'Savings after the example cut',
            [('bal', 'Balance', 10000), ('now', 'Interest this year at 3%', 300)],
            subtitle='The old example rate was 4%, which paid $400',
            note='Both rates are examples so the dollar gap is easy to see.')

cut = lesson('fd-cut', 'A Cut, in Dollars', 'The balance stayed. The interest did not.', [
    info('Four percent to three',
         'In this example a savings account held $10,000. At 4% it paid $400 a year. After a rate cut the example APY is 3%, so it pays $300. The balance did not shrink. The yield did. A borrower shopping for a new loan may like the same news.'),
    num('How many dollars of interest does the page show for the year?', 300,
        doc=after,
        explain='$10,000 × 0.03 = $300.'),
    num('The old example rate paid $400. How many dollars a year did this cut remove?', 100,
        '$400 − $300 = $100. Same $10,000. Smaller yield.'),
    tf('The $100 gap means the bank took $100 of principal.', False,
       'Principal is still $10,000. You earned $100 less interest than in the old example.'),
    mc('Who might welcome the same cut?',
       ['A person about to borrow, if the new loan is cheaper', 'A person who wanted the old 4% forever', 'Nobody, because cuts are illegal'], 0,
       'Savers earn less in the example. New borrowers may pay less. It is the same news, two seats.'),
], fmt='document')

today = doc('statement', 'Lock today’s example rate',
            [('ratepay', 'Payment at the 6% example', 1800)],
            subtitle='The house is available now')
wait = doc('statement', 'Wait for a lower rate',
           [('hope', 'A hoped-for payment you cannot lock', 1650)],
           subtitle='The house may not wait with you',
           note='Both payments are examples. The second one is not an offer.')

lock = lesson('fd-lock', 'Lock or Wait', 'A rate you can sign, or a wish.', [
    info('The house is a date',
         'You can lock an example 6% mortgage with a $1,800 payment, or you can wait and hope for something like $1,650. The hope is not a contract. The house can sell to someone else while you wait. This is not a forecast of real rates.'),
    mc('Which page is a rate you can actually sign today?',
       [today['title'], wait['title']], 0,
       docs=(today, wait),
       explain='The lock is an offer. The lower payment is a hope, and the house is not required to stay on the market.'),
    num('How many dollars a month is the payment you can lock in this example?', 1800,
        doc=today,
        explain='The signable page is $1,800. The $1,650 is not an offer.'),
    num('How many dollars a month would you save if the hope became real?', 150,
        '$1,800 − $1,650 = $150. That saving is real only if you both get the rate and still get a house.'),
    tf('Waiting is free, because a lower rate is guaranteed if you are patient.', False,
       'A lower rate is not guaranteed, and the house can disappear. The cost of waiting is the chance you lose the house.'),
], fmt='call')

nina = lesson('fd-nina', 'Nina Reads the Cut', 'The news is one number. Her loan is another.', [
    info('Meet Nina, on a rate day',
         'Nina is 28 and a warehouse supervisor, the same Nina who owns a few shares for the lesson, not as a tip. The news says the Fed cut its target. Her savings example falls from 4% to 3% on $10,000, so the year pays $300 instead of $400.\n\nHer fixed car note stays $320 a month. The cut did not rewrite it. A neighbor shopping for a car today might be offered less.',
         ),
    num('How many dollars of yearly savings interest did Nina lose in the example?', 100,
        '$400 − $300 = $100. The $10,000 is still there.'),
    num('What is Nina’s car payment next month, in dollars?', 320,
        'Still $320. A fixed note does not follow the headline.'),
    tf('Nina should refinance the car automatically because the Fed cut rates.', False,
       'A refinance is a new loan with its own costs. The headline is not a new contract.'),
    mc('Who on this street might see a cheaper new loan?',
       ['Nina’s already-signed car note', 'A neighbor who has not borrowed yet', 'The shares, which are now a bond'], 1,
       'New borrowers see new offers. Signed fixed payments stay. Shares are still shares.'),
], fmt='story', story={
    'title': 'The cut, two seats',
    'character': 'Nina, 28, warehouse supervisor',
    'body': 'The Fed cuts its target. Nina’s example savings rate on **$10,000** falls from **4%** to **3%**, so the year pays **$300** instead of **$400**.\n\nHer fixed car note stays **$320** a month. A neighbor who has not borrowed yet might see a cheaper offer.',
})

write_unit('02-the-fed.json', 'the-fed', 2, 'Interest Rates & the Fed',
           'The short-term target, the ripple, and the contract that does not move.',
           'New offers move. A signed fixed payment stays signed.',
           terms, [fed, funds, ripple, markets, fixed, cut, lock, nina, review('fd'), trial('fd', 'Interest Rates & the Fed', [
               tf('The federal funds rate is the payment on a mortgage you already locked.', False,
                  'It is the overnight rate between banks. A signed fixed payment does not follow it.'),
               num('An example savings rate falls from 5% to 4% on $20,000. How many dollars of yearly interest did you lose?', 200,
                   '5% is $1,000. 4% is $800. The gap is $200.'),
               mc('When the Fed raises rates, the price of an existing bond generally does what?',
                  ['Rises', 'Falls', 'Becomes a stock'], 1,
                  'The old coupon has to compete. The price falls so the yield can rise.'),
               mc('A lower rate you hope for, but cannot lock, is what?',
                  ['A contract', 'A hope, and the purchase might not wait', 'A federal funds payment you already owe'], 1,
                  'Until it is an offer you can sign, it is a hope. The thing you want to buy can sell to someone else.'),
           ])],
           section=S)
