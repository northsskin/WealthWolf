from lib import *

S = 'protecting'
terms = {
    'phishing': term('Phishing',
                     'A fake email, text, or call that pretends to be someone you trust, so you will give up a password, a code, or money.',
                     'A text that looks like your bank and asks you to tap a link and type your password.'),
}

how = lesson('sc-how', 'How Scams Work', 'The trap is the feeling, not the costume.', [
    info('Three levers',
         'Most scams pull the same three levers.\n\nUrgency: act today or lose something. Authority: they dress up as a bank, the police, or the government. Secrecy: they tell you not to check with anyone else.'),
    mc('A text says your account closes in 15 minutes unless you tap now. Which lever is that?',
       ['Urgency', 'A paper receipt', 'A paycheck'], 0,
       'The clock is the pressure. Real problems still let you hang up and check.'),
    mc('The caller says, “I am from your bank. Do not tell your family.” Which lever is the second sentence?',
       ['Secrecy', 'A sale', 'A budget'], 0,
       'Secrecy keeps you from the person who would spot the trick.'),
    tf('A real bank will ask you to keep a problem secret from the people you trust.', False,
       'Secrecy is the scammer’s rule, not the bank’s.'),
    fill('A message that rushes you to act before you can think is using ___.',
         ['urgency', 'a deductible', 'a paycheck'], 0,
         'Slow down. The rush is the product.'),
])

phish = lesson('sc-phishing', 'Phishing', 'The logo can be copied. The link is the hook.', [
    mc('What is phishing?',
       ['A fake message that wants a password, a code, or money', 'A fee your bank prints on a statement', 'A type of savings account'], 0,
       'The disguise is the trusted name. The goal is something only you should have.',
       context='[[Phishing]] is a fake email, text, or call that pretends to be someone you trust.'),
    tf('Your bank may text you to ask for your full password.', False,
       'Banks do not ask for your password or PIN by text, email, or phone.'),
    mc('The text uses your bank’s logo and a link. What is the careful move?',
       ['Leave the link alone and open the bank’s app yourself', 'Tap the link so the bank can fix it', 'Reply with the code they asked for'], 0,
       'You go to the bank. You do not let the message take you there.'),
    mc('A link’s real job in a phishing text is to:',
       ['Take you to a fake page that collects your login', 'Print a receipt', 'Raise your credit score'], 0,
       'The page can look perfect and still belong to someone else.'),
    tf('A correct logo means the message is safe.', False,
       'Logos are easy to copy. The ask is what matters.'),
])

notice_lines = [
    ('pkg', 'Package you ordered last week', 48),
    ('fee', 'Redelivery fee, pay by gift card', 12),
    ('tax', 'Sales tax on the original order', 3),
]
assert 48 + 12 + 3 == 63
NOTICE = doc('receipt', 'Delivery alert', notice_lines, subtitle='From a number you do not know',
             totals=[('They want you to pay', 12, True)],
             note='The store’s real app shows the package is already on the truck.')
spot = lesson('sc-spot', 'Spot the Fake', 'One line gives the scam away.', [
    spot('Which line is the trap?', NOTICE, 'fee',
         'A surprise fee that must be paid by gift card is the hook. The package line is bait.',
         context='Read the whole message. The honest lines make the bad line look normal.'),
    num('How much is the gift-card fee they invented?', 12, 'The redelivery line says $12.', doc=NOTICE),
    mc('Why is a gift card a warning?',
       ['Gift cards are like cash, and you cannot get them back', 'Gift cards earn interest', 'Stores only take gift cards for taxes'], 0,
       'Once the code is read, the money is gone.'),
    tf('You should tap the link first, then decide.', False,
       'The link is how the fake page gets your login.'),
    mc('Where do you check the package instead?',
       ['The store’s app, opened by you', 'The link in the text', 'A number the text tells you to call'], 0,
       'You choose the door. The message does not.'),
], fmt='spot')

calls = lesson('sc-calls', 'Impostor Calls', 'Anyone can claim a title. Hang up and call back yourself.', [
    mc('A caller says they are the IRS and you must pay today with gift cards. What is true?',
       ['The IRS does not demand gift cards over the phone', 'Gift cards are the official way to pay taxes', 'You should stay on the line so they do not fine you'], 0,
       'Taxes are not collected by a stranger who needs a gift card.'),
    tf('“Your grandchild is in trouble. Do not tell their parents. Send money now.” That is a classic impostor setup.', True,
       'Urgency, a loved one’s name, and secrecy. All three levers at once.'),
    mc('Someone calls and says they are your bank’s fraud desk. What do you do?',
       ['Hang up and call the number on your card', 'Give them the code that just arrived by text', 'Move your money where they tell you'], 0,
       'The number on the card is yours to choose. Theirs is not.'),
    mc('They already know the last four digits of your account. Does that prove they are the bank?',
       ['No. Those digits leak, and scammers buy them', 'Yes. Only your bank can know that', 'Yes, if they sound polite'], 0,
       'A few digits are not a secret handshake.'),
    tf('You owe a caller an explanation before you hang up.', False,
       'You can hang up. A real office will still be there when you call back.'),
])

