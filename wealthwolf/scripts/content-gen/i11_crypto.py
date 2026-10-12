from lib import *

S = 'investing'
terms = {
    'cryptocurrency': term('Cryptocurrency',
                           'A digital token recorded on a shared ledger. Its price is what the next buyer will pay. It pays no coupon and it can go to zero.',
                           'A coin that was $1,000 and is later $400.'),
}

what = lesson('cy-what', 'What Crypto Is', 'A token with a price, not a plan.', [
    info('No coupon, no building',
         'A [[cryptocurrency]] is a digital token on a shared ledger. Nobody owes you interest. There is no company earnings line and no rent. The price is the next buyer. This unit is education. It is not a coin to buy, and it will not name one.'),
    mc('What sets a coin’s price?',
       ['A coupon written on the token', 'Whatever the next buyer will pay', 'FDIC insurance'], 1,
       'No coupon, no insurance on the price. Buyers and sellers are the whole price.'),
    tf('A cryptocurrency pays a bond-style coupon.', False,
       'There is no issuer promising interest and a face value back. The price can go to zero.'),
    mc('How should you read this unit?',
       ['As a list of coins to buy', 'As education about a risky token, not a recommendation', 'As a replacement for an index fund'], 1,
       'No ticker. No promise. The risks are the lesson.'),
    fill('A digital token whose price is the next buyer is a ___.',
         ['cryptocurrency', 'coupon', 'CD'], 0,
         'Cryptocurrency. A CD is a bank deposit. A coupon is a bond’s interest.'),
])

drop = lesson('cy-drop', 'A 60% Drop', 'The math does not care about the story.', [
    info('Round and harsh',
         'Crypto prices have swung harder than a broad stock [[index]]. This lesson uses one clean case: a $1,000 coin falls 60%. You have $400. The other $600 is gone unless the price comes back, which it does not owe you. Historically, on average, is the wrong phrase here. A single coin is not “the market.”'),
    num('A $1,000 coin falls 60%. How many dollars are left?', 400,
        '$1,000 × 0.40 = $400.'),
    num('How many dollars did that drop destroy?', 600,
        '$1,000 − $400 = $600.'),
    tf('A 60% drop needs only a 60% rise to get back to $1,000.', False,
       '$400 × 1.60 = $640. Getting from $400 back to $1,000 is a 150% gain. $400 × 2.5 = $1,000.'),
    num('What percent gain turns $400 back into $1,000?', 150, unit='%',
        explain='You need $600 more on a $400 base. $600 ÷ $400 = 1.50, which is 150%.'),
])

scam_doc = doc('statement', 'A message, not a market',
               [('gain', 'What they say you are “up”', 2000),
                ('fee', 'Unlock fee they want sent first', 80)],
               subtitle='You cannot withdraw until you pay',
               note='A fee to unlock your own money is the scam.')

scam = lesson('cy-scam', 'Scams and Rug Pulls', 'The fee to unlock your money is the tell.', [
    info('Two shapes',
         'A rug pull is when the people behind a new token take the money and disappear. The other shape is a message: your coins are “up,” but you must send a fee before you can withdraw. Real investments do not charge you a secret fee to touch your own money. Nobody legitimate needs you to move coins to a stranger’s wallet so they can “fix” an account.'),
    spot('Which line is the scam?', scam_doc, 'fee',
         'The $80 unlock fee is the trap. The $2,000 “gain” is the bait. You do not pay a stranger to access your own money.'),
    tf('A promise of 10% every day is a normal yield.', False,
       'Ten percent a day is the shape of a scam, not a bond yield. Walk away.'),
    mc('Someone asks you to send coins to a wallet they control so they can repair your account. What do you do?',
       ['Send a small test', 'Stop. Do not send anything. Real support does not need your coins moved to them.', 'Send more, because the gain looks large'], 1,
       'Moving the coins to them is the theft. Stop.'),
    num('The bait says you are up $2,000, and the unlock fee is $80. If you pay it and the “gain” was never real, how many dollars did you just hand over?', 80,
        'The $80 is gone. The $2,000 was a picture on a screen.'),
], fmt='spot')

