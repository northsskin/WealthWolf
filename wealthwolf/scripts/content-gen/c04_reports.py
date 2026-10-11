from lib import *

S = 'credit-debt'
terms = {
    'credit-report': term('Credit report', 'The file of your credit accounts: what you owe, whether you paid on time, and who has looked. The score is a number built from this file.',
                          'A report lists a $420 card balance and a car loan. It does not, by itself, show the score.'),
    'credit-bureau': term('Credit bureau', 'A company that collects credit information and sells reports. The three big ones are Equifax, Experian, and TransUnion.',
                          'A loan might show on Experian and not yet on Equifax.'),
    'credit-freeze': term('Credit freeze', 'A lock you place at each bureau so new lenders cannot pull your report. You lift it when you want to apply.',
                          'Freeze all three, then thaw one the week you shop for a car loan.'),
}

vs = lesson('cr-vs-score', 'Report and Score', 'The report is the story. The score is one number squeezed out of it.', [
    mc('What is a credit report?',
       ['The file of your accounts, payments, and inquiries', 'A single number from 300 to 850', 'Your tax return'], 0,
       'The file comes first. The score is calculated from it.',
       context='A [[credit report]] lists your accounts and whether you paid. A [[credit score]] is a number built from that file. The free reports at AnnualCreditReport.com do not include the score.'),
    tf('Your credit report and your credit score are the same thing.', False, 'One is the file. The other is a number made from the file.'),
    mc('Where do the free weekly reports come from, with no score attached?',
       ['AnnualCreditReport.com', 'A random “free score” ad', 'Your employer’s payroll site'], 0,
       'That is the official site. As of 2026 the three bureaus still offer those reports weekly.'),
    mc('Why read the report if you already know the score?',
       ['The report shows the accounts and errors behind the number', 'The score already lists every account', 'Reports are only for lenders'], 0,
       'You cannot fix a wrong account from a number alone.'),
    match('Match each word to what it is.',
          [('Credit report', 'The file of accounts and payments'), ('Credit score', 'A number built from that file'), ('Hard inquiry', 'A lender’s check when you apply')]),
    tf('A free credit report from AnnualCreditReport.com includes your FICO score.', False,
       'The report is free. The score is a separate product.'),
])

bureaus = lesson('cr-bureaus', 'Three Bureaus', 'Equifax, Experian, TransUnion. None of them has to match the others.', [
    mc('How many big nationwide credit bureaus are there?', ['Three', 'One', 'Twelve'], 0, 'Equifax, Experian, and TransUnion.',
       context='A [[credit bureau]] collects your credit data and sells reports. The three nationwide ones are Equifax, Experian, and TransUnion. A lender might report to one and not the others, so the files can differ.'),
    match('Match each bureau to the file it keeps.',
          [('Equifax', 'Its own copy of your report'), ('Experian', 'A second, separate report'), ('TransUnion', 'A third report that can differ')]),
    tf('If one bureau’s report is clean, the other two must be clean too.', False,
       'Each file is its own. Check all three.'),
    mc('Why check all three reports?',
       ['An error or a fraud account may sit on only one of them', 'The law says you pick a favorite', 'They always show the same score'], 0,
       'One clean file does not clear the other two.'),
    mc('Who do you freeze if you want new lenders blocked?',
       ['Each bureau, because a freeze at one does not cover the others', 'Only Equifax', 'Your bank’s app'], 0,
       'Three files, three locks.'),
    fill('Experian, Equifax, and TransUnion are credit ___.', ['bureaus', 'scores', 'unions'], 0, 'They keep the reports.'),
])

free = lesson('cr-free-reports', 'Free Reports', 'Once a week, from the official site. Still true in 2026.', [
    info('Where the free ones live',
         'AnnualCreditReport.com is the official site for the free reports required by federal law. Equifax, Experian, and TransUnion made weekly free reports permanent in 2023, and that was still the offer in 2026.\n\n'
         'Other sites may sell you a score, a subscription, or nothing. The weekly reports do not include your credit score.'),
    mc('How often could you get a free report from each big bureau in 2026?',
       ['Every week', 'Once in your life', 'Only in December'], 0,
       'Weekly, at the official site.'),
    mc('Which site is the official one?',
       ['AnnualCreditReport.com', 'Any site that says “free score” in an ad', 'A link in a random text'], 0,
       'Type it yourself. Do not trust a look-alike.'),
    tf('The free weekly report includes your credit score.', False, 'It is the report, not the score.'),
    mc('A site asks for a credit card “to verify you” before showing a free report. What do you do?',
       ['Leave. The official weekly reports do not require a card', 'Enter the card', 'Send a photo of your license in a text'], 0,
       'Paying is the clue that it is not the official free report.'),
    mc('You want all three files. What do you request?',
       ['A report from Equifax, Experian, and TransUnion', 'Only the bureau you like', 'Your old tax return'], 0,
       'Three files. One sitting can still hide a problem.'),
])

