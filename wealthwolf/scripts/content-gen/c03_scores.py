from lib import *
from preserved import kept, kept_term

S = 'credit-debt'
terms = {
    'credit-score': kept_term('credit-score'),
    'credit-limit': kept_term('credit-limit'),
    'credit-utilization': kept_term('credit-utilization'),
    'hard-inquiry': term('Hard inquiry', 'A credit check a lender makes when you apply to borrow. It can nudge your score down a little and stays on your report for about two years.',
                         'Applying for a car loan puts a hard inquiry on your report.'),
    'secured-card': term('Secured card', 'A credit card you qualify for by putting down a deposit, often equal to the limit. The deposit is the lender’s backup while you build a payment record.',
                         'Put down $200, get a $200 limit, and use the card like any other.'),
    'credit-mix': term('Credit mix', 'The variety of credit you have, such as a card and a loan. On a FICO score it is a small slice, about 10%.',
                        'One card and one car loan is a mix. Ten new cards is not the goal.'),
}

factors = lesson('cs-factors', 'What the Score Weighs', 'Five ingredients. Two of them do most of the work.', [
    info('FICO’s five factors',
         'The FICO score, the one most lenders still use, weighs five things:\n\n'
         'Payment history, about 35%. Amounts owed, about 30%. Length of history, about 15%. New credit, about 10%. [[Credit mix]], about 10%.\n\n'
         'Other scores use their own recipes. These weights are FICO’s, and they are the ones to remember.'),
    mc('On a FICO score, which factor weighs the most?', ['Payment history, about 35%', 'Credit mix, about 10%', 'New credit, about 10%'], 0,
       'On-time payments are the biggest slice.'),
    mc('Which factor is about 30%?', ['Amounts owed', 'Length of history', 'Credit mix'], 0,
       'How much of your limits you are using lives here.'),
    match('Match the FICO factor to its weight.',
          [('Payment history', 'About 35%'), ('Amounts owed', 'About 30%'), ('Length of history', 'About 15%'), ('Credit mix', 'About 10%')]),
    tf('Every credit score in the country uses these exact five weights.', False,
       'FICO does. Other scores have their own formulas.'),
    mc('You can control which two factors fastest?',
       ['Paying on time, and keeping balances low', 'The year you opened your first card', 'Your parents’ old loans'], 0,
       'History length takes years. Payments and balances move now.'),
])

history = lesson('cs-history', 'Payment History', 'One late payment echoes. A long streak of on-time ones helps.', [
    mc('What helps a credit score the most, month after month?', ['Paying every bill on time', 'Carrying a balance so the card “sees activity”', 'Opening a new card each month'], 0,
       'Payment history is the heaviest factor.',
       context='Your [[credit score]] cares most about whether you pay on time. A paid-off bill and a [[minimum payment]] made by the [[due date]] both count as on time. Late is late.'),
    tf('Paying only the minimum, but paying it by the due date, still counts as on time.', True,
       'On time and “paid in full” are different jobs. The score is watching the due date.'),
    mc('A payment is 30 days late. What is the likely effect?',
       ['It can hurt the score and stay on the report for years', 'Nothing, if you pay the next day', 'The score goes up, because you used the card'], 0,
       'Thirty days late is a negative mark. Under federal rules it can stay about seven years.'),
    num('You have 24 months of payments and 1 of them was late. How many were on time?', 23, '24 − 1 = 23. One miss still stings.', unit=None),
    mc('Which is the safer habit?',
       ['Autopay at least the minimum, then pay extra when you can', 'Waiting until you feel like paying', 'Paying a day after the due date to earn interest'], 0,
       'Autopay covers the “on time” job. Extra payments do the “get out of debt” job.'),
    tf('A single late payment is a secret. Lenders never see it.', False, 'It can land on your credit report.'),
])

