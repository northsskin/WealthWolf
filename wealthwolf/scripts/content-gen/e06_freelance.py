from lib import *

S = 'earning'
terms = {
    'freelancer': term('Freelancer', 'Someone who sells their skills to clients, project by project, instead of working for one employer.',
                       'A designer making logos for several small businesses.'),
    'invoice': term('Invoice', 'The bill you send a client: what you did, what it costs, and when it’s due.', 'Invoice #0042: $1,290, due Apr 2.'),
    'payment-terms': term('Payment terms', 'The deadline for a client to pay you. “Net 30” means within 30 days of the invoice date.',
                          'Invoiced Mar 3, net 30: due Apr 2.'),
    'business-expense': term('Business expense', 'A cost of running your work, like software, equipment or a website. Many lower the profit you’re taxed on.',
                             'A $55 monthly design software subscription.'),
    'estimated-taxes': term('Estimated taxes', 'Tax payments self-employed people make four times a year, since nothing is taken out of their pay.',
                            'Paying the IRS on April 15, June 15, September 15 and January 15.'),
}

what = lesson('fl-what', 'Working for Yourself', 'Freedom, clients, and everything an employer used to handle.', [
    mc('Which is freelancing?', ['Designing logos for several small businesses', 'Working shifts at one store', 'Collecting unemployment'], 0,
       'Many clients, one project at a time.',
       context='A [[freelancer]] sells their skills to clients, project by project, instead of working for one employer.'),
    mc('What does a freelancer handle that an employer usually would?', ['Finding clients, taxes, health insurance and retirement', 'Nothing', 'Only taxes'], 0,
       'You’re the boss, and also the payroll department.'),
    tf('Freelancers can choose which clients and projects to take.', True, 'One of the best parts.'),
    mc('What’s a smart way to start?', ['Alongside a job, with a few clients first', 'Quit with no clients and no savings', 'Work for free forever'], 0,
       'Prove it before you leap.'),
    num('You need $3,000 a month to live and have $9,000 saved. How many months can savings carry you while you build clients?', 3,
        '$9,000 ÷ $3,000 = 3 months.', unit='months'),
    fill('Freelancers are paid by ___, not by an employer’s payroll.', ['clients', 'the government', 'their bank'], 0, 'Every client is a little paycheck.'),
])

rates = lesson('fl-rates', 'Setting Your Rate', 'Work backwards from what you need.', [
    info('Work backwards',
         'Start from what you want to earn in a year, add your business costs, then divide by the hours you can actually bill.\n\n'
         'Not every hour is billable. Finding clients, emails and admin are unpaid.'),
    num('You want $50,000 a year for yourself, plus $5,000 of business costs. How much must you bring in?', 55000, '$50,000 + $5,000 = $55,000.'),
    num('You can bill about 1,100 hours a year. What hourly rate do you need?', 50, '$55,000 ÷ 1,100 = $50 an hour.'),
    mc('Why only 1,100 billable hours, when a full-time year is about 2,080?', ['Much of your time goes to finding clients and admin', 'Freelancers are lazy', 'It’s the law'], 0,
       'Plan for roughly half your hours being unpaid.'),
    num('Raise your rate from $50 to $60 an hour. Over 1,100 hours, how much more do you earn?', 11000, '$10 × 1,100 = $11,000.'),
    tf('Charging too little at the start makes it harder to raise prices later.', True, 'Clients anchor on your first price.'),
])

proj = lesson('fl-hourly-project', 'Hourly or Per Project?', 'Two ways to price the same job.', [
    num('You quote $2,400 for a website project. It takes you 30 hours. What did you earn per hour?', 80, '$2,400 ÷ 30 = $80.',
        context='Hourly means you’re paid for time. Per project means one fixed price for the whole job.'),
    num('It takes 48 hours instead. Per hour now?', 50, '$2,400 ÷ 48 = $50.'),
    mc('Which pricing rewards you for getting faster?', ['Per project', 'Hourly'], 0, 'Finish sooner, earn more per hour.'),
    mc('Which protects you when a client keeps adding changes?', ['Hourly, or a project price with a set number of revisions', 'A vague project price', 'Free work'], 0,
       'Define what’s included.'),
    tf('Writing down exactly what’s included protects both you and the client.', True, 'No surprises on either side.'),
    mc('The client asks for “just one more small thing” for the fifth time. Your move?', ['Point to the agreement and quote the extra work', 'Do it all free', 'Ignore their emails'], 0,
       'Friendly, firm, and in writing.'),
], fmt='call')

