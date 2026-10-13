from lib import *

S = 'building-wealth'
terms = {
    'fiduciary': term('Fiduciary',
                      'Someone who must put your interest first. A salesperson is paid to sell a product. The titles on a business card do not settle which one you are talking to. Ask.',
                      'A fiduciary who is paid by you, versus a commission for selling one fund.'),
    'fee-only': term('Fee-only',
                     'Paid by you, not by a commission on the products you buy. A 1% yearly fee on $200,000 is $2,000 a year. Fee-only is not the same phrase as “fee-based,” which can include commissions.',
                     'A 1% fee on a balance that stayed $200,000 is $60,000 over 30 years, before any growth in the fee.'),
}

simple = doc('statement', 'A three-fund plan',
             [('auto', 'Automatic monthly investment', 200)],
             subtitle='One mix, already automated')
messy = doc('statement', 'A business, a trust, and three accounts',
            [('biz', 'Business value in the sketch', 180000)],
            subtitle='More moving parts than a single fund')

need = lesson('ad-need', 'Do You Need a Person?', 'Complexity is the reason. A simple plan may not be.', [
    info('Two clients',
         'Some people want a human. The stronger case is a messy life: a business, a trust, a pile of old accounts. A single automatic [[three-fund portfolio|three-fund-portfolio]] is a weaker case. A robo-advisor or doing it yourself can be enough there. Hiring someone is allowed either way. This is not a rule that you must, or must not.'),
    mc('Which page is the stronger case for paying a human?',
       [simple['title'], messy['title']], 1,
       docs=(simple, messy),
       explain='The business and the trust have more parts than one automated mix. The simple page can stay automated.'),
    tf('A three-fund plan is illegal unless an advisor signs it.', False,
       'You can hold it yourself. An advisor is a hire, not a permission slip.'),
    mc('What is a fair reason to hire help on the simple page anyway?',
       ['You know you will not stay the course alone', 'A headline told you to', 'So the advisor can guarantee the return'], 0,
       'Behavior is a real reason. A guarantee is not something they can honestly sell.'),
    num('The simple page invests how many dollars a month?', 200,
        doc=simple,
        explain='The automatic line is $200. The complexity is not in that number.'),
], fmt='call')

duty = lesson('ad-duty', 'Fiduciary or Salesperson', 'Ask who pays them.', [
    info('The duty',
         'A [[fiduciary]] must put your interest first. A salesperson is paid when you buy the product they offer. Some people are both, and “fee-based” can mean a fee plus a commission. “Fee-only” means you pay them and the product does not. Ask the question in those words.'),
    mc('Who must put your interest first?',
       ['A fiduciary', 'Anyone with a nice office', 'The person who texts a stock tip'], 0,
       'Fiduciary is the duty. An office is furniture. A text is not a duty.'),
    tf('The word “advisor” on a card proves the person is a fiduciary.', False,
       'The card is marketing. Ask whether they are a fiduciary, all of the time, for you.'),
    mc('A commission on the fund they sell is a clue that they are what?',
       ['Paid by the product', 'Fee-only', 'A government examiner'], 0,
       'The product is paying them. That is the salesperson side. Fee-only means you are the client paying the bill.'),
    fill('Someone who must put your interest first is a ___.',
         ['fiduciary', 'ticker', 'coupon'], 0,
         'Fiduciary. Then ask how they get paid.'),
])

fee = lesson('ad-fee', 'What 1% Costs', 'A small percent, many years, balance held still.', [
    info('Hold the balance still',
         'A [[fee-only]] advisor who charges 1% a year on $200,000 costs $2,000 this year. If the balance never changed, 30 years would be $60,000. A growing balance makes a percent fee a larger dollar bill. This sketch holds it still so you can see the yearly number. The fee can be worth it. It is never invisible.'),
    num('What is 1% of $200,000, in dollars, for one year?', 2000,
        '$200,000 × 0.01 = $2,000.'),
    num('If that $2,000 stayed the same for 30 years, how many dollars is the fee?', 60000,
        '30 × $2,000 = $60,000. The still-balance sketch understates a percent fee on a growing pile.'),
    tf('Because the sketch held the balance still, a growing account would owe a smaller dollar fee at the same 1%.', False,
       'One percent of a larger balance is more dollars. The still sketch is the gentle version.'),
    mc('What is the fee, in plain words?',
       ['Money that leaves every year, whether the market was kind or not', 'A one-time stamp', 'A tax credit'], 0,
       'Yearly. A bad year does not cancel the percent.'),
])

