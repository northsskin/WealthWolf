from lib import *

terms = {
    'fdic-insurance': term('FDIC insurance', 'US government protection for bank deposits: if an insured bank fails, you get your money back, up to $250,000 per person, per bank.',
                           'Your bank closes with $3,000 of yours inside. The FDIC pays you the $3,000.'),
    'direct-deposit': term('Direct deposit', 'Your pay sent electronically straight into your bank account, with no paper check.',
                           'Your paycheck lands in checking every other Friday morning.'),
    'checking-account': term('Checking account', 'A bank account for everyday money: your pay lands there, and card payments and bills come out of it.',
                             'Your paycheck arrives, then rent and groceries leave from the same account.'),
    'debit-card': term('Debit card', 'A card that spends money straight from your checking account.',
                       'Tap it for a $30 shirt and $30 leaves your checking account right away.'),
    'atm': term('ATM', 'A cash machine. Use your debit card and PIN to take out or deposit cash.',
                'Taking $60 out of the machine outside your bank.'),
    'deposit': term('Deposit', 'Money going into your account, like your pay, a check or cash.',
                    'Your $1,079.40 paycheck arriving is a deposit.'),
    'available-balance': term('Available balance', 'The money you can actually spend right now, after holds and pending payments.',
                              'Your balance is $520, but a $400 check is on hold, so $120 is available.'),
    'pending-transaction': term('Pending transaction', 'A payment that’s started but hasn’t finished going through. The money is already promised.',
                                'A $58 grocery charge from last night that hasn’t come off your balance yet.'),
    'credit-union': term('Credit union', 'A bank-like institution owned by its members, which often means lower fees and better rates.',
                         'A credit union for teachers in your county.'),
    'online-bank': term('Online bank', 'A bank with no branches: everything happens in an app or website, which often means fewer fees.',
                        'An app-only bank with no monthly fee and a higher savings rate.'),
    'two-factor-authentication': term('Two-factor authentication', 'Logging in with two things: your password plus a code sent to your phone.',
                                      'You type your password, then a 6-digit code your bank texts you.'),
}

why_bank = lesson('bk-why-bank', 'Why Use a Bank?', 'Safer than a mattress, and it does work for you.', [
    info('Your money’s home base',
         'A bank keeps your money safe, lets you pay bills and spend with a card, and gives your employer somewhere to send your pay.\n\n'
         'Cash at home can be lost, stolen or burned, and nobody pays it back. Money in an insured bank is protected.'),
    mc('Your bank goes out of business. You had $3,000 in your account. What happens?',
       ['FDIC insurance pays it back', 'The money is gone', 'You get back half'], 0,
       'Up to $250,000 per person, per bank, is covered. Your $3,000 is safe.',
       context='Most US bank accounts have [[FDIC insurance]]: if the bank fails, the government pays you back, up to **$250,000** per person, per bank.'),
    tf('Cash hidden at home is protected by FDIC insurance.', False, 'FDIC insurance only covers money in an insured bank.'),
    mc('What’s the main benefit of direct deposit?',
       ['Your pay arrives on its own, often faster', 'You get paid more', 'You skip taxes'], 0,
       'No paper check to lose, no trip to the bank, and often the money arrives sooner.',
       context='With [[direct deposit]], your employer sends your pay straight into your account. No paper check needed.'),
    mc('Which is the safest place for $2,000 of savings?', ['An FDIC-insured bank account', 'A shoebox under your bed', 'Your wallet'], 0,
       'Insured, protected, and it can earn a little interest.'),
    fill('If your bank fails, FDIC insurance covers up to ___ per person, per bank.', ['$2,500', '$250,000', '$2.5 million'], 1,
         '$250,000. More than enough for most people.'),
])