inv_lines = [('logo', 'Logo design', 600.00), ('menu', 'Menu layout, 3 pages × $150', 450.00), ('social', 'Social media graphics, 6 × $40', 240.00)]
INV = doc('bill', 'Invoice #0042', inv_lines, subtitle='From: Rosa Diaz Design · To: Sunny Side Bakery',
          meta=[['Issued', 'Mar 3'], ['Due date', 'Apr 2']], totals=[('Total due', total(l[2] for l in inv_lines), True)],
          note='Payment terms: net 30. Late payments add 1.5% a month.')
assert total(l[2] for l in inv_lines) == 1290 and money(1290 * 0.015) == 19.35
invoice = lesson('fl-invoice', 'Send an Invoice', 'The bill that gets you paid.', [
    mc('When is this invoice due?', ['Apr 2', 'Mar 3'], 0, 'The due date, top right.',
       context='An [[invoice]] is the bill you send a client: what you did, what it costs, and when it’s due.', doc=INV),
    num('What’s the total due?', 1290, '$600 + $450 + $240 = $1,290.', doc=INV),
    mc('What does “net 30” mean here?', ['Pay within 30 days of Mar 3', '30% off', 'Pay $30'], 0, 'Mar 3 plus 30 days is Apr 2.',
       context='[[Payment terms]] say when you must be paid. “Net 30” means within 30 days of the invoice date.', doc=INV),
    num('If it’s paid a month late, what’s the 1.5% late fee on $1,290?', 19.35, '$1,290 × 0.015 = $19.35.', doc=INV),
    tf('Number every invoice and keep a copy.', True, 'You’ll need them for taxes and for chasing late payers.'),
    mc('What gets an invoice paid faster?', ['A clear due date and easy ways to pay', 'No due date', 'Sending it months later'], 0, 'Make paying you effortless.'),
], fmt='document')

late = lesson('fl-late-payers', 'When Clients Pay Late', 'Deposits, reminders and a cushion.', [
    mc('What’s the best protection on a big project?', ['A deposit upfront, like 50%', 'Trust', 'Finishing everything first'], 0, 'Half before you start, half when you finish.'),
    num('What’s a 50% deposit on a $2,400 project?', 1200, '$2,400 × 0.50 = $1,200.'),
    order('A client is late. Put your steps in order.', ['Send a friendly reminder', 'Follow up with the invoice and late fee', 'Call them', 'Pause new work until they pay'],
          'Polite, then firmer, then stop working for free.'),
    tf('Clients paying 30 to 60 days after the work means you need savings to cover the gap.', True, 'Your rent doesn’t wait for net 30.'),
    mc('You invoice $4,000 on Mar 31, net 30. When should you expect the money?', ['Around Apr 30', 'Mar 31', 'Next year'], 0, '30 days after the invoice.'),
    mc('A client never pays $800, even after reminders. Last resort?', ['Small claims court, often without a lawyer', 'Post their address online', 'Forget it'], 0,
       'Small claims is built for exactly this.'),
])

exp = lesson('fl-expenses', 'Business Expenses', 'What counts, and why receipts matter.', [
    mc('Which is a business expense for a freelance designer?', ['Design software', 'Netflix', 'Groceries'], 0, 'Used for the work.',
       context='A [[business expense]] is a cost of running your work: software, equipment, a website. Many of them lower the profit you’re taxed on.'),
    sort('Business or personal?', ['Business', 'Personal'],
         [('Laptop used for client work', 0), ('Design software', 0), ('Dinner with friends', 1), ('Website hosting for your portfolio', 0),
          ('Your gym membership', 1), ('Printer ink for client proofs', 0)]),
    num('Income $40,000, business expenses $6,000. What’s the profit?', 34000, '$40,000 − $6,000 = $34,000.'),
    num('Setting aside about 25% of profit for taxes, how much?', 8500, '$34,000 × 0.25 = $8,500.'),
    tf('Keeping receipts for business expenses matters at tax time.', True, 'No receipt, no proof.'),
    mc('What’s the easiest way to keep track?', ['A separate account and card just for business', 'Mixing everything together', 'Cash only'], 0,
       'One account, one clean record.'),
], fmt='sort')