util = lesson('cs-utilization', 'Utilization Math', 'Balance divided by limit. Lower is kinder to the score.', [
    num('Limit $1,500. Balance $450. What is your utilization?', 30, '$450 ÷ $1,500 = 0.30, which is 30%.',
        context='[[Credit utilization]] is balance ÷ [[credit limit]]. A common rule of thumb is to stay under 30%, and lower is better. It is a habit, not a law.', unit='%'),
    num('Limit $2,500. Balance $250. What is your utilization?', 10, '$250 ÷ $2,500 = 0.10, which is 10%.', unit='%'),
    num('You owe $800 on a $1,000 limit. How much must you pay so the balance is $300?', 500, '$800 − $300 = $500.'),
    num('After that payment, what is utilization on the $1,000 limit?', 30, '$300 ÷ $1,000 = 30%.', unit='%'),
    mc('Which balance looks better on a $4,000 limit?', ['$400', '$3,200', '$3,900'], 0,
       '$400 is 10%. $3,200 is 80%. $3,900 is almost the whole limit.',
       why=['10% used.', '80% used.', '97.5% used.']),
    tf('Maxing out a card, even if you pay on time, can still hurt the score.', True,
       'On-time payments and high utilization are different factors.'),
])

length = lesson('cs-length', 'Length of History', 'Old accounts are a track record. Closing them can shrink it.', [
    mc('What does “length of credit history” look at?',
       ['How long your accounts have been open, and how long since you used them', 'How long your shift at work is', 'How many years until a loan is illegal'], 0,
       'Older, well-kept accounts help.',
       context='Length of history is about 15% of a FICO score. An old card you keep open and pay can help. Closing your oldest card can shorten the story lenders see.'),
    tf('Closing your oldest credit card can shorten your credit history.', True,
       'That account’s age may stop counting the way it did.'),
    mc('You opened your first card 8 years ago and a second card last month. Which one is the long history?',
       ['The 8-year-old card', 'The new card', 'Whichever has the higher balance'], 0,
       'Age is the point of this factor.'),
    num('Your oldest account was opened in 2018. It is now 2026. How many years has it been open?', 8, '2026 − 2018 = 8 years.', unit='years'),
    mc('A new borrower has a thin file. What does that mean?',
       ['There is not much history for a lender to read', 'Their score is automatically 850', 'They cannot be charged interest'], 0,
       'Thin is not the same as bad. It means “we hardly know you.”'),
    tf('Keeping an old card open, with a zero or small balance, can help the length factor.', True,
       'The account keeps aging. You do not have to carry debt for that.'),
])

inquiry = lesson('cs-inquiries', 'New Credit and Hard Inquiries', 'Shopping for a loan leaves footprints. Checking yourself does not.', [
    mc('What is a hard inquiry?',
       ['A lender checking your credit because you applied to borrow', 'You looking at your own score', 'A store mailing you an ad'], 0,
       'You asked to borrow, so they looked.',
       context='A [[hard inquiry]] happens when you apply for credit. It can dip a score a little and stays on the report for about two years. You checking your own score is not a hard inquiry.'),
    tf('Looking up your own credit score lowers it.', False, 'That check is yours. It does not count as a hard inquiry.'),
    mc('You apply for four cards in one week. What is the likely result?',
       ['Several hard inquiries, and maybe a lower score', 'A higher score, because you look popular', 'The old inquiries get deleted'], 0,
       'A burst of new applications looks risky.'),
    mc('Rate-shopping one car loan at three lenders in a short window is often treated more kindly than four random cards. Why?',
       ['Scoring models often group loan shopping into one search', 'Car loans are invisible', 'Inquiries only count in December'], 0,
       'One car, one search. Do not stretch it across months.'),
    num('A hard inquiry stays about two years. You applied in 2026. About what year does it drop off?', 2028,
        '2026 + 2 = 2028.', unit=None),
    fill('A lender’s credit check when you apply is a ___ inquiry.', ['hard', 'soft', 'secret'], 0, 'Hard inquiry. Your own check is the harmless kind.'),
])