romance = lesson('sc-romance', 'Romance and Investment Scams', 'Love and easy profits are the oldest bait.', [
    mc('You have never met them, and they ask you to send money for a plane ticket. What is the careful read?',
       ['This is a common romance scam', 'Plane tickets are always a gift', 'Meeting online makes the request safer'], 0,
       'The relationship is the setup. The ticket is the withdrawal.'),
    tf('An investment that “guarantees” a huge return, and punishes you for asking questions, is a warning.', True,
       'Real investments can lose money. A guarantee plus secrecy is the tell.'),
    num('You already sent $500, then $500, then $500. How much is gone?', 1500,
        '$500 × 3 = $1,500.'),
    mc('They say you must pay a “tax” before you can withdraw your profits. What is that?',
       ['Another payment in the same scam', 'A normal IRS form', 'Proof the profits are real'], 0,
       'The profits were never there. The tax is the next ask.'),
    mc('What should you do with the chat?',
       ['Stop paying and tell someone you trust', 'Send one more payment to unlock the rest', 'Keep it secret so you are not embarrassed'], 0,
       'Secrecy is how the loss grows. Tell someone.'),
])

flags = lesson('sc-red-flags', 'Gift Cards and Wires', 'The payment method is the clue.', [
    sort('Red flag, or an ordinary payment?',
         ['Red flag', 'Ordinary'],
         [('Pay a fee with gift cards', 0),
          ('Wire the money today and tell no one', 0),
          ('A bill you expected, from a company you already pay', 1),
          ('A receipt from a store you stood in today', 1),
          ('A stranger who will not take a normal card or bank payment', 0)],
         'Gift cards, wires, and secrecy move money in a way you cannot undo.'),
    num('Two $200 gift cards. How much would you lose?', 400, '$200 + $200 = $400.'),
    mc('Why do scammers love gift cards?',
       ['The code spends like cash, and the store cannot pull it back', 'Gift cards build your credit score', 'The IRS prefers them'], 0,
       'There is no refund button after the code is read.'),
    tf('A wire to a stranger is easy to reverse the next day.', False,
       'A wire is built to arrive and stay.'),
    mc('A seller will only take a wire, and the deal closes tonight. What fits?',
       ['Treat it as a red flag and walk away', 'Wire it so you do not lose the deal', 'Send half now as a compromise'], 0,
       'A real seller can wait for a payment you can reverse.'),
], fmt='sort')

hour = lesson('sc-first-hour', 'The First Hour', 'Stop the bleeding, then check the real door.', [
    order('Put the first hour in order.',
          ['Stop. Do not send money or a login code',
           'Call the real company on a number you look up yourself',
           'Change the password and turn on two-factor authentication',
           'Tell your bank if money already moved'],
          'Stop first. Then use a door you chose, not the one they sent.',
          context='You already know [[two-factor authentication|two-factor-authentication]]: a password plus a code.'),
    mc('A code just arrived by text, and the caller wants it. What is it for?',
       ['It lets them into the account', 'It proves they are the bank', 'It cancels the scam'], 0,
       'The code is the key. Reading it aloud hands the key over.'),
    tf('Paying “just this once” so they will stop is a good way to end it.', False,
       'The first payment teaches them you will pay. They ask again.'),
    mc('Money already left the account. Who do you tell first among these?',
       ['Your bank or the payment app', 'The caller, so they can refund you', 'No one, until you are sure'], 0,
       'The bank can sometimes freeze what is left. The caller will not.'),
    fill('Look up the company’s number yourself. Do not use the number in the ___.',
         ['message', 'paycheck', 'glossary'], 0,
         'The message is the trap. The number you find is the exit.'),
])

rosa_story = {
    'title': 'The package that was never stuck',
    'character': 'Rosa, 34, delivery dispatcher',
    'body': 'Rosa is on her break when a text arrives. It uses a shipping logo and says her **$48** package is held. Pay a **$12** “redelivery fee” with a **$100** gift card, or the box goes back.\n\nShe sells nothing online and she did order a **$48** item last week. The logo looks right. The ask does not. Her store’s app, which she opens herself, says the box is on the truck.',
}
rosa = lesson('sc-rosa', 'Rosa’s Fake Delivery', 'The logo was real. The fee was not.', [
    num('How much would the gift card have cost Rosa?', 100, 'The text asks for a $100 gift card.'),
    num('The package itself was $48. How much bigger is the gift card than the fake fee?', 88,
        '$100 − $12 = $88. The fee was the excuse. The card was the theft.'),
    mc('What should Rosa do with the link?',
       ['Ignore it and trust the app she opened herself', 'Pay the $12 so the package moves', 'Send the gift-card code and ask for a receipt'], 0,
       'The app she opened is the real status. The text is the pitch.'),
    tf('A real carrier asks you to pay a redelivery fee with a gift card.', False,
       'Gift cards are a scammer’s payment rail.'),
    mc('Which lever did the text use hardest?',
       ['Urgency: pay now or lose the box', 'A paper statement', 'A lower deductible'], 0,
       'The deadline is fake. The package was already coming.'),
], fmt='story', story=rosa_story)

trial_steps = [
    mc('Which ask is a scam’s favorite payment?',
       ['Gift cards or a wire to a stranger', 'A bill you already pay each month', 'A debit card at the store you are standing in'], 0,
       'The payment you cannot undo is the one they want.'),
    tf('Knowing the last four digits of your account proves the caller is your bank.', False,
       'Those digits are not a secret.'),
    num('A phishing text wants two $50 gift cards. How much is that?', 100, '$50 × 2 = $100.'),
    mc('You think a call was a scam. What is the first move?',
       ['Stop, and do not read them any code', 'Stay on the line until they are satisfied', 'Send a small payment to test them'], 0,
       'The code is the key. Keep it.'),
]

lessons = [how, phish, spot, calls, romance, flags, hour, rosa,
           review('sc'), trial('sc', 'Scams & Fraud', trial_steps)]
write_unit('01-scams.json', 'scams', 1, 'Scams & Fraud',
           'Urgency, fake authority, and payments you cannot undo.',
           'The costume changes. The hurry does not.', terms, lessons, section=S)
