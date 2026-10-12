from lib import *

S = 'investing'
terms = {
    'coupon': term('Coupon',
                   'The interest a bond pays you. A $40 coupon is $40 a year, usually split into smaller payments.',
                   'A $1,000 bond with a $40 coupon pays $40 a year.'),
    'maturity': term('Maturity',
                     'The date a bond ends. If the issuer pays, you get the face value back then.',
                     'A bond that matures in 10 years pays the $1,000 face value in year 10.'),
    'yield': term('Yield',
                  'What a bond pays you compared with the price you paid, as a percent. Coupon divided by price.',
                  'A $40 coupon on a bond you buy for $800 is a 5% yield.'),
}

bond_doc = doc('statement', 'A Treasury bond',
               [('face', 'Face value', 1000), ('coupon', 'Coupon each year', 40)],
               meta=[('Matures in', '10 years')],
               subtitle='You are the lender',
               note='If you hold to maturity and the issuer pays, the face value comes back. The coupon is the interest along the way.')

how = lesson('bd-how', 'How a Bond Works', 'You lend. They pay interest. Then they pay you back.', [
    info('The loan, written down',
         'A [[bond]] has a face value, a [[coupon]], and a [[maturity]]. The coupon is the interest. Maturity is the end date. This page is a simple Treasury: you lend $1,000, it pays $40 a year, and it ends in 10 years.'),
    num('How many dollars is the coupon each year?', 40,
        doc=bond_doc,
        explain='The coupon is $40 a year on the $1,000 face value.'),
    num('If you buy this bond for the $1,000 face value, what is the yield in percent?', 4, unit='%',
        doc=bond_doc,
        explain='$40 ÷ $1,000 = 0.04, which is 4%.'),
    tf('If you hold this bond to maturity and the issuer pays, you get the $1,000 face value back.', True,
       'The coupons were the interest. Maturity returns the face value. Selling early is a different price.'),
    mc('Who is the lender on this page?',
       ['The government is lending to you', 'You are lending to the government', 'The bond is a share of a company'], 1,
       'A bond is a loan you make. A stock would be ownership.'),
], fmt='document')

who = lesson('bd-who', 'Treasuries and Corporate Bonds', 'Same shape of loan, different borrower.', [
    info('Who borrowed',
         'A Treasury is a [[bond]] from the US government. A corporate bond is a loan to a company. The company can fail to pay. The higher [[coupon]] on a corporate bond is pay for that extra chance. Neither one is a stock.'),
    mc('Which borrower can more realistically fail to pay you back?',
       ['The US government, on a Treasury', 'A company, on a corporate bond', 'Neither can ever fail'], 1,
       'A company can run out of money. That extra chance is why corporate bonds usually offer more interest.'),
    tf('A Treasury bond’s price can fall before maturity.', True,
       'You can sell early for less than face value. Holding to maturity is what brings the face value back, if the issuer pays.'),
    mc('Why might a corporate bond pay a higher coupon than a Treasury?',
       ['Because the company is the government', 'Because lenders want pay for the chance the company cannot pay', 'Because coupons are dividends'], 1,
       'More chance of a missed payment, more interest. It is not free extra money.'),
    fill('A bond from the US government is called a ___.',
         ['Treasury', 'dividend', 'ticker'], 0,
         'Treasury. A corporate bond is the loan to a company.'),
])

rates = lesson('bd-rates', 'When Rates Rise', 'Old bonds get cheaper so they can compete.', [
    info('The seesaw',
         'You hold a bond with a $40 [[coupon]]. New bonds start paying more, because rates rose. Nobody wants your $40 if they can get more on a new bond, unless your bond’s price falls. A lower price raises the [[yield]] for the buyer.'),
    num('Your $40 coupon bond falls to a price of $800. What is the buyer’s yield, in percent?', 5, unit='%',
        explain='$40 ÷ $800 = 0.05, which is 5%.'),
    num('The face value is $1,000 and the price is $800. How many dollars below face is that price?', 200,
        '$1,000 − $800 = $200. That gap is the price risk if you sell now.'),
    tf('When interest rates rise, the price of an existing bond generally falls.', True,
       'The old coupon has to compete. The price does the competing.'),
    mc('You do not need the money until maturity, and the issuer is paying. What does the $800 price mean for you?',
       ['You already lost the $200 for good', 'It is the price if you sell today. Maturity can still pay the $1,000 face value', 'The coupon stops'], 1,
       'The coupon is still $40. The $800 matters if you sell. Maturity, if the issuer pays, is the face value.'),
])

