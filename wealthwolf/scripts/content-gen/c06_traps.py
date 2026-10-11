from lib import *

S = 'credit-debt'
terms = {
    'cash-back': term('Cash back', 'A card reward that returns a percentage of what you spend, as money.',
                      '2% cash back on $1,000 of spending is $20.'),
    'intro-apr': term('Intro APR', 'A temporary low rate, often 0%, that lasts for a set number of months and then jumps to the regular APR.',
                      '0% for 12 months, then 24%. The debt still left in month 13 is charged 24%.'),
    'balance-transfer': term('Balance transfer', 'Moving debt from one card to another, usually to a lower rate. The new card often charges a fee of a few percent.',
                             'Transfer $2,000 with a 3% fee and you owe $2,060 on the new card.'),
}

cashback = lesson('ct-cashback', 'Cash-Back Math', 'A percent of what you spend. It never covers interest you did not have to pay.', [
    num('A card pays 2% cash back. You spend $2,500. How much do you get back?', 50, '$2,500 × 0.02 = $50.',
        context='[[Cash back]] returns a slice of your spending. 2% of $100 is $2. It is real money only if you were going to spend that $100 anyway.'),
    num('You spend $800 at 1.5% cash back. How much is the reward?', 12, '$800 × 0.015 = $12.'),
    num('The same month you pay $40 of interest. What is the reward minus the interest?', -28,
        '$12 − $40 = −$28. The “reward” month cost you $28.'),
    mc('When is cash back actually a gain?',
       ['When you pay the statement in full, so you are not buying the reward with interest', 'When you carry a balance', 'When you spend more just to earn it'], 0,
       'Interest eats rewards fast.'),
    tf('Earning 2% back means the purchase was 2% cheaper, even if you pay interest on it.', False,
       'Interest can cost more than the reward.'),
    mc('You do not need the item. It offers 5% back. What do you do?',
       ['Skip it. A reward on a wasted purchase is still wasted money', 'Buy it for the 5%', 'Buy two'], 0,
       'Five percent back on $100 you did not need is $5, and you are out $95.'),
])

points = lesson('ct-points', 'Points or Cash', 'Turn the points into cents before you call them generous.', [
    mc('A program says 1 point per dollar, and 100 points equal $1. What is a point worth?',
       ['1 cent', '1 dollar', '$100'], 0, '100 points = $1, so 1 point = 1 cent.',
       context='Points are just cash back in costume. Divide the reward by the points to get a value in cents. If 100 points equal $1, each point is worth one cent, which is 1% back.'),
    num('You earn 2,000 points at 1 cent each. What are they worth in dollars?', 20, '2,000 × $0.01 = $20.'),
    num('A 2% cash-back card on the same $2,000 of spending pays how much?', 40, '$2,000 × 0.02 = $40.'),
    num('How much more does the 2% card pay than those 2,000 points?', 20, '$40 − $20 = $20.'),
    mc('A bonus category pays 3 points per dollar, still at 1 cent a point, at grocery stores. What is that in percent?',
       ['3%', '30%', '0.3%'], 0, '3 cents per dollar is 3%.'),
    tf('A point is always worth more than a cent of cash back.', False,
       'Check the redemption. Some points are worth less than a cent.'),
])

costmore = lesson('ct-rewards-cost', 'Rewards That Cost More', 'If you spend extra to chase the bonus, you lost.', [
    num('A jacket is $100. You do not need it, but the card pays 5% back. How much is the reward?', 5, '$100 × 0.05 = $5.',
        context='A reward you would not have earned on a purchase you would not have made is not a discount. It is a reason someone hoped you would spend.'),
    num('After the $5 reward, how much did the unneeded jacket really cost you?', 95, '$100 − $5 = $95.'),
    mc('You carry the $100 for a year at 24% APR. Rough interest?', ['$24', '$5', '$0'], 0, '$100 × 0.24 = $24, against a $5 reward.'),
    num('Interest $24, reward $5. How much are you behind?', 19, '$24 − $5 = $19 behind, plus you own a jacket you did not need.'),
    tf('A sign that says “5% back” means you should buy something.', False, 'It means the price is 5% less only if you were buying it anyway, and only if you pay in full.'),
    mc('Which spending earns a reward that is really yours?',
       ['The grocery run you were making anyway, paid in full', 'A gadget you bought for the points', 'A balance you are paying interest on'], 0,
       'Planned spending, no interest.'),
])

