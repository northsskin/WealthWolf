from lib import *

S = 'protecting'
terms = {
    'identity-theft': term('Identity theft',
                           'Someone uses your name, Social Security number, or accounts to open credit, file taxes, or spend money as you.',
                           'A card you never applied for shows up, and the bill is already $1,800.'),
}

want = lesson('it-wants', 'What Thieves Want', 'The number they want most is the one that opens other accounts.', [
    sort('Useful to a thief, or not the prize?',
         ['Useful to a thief', 'Not the prize'],
         [('Your Social Security number', 0),
          ('Your bank login and the text code', 0),
          ('The name of your favorite band', 1),
          ('A store receipt with no card number on it', 1),
          ('A copy of your tax return', 0)],
         'The prize is anything that opens money or credit in your name.',
         context='[[Identity theft]] means someone uses your name or numbers to borrow, spend, or file as you.'),
    mc('Why is a Social Security number so useful to a thief?',
       ['It can help them open credit or file a tax return as you', 'It unlocks your email account', 'It is printed on every bank card'], 0,
       'That number follows you. A store login does not.'),
    tf('A one-time text code is safe to read aloud to a caller.', False,
       'The code is the second key. Say it and the account is theirs.'),
    mc('Which is worth locking up, not posting?',
       ['A photo of your driver’s license', 'A photo from a concert', 'A screenshot of your playlist'], 0,
       'The license has the numbers a form asks for.'),
    fill('Identity theft is someone acting as ___ with your information.',
         ['you', 'your bank', 'your employer'], 0,
         'The accounts and the bills land on you.'),
], fmt='sort')

how = lesson('it-how', 'How It Happens', 'A stolen password, a lost wallet, or a form left in the trash.', [
    mc('Which is a common way identity theft starts?',
       ['A stolen login, a lost wallet, or a data leak', 'Paying a bill you actually owe', 'Using two-factor authentication'], 0,
       'The thief needs a way in. A leak, a purse, or a reused password is enough.',
       context='You already use [[two-factor authentication|two-factor-authentication]] so a password alone is not enough.'),
    tf('Using the same password on your email and your bank makes one leak enough.', True,
       'Email is the reset button for everything else.'),
    mc('A form in the mailbox with your Social Security number on it. What is the risk?',
       ['Anyone who takes the mail can use that number', 'Only the post office can open it', 'Nothing. Thieves want cards, not paper'], 0,
       'Outgoing and incoming mail is a pile of keys.'),
    mc('What is a safer habit for old tax forms?',
       ['Shred them or lock them', 'Toss them in the recycling as they are', 'Tear them in half and recycle them'], 0,
       'Recycling does not hide a Social Security number.'),
    tf('A data leak at a company means your identity has already been stolen.', False,
       'A leak is a head start, not a finished theft. A credit freeze still blocks new loans.'),
])

report_lines = [
    ('card', 'Harbor Card, opened 2019', 640.00),
    ('car', 'Lakeshore auto loan, opened 2023', 9850.00),
    ('loan', 'QuickLend personal loan, opened Feb 12', 2400.00),
    ('phone', 'Phone plan, opened 2021', 70.00),
]
assert 640 + 9850 + 70 == 10560
STMT = doc('statement', 'Your credit report', report_lines, subtitle='Open accounts · TransUnion',
           note='You opened the card, the car loan, and the phone plan yourself.')
spot = lesson('it-spot', 'Warning Signs', 'The bill you do not recognize is the alarm.', [
    spot('Which line is the warning?', STMT, 'loan',
         'An online loan you never opened is someone borrowing in your name.',
         context='A [[credit report]] lists every account in your name. A new one you never opened is the alarm.'),
    num('How much is the loan you never opened?', 2400, 'That line is $2,400.', doc=STMT),
    num('What do the three accounts you do recognize add up to?', 10560,
        '$640 + $9,850 + $70 = $10,560.', doc=STMT),
    mc('A new card arrives that you did not apply for. What is that?',
       ['A warning sign of identity theft', 'A normal offer, since card companies mail them out', 'Proof your score went up'], 0,
       'You did not ask. Someone may have asked as you.'),
    tf('The auto loan is the line to worry about, because it is the biggest balance.', False,
       'Size isn’t the signal. The account you never opened is.'),
], fmt='spot')