check_save = lesson('bk-checking-savings', 'Checking vs. Savings', 'One account for spending, one for keeping.', [
    mc('What’s a checking account for?', ['Everyday spending and bills', 'Money you won’t touch for years', 'Borrowing money'], 0,
       'Checking is where money comes and goes.',
       context='A [[checking account]] is for everyday money: your pay lands there, and bills and card payments come out of it.'),
    mc('Where should next year’s holiday money live?', ['In savings', 'In checking with the rent money', 'In your wallet'], 0,
       'Separate and growing, so you don’t spend it by accident.',
       context='A [[savings account]] is for money you’re keeping, not spending. It usually pays you a little [[interest]]: extra money for leaving it there.'),
    sort('Checking or savings? Sort them.', ['Checking', 'Savings'],
         [('Paying rent', 0), ('Emergency money', 1), ('Buying groceries with your card', 0), ('Money for a car in two years', 1),
          ('Your paycheck landing', 0), ('Holiday fund', 1)]),
    tf('Keeping savings in a separate account makes you less likely to spend it by accident.', True,
       'Out of sight of your card, out of reach of your impulses.'),
    num('Your savings account pays 2% a year. How much interest does $1,500 earn in a year?', 30, '$1,500 × 0.02 = $30.',
        context='Savings interest is shown as a yearly percentage. 1% of $1,000 is $10 a year.'),
    mc('Why not keep everything in savings?',
       ['Savings accounts aren’t built for daily card payments and bills', 'Savings accounts are illegal for young people', 'Savings never pay interest'], 0,
       'Many savings accounts limit withdrawals. Checking handles the daily traffic.'),
    mc('You get paid. What’s a simple setup?',
       ['Pay lands in checking, and a set amount moves to savings', 'Everything stays in checking', 'Everything goes into savings'], 0,
       'Spend from one account, build in the other.'),
], fmt='sort')

opening = lesson('bk-opening', 'Opening an Account', 'What to bring, what to ask, what to skip.', [
    info('What you’ll need',
         'To open an account you usually need a photo ID, your Social Security number, an address, and sometimes a small first deposit.\n\n'
         'Under 18? You’ll usually need a parent or guardian on the account with you.'),
    mc('Which do you usually need to open a bank account?', ['A photo ID and your Social Security number', 'A credit card', 'A job offer letter'], 0,
       'Banks have to check who you are. ID and Social Security number do that.'),
    mc('Before you sign up, what’s the most important thing to ask?',
       ['What fees could I be charged, and how do I avoid them?', 'What color is the debit card?', 'How many branches are downtown?'], 0,
       'Fees are where a “free” account stops being free.'),
    order('Put opening an account in order.',
          ['Compare a few banks or credit unions', 'Check the fees and the insurance', 'Apply with your ID and Social Security number',
           'Make your first deposit and set up direct deposit'],
          'Shop, check, apply, fund.'),
    tf('A bank asking for your Social Security number when you open an account is normal.', True,
       'Banks are required to confirm who you are. Just never give it to someone who contacts you out of the blue.'),
    mc('The banker offers a credit card, an overdraft plan and a paid “account protection” add-on. What do you do?',
       ['Say no for now and open just the basic accounts', 'Sign up for everything', 'Walk out without an account'], 0,
       'Start simple. You can always add things later once you understand them.'),
])

debit = lesson('bk-debit-atm', 'Debit Cards & ATMs', 'Spending your own money, one tap at a time.', [
    mc('You buy a $30 shirt with your debit card. Where does the money come from?',
       ['Your checking account', 'The bank lends it to you', 'Your savings account'], 0, 'Straight out of checking, right away.',
       context='A [[debit card]] spends money straight from your checking account. Tap it, and the money leaves.'),
    mc('Which of these is a mistake?',
       ['Writing your PIN on the back of your card', 'Covering the keypad as you type your PIN', 'Memorizing your PIN'], 0,
       'Lose the card and you’ve handed over the code too.',
       context='An [[ATM]] is a cash machine. Your debit card and PIN (a secret 4-digit code) let you take out cash.'),
    num('The ATM charges $3.50 and your own bank adds $2.50. What does it cost to take out $40?', 6,
        '$3.50 + $2.50 = $6 to get $40. That’s 15% of the cash.',
        context='ATMs outside your bank’s network often charge a fee, and your own bank may charge one too.'),
    num('You do that twice a week for a year, 104 times. What do the fees add up to?', 624, '$6 × 104 = $624.'),
    tf('With a debit card, you can never spend more than what’s in your account.', False,
       'Some banks let the payment through anyway and charge a fee for it. You’ll meet that trap in the next unit.'),
    mc('Your debit card is lost. First move?', ['Lock or report it in your bank app right away', 'Wait a week to see if it turns up', 'Keep using the card number online'], 0,
       'Lock it now. You can unlock it if it turns up in your jacket.'),
    fill('A debit card takes money from your ___ account.', ['checking', 'savings', 'credit'], 0, 'Checking. That’s what it’s linked to.'),
])