robo = lesson('ad-robo', 'Robo-Advisors', 'A mix and a rebalance, for a smaller fee.', [
    info('Software with a fee',
         'A robo-advisor picks a mix from your answers, buys the funds, and rebalances. The fee is often lower than a human’s 1%, and it is still a fee. It will not draft a will or sit with you after a death in the family. It also does not promise a return.'),
    mc('What is a robo-advisor good at?',
       ['A simple mix, bought and rebalanced on a schedule', 'Replacing a will and a guardian', 'Guaranteeing a 12% year'], 0,
       'The simple investing chore. Legal documents and hard family years are a different hire.'),
    tf('A lower fee means the robo-advisor cannot lose you money.', False,
       'The funds can fall. The fee is only the cost of the service, not a shield.'),
    num('A robo-advisor charges 0.25% a year on $200,000. How many dollars is that this year?', 500,
        '$200,000 × 0.0025 = $500. The human’s 1% on the same pile was $2,000.'),
    num('How many dollars a year cheaper is that $500 than the $2,000 human fee, on this still balance?', 1500,
        '$2,000 − $500 = $1,500. Cheaper is not the same as sufficient, if your life is the messy page.'),
])

check = lesson('ad-check', 'Look Them Up', 'BrokerCheck, before the first transfer.', [
    info('The public record',
         'FINRA BrokerCheck is a public lookup for brokers. You can see employment history and disclosed events. It is not a Yelp star, and it is not a promise the person is a [[fiduciary]]. It is the minimum look before you move money. If you do not know how to spell their name, you are not ready to hire them.'),
    mc('When do you use BrokerCheck?',
       ['Before you transfer money', 'After the first year, if you feel like it', 'Only if they promise a guarantee'], 0,
       'Before. A guarantee is a reason to walk, not a reason to skip the lookup.'),
    tf('A clean BrokerCheck page proves the person is a fiduciary who charges a fair fee.', False,
       'It is a record of disclosures and history. The duty and the fee are questions you still ask.'),
    mc('What belongs in the lookup?',
       ['The person’s name and record', 'Your account password', 'The federal funds target'], 0,
       'Their name. Never your password. No legitimate lookup needs it.'),
    fill('Look the broker up on BrokerCheck ___ you send the money.',
         ['before', 'after', 'instead of'], 0,
         'Before. The transfer is the point of no casual return.'),
])

pitch = doc('statement', 'A pitch',
            [('fee', 'Yearly fee they mentioned', 2000),
             ('promise', '“Guaranteed” yearly gain they advertised', 24000)],
            subtitle='$200,000 account, 12% “guaranteed”',
            note='A guarantee of a market return is the line to refuse.')

flags = lesson('ad-flags', 'Red Flags', 'The guarantee is the tell.', [
    info('Walk-away lines',
         'A real advisor can explain fees, the mix, and what they cannot promise. “Guaranteed 12%” on a $200,000 account would be $24,000 a year, and markets do not work that way. Pressure to sign today, or a request for your password, is the same family of problem.'),
    spot('Which line is the one you refuse?', pitch, 'promise',
         'A guaranteed market gain is the line. The fee line is something you can discuss. A guarantee is a fiction.'),
    num('Twelve percent of $200,000 is how many dollars they are “guaranteeing”?', 24000,
        '$200,000 × 0.12 = $24,000. That promise is the problem, not a goal you can hold them to.'),
    tf('Signing today is fine if the guarantee is large.', False,
       'A larger fiction is not a better contract. You leave.'),
    mc('Someone offering advice asks for your brokerage password. What do you do?',
       ['Give it, so they can help faster', 'Refuse. They can work with limited access you control', 'Email it and then check BrokerCheck'], 1,
       'Your password stays yours. Limited access that you can revoke is a different, safer arrangement.'),
], fmt='spot')