report_lines = [
    ('card', 'City Bank card · balance', 420),
    ('auto', 'MileAuto loan · balance', 6400),
    ('coll', 'QuickCash Collections · balance', 340),
]
REPORT = doc('statement', 'Sample credit report', report_lines, subtitle='One bureau · you, age 29',
             meta=[['Report date', 'Oct 2026']],
             note='QuickCash Collections is an account you have never opened.')
reading = lesson('cr-reading', 'Reading a Report', 'Names, balances, and a line that should not be there.', [
    num('What is the City Bank card balance on this report?', 420, 'The card line: $420.',
        context='Read a report line by line: who you owe, how much, and whether a late payment is listed.',
        doc=REPORT),
    num('What is the car loan balance?', 6400, 'MileAuto: $6,400.', doc=REPORT),
    num('Add the card and the car loan. What do those two balances total?', 6820, '$420 + $6,400 = $6,820.', doc=REPORT),
    num('What is the QuickCash Collections balance?', 340, 'The collections line: $340.', doc=REPORT),
    mc('Which line needs a harder look?',
       ['QuickCash Collections, an account you never opened', 'The car loan you know about', 'A zero late-payment count'], 0,
       'Unknown accounts are how fraud hides.', doc=REPORT),
    tf('A balance on the report means you should pay it today, even if you do not recognize the account.', False,
       'Recognize it first. An account that is not yours gets disputed, not paid on a hunch.'),
], fmt='document')

spot_lines = [
    ('card', 'Harbor Card · opened 2021 · balance', 180),
    ('loan', 'Campus credit union loan · balance', 2100),
    ('fake', 'Luma Store card · opened last month · balance', 890),
]
SPOT = doc('statement', 'Your report · one bureau', spot_lines, subtitle='You have never shopped at Luma',
           note='The Luma card was opened last month. You did not apply.')
spot = lesson('cr-not-yours', 'An Account That Is Not Yours', 'Tap the line that does not belong.', [
    spot('Which line is the account you never opened?', SPOT, 'fake',
         'Luma Store card, opened last month, is not yours. The others match accounts you know.',
         context='Fraud often shows up as a new account you do not remember. That is the line to dispute.'),
    mc('What do you do about the Luma card?',
       ['Dispute it with the bureau, and tell the lender it is fraud', 'Pay the $890 so it goes away', 'Ignore it. Strange accounts fall off in a week'], 0,
       'Paying a fraud account can look like you accept it.'),
    num('If the fake $890 were counted, how much would it add to the $180 and $2,100 you really owe?', 890,
        'It adds its own $890. $180 + $2,100 + $890 = $3,170, but $890 of that is not yours.'),
    tf('An account you never opened can still hurt your score while it sits on the report.', True,
       'The score reads the file, including the bad lines.'),
    mc('You see the same fake account on only one bureau. Do you still act?',
       ['Yes. Fix the file that has it, and check the other two', 'No. One out of three is fine', 'Only if the balance is over $10,000'], 0,
       'Lenders read the file they happen to pull.'),
    order('Put a fraud response in order.',
          ['Confirm the account is not yours', 'Dispute it with the bureau and the lender', 'Place a credit freeze', 'Check all three reports again'],
          'Name it, challenge it, lock new applications, then look again.'),
], fmt='spot')

dispute = lesson('cr-dispute', 'Disputing an Error', 'Tell the bureau what is wrong, in writing, and keep a copy.', [
    mc('An old address and a paid-off loan still show as open. What is that?',
       ['Errors you can dispute', 'Facts you are not allowed to question', 'A hard inquiry'], 0,
       'Wrong facts get challenged.',
       context='If a report is wrong, you dispute it: you tell the [[credit bureau]] what is incorrect and ask for a fix. Do it with each bureau that shows the error. Send copies of proof, and keep your own copy. This is not the same as asking your bank to reverse a charge.'),
    order('Put a dispute in order.',
          ['Find the wrong line on the report', 'Write what is wrong and include proof', 'Send it to the bureau that shows it', 'Read the result and check the report again'],
          'Find it, explain it, send it, confirm the fix.'),
    tf('You should dispute a wrong account with every bureau that lists it.', True,
       'A fix at one bureau does not rewrite the others.'),
    mc('What belongs in the dispute?',
       ['What is wrong, and a copy of anything that proves it', 'Only your opinion, with no details', 'Your card number in a text to a stranger'], 0,
       'Specific and documented.'),
    mc('The bureau corrects the fake account. What do you do next?',
       ['Check that the line is actually gone, on a fresh report', 'Assume it is fixed forever', 'Close every real account too'], 0,
       'Trust the new report, not the promise.'),
    tf('Paying a collection you do not owe is the fastest way to clean a report.', False,
       'Pay what you owe. Dispute what you do not.'),
])

