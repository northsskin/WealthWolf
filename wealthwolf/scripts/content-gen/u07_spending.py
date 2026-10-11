from lib import *

terms = {
    'unit-price': term('Unit price', 'The price for one unit (an ounce, a pound, a roll), so you can compare packs of different sizes.',
                       'A 24 oz jar for $4.80 is $0.20 an ounce.'),
    'cost-per-use': term('Cost per use', 'The price divided by how many times you’ll use something.',
                         '$120 boots worn 300 times cost $0.40 a wear.'),
    'anchor-price': term('Anchor price', 'A big “was” price shown next to a sale price, so the sale price feels like a steal.',
                         '“Was $200, now $99!” The $200 is the anchor.'),
    'impulse-buy': term('Impulse buy', 'Something you buy on the spot, unplanned, because it grabbed you in the moment.',
                        'Candy at the checkout that wasn’t on your list.'),
    'opportunity-cost': term('Opportunity cost', 'What you give up when you choose one thing over another.',
                             'Spend $60 on a game, and that $60 can’t go into savings.'),
    'refurbished': term('Refurbished', 'Returned or used, then checked and repaired by the seller, and sold again for less, often with a warranty.',
                        'A refurbished laptop for $780 instead of $1,100 new.'),
}

SMALL = doc('receipt', 'Small pack', [('rolls', 'Paper towels, 12 rolls', 9.00)], subtitle='Shelf price')
BIG = doc('receipt', 'Big pack', [('rolls', 'Paper towels, 30 rolls', 19.50)], subtitle='Shelf price')
assert 9 / 12 == 0.75 and 19.5 / 30 == 0.65
unit_price = lesson('ss-unit-price', 'Unit Prices', 'Compare packs of different sizes the right way.', [
    mc('A 10 oz bag of rice costs $2.00. What’s the unit price?', ['$0.20 an ounce', '$2.00 an ounce', '$10 an ounce'], 0,
       '$2.00 ÷ 10 = $0.20 an ounce.',
       context='The [[unit price]] is the price for one unit (an ounce, a pound, a roll), so you can compare packs of different sizes.'),
    num('A 24 oz jar of peanut butter costs $4.80. What’s the price per ounce?', 0.20, '$4.80 ÷ 24 = $0.20 an ounce.'),
    mc('Which pack is cheaper per roll?', ['The 30-roll pack', 'The 12-roll pack'], 0,
       '12 rolls: $9.00 ÷ 12 = $0.75 a roll. 30 rolls: $19.50 ÷ 30 = $0.65 a roll.', docs=[SMALL, BIG]),
    num('What’s the big pack’s price per roll?', 0.65, '$19.50 ÷ 30 = $0.65.', docs=[SMALL, BIG]),
    tf('The bigger pack is always the better deal.', False,
       'Usually, not always. Check the unit price, and only buy big if you’ll use it before it goes bad.'),
    mc('When is the bigger pack a bad deal even though it’s cheaper per unit?',
       ['When half of it goes bad before you use it', 'When it’s on the bottom shelf', 'Never'], 0,
       'Food you throw away has a unit price of “all of it.”'),
], fmt='call')

cost_use = lesson('ss-cost-per-use', 'Cost per Use', 'Why the pricier thing is sometimes the cheaper one.', [
    mc('What does cost per use tell you?', ['How much each use really costs', 'The sale price', 'The tax on an item'], 0,
       'It spreads the price over every time you use the thing.',
       context='[[Cost per use]] is the price divided by how many times you’ll use something. A cheap thing used once can cost more per use than a pricey thing used every day.'),
    num('Boots cost $120 and you’ll wear them about 300 times. What’s the cost per wear?', 0.40, '$120 ÷ 300 = $0.40.'),
    num('Cheaper boots cost $45 but fall apart after about 50 wears. Cost per wear?', 0.90, '$45 ÷ 50 = $0.90.'),
    mc('Which boots are the better buy?', ['The $120 pair', 'The $45 pair'], 0, '$0.40 a wear beats $0.90 a wear.'),
    num('A $60 outfit you’ll wear twice. Cost per wear?', 30, '$60 ÷ 2 = $30 a wear.'),
    num('A gym membership is $50 a month and you go 4 times a month. Cost per visit?', 12.50, '$50 ÷ 4 = $12.50 a visit.'),
    tf('Cost per use only works for clothes.', False, 'Phones, tools, memberships: anything you use again and again.'),
])