ask = lesson('ad-ask', 'Questions to Ask', 'Duty, pay, and what they will not promise.', [
    info('The short list',
         'Ask if they are a [[fiduciary]] for you, how they are paid, what the yearly dollars are on your balance, and what they cannot promise. Then look them up. The order matters less than asking all of it before a transfer. This list is the calm version.'),
    order('Put the interview in a sensible order.',
          ['Ask whether they are a fiduciary for you',
           'Ask how they are paid, fee-only or commission',
           'Turn the percent fee into dollars on your balance',
           'Look them up before you transfer anything'],
          'Duty, then pay, then the dollars, then the public record. The transfer is not on this list because it comes after.'),
    tf('You only need to ask one of those questions.', False,
       'Duty without the fee, or a fee without the lookup, leaves a hole.'),
    mc('What should they be willing to say they cannot do?',
       ['Guarantee a yearly market return', 'Explain their fee', 'Tell you whether they are a fiduciary'], 0,
       'No honest person guarantees the market. The fee and the duty are things they should answer plainly.'),
    fill('Turn a percent fee into ___ on your actual balance.',
         ['dollars', 'hope', 'tickets'], 0,
         'Dollars. One percent is not a feeling. It is $2,000 on $200,000.'),
])

omar = lesson('ad-omar', 'Omar’s Two Interviews', 'He prices the help, and he walks from the promise.', [
    info('Meet Omar, later',
         'Omar is 34 and owns the bike shop. He has $200,000 invested in the cheap funds he started years ago. One advisor is a fiduciary, fee-only, at 1% : $2,000 a year, $60,000 over 30 years if the balance never grew.\n\nThe other says the account will “make 12% guaranteed.” Omar looks both up, asks the questions, and does not hire the guarantee. He has not decided the 1% is worth it. He has decided the promise is not.',
         ),
    num('How many dollars a year is the 1% fee on Omar’s $200,000?', 2000,
        '$200,000 × 0.01 = $2,000.'),
    num('How many dollars is that fee over 30 years if the balance stays still?', 60000,
        '30 × $2,000 = $60,000, if the balance never changed.'),
    tf('Omar should hire the person who guaranteed 12%.', False,
       'That sentence is the red flag. A guarantee of a market return is a reason to leave.'),
    mc('What has Omar actually decided?',
       ['The guarantee is a no, and the 1% fee is a question he can take home', 'He must pay 1% because he owns a shop', 'He should move the $200,000 into one stock'], 0,
       'Refuse the fiction. Decide the fee on a calm day, after the lookup.'),
], fmt='story', story={
    'title': 'Two interviews',
    'character': 'Omar, 34, bike shop owner',
    'body': 'Omar has **$200,000** in the cheap funds he started years ago. A fee-only fiduciary wants **1%**, which is **$2,000** a year.\n\nAnother person guarantees **12%**. Omar will not hire the guarantee.',
})

write_unit('09-advisors.json', 'advisors', 9, 'Working with Advisors',
           'When a person helps, how they get paid, and the sentence that means leave.',
           'Ask who pays them. Then turn the percent into dollars.',
           terms, [need, duty, fee, robo, check, flags, ask, omar, review('ad'), trial('ad', 'Working with Advisors', [
               num('A 1% yearly fee on $80,000 is how many dollars this year?', 800,
                   '$80,000 × 0.01 = $800.'),
               tf('“Advisor” on a business card proves a fiduciary duty.', False,
                  'Ask. The card is not the duty.'),
               mc('Which sentence is a reason to walk away?',
                  ['“I am a fiduciary and you pay me 0.8%.”', '“I guarantee the market will return 12%.”', '“Look me up on BrokerCheck.”'], 1,
                  'A guaranteed market return is the fiction. A stated fee and a lookup are ordinary.'),
               num('0.25% of $80,000 is how many dollars?', 200,
                   '$80,000 × 0.0025 = $200.'),
           ])],
           section=S)