freeze = lesson('it-freeze', 'Freeze Your Credit', 'A freeze is free, and it is one lock per bureau.', [
    mc('A credit freeze stops what?',
       ['New lenders from opening credit in your name', 'Charges on the cards you already have', 'You from checking your own report'], 0,
       'Old accounts still work. New credit applications stall until you lift the freeze.',
       context='A [[credit freeze]] is a lock at each [[credit bureau]]. The three big ones are Equifax, Experian, and TransUnion.'),
    num('How many bureaus do you freeze to cover the three big ones?', 3,
        'Equifax, Experian, and TransUnion. One freeze is not all three.', unit=None),
    tf('A freeze at one bureau protects you at the other two.', False,
       'Each bureau has its own lock.'),
    mc('You want to apply for a car loan. What do you do with the freeze?',
       ['Lift it at the bureau the lender will check, then freeze again', 'Leave it on. Lenders can see past a freeze', 'Remove it for good, since a freeze can’t be paused'], 0,
       'You hold the key. Lift it for the application, then lock it again.'),
    tf('Placing a credit freeze costs a yearly fee at each bureau.', False,
       'A freeze is free. A company that charges you to “freeze” is selling something else.'),
])

steps = lesson('it-steps', 'The Recovery Steps', 'Start the official plan, then lock the doors.', [
    order('Put the first recovery steps in order.',
          ['Report it at IdentityTheft.gov',
           'Freeze your credit at each bureau',
           'Dispute the accounts that are not yours',
           'Keep checking your reports after that'],
          'IdentityTheft.gov builds the plan. The freeze stops the next account. The dispute challenges the one already there.',
          context='[[Identity theft]] recovery starts at IdentityTheft.gov. A [[credit freeze]] is part of that plan.'),
    mc('What is IdentityTheft.gov for?',
       ['The federal place that walks you through a recovery plan', 'A site that sells you a new Social Security number', 'Your bank’s login page'], 0,
       'It is the Federal Trade Commission’s recovery site, not a shop.'),
    tf('You should pay a company that promises a new Social Security number.', False,
       'You almost never get a new number. Anyone selling one is a second scam.'),
    mc('An account on your report is not yours. What do you do with it?',
       ['Dispute it and say it is the result of identity theft', 'Pay it so it will go away quietly', 'Ignore it for a year'], 0,
       'Paying a debt you do not owe can make it look like you agreed.'),
    fill('Freeze your credit at ___ of the three big bureaus.',
         ['each', 'one', 'two'], 0,
         'One lock leaves two doors open.'),
])

mail = lesson('it-mail', 'Mail and Documents', 'The trash can is a filing cabinet if you let it be.', [
    mc('Which paper is worth shredding?',
       ['A tax form with your Social Security number', 'A grocery flyer', 'A blank envelope'], 0,
       'The form has the number. The flyer does not.'),
    tf('Mail can be stolen right out of an unlocked box at the curb.', True,
       'Card offers, checks, and tax forms all travel by mail. A locked box or quick pickup helps.'),
    mc('You are going on a trip. What do you do about the mail?',
       ['Have it held, or ask someone you trust to pick it up', 'Leave it. The carrier holds it once the box is full', 'Post your trip dates so friends can watch the house'], 0,
       'A full box advertises an empty house and hands over your papers.'),
    mc('A medical bill has your name, your address, and your account number. Where does it belong?',
       ['In a file you control, then shredded when you no longer need it', 'In the recycling, once you have paid it', 'Taped to the fridge until it is paid'], 0,
       'Account numbers are keys. Treat the paper like one.'),
    tf('Posting a photo of your boarding pass is harmless.', False,
       'The barcode can hold a record locator. Crop it or skip the photo.'),
])