freeze = lesson('cr-freeze', 'Freezing Your Credit', 'A lock on new loans. You still use the cards you already have.', [
    mc('What does a credit freeze do?',
       ['Stops new lenders from pulling your report until you lift it', 'Erases your old late payments', 'Closes your cards'], 0,
       'It blocks new credit. It does not wipe history.',
       context='A [[credit freeze]] (also called a security freeze) stops new lenders from seeing your report. You place one at each [[credit bureau]], for free, and lift it when you want to apply. Cards you already have keep working.'),
    tf('A freeze at Experian also freezes Equifax and TransUnion.', False, 'Each bureau needs its own freeze.'),
    mc('You want to apply for a car loan next week. What do you do with the freeze?',
       ['Lift it, apply, then freeze again', 'Leave it and hope the dealer guesses', 'Close the loan you already have'], 0,
       'Thaw, shop, lock.'),
    mc('Does a freeze stop you from using a card you already have?',
       ['No. Existing accounts still work', 'Yes. Every card is frozen shut', 'Only on weekends'], 0,
       'The lock is on new applications.'),
    tf('Placing a credit freeze is free by law.', True, 'You do not pay the bureau to freeze or to lift a freeze.'),
    mc('When is a freeze especially worth it?',
       ['After a data leak, or if a fake account just showed up', 'Only after you retire', 'When you want a higher score this week'], 0,
       'It does not raise the score. It makes the next fake account harder.'),
])

marks = lesson('cr-how-long', 'How Long Marks Stay', 'Most bad news lasts years. The clock is federal, not a rumor.', [
    info('The usual clocks',
         'Under the Fair Credit Reporting Act, most negative marks stay about seven years. A late payment is in that group. A Chapter 7 bankruptcy can stay up to 10 years. A hard inquiry stays about two years.\n\n'
         'These are the federal limits. Paying a collection does not rewind the clock to zero, and a credit freeze does not delete old marks.'),
    mc('About how long can a late payment stay on a report?', ['About 7 years', 'About 7 weeks', 'Forever'], 0,
       'Seven years is the usual federal limit for late payments.'),
    mc('About how long can a Chapter 7 bankruptcy stay?', ['Up to 10 years', '1 year', 'Until you ask'], 0,
       'Chapter 7 is the long one: up to 10 years.'),
    mc('About how long does a hard inquiry stay?', ['About 2 years', 'About 10 years', 'Until the loan is paid'], 0,
       'Two years, and the score often cares less after the first year.'),
    tf('A credit freeze deletes late payments.', False, 'A freeze blocks new pulls. It does not erase history.'),
    num('A late payment is reported in 2026. About what year does that seven-year clock run out?', 2033,
        '2026 + 7 = 2033.', unit=None),
])

trial_steps = [
    mc('Which site is the official source for a free credit report?',
       ['AnnualCreditReport.com', 'Whatever the newest ad says', 'Your streaming app'], 0,
       'Type the official address yourself.'),
    tf('A credit freeze at one bureau covers all three.', False, 'Freeze each bureau on its own.'),
    mc('A Chapter 7 bankruptcy can stay on a report for up to how long?', ['10 years', '10 weeks', '10 days'], 0,
       'Up to 10 years under federal rules.'),
    num('A report shows a $250 card and a $1,750 loan, both yours. What do those balances add up to?', 2000,
        '$250 + $1,750 = $2,000.'),
]

lessons = [vs, bureaus, free, reading, spot, dispute, freeze, marks,
           review('cr'), trial('cr', 'Credit Reports', trial_steps)]
write_unit('04-credit-reports.json', 'credit-reports', 4, 'Credit Reports',
           'Read the file behind the score, fix what is wrong, and lock what you can.',
           'The report is the story. Read it before someone else does.', terms, lessons, section=S)