fee_a = [
    ('fee', 'Annual fee', 0),
    ('back', 'Cash back on $4,000 of spending at 1%', 40),
]
fee_b = [
    ('fee', 'Annual fee', 80),
    ('back', 'Cash back on $4,000 of spending at 3%', 120),
]
assert 120 - 80 == 40 and 40 - 40 == 0
FEE_A = doc('statement', 'Simple Card', fee_a, subtitle='1% cash back · no fee', totals=[('Reward after the fee', 40, True)])
FEE_B = doc('statement', 'Bonus Card', fee_b, subtitle='3% cash back · $80 fee', totals=[('Reward after the fee', 40, True)])
annual = lesson('ct-annual-fee', 'Is the Annual Fee Worth It?', 'The extra percent has to earn the fee before you are ahead.', [
    num('The bonus card pays 2 percentage points more (3% instead of 1%). The fee is $80. How much must you spend before that extra 2% covers the fee?',
        4000, '$80 ÷ 0.02 = $4,000.',
        context='Subtract the annual fee from the rewards. If you will not spend enough for the extra percent to cover the fee, the free card wins.'),
    num('On $4,000 of spending, what does the 1% card pay?', 40, '$4,000 × 0.01 = $40.', docs=[FEE_A, FEE_B]),
    num('On $4,000, what does the 3% card pay after its $80 fee?', 40, '$4,000 × 0.03 = $120. $120 − $80 = $40.', docs=[FEE_A, FEE_B]),
    num('You only spend $2,000. The 3% card pays $60 before the fee. What is left after the $80 fee?', -20,
        '$60 − $80 = −$20. You paid for the privilege.'),
    mc('You spend about $2,000 a year on the card and always pay in full. Which card?',
       ['The 1% card with no fee', 'The 3% card with the $80 fee', 'Whichever is metal'], 0,
       'At $2,000 the fee eats the bonus and more.'),
    tf('A higher cash-back rate is a better deal even when you barely use the card.', False,
       'The fee can be bigger than the rewards.'),
], fmt='call')

intro = lesson('ct-intro-apr', 'The 0% Intro Rate', 'Zero has an expiration date. The balance that remains does not.', [
    mc('What is an intro APR?',
       ['A temporary low rate that ends on a set date', 'A rate that stays 0% for as long as you own the card', 'A fee'], 0,
       'Read the number of months. That is the whole sale.',
       context='An [[intro APR]] is a teaser, often 0% for 12 or 15 months. When it ends, the regular [[APR]] applies to whatever [[balance]] is left. Miss a payment and some offers end early.'),
    num('You move $1,800 onto a 0% intro rate for 15 months and pay $120 a month. How much have you paid after 15 months?', 1800,
        '$120 × 15 = $1,800.'),
    num('Is anything left to charge the regular rate on?', 0, '$1,800 − $1,800 = $0. You finished inside the window.'),
    num('Suppose you pay only $60 a month for those 15 months. How much is left when the 0% ends?', 900,
        '$60 × 15 = $900 paid. $1,800 − $900 = $900 still owed, now at the regular APR.'),
    tf('A 0% intro rate means the purchase is free.', False, 'It means interest is postponed. The principal is still due.'),
    mc('You cannot pay the balance off before the intro rate ends. What should you assume?',
       ['The leftover balance will cost the regular APR', 'The 0% will renew itself', 'The bank will forgive the rest'], 0,
       'Plan for the rate on the letter, not the rate in the ad.'),
])

transfer = lesson('ct-transfer', 'Balance Transfers', 'A lower rate can be worth a fee. Only if the debt actually gets paid.', [
    num('You transfer $4,000 with a 3% fee. How much is the fee?', 120, '$4,000 × 0.03 = $120.',
        context='A [[balance transfer]] moves debt to a new card. The fee, often 3%, is added to what you owe. A 0% window only helps if you pay the debt down before it shuts.'),
    num('What is the balance on the new card the day the transfer posts?', 4120, '$4,000 + $120 = $4,120.'),
    num('The old card was 24% APR. A rough year of interest on $4,000 would have been?', 960, '$4,000 × 0.24 = $960.'),
    num('If you pay the new card off during a 0% year, how much less is the $120 fee than that $960 of interest?', 840,
        '$960 − $120 = $840. That gap is the point of the move, and it vanishes if the balance is still there when the rate jumps.'),
    tf('After a transfer, you should keep spending on the old card.', False,
       'You moved the debt. Adding new debt puts you back where you started.'),
    mc('The 0% period is 12 months and you can only pay $100 a month. $4,120 ÷ $100 is about 41 months. Is this transfer a good fit?',
       ['No. The debt outlasts the 0% window by years', 'Yes. Any transfer is a win', 'Yes, if the fee is under $500'], 0,
       'Do the months before you do the move.'),
])