deposits = lesson('bk-deposits', 'Money In: Deposits & Holds', 'Why your balance and your spendable money can differ.', [
    mc('Which of these is a deposit?', ['Your paycheck arriving', 'Paying your phone bill', 'Taking cash from an ATM'], 0,
       'Money in is a deposit. The other two are money out.',
       context='A [[deposit]] is money going into your account: your pay, a check, cash at the counter.'),
    mc('You deposit a $400 check this morning. Your account shows $520, but your available balance is $120. Why?',
       ['The check is on hold', 'The bank took a $400 fee', 'Someone stole $400'], 0, '$520 − $400 on hold = $120 you can use right now.',
       context='When you deposit a check, the bank may hold it for a day or two before you can spend it. Your [[available balance]] is what you can spend right now.'),
    num('Your balance is $860. A $250 check you deposited is still on hold. What’s your available balance?', 610, '$860 − $250 = $610.'),
    tf('You should spend based on your available balance, not your total balance.', True,
       'The available balance is the real number.'),
    mc('You deposited a check by photographing it in your bank app. What should you do with the paper check?',
       ['Keep it safe for a couple of weeks, then destroy it', 'Deposit it again at the branch', 'Hand it back to the person who wrote it'], 0,
       'Keep it until the deposit fully clears. Depositing it twice causes real trouble.'),
    order('Put a phone check deposit in order.',
          ['Sign the back of the check', 'Photograph it in your bank app', 'Wait for the hold to clear', 'Spend the money'],
          'Sign, snap, wait, spend.'),
])

alex_story = {
    'title': 'Plenty of money. Or not?',
    'character': 'Alex, 19, first checking account',
    'body': 'On Friday morning Alex’s banking app shows a balance of **$412**. Alex wants to buy a concert ticket.\n\n'
            'What Alex doesn’t notice: three [[pending transactions|pending-transaction]] haven’t finished going through. '
            'A **$58** grocery run, **$24** of gas and **$9** for a streaming service. Pending means the money is already promised, '
            'even though the balance hasn’t dropped yet.\n\n'
            'The concert ticket costs **$340**.',
}
alex = lesson('bk-alex', 'Alex Checks the Balance', 'A balance can look bigger than it really is.', [
    num('Add up the three pending transactions.', 91, '$58 + $24 + $9 = $91.'),
    num('How much does Alex really have once they go through?', 321, '$412 − $91 = $321.'),
    mc('Can Alex afford the $340 ticket today?',
       ['No, there’s only $321 once the pending payments clear', 'Yes, the balance says $412', 'Yes, pending payments don’t count'], 0,
       'The balance hasn’t caught up with what’s already been spent.',
       why=['', 'The balance is out of date by $91.', 'They count. The money is already promised.']),
    num('How much is Alex short?', 19, '$340 − $321 = $19.'),
    tf('Pending transactions can take a day or two to fully go through.', True, 'That’s why the balance lags behind.'),
    mc('Which habit would have saved Alex?', ['Checking pending transactions before a big purchase', 'Only looking at the balance', 'Never buying concert tickets'], 0,
       'Balance minus pending is what you really have.'),
], fmt='story', story=alex_story)

CITY = doc('bill', 'City Bank Everyday', [
    ('fee', 'Monthly fee', 12.00), ('atm', 'Other banks’ ATMs, each time', 3.00)], subtitle='Checking account',
    note='Monthly fee waived if you keep $1,500 or more in the account.')
CLOUD = doc('bill', 'Cloud Checking', [
    ('fee', 'Monthly fee', 0.00), ('atm', 'ATMs in a 55,000-machine network', 0.00)], subtitle='Online bank checking',
    note='No branches. Everything happens in the app.')