tax = lesson('it-tax', 'Tax Identity Theft', 'Someone files as you, and your refund becomes their payday.', [
    info('The refund you never asked for',
         'Tax identity theft is when someone files a return using your Social Security number, usually to steal the refund.\n\nYou find out when the IRS rejects your real return because one was already filed, or when a transcript shows wages from a job you never had.'),
    mc('The IRS rejects your return because a return was already filed. What might that mean?',
       ['Someone may have filed using your Social Security number', 'You made a math mistake on the return', 'Your employer forgot to send your W-2'], 0,
       'A return you did not file is the warning.'),
    tf('The IRS usually first contacts you about a tax problem by text or social media.', False,
       'The IRS starts with a letter in the mail. A text or DM that says it is the IRS is a scam.'),
    mc('What is a careful response to a letter that really is from the IRS?',
       ['Read it and respond the way the letter says, or call the number on irs.gov', 'Wire the amount to the person who texted you about the letter', 'Ignore every IRS letter'], 0,
       'Use the letter and the official site, not a stranger who already knows you got mail.'),
    mc('What helps stop someone filing as you next year?',
       ['An Identity Protection PIN from the IRS, used on your return', 'Filing your return as late as you can', 'Changing the bank account your refund goes to'], 0,
       'The IRS rejects any return filed under your number without your six-digit PIN. Anyone can request one at irs.gov.',
       why=['', 'The thief wants to file first. Filing late makes that easier.', 'The thief puts their own account on the fake return.']),
])

marcus_story = {
    'title': 'The card he never asked for',
    'character': 'Marcus, 41, school bus driver',
    'body': 'Marcus opens a letter from a store card he has never held. The balance is **$1,800**. He did not shop there. He pulls his [[credit report]] and finds the card, opened six weeks ago, plus an inquiry he does not remember.\n\nHe has not frozen his credit. The three bureaus are still taking new applications in his name.',
}
marcus = lesson('it-marcus', 'Marcus Finds an Account', 'The letter was the alarm. The freeze is the lock.', [
    num('How much is the store card he never opened?', 1800, 'The letter says $1,800.'),
    mc('What is the first official place to start a recovery plan?',
       ['IdentityTheft.gov', 'A text from someone offering to fix it for $300', 'A new Social Security number sold online'], 0,
       'Start with the Federal Trade Commission’s site, not a helper who found you.'),
    num('He freezes Equifax, Experian, and TransUnion. How many freezes is that?', 3,
        'Three bureaus, three freezes.', unit=None),
    tf('Paying the $1,800 quickly is the best way to prove the card is not his.', False,
       'Paying can look like he accepts the debt. He disputes it.'),
    mc('After the freeze, a new lender wants to open credit in his name. What happens?',
       ['The lender cannot pull the report until Marcus lifts the freeze', 'The card opens if Marcus’s score is high enough', 'The freeze only blocks store cards'], 0,
       'That is what the lock is for.'),
], fmt='story', story=marcus_story)

trial_steps = [
    mc('Which of these belongs in the shredder?',
       ['Last year’s tax form', 'A takeout menu', 'A birthday card with no numbers on it'], 0,
       'The tax form carries the Social Security number.'),
    tf('A freeze at Experian also freezes Equifax and TransUnion.', False,
       'Each bureau keeps its own lock.'),
    num('A card you never opened shows a $900 balance and a $300 fee. How much is on that account in total?', 1200,
        '$900 + $300 = $1,200.'),
    mc('Where do you start the federal recovery plan?',
       ['IdentityTheft.gov', 'A gift-card payment to the caller', 'By ignoring the strange account'], 0,
       'That site is the front door. The freeze and the disputes follow.'),
]

lessons = [want, how, spot, freeze, steps, mail, tax, marcus,
           review('it'), trial('it', 'Identity Theft', trial_steps)]
write_unit('02-identity-theft.json', 'identity-theft', 2, 'Identity Theft',
           'What thieves steal, how you spot it, and how you lock the file.',
           'Your name is a key. Do not leave copies lying around.', terms, lessons, section=S)