store = lesson('ct-store-card', 'Store Cards', 'Today’s discount can cost more than it saves.', [
    num('A $150 jacket is 20% off if you open the store card. How much is the discount?', 30, '$150 × 0.20 = $30.',
        context='Store cards often pair a same-day discount with a very high [[APR]]. The discount is yours only if you were buying the item, and only if you do not carry the balance.'),
    num('What is the sale price?', 120, '$150 − $30 = $120.'),
    num('You carry that $120 for a year at 30% APR. Roughly how much interest?', 36, '$120 × 0.30 = $36.'),
    num('How much more is the interest than the discount you “saved”?', 6, '$36 − $30 = $6. You paid for the sale.'),
    mc('You can pay the $120 today in cash. Should you open the store card for the discount?',
       ['No. Pay cash. The card’s rate is the trap, and you do not need it', 'Yes. Store cards always help a credit score', 'Yes, and leave the balance for a year'], 0,
       'A discount you can already afford in cash does not require a 30% card.'),
    tf('A store card at a high APR is a cheap way to build credit if you carry a balance.', False,
       'On-time and paid in full builds credit. Carrying a 30% balance just costs money.'),
])

jay_story = {
    'title': 'The rewards chase',
    'character': 'Jay, 24, retail associate',
    'body': 'Jay’s card pays **5%** back at restaurants this quarter. He starts eating out so the category “pays him.” In three months he puts **$600** on the card. About **$200** of that was meals he would have bought anyway.\n\n'
            'He pays the statement in full, which is the one part he gets right. The extra **$400** was spent to chase the bonus.',
}
assert round(600 * 0.05) == 30 and 400 - 30 == 370
jay = lesson('ct-jay', 'Jay’s Rewards Chase', 'He earned $30 and spent $400 he did not need to spend.', [
    num('How much cash back does Jay earn on the $600?', 30, '$600 × 0.05 = $30.'),
    num('How much of the $600 was extra spending he would not have done?', 400, 'The story: $600 − $200 of ordinary meals = $400.'),
    num('After the $30 reward, how much did that extra spending cost him?', 370, '$400 − $30 = $370.'),
    mc('What went well?',
       ['He paid the statement in full, so he did not add interest', 'The extra meals were free', '5% back means he made money overall'], 0,
       'No interest. The waste was the extra $400.'),
    tf('Spending more in a bonus category is a good idea whenever the percent is high.', False,
       'The percent applies to money leaving your account.'),
    mc('What should Jay do next quarter?',
       ['Use the 5% on meals he was buying anyway, and skip the rest', 'Double his restaurant budget', 'Open three more cards for the same chase'], 0,
       'Rewards ride along. They do not pick the purchase.'),
], fmt='story', story=jay_story)

trial_steps = [
    num('3% cash back on $2,000. How much is the reward?', 60, '$2,000 × 0.03 = $60.'),
    num('A $90 annual fee needs to be covered by an extra 1.5% back. How much spending is that?', 6000, '$90 ÷ 0.015 = $6,000.'),
    tf('A 0% intro APR lasts for the life of the card.', False, 'It lasts for the months in the offer, then the regular APR starts.'),
    mc('A balance transfer charges 3% on $1,000. What is the fee?', ['$30', '$300', '$3'], 0, '$1,000 × 0.03 = $30.'),
]

lessons = [cashback, points, costmore, annual, intro, transfer, store, jay,
           review('ct'), trial('ct', 'Card Rewards & Traps', trial_steps)]
write_unit('06-card-traps.json', 'card-traps', 6, 'Card Rewards & Traps',
           'Rewards, teaser rates, and the fees that eat them.',
           'A reward you pay interest to earn is not a reward.', terms, lessons, section=S)