cds = lesson('bd-cd', 'CDs and I Bonds', 'Two ways to lock money, with rules.', [
    info('Read the lock',
         'A CD is a bank deposit for a set term. CDs at a bank are FDIC insured, generally up to $250,000 per depositor, per bank, per ownership category. Cashing out early usually costs a penalty.\n\nAn I bond is a US savings bond. The rate mixes a fixed part with inflation and changes in May and November, so this course will not grade today’s rate. Electronic I bonds are capped at $10,000 per person per calendar year. You cannot cash one in the first 12 months. Cash out before 5 years and you lose the last 3 months of interest.'),
    num('What is the electronic I bond purchase cap, in dollars, for one person in one calendar year?', 10000,
        'TreasuryDirect caps electronic I bonds at $10,000 per person per calendar year. The rate itself changes twice a year.'),
    tf('You can cash a brand-new I bond after one month.', False,
       'The first 12 months are locked. Before 5 years, leaving also costs the last 3 months of interest.'),
    mc('You cash an I bond in year 3. What do the rules take?',
       ['The last 3 months of interest', 'Half the bond, always', 'Nothing, because 12 months have passed'], 0,
       'Past 12 months you can cash out. Before 5 years you forfeit the last 3 months of interest.'),
    tf('A CD and an I bond are the same product.', False,
       'A CD is a bank deposit. An I bond is a savings bond from the US Treasury, with its own cap and lockup.'),
])

bond_yield = lesson('bd-yield', 'Yield', 'The coupon only tells the story at the price you paid.', [
    info('Price changes the percent',
         '[[Yield]] is the [[coupon]] divided by the price you pay. A $30 coupon on a $1,000 price is 3%. The same $30 on a lower price is a higher yield. This is the current yield, a beginner version.'),
    num('A bond pays a $30 coupon and you buy it for $1,000. What is the yield, in percent?', 3, unit='%',
        explain='$30 ÷ $1,000 = 0.03, which is 3%.'),
    num('The same $30 coupon is on a bond priced at $600. What is the yield, in percent?', 5, unit='%',
        explain='$30 ÷ $600 = 0.05, which is 5%.'),
    mc('The coupon stays $30 and the price falls. What happens to the yield?',
       ['It falls', 'It rises', 'It cannot change'], 1,
       'Yield is coupon ÷ price. A smaller price makes a bigger percent.'),
    tf('Yield and coupon are always the same number.', False,
       'They match when you pay face value. Pay a different price and the yield moves.'),
])

role = lesson('bd-role', 'Bonds in a Portfolio', 'The steadier slice, not a zero-risk slice.', [
    info('Why they sit next to stocks',
         '[[Stock]]s usually swing more. [[Bond]]s often swing less, and they often move differently. That is why a [[portfolio]] uses both. Bonds can still lose money if you sell when rates have risen, or if a company cannot pay.'),
    mc('What job do bonds usually have next to stocks?',
       ['To guarantee the stocks rise', 'To be a steadier slice that often moves differently', 'To replace the emergency fund'], 1,
       'Steadier, not frozen. The emergency fund is still cash.'),
    tf('A bond fund cannot lose money in a year when rates rise.', False,
       'Rising rates push existing bond prices down. A fund that holds those bonds can fall.'),
    mc('You need the money in one year. A 10-year bond is a weak fit because…',
       ['The coupon is illegal', 'You might have to sell before maturity, at a lower price', 'Bonds are stocks'], 1,
       'A short timeline wants cash. A long bond’s price can be down in the exact year you sell.'),
    num('A portfolio is $8,000 in stocks and $2,000 in bonds. How many dollars are in the bond slice?', 2000,
        'The bond slice is the $2,000. The mix itself is the next unit’s subject.'),
])