types = lesson('bk-account-types', 'Banks, Credit Unions & Online Banks', 'Three kinds of homes for your money. Compare them.', [
    mc('Who owns a credit union?', ['Its members', 'The government', 'One wealthy owner'], 0,
       'Members own it, so profits go back to them.',
       context='A [[credit union]] is like a bank, but owned by its members. Profits come back as lower fees and better rates.'),
    mc('What’s the usual trade-off with an online bank?', ['No branch to walk into', 'No insurance on your money', 'No debit card'], 0,
       'Insured online banks are just as protected. You just can’t visit one.',
       context='An [[online bank]] has no branches. Lower costs often mean fewer fees and better interest on savings.'),
    mc('You usually keep about $600 in checking. Which account costs you less?', ['Cloud Checking', 'City Bank Everyday'], 0,
       'With $600 you’d never reach City Bank’s $1,500 waiver, so you’d pay $12 every month.',
       docs=[CITY, CLOUD], context='Compare accounts on what **you** would pay, based on how you actually bank.'),
    num('With $600 in the account, what would City Bank’s monthly fee cost you over a year?', 144, '$12 × 12 = $144.', docs=[CITY, CLOUD]),
    tf('Online banks and credit unions can’t be insured.', False,
       'Insured online banks have FDIC insurance. Credit unions have the same kind of cover through the NCUA.'),
    sort('Which is it?', ['Bank', 'Credit union', 'Online bank'],
         [('Owned by investors who want a profit', 0), ('Owned by its members', 1), ('No branches, all in an app', 2),
          ('You join through where you live or work', 1), ('Lower fees because there are no branches', 2), ('Big branch network across the country', 0)]),
], fmt='call')

safe = lesson('bk-safe', 'Keep Your Account Safe', 'Passwords, codes and alerts: lock the den.', [
    mc('Which password is strongest?', ['A long phrase only you know, used nowhere else', 'Your birthday', 'The same password you use everywhere'], 0,
       'Long, unique, and not guessable from your social media.',
       context='Most account break-ins start with a stolen password, not a bank robbery.'),
    mc('Someone steals your password. With two-factor on, what stops them?', ['They don’t have the code from your phone', 'Nothing', 'The password expires'], 0,
       'Without your phone, the password alone isn’t enough.',
       context='[[Two-factor authentication]] means logging in takes two things: your password **and** a code sent to your phone.'),
    tf('Your bank may text you to ask for your full password or PIN.', False,
       'Banks never ask for your PIN or password by text, email or phone. Anyone who does is a scammer.'),
    mc('You get an alert for a $240 purchase you didn’t make. First move?',
       ['Lock your card and call the bank on the number printed on your card', 'Reply to the text with your details', 'Wait and see if more charges appear'], 0,
       'Use a number you trust, never one from the message.',
       context='Turn on alerts. Your bank can message you for every purchase, low balances and big withdrawals.'),
    order('A strange charge shows up. Put your response in order.',
          ['Lock your card in the app', 'Call the bank on the number on your card', 'Report the charge as fraud', 'Change your password'],
          'Stop the bleeding, tell the bank, then lock things down.'),
    tf('Logging into your bank on public café Wi-Fi is as safe as at home.', False,
       'Public Wi-Fi can be watched. Use your phone’s data or a network you trust.'),
])

trial_steps = [
    mc('Which account should your paycheck land in?', ['Checking', 'Savings', 'A payment app'], 0, 'Checking, then move your saving out.'),
    num('Your balance is $730, with pending charges of $85 and $40. How much is available to spend?', 605, '$730 − $85 − $40 = $605.'),
    tf('FDIC insurance covers up to $250,000 per person, per bank.', True, 'That’s the limit.'),
    mc('A text says “Your account is locked. Reply with your PIN.” What is it?', ['A scam', 'Your bank', 'A routine check'], 0,
       'Banks never ask for your PIN. Delete it.'),
]

lessons = [why_bank, check_save, opening, debit, deposits, alex, types, safe,
           review('bk'), trial('bk', 'Banking', trial_steps)]
write_unit('04-banking.json', 'banking', 4, 'Banking Basics',
           'Checking, savings, debit cards and deposits: how a bank account actually works.',
           'A bank is a den for your money. Pick a good one.', terms, lessons)