sales = lesson('ss-sale-tricks', 'Sale Tricks', 'How stores make spending feel like saving.', [
    mc('“Was $200, now $99!” What does the $200 do?',
       ['Makes $99 feel cheap, whether or not it is', 'Proves it’s worth $200', 'Shows the store is losing money'], 0,
       'The “was” price may never have been what anyone actually paid.',
       context='An [[anchor price]] is the big “was” price stores show so the sale price feels like a steal.'),
    tf('If something is 50% off, buying it saves you money.', False, 'You only save if you’d have bought it anyway. Otherwise you spent 50%.'),
    num('Buy one, get one 50% off. Each shirt is $30. What do two cost?', 45, '$30 + $15 = $45.'),
    mc('You need one shirt. Is buy-one-get-one-50%-off a deal?', ['Only if you’d really wear a second shirt', 'Always, it’s a sale', 'Never'], 0,
       'One shirt costs $30. Two cost $45. Only worth it if you wanted two.'),
    num('Your cart is $41 and shipping is $6. To get free shipping over $50, you add a $14 item you don’t need. How much more did you spend than if you’d paid shipping?', 8,
        '$14 − $6 = $8 more, for something you didn’t want.',
        context='“Free shipping over $50” is designed to get you to add things.'),
    sort('Real deal or trick?', ['Could be a real deal', 'Usually a trick'],
         [('Lower unit price on something you use every week', 0), ('“Only 2 left!” countdown banner', 1),
          ('Adding items to reach free shipping', 1), ('Sale on a winter coat you already planned to buy', 0),
          ('“Was $300” on something that never sold for $300', 1), ('Coupon for your usual groceries', 0)]),
], fmt='sort')

impulse = lesson('ss-impulse', 'Impulse Buys', 'Wait a day. Most wants wear off.', [
    mc('Which is an impulse buy?', ['Candy at the checkout that wasn’t on your list', 'This week’s planned groceries', 'Your monthly bus pass'], 0,
       'Unplanned, grabbed in the moment: that’s an impulse buy.',
       context='An [[impulse buy]] is something you buy on the spot, unplanned, because it grabbed you in the moment.'),
    mc('You see $80 sneakers you love. What does the 24-hour rule say?', ['Wait a day, then decide', 'Buy now before they’re gone', 'Never buy sneakers'], 0,
       'If you still want them tomorrow, they might be worth it.',
       context='The 24-hour rule: if it isn’t a need and wasn’t planned, wait a day. If you still want it tomorrow, it might be worth it.'),
    num('You make about 6 impulse buys a month at $15 each. What’s that in a year?', 1080, '6 × $15 × 12 = $1,080.'),
    tf('Saved card details and one-click checkout make impulse buys easier.', True, 'Every step removed is one less moment to think.'),
    mc('Which trick cuts impulse buys the most?', ['Removing saved cards and waiting a day', 'Shopping when you’re bored', 'Following more brands online'], 0,
       'A little friction gives your brain time to catch up.'),
    order('Something catches your eye online. Put the smart steps in order.',
          ['Add it to a wish list instead of the cart', 'Wait at least 24 hours', 'Check if it fits your budget', 'Buy it, or let it go'],
          'Park it, wait, check, decide.'),
])

groc_lines = [('milk', 'Milk, half gallon', 3.29), ('yogurt', 'Greek yogurt, 4-pack', 4.99), ('apples', 'Apples, 2 lb', 4.10),
              ('pasta', 'Pasta, 1 lb', 1.79), ('cheese', 'Cheddar cheese', 5.49)]
groc_total = total(l[2] for l in groc_lines)
GROC = doc('receipt', 'Fresh Market', groc_lines, subtitle='Store #214 · Tue 6:18 PM', totals=[('Total', groc_total, True)])
cafe_lines = [('latte', 'Large latte', 5.25), ('oat', 'Oat milk', 0.75), ('shot', 'Extra espresso shot', 0.95), ('muffin', 'Blueberry muffin', 3.10)]
CAFE = doc('receipt', 'Bean There Café', cafe_lines, subtitle='Order #88', totals=[('Total', total(l[2] for l in cafe_lines), True)])
receipt = lesson('ss-receipt-check', 'Check the Receipt', 'Scanners make mistakes. Catch them before you leave.', [
    spot('The shelf tag said the yogurt was $3.49. Tap the line that’s wrong.', GROC, 'yogurt',
         'It rang up at $4.99, not $3.49.', context='Prices on the shelf and prices at the register don’t always match.'),
    num('How much were you overcharged?', 1.50, '$4.99 − $3.49 = $1.50.', doc=GROC),
    spot('You ordered a large latte with oat milk and a muffin. Tap the charge you didn’t ask for.', CAFE, 'shot',
         'Nobody asked for the extra shot.'),
    tf('Stores sometimes scan the wrong price, so checking your receipt is worth the ten seconds.', True,
       'Especially on sale items, where the shelf and the register often disagree.'),
    mc('You spot a mistake after leaving the store. Best move?', ['Go back or call with the receipt', 'Let it go, it’s only $1.50', 'Post an angry review'], 0,
       'Most stores fix it on the spot, and some give you the item free.'),
    num('If you were overcharged $1.50 every week, what would that add up to over a year of 52 weeks?', 78, '$1.50 × 52 = $78.'),
], fmt='spot')