cd_page = doc('statement', 'One-year CD at a bank',
              [('dep', 'You deposit', 1000), ('pay', 'Interest at 4%', 40)],
              subtitle='FDIC insured, generally up to $250,000 at that bank',
              note='Leaving early usually costs a penalty.')
tsy_page = doc('statement', 'One-year Treasury',
               [('face', 'You lend', 1000), ('pay', 'Coupon at 4%', 40)],
               subtitle='A loan to the US government',
               note='Hold it the year and, if the issuer pays, the $1,000 comes back.')

compare = lesson('bd-compare', 'A CD or a Treasury', 'Same dollars in this example. Different borrower.', [
    info('Line them up',
         'Both pages pay $40 on $1,000, so 4%. The CD is a bank deposit. The Treasury is a loan to the US government. The example uses the same rate on purpose, so the choice is about the borrower and the rules, not about chasing a higher number.'),
    mc('Which page is a loan to the US government?',
         [cd_page['title'], tsy_page['title']], 1,
         docs=(cd_page, tsy_page),
         explain='The Treasury is the government loan. The CD is the bank deposit, with FDIC insurance up to the usual limit.'),
    num('How many dollars of interest does each page pay in this example?', 40,
        'Both are $1,000 × 0.04 = $40. The rate match is the point of the comparison.'),
    mc('You might need the cash in three months. Which fits better than either locked page?',
       ['The one-year CD', 'The one-year Treasury', 'A savings account you can take money from'], 2,
       'Both locked pages want the year. Three months wants the savings account.'),
    tf('Because both pay $40, they are the same product.', False,
       'The dollars match. The borrower, the insurance, and the early-exit rules do not.'),
], fmt='call')

helen = lesson('bd-helen', 'Helen Holds', 'The price on the screen is not the maturity check.', [
    info('Meet Helen',
         'Helen is 36 and a school librarian. She owns the $1,000 Treasury from this unit: a $40 coupon, maturity in 10 years. She does not need the money until then.\n\nRates rise. The price she would get if she sold today falls to $800. The coupon is still $40.'),
    num('If Helen sells today at $800, how many dollars does she get?', 800,
        'The sale price is $800. That is $200 below the $1,000 face value.'),
    num('If she holds and the issuer pays at maturity, how many dollars of face value come back?', 1000,
        'Maturity pays the $1,000 face value. The $800 was the “sell today” price, not the end.'),
    tf('Helen’s coupon changed to $32 because the price fell.', False,
       'The coupon stays $40. The price fell so a new buyer’s yield can compete.'),
    mc('What is Helen’s fitting move if she still does not need the money?',
       ['Sell because the screen says $800', 'Hold to maturity, since that was the plan', 'Borrow to buy more of the same bond'], 1,
       'The plan was 10 years. The screen price is for someone who sells today.'),
], fmt='story', story={
    'title': 'The screen says $800',
    'character': 'Helen, 36, school librarian',
    'body': 'Helen owns a **$1,000** Treasury with a **$40** coupon. It matures in **10 years**, and she does not need the money until then.\n\nRates rise. If she sold today she would get **$800**. The coupon is still $40.',
})

write_unit('03-bonds.json', 'bonds', 3, 'Bonds & Interest Rates',
           'Coupons, prices, and why a bond is a loan with a date on it.',
           'The price moves. The maturity date is the plan.',
           terms, [how, who, rates, cds, bond_yield, role, compare, helen, review('bd'), trial('bd', 'Bonds & Interest Rates', [
               num('A bond pays a $50 coupon and you buy it for $1,000. What is the yield, in percent?', 5, unit='%',
                   explain='$50 ÷ $1,000 = 0.05, which is 5%.'),
               tf('You can redeem a new I bond in the first 12 months.', False,
                  'The first year is locked. Before five years, cashing out also costs the last three months of interest.'),
               mc('Rates rise and you sell a bond before maturity. What is the usual price effect?',
                  ['The price rises', 'The price falls', 'The price is frozen at face value'], 1,
                  'Existing bonds get cheaper so their yield can compete with new, higher rates.'),
               num('What is the electronic I bond cap, in dollars, for one person in a calendar year?', 10000,
                   'The cap is $10,000. This trial asks the cap, not today’s changing rate.'),
           ])],
           section=S)