keep = lesson('cy-keep', 'Exchanges and Custody', 'Someone else holding it is a risk of its own.', [
    info('Who has the coins',
         'On an exchange, the platform holds the coins and you have an account. If the platform freezes withdrawals or fails, you are in line with everyone else. A private wallet puts the keys with you. Lose the keys and the coins are gone. There is no password reset. Do not assume [[SIPC]] covers a crypto app. SIPC is about securities at member brokerages, not about a coin’s price, and not about a typical crypto platform.'),
    mc('You keep coins on an exchange. Who is holding them?',
       ['The platform', 'SIPC', 'Your bank, with FDIC insurance on the coin’s price'], 0,
       'The platform. If it fails or freezes, that is your problem. The coin’s price is a separate risk.'),
    tf('SIPC replaces a drop in a coin’s price.', False,
       'SIPC does not cover a market drop, and a typical crypto app is not that kind of brokerage protection anyway.'),
    mc('You hold the keys in a private wallet and you lose them. What happens?',
       ['The exchange resets the password', 'The coins are gone', 'FDIC sends a check'], 1,
       'No reset. The keys are the ownership. This is why “I’ll remember it” is not a plan, and why a coin is a bad place for rent money.'),
    fill('If the platform holds the coins for you, that platform is the ___.',
         ['exchange', 'coupon', 'cap rate'], 0,
         'Exchange. Your account is an IOU from them until you withdraw.'),
])

spec = lesson('cy-spec', 'Speculation or Investing', 'A plan has earnings or a coupon. A bet has a story.', [
    info('The line',
         '[[Investing]], in this course, means owning a broad fund, a bond, or a real business you can leave alone for years. Speculation is a bet that a price will rise because other people will pay more. A coin, a meme stock, and a short-term options bet sit on the speculation side. You may still do it. You do not call it the plan.'),
    sort('Which pile is this?',
         ['The plan', 'A speculation'],
         [('A broad index fund for a 30-year goal', 0),
          ('A coin bought because a video said it would triple', 1),
          ('A Treasury you intend to hold to maturity', 0),
          ('A meme stock from a screenshot', 1)],
         'The plan has a job and a long date. The screenshot and the video are bets that someone else pays more.'),
    tf('Calling a bet an investment changes what it is.', False,
       'The name does not add earnings, a coupon, or a recovery schedule.'),
    mc('Where does a coin you cannot explain sit?',
       ['In the emergency fund', 'On the speculation side, in money you can lose', 'Inside the 401(k) match, as the whole match'], 1,
       'If you do it, it is a slice you can lose. It is not the rent, the match, or the emergency fund.'),
    fill('A bet that someone else will pay more is ___.',
         ['speculation', 'a coupon', 'vesting'], 0,
         'Speculation. The plan is the fund, the bond, and the years.'),
], fmt='sort')

slice = lesson('cy-slice', 'How Much Is Too Much', 'Rent money is too much. A slice you can lose is the cap.', [
    info('The test',
         'The cap is the amount you can watch go to zero without missing rent, food, or the [[emergency fund]]. If that amount is $200, then $200 is the cap. A $2,000 buy is $1,800 past it. There is no clever percent that makes a coin safe. The test is the bills.'),
    num('You can afford to lose $200. You are about to buy $2,000 of a coin. How many dollars over the cap is that?', 1800,
        '$2,000 − $200 = $1,800 too much.'),
    tf('Five percent of your money is a safe rule that makes a coin fine.', False,
       'No percent makes the price safe. The test is whether you can lose the dollars and still pay your life.'),
    mc('Which pile is allowed to be the speculation slice?',
       ['The emergency fund', 'Money you can lose without missing a bill', 'The rent'], 1,
       'Loseable money only. The emergency fund and the rent have jobs.'),
    num('Your cap is $200 and you already bought $200 of a coin. How many more dollars fit inside the cap?', 0,
        'The cap is full. More would be money you decided you could not lose.'),
])