tax = lesson('fl-taxes', 'Quarterly Taxes', 'Four deadlines a year, and how to be ready.', [
    mc('How often are estimated taxes usually paid?', ['Four times a year', 'Once a decade', 'Every day'], 0, 'Quarterly.',
       context='Self-employed people usually pay [[estimated taxes]] four times a year, since nothing is taken out of their pay.'),
    order('Put the estimated tax due dates in order, starting in spring.', ['April 15', 'June 15', 'September 15', 'January 15'],
          'Not quite every three months, so put them in your calendar.'),
    num('You set aside 25% of $2,800 profit each month. How much over a quarter (3 months)?', 2100, '$2,800 × 0.25 × 3 = $2,100.'),
    tf('Missing estimated tax payments can mean penalties.', True, 'Late payments add interest and penalties.'),
    mc('Where should tax money wait until it’s due?', ['In a separate savings account', 'In your spending account', 'In a shoebox'], 0, 'Earning a little interest, out of reach.'),
    mc('Not sure how much to pay?', ['Ask a tax pro or follow the IRS guide. It’s worth it the first year', 'Guess wildly', 'Pay nothing'], 0,
       'The Taxes section of this course goes deeper too.'),
])

rosa_story = {
    'title': 'Year one on her own',
    'character': 'Rosa, 30, graphic designer',
    'body': 'Rosa left her job in January with **$12,000** saved. By December she had billed clients **$58,000**.\n\n'
            'But one client, Bluefin, still owes her **$3,500**. Her business expenses (software, a new laptop, her website) came to **$7,000**. '
            'She set aside **25%** of her profit for taxes.\n\n'
            'Her old job paid **$45,000**, with health insurance and a 401(k) match.',
}
assert 58000 - 3500 == 54500 and 54500 - 7000 == 47500 and 47500 * 0.25 == 11875 and 47500 - 11875 == 35625
rosa = lesson('fl-rosa', 'Rosa’s First Freelance Year', 'More money billed. Is it more money earned?', [
    num('What did Rosa actually collect this year?', 54500, '$58,000 − $3,500 = $54,500.'),
    num('What’s her profit, using what she collected minus $7,000 of expenses?', 47500, '$54,500 − $7,000 = $47,500.'),
    num('25% of profit for taxes?', 11875, '$47,500 × 0.25 = $11,875.'),
    num('What’s left for Rosa to live on?', 35625, '$47,500 − $11,875 = $35,625.'),
    mc('Her old job paid $45,000 with health insurance and a match. Is freelancing paying more yet?',
       ['Not yet: she now covers insurance and retirement herself', 'Yes, much more', 'She’s losing money'], 0,
       'Billing more isn’t the same as keeping more.'),
    mc('What would help most next year?', ['Deposits upfront and a higher rate', 'More unpaid work', 'Spending her savings'], 0,
       'Get paid sooner, and get paid more.'),
], fmt='story', story=rosa_story)

trial_steps = [
    num('3 hours at $75 an hour, plus $50 of stock images, on one invoice. Total?', 275, '3 × $75 + $50 = $275.'),
    mc('What does “net 30” mean?', ['Pay within 30 days of the invoice date', '30% off', 'Pay $30 a month'], 0, '30 days to pay.'),
    tf('Freelancers have taxes taken out of their pay automatically.', False, 'They pay estimated taxes themselves.'),
    num('$3,000 of profit this month. Set aside 25% for taxes. How much?', 750, '$3,000 × 0.25 = $750.'),
]

lessons = [what, rates, proj, invoice, late, exp, tax, rosa, review('fl'), trial('fl', 'Freelancing', trial_steps)]
write_unit('06-freelancing.json', 'freelancing', 6, 'Freelancing Basics', 'Rates, invoices, late payers and quarterly taxes.',
           'When you hunt alone, you carry your own kill. Price accordingly.', terms, lessons, section=S)
