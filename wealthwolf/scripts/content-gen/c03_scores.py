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
       ['Paying on time, and keeping balances low', 'The year you opened your first card', 'How many cards you have ever opened'], 0,
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
       ['Autopay at least the minimum, then pay extra when you can', 'Paying in full, whenever you remember', 'Paying a day after the due date to earn interest'], 0,
       'Autopay covers the “on time” job. Extra payments do the “get out of debt” job.'),
    tf('A single late payment is a secret. Lenders never see it.', False, 'It can land on your credit report.'),
])

CARDS = doc('statement', 'Your cards', [
    ('harbor', 'Harbor Card · limit $1,500', 450.00),
    ('store', 'City Store Card · limit $500', 400.00),
    ('cloud', 'Cloud Card · limit $2,000', 150.00)],
    subtitle='Balances on statement day', totals=[('Total balance', 1000.00, True)])
assert 450 + 400 + 150 == 1000 and 1500 + 500 + 2000 == 4000
util = lesson('cs-utilization', 'Utilization Math', 'Read three cards, then work out what the score sees.', [
    num('What is the utilization on the Harbor Card alone?', 30, '$450 ÷ $1,500 = 0.30, which is 30%.',
        context='[[Credit utilization]] is balance ÷ [[credit limit]]. Scores look at each card and at all of them together. A common rule of thumb is to stay under 30%, and lower is better.',
        unit='%', doc=CARDS),
    num('And on the City Store Card?', 80, '$400 ÷ $500 = 0.80, which is 80%.', unit='%', doc=CARDS),
    num('Add up the three limits. What is your total credit limit?', 4000, '$1,500 + $500 + $2,000 = $4,000.', doc=CARDS),
    num('What is your overall utilization: total balance ÷ total limit?', 25, '$1,000 ÷ $4,000 = 0.25, which is 25%.', unit='%', doc=CARDS),
    mc('You have $300 extra this month. Where does it fix the worst number?',
       ['Pay down the City Store Card', 'Pay down the Cloud Card', 'Split it evenly across all three'], 0,
       '$100 left on a $500 limit is 20%, down from 80%.',
       why=['', 'That card is already at 7.5%. The store card is the one at 80%.', 'Helpful, but the store card stays high.'],
       doc=CARDS),
    tf('Maxing out a card, even if you pay on time, can still hurt the score.', True,
       'On-time payments and high utilization are different factors.'),
], fmt='document')

nina_story = {
    'title': 'The old student card',
    'character': 'Nina, 29, office manager',
    'body': 'Nina opened her first credit card at **21**: a student card with a **$1,000** limit. She has used it for gas ever since and paid it in full every month. Two years ago she added a second card with a **$3,000** limit.\n\n'
            'Now the student card charges a **$45** annual fee, and she is thinking of closing it. Her statements usually add up to about **$800** across both cards, which she pays in full.',
}
assert 800 / 4000 == 0.20 and round(800 / 3000 * 100) == 27
length = lesson('cs-length', 'Nina’s Oldest Card', 'Old accounts are a track record. Closing one can cost more than the fee.', [
    mc('What does “length of credit history” look at?',
       ['How long your accounts have been open', 'How long you have had your current job', 'How long until your loans are paid off'], 0,
       'Older, well-kept accounts help.',
       context='Length of history is about 15% of a FICO score. An old card you keep open and pay can help. Closing your oldest card can shorten the story lenders see.'),
    num('Nina is 29 and opened the student card at 21. How old is that account?', 8, '29 − 21 = 8 years.', unit='years'),
    tf('Closing the student card could shorten the history lenders see.', True, 'It is her oldest account.'),
    num('With both cards open, her $800 is what share of her $4,000 total limit?', 20, '$800 ÷ $4,000 = 20%.', unit='%'),
    num('If she closes the $1,000 card, what share of the remaining $3,000 limit is $800? Round to the nearest whole percent.', 27,
        '$800 ÷ $3,000 = 0.267, about 27%. Same spending, higher utilization.', unit='%'),
    mc('What is a common middle path for Nina?',
       ['Ask the issuer to switch it to a no-fee card and keep it open', 'Close it and open a new card to replace the limit', 'Close it, since old accounts stop counting after five years'], 0,
       'She keeps the history and the limit, and drops the fee.',
       why=['', 'A new card means a hard inquiry and a brand-new account.', 'Old accounts keep counting. That’s the point of this factor.']),
], fmt='story', story=nina_story)