opp = lesson('ss-opportunity-cost', 'What Else Could It Buy?', 'Every yes is a no to something else.', [
    mc('You spend $60 on a new game. What’s the opportunity cost?',
       ['Whatever else that $60 could have done, like going into savings', 'Nothing, it was on sale', '$60 of taxes'], 0,
       'Not that the game was bad. Just that the $60 can’t do anything else now.',
       context='[[Opportunity cost]] is what you give up when you choose one thing over another.'),
    num('A $6 lunch out every workday, about 20 days a month. What’s that a month?', 120, '$6 × 20 = $120.'),
    num('And over a year?', 1440, '$120 × 12 = $1,440.'),
    num('Making lunch costs about $2. Over a year, how much more does buying lunch cost than making it?', 960,
        '($6 − $2) × 20 days × 12 months = $960.'),
    tf('Thinking about opportunity cost means never buying anything fun.', False,
       'It means choosing on purpose. Buy the fun thing, knowing what it cost.'),
    mc('Which question captures opportunity cost?', ['What else could this money do?', 'Is it on sale?', 'Do my friends have one?'], 0,
       'Ask it before any purchase that isn’t a need.'),
])

NEW = doc('bill', 'New laptop', [('price', 'Price', 1100.00), ('warranty', '1-year warranty', 0.00)], subtitle='TechWorld')
REFURB = doc('bill', 'Refurbished laptop', [('price', 'Price, same model', 780.00), ('warranty', '1-year warranty', 0.00)], subtitle='TechWorld Certified')
big = lesson('ss-big-purchase', 'Big Purchase, Smart Way', 'New vs. refurbished, add-ons and “only $70 a month.”', [
    mc('Same model, both with a 1-year warranty. Which is the better deal?', ['The refurbished one', 'The new one'], 0,
       'Same machine, same warranty, $320 less.', docs=[NEW, REFURB],
       context='A [[refurbished]] item was returned or used, then checked and repaired by the seller. It often comes with a warranty and costs much less.'),
    num('How much does the refurbished one save?', 320, '$1,100 − $780 = $320.', docs=[NEW, REFURB]),
    mc('The store offers a $150 “protection plan” on the $780 laptop. What should you check first?',
       ['What it covers that the free warranty doesn’t', 'Nothing, always buy it', 'Whether the cashier recommends it'], 0,
       'Many plans repeat what the warranty already covers.',
       context='Store protection plans often cost a lot for problems that rarely happen.'),
    num('“Only $70 a month for 12 months!” What’s the total?', 840, '$70 × 12 = $840.',
        context='Monthly payments can hide extra cost. Always add it all up.'),
    num('Compared with paying $780 upfront, how much extra is that?', 60, '$840 − $780 = $60.'),
    order('Before a big purchase, put these steps in order.',
          ['Decide what you need it to do', 'Compare prices, including refurbished', 'Check the total cost, not the monthly price', 'Wait a day, then buy'],
          'Need, compare, total, wait.'),
], fmt='call')

taylor_story = {
    'title': 'The $40 errand',
    'character': 'Taylor, 23, warehouse shift lead',
    'body': 'Taylor went to the store for one thing: a **$40** pair of work gloves.\n\n'
            'Near the entrance, a speaker was marked “Was $120, now **$69**!” Taylor grabbed it. At checkout there was a buy-one-get-one-50%-off deal '
            'on **$12** phone chargers, so Taylor took two. A **$3** pack of gum went in at the register.\n\n'
            'Taylor already owned a speaker and one working charger.',
}
taylor = lesson('ss-taylor', 'Taylor’s Shopping Trip', 'One errand, four purchases. Work out what happened.', [
    num('How much did the two chargers cost?', 18, '$12 + $6 = $18.'),
    num('What was Taylor’s total bill?', 130, '$40 + $69 + $18 + $3 = $130.'),
    num('Taylor planned to spend $40. How far over plan was the trip?', 90, '$130 − $40 = $90.'),
    sort('Planned or impulse?', ['Planned', 'Impulse'], [('Work gloves', 0), ('Speaker', 1), ('Two chargers', 1), ('Gum', 1)]),
    mc('What made the speaker feel like a deal?', ['The “Was $120” anchor price', 'Taylor needed a speaker', 'The store was out of gloves'], 0,
       'The anchor did the selling.'),
    mc('Taylor can return the speaker within 30 days. Smart move?', ['Return it: Taylor already has one', 'Keep it, returning is awkward', 'Buy a second one while it’s cheap'], 0,
       'A $69 refund turns a $90 overspend into $21.'),
], fmt='story', story=taylor_story)

trial_steps = [
    num('16 oz costs $3.20. 40 oz costs $7.20. What’s the 40 oz price per ounce?', 0.18, '$7.20 ÷ 40 = $0.18 an ounce, cheaper than $0.20.'),
    mc('“Was $90, now $45.” What’s the $90?', ['An anchor price', 'A unit price', 'A tax'], 0, 'It’s there to make $45 feel small.'),
    tf('Cost per use can make a pricier item the cheaper choice.', True, 'If it lasts much longer, yes.'),
    num('$9 a day on snacks for 20 workdays. What’s that a month?', 180, '$9 × 20 = $180.'),
]

lessons = [unit_price, cost_use, sales, impulse, receipt, opp, big, taylor,
           review('ss'), trial('ss', 'Smart Spending', trial_steps)]
write_unit('07-smart-spending.json', 'smart-spending', 7, 'Smart Spending',
           'Get more for every dollar: unit prices, sale tricks, impulse buys.',
           'A sale is only a deal if you were going to buy it anyway.', terms, lessons)