zero = lesson('cs-from-zero', 'Building Credit from Zero', 'No history yet. A small, boring account starts one.', [
    mc('What is a secured card?',
       ['A card you open by putting down a deposit, often equal to the limit', 'A card that spends your savings with no bill', 'A debit card'], 0,
       'The deposit backs the limit while you build a record.',
       context='A [[secured card]] asks for a deposit, often the same size as the [[credit limit]]. Use a little, pay the statement in full, and on-time payments start a history. A credit-builder loan is the other common door: you pay into a small loan, and those payments get reported.'),
    num('You put down $300 and the secured card’s limit is $300. You spend $30. What is your utilization?', 10,
        '$30 ÷ $300 = 10%.', unit='%'),
    mc('What should you do with that $30 charge?',
       ['Pay it in full, on time', 'Pay nothing so the deposit covers it', 'Spend the other $270 too'], 0,
       'The deposit is not a free pass. The bill is still yours.'),
    tf('A debit card builds a credit score the same way a credit card does.', False,
       'Debit spends your own money. It usually is not a credit account.'),
    mc('A credit-builder loan is useful because…',
       ['The payments can be reported, and you end up with the money you paid in', 'It erases old late payments', 'It raises your salary'], 0,
       'You are practicing paying, and the record shows it.'),
    mc('Which habit builds the file without digging a hole?',
       ['Small balance, paid in full, every month', 'Max the card and pay the minimum', 'Apply for five cards this week'], 0,
       'Boring and on time wins.'),
])

myths = lesson('cs-myths', 'Score Myths', 'Sort the rumor from the rule.', [
    sort('Myth or fact?', ['Myth', 'Fact'], [
        ('Carrying a balance on purpose raises your score', 0),
        ('Checking your own score lowers it', 0),
        ('You must earn a high income to have a high score', 0),
        ('Paying on time is the heaviest FICO factor', 1),
        ('High utilization can hurt even when you pay on time', 1),
        ('A hard inquiry can nudge a score down', 1),
    ], context='The score measures how you handle borrowed money, not how big your paycheck is.'),
    mc('You pay the statement in full every month. Are you “failing” to build credit?',
       ['No. On-time, paid-in-full use is a strong record', 'Yes. You must leave a balance', 'Yes. Interest is what builds the score'], 0,
       'Interest is a cost, not a strategy.'),
    tf('A higher income automatically means a higher credit score.', False, 'Income is not a FICO factor.'),
    mc('Someone says “close all your cards so you have zero debt and a perfect score.” What is wrong?',
       ['Closing cards can shorten history and raise utilization on what remains', 'Nothing. Zero cards is the top score', 'Cards cannot be closed'], 0,
       'Zero debt is good. Zero history is a blank page.'),
    num('Two cards, $1,000 limit each. You close one. You still owe $400. What is utilization now?', 40,
        'The open limit is $1,000. $400 ÷ $1,000 = 40%. Before, it was $400 ÷ $2,000 = 20%.', unit='%'),
    mc('Which statement is a fact?',
       ['Lower utilization is generally better', 'Maxing out a card helps the mix factor', 'Late payments vanish after one month'], 0,
       'Keep the slice you use small.'),
], fmt='sort')

trial_steps = [
    mc('On a FICO score, payment history is about what share?', ['35%', '10%', '5%'], 0, 'It is the largest factor.'),
    num('Balance $600, limit $2,000. What is the utilization?', 30, '$600 ÷ $2,000 = 30%.', unit='%'),
    tf('A secured card requires a deposit and can be a first credit account.', True, 'The deposit backs a small limit.'),
    mc('Which check is a hard inquiry?',
       ['Applying for a new card', 'Looking at your own score', 'Reading a lesson about credit'], 0,
       'You applied to borrow. That is the hard kind.'),
]

lessons = [kept('dc-credit-score'), factors, history, util, length, inquiry, zero, myths,
           review('cs'), trial('cs', 'Credit Scores', trial_steps)]
write_unit('03-credit-scores.json', 'credit-scores', 3, 'Credit Scores',
           'What a score weighs, and how to start one from nothing.',
           'Your score is a rumor lenders believe. Pay on time and it stays kind.', terms, lessons, section=S)