inquiry = lesson('cs-inquiries', 'New Credit and Hard Inquiries', 'Shopping for a loan leaves footprints. Checking yourself does not.', [
    mc('What is a hard inquiry?',
       ['A lender checking your credit because you applied to borrow', 'You looking at your own score', 'A store mailing you an ad'], 0,
       'You asked to borrow, so they looked.',
       context='A [[hard inquiry]] happens when you apply for credit. It can dip a score a little and stays on the report for about two years. You checking your own score is not a hard inquiry.'),
    tf('Looking up your own credit score lowers it.', False, 'That check is yours. It does not count as a hard inquiry.'),
    mc('You apply for four cards in one week. What is the likely result?',
       ['Several hard inquiries, and maybe a lower score', 'A higher score, because you have more credit available', 'The old inquiries get deleted'], 0,
       'A burst of new applications looks risky.'),
    mc('Rate-shopping one car loan at three lenders in a short window is often treated more kindly than four random cards. Why?',
       ['Scoring models often group loan shopping into one search', 'Car loans don’t appear on credit reports', 'Lenders delete inquiries once a loan is approved'], 0,
       'One car, one search. Do not stretch it across months.'),
    num('A hard inquiry stays about two years. You applied in 2026. About what year does it drop off?', 2028,
        '2026 + 2 = 2028.', unit=None),
    fill('A lender’s credit check when you apply is a ___ inquiry.', ['hard', 'soft', 'monthly'], 0, 'Hard inquiry. Your own check is the harmless kind.'),
])

SECURED = doc('bill', 'Secured card', [('deposit', 'Deposit, refundable', 300.00), ('fee', 'Annual fee', 0.00)],
              subtitle='Harbor Bank', meta=[['Credit limit', '$300'], ['APR', '27%']],
              note='Pay the statement in full and the APR never applies.')
BUILDER = doc('bill', 'Credit-builder loan', [('loan', 'Loan held in savings for you', 600.00), ('pay', '12 monthly payments of $52', 624.00)],
              subtitle='Lakeshore Credit Union', note='You get the $600 at the end. The rest is interest and fees.')
assert 52 * 12 == 624 and 624 - 600 == 24
zero = lesson('cs-from-zero', 'Building Credit from Zero', 'Two common first steps. Pick the one that fits your budget.', [
    mc('What is a secured card?',
       ['A card you open with a deposit, often equal to the limit', 'A prepaid card that never reports to the bureaus', 'A debit card linked to your savings'], 0,
       'The deposit backs the limit while you build a record.',
       context='A [[secured card]] asks for a deposit, often the same size as the [[credit limit]]. Use a little, pay the statement in full, and on-time payments start a history. A credit-builder loan is the other common door: you pay into a small loan, and those payments get reported.',
       docs=[SECURED, BUILDER]),
    num('On the secured card you spend $30 a month and pay it in full. What is your utilization on the $300 limit?', 10,
        '$30 ÷ $300 = 10%.', unit='%', docs=[SECURED, BUILDER]),
    num('What does the credit-builder loan cost in total, beyond the $600 you get back?', 24, '$624 − $600 = $24.', docs=[SECURED, BUILDER]),
    mc('Rina has $300 saved but no room in her budget for a new monthly bill. Which fits her?',
       ['The secured card, used lightly and paid in full', 'The credit-builder loan', 'Neither: her debit card already builds credit'], 0,
       'The deposit is money she has. The loan would add a $52 bill every month.',
       why=['', 'It adds a $52 bill every month for a year.', 'Debit cards usually don’t report to the bureaus.'], docs=[SECURED, BUILDER]),
    mc('Malik can spare $52 a month but has nothing saved to lock up. Which fits him?',
       ['The credit-builder loan', 'The secured card'], 0,
       'No deposit needed, and he ends the year with $600 saved.', docs=[SECURED, BUILDER]),
    mc('Which habit builds the file without digging a hole?',
       ['Small balance, paid in full, every month', 'Max the card and pay the minimum', 'Apply for five cards this week'], 0,
       'Boring and on time wins.'),
], fmt='call')

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
       ['Applying for a new card', 'Looking at your own score', 'A card company sending you a pre-approved offer'], 0,
       'You applied to borrow. That is the hard kind.'),
]

lessons = [kept('dc-credit-score'), factors, history, util, length, inquiry, zero, myths,
           review('cs'), trial('cs', 'Credit Scores', trial_steps)]
write_unit('03-credit-scores.json', 'credit-scores', 3, 'Credit Scores',
           'What a score weighs, and how to start one from nothing.',
           'Your score is a rumor lenders believe. Pay on time and it stays kind.', terms, lessons, section=S)