bets = lesson('cy-bets', 'Meme Stocks and Options', 'A bet can expire. The plan should not.', [
    info('Same family as the coin',
         'A meme stock is a share people pile into because it is a story, not because you read the business. An option is a contract with a deadline. The premium you pay can expire and be worth $0. A $300 option can become nothing. Neither belongs in the emergency fund, the match, or the long-term [[index fund]]. If you touch them, they are speculation, in the small slice.'),
    num('You pay a $300 option premium and it expires worthless. How many dollars are left of that premium?', 0,
        'Worthless means $0. The $300 is the cost of the bet, gone.'),
    tf('A meme stock is a diversified index fund with a fun name.', False,
       'It is one company, plus a crowd. One company is concentration. The crowd is not a plan.'),
    mc('Where do options and meme stocks belong in this course’s sorting?',
       ['The core of the retirement mix', 'With speculation, in money you can lose', 'Inside the emergency fund, because they are exciting'], 1,
       'The slice you can lose. The retirement mix stays the broad, cheap funds.'),
    mc('What can an option do that a savings account cannot?',
       ['Expire and be worth $0', 'Earn a posted APY', 'Get FDIC insurance on the premium'], 0,
       'The deadline is the point. The premium can vanish. Savings do not expire.'),
])

kai = lesson('cy-kai', 'Kai’s Lesson', 'The drop was real. The “agent” was the second trap.', [
    info('Meet Kai',
         'Kai is 24 and a barista. He put $1,000 into a coin after a video. It fell 60%, to $400. Then a “support agent” offered to unlock the loss if Kai sent $200 first.\n\nHe did not send it. His real plan, a broad index fund in his Roth IRA, was untouched. Any future bet stays inside $100 he can lose.'),
    num('How many dollars did Kai lose on the 60% drop?', 600,
        '$1,000 − $400 = $600. The video did not change the subtraction.'),
    num('If he had paid the unlock fee, how many more dollars would have left, on top of the $600?', 200,
        'The $200 would be a second loss. The agent does not have his coins to unlock.'),
    tf('Kai should move his Roth IRA index fund into the coin to win the $600 back.', False,
       'The fund is the plan. Chasing the loss with the plan is how a speculation becomes the whole portfolio.'),
    mc('What did Kai get right?',
       ['Buying because of the video', 'Refusing to send $200 to a stranger, and leaving the index fund alone', 'Emptying the emergency fund to average down'], 1,
       'The drop already happened. The scam was optional, and he skipped it. The fund stayed the plan.'),
], fmt='story', story={
    'title': 'The video and the agent',
    'character': 'Kai, 24, barista',
    'body': 'Kai put **$1,000** into a coin. It fell **60%**, to **$400**. A “support agent” then asked for **$200** to unlock the account.\n\nHe did not send it. His Roth IRA index fund stayed where it was.',
})

write_unit('11-crypto.json', 'crypto', 11, 'Crypto & Speculation',
           'Tokens, scams, and the small slice you can actually lose.',
           'A story is not a plan. The fee to unlock your money is a scam.',
           terms, [what, drop, scam, keep, spec, slice, bets, kai, review('cy'), trial('cy', 'Crypto & Speculation', [
               num('A $2,500 coin falls 60%. How many dollars are left?', 1000,
                   '$2,500 × 0.40 = $1,000.'),
               tf('You should send a fee to a stranger before you can withdraw.', False,
                  'A fee to unlock your own money is the scam. Do not send it.'),
               mc('A meme stock belongs in which pile?',
                  ['The emergency fund', 'Speculation, with money you can lose', 'The bond you hold to maturity'], 1,
                  'It is a bet on a crowd. The plan stays the broad fund and the real bills.'),
               num('Your loseable cap is $150 and a friend wants you to put in $500. How many dollars over the cap is $500?', 350,
                   '$500 − $150 = $350 too much.'),
           ])],
           section=S)
