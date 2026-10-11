from lib import *

S = 'earning'
terms = {
    'offer-letter': term('Offer letter', 'The written job offer: title, pay, start date and benefits.', 'Patient Coordinator, $54,000, start Jan 6.'),
    'base-salary': term('Base salary', 'Your yearly pay before any bonuses or benefits.', 'A $54,000 base salary plus a $2,000 signing bonus.'),
    'total-compensation': term('Total compensation', 'Everything a job pays you in a year: base salary, bonuses and the value of benefits.',
                               '$54,000 salary + $2,000 bonus + $7,620 of benefits = $63,620.'),
    'salary-range': term('Salary range', 'The low-to-high pay a company expects to offer for a role.', 'Posted range: $48,000–$58,000.'),
    'counteroffer': term('Counteroffer', 'Your polite reply to a job offer asking for more: higher pay, a bonus or more time off.',
                         '“I’m excited to join. Based on my research, could we do $56,000?”'),
    'signing-bonus': term('Signing bonus', 'A one-time payment for accepting a job offer, often with a payback rule if you leave early.',
                          '$3,000 when you start, repaid if you leave within a year.'),
}

OFFER = doc('bill', 'Harbor Health', [
    ('base', 'Base salary, yearly', 54000.00), ('bonus', 'Signing bonus, paid once', 2000.00),
    ('match', '401(k) match: 100% of the first 3% you save', 1620.00), ('health', 'Health insurance, employer share', 6000.00)],
    subtitle='Offer letter · Patient Coordinator', meta=[['Start date', 'Jan 6'], ['Please reply by', 'Dec 15']])
letter = lesson('jo-offer-letter', 'Reading an Offer Letter', 'Before you say yes, read every line.', [
    mc('What’s the base salary in this offer?', ['$54,000', '$56,000', '$63,620'], 0, 'The yearly pay, before the bonus and benefits.',
       context='An [[offer letter]] is the written job offer: title, pay, start date and benefits. Your [[base salary]] is the yearly pay before bonuses or benefits.',
       doc=OFFER),
    num('The signing bonus is paid once. Base salary plus signing bonus: how much cash in the first year?', 56000, '$54,000 + $2,000 = $56,000.', doc=OFFER),
    mc('When do you need to reply?', ['By Dec 15', 'On your first day', 'Never, it’s automatic'], 0, 'Offers often have a deadline. Ask for more time if you need it.', doc=OFFER),
    tf('Get the offer in writing before you quit your current job.', True, 'A phone promise isn’t an offer.'),
    mc('Something in the letter differs from what they said on the phone. What do you do?',
       ['Ask them to fix it in writing before you sign', 'Sign now and sort it out later', 'Ignore it'], 0, 'What’s written is what counts.'),
    num('They match 100% of the first 3% you save. If you only save 1% of $54,000, what’s the match?', 540, '$54,000 × 0.01 = $540.', doc=OFFER),
], fmt='document')

total_comp = lesson('jo-total-comp', 'Total Compensation', 'The real size of an offer is more than the salary.', [
    mc('Which counts toward total compensation?', ['Salary, bonus and the employer’s share of benefits', 'Only salary', 'Only take-home pay'], 0,
       'Everything the job pays you, in cash or in benefits.',
       context='[[Total compensation]] is everything a job pays you in a year: base salary, bonuses, and the value of benefits.'),
    num('Base $54,000, bonus $2,000, 401(k) match $1,620, health insurance employer share $6,000. What’s the total compensation?', 63620,
        '$54,000 + $2,000 + $1,620 + $6,000 = $63,620.'),
    num('Another job offers $58,000, no bonus, no match, and $3,000 toward health insurance. Total compensation?', 61000, '$58,000 + $3,000 = $61,000.'),
    mc('Which offer is worth more?', ['The $54,000 job, at $63,620', 'The $58,000 job, at $61,000'], 0, 'The lower salary wins by $2,620.'),
    tf('The job with the higher salary always pays more overall.', False, 'Benefits can flip it.'),
    mc('What else matters besides total compensation?', ['Commute, schedule, growth and how you’ll be treated', 'Nothing', 'Only the logo'], 0,
       'Money first, but not money only.'),
])

research = lesson('jo-research', 'Know Your Number', 'Research pay before anyone asks what you want.', [
    mc('A posting says $48,000–$58,000. What does that tell you?', ['Where offers for this role will likely land', 'Exactly what you’ll get', 'Nothing'], 0,
       'It’s the company’s planned range.',
       context='A [[salary range]] is the low-to-high pay a company expects for a role. A growing number of states require it in job postings.'),
    mc('Where can you research pay for a role?', ['Postings with ranges, salary sites, and people in the field', 'Guessing', 'Your rent'], 0,
       'Three sources beat one.'),
    num('Range $48,000–$58,000. What’s the middle?', 53000, '($48,000 + $58,000) ÷ 2 = $53,000.'),
    mc('You have 3 years of experience and the role asks for 2. Where in the range should you aim?', ['The upper half', 'The bottom', 'Above the top'], 0,
       'You bring more than they asked for.'),
    tf('Asking “What’s the salary range?” early in the process is reasonable.', True, 'It saves everyone time.'),
    mc('They ask your current salary. What’s a safe answer?', ['Share the range you’re looking for instead', 'Make up a number', 'Refuse to talk'], 0,
       'Many states ban employers from asking about pay history. Either way, keep it about this job.'),
])

CITY = doc('bill', 'Cityline Bank', [('base', 'Base salary', 56000.00), ('health', 'Health insurance, employer share', 5500.00),
                                      ('match', '401(k) match', 2800.00), ('commute', 'Commute, yearly cost to you', -1440.00)],
           subtitle='Offer A · 5 days in the office')
NORTH = doc('bill', 'Northgate Credit Union', [('base', 'Base salary', 52000.00), ('health', 'Health insurance, employer share', 7200.00),
                                                ('match', '401(k) match', 3120.00), ('commute', 'Commute, yearly cost to you', -600.00)],
            subtitle='Offer B · 2 days in the office')
assert 56000 + 5500 + 2800 - 1440 == 62860 and 52000 + 7200 + 3120 - 600 == 61720
two = lesson('jo-two-offers', 'Two Offers', 'Line them up properly, then think about your time.', [
    mc('Adding everything up and subtracting commute costs, which offer is worth more in money?', ['Cityline Bank', 'Northgate Credit Union'], 0,
       'Cityline: $62,860. Northgate: $61,720.', docs=[CITY, NORTH], context='Compare offers on everything: pay, benefits, and what the job costs you.'),
    num('Cityline’s total, after commute costs?', 62860, '$56,000 + $5,500 + $2,800 − $1,440 = $62,860.', docs=[CITY, NORTH]),
    num('Northgate’s total?', 61720, '$52,000 + $7,200 + $3,120 − $600 = $61,720.', docs=[CITY, NORTH]),
    num('How much more is Cityline worth per year?', 1140, '$62,860 − $61,720 = $1,140.'),
    mc('Cityline’s commute eats about 200 more hours a year. What does that tell you?',
       ['That time pays about $5.70 an hour, so Northgate may be the better deal', 'Commute time doesn’t matter', 'Cityline is clearly better'], 0,
       '$1,140 ÷ 200 hours = $5.70 an hour. Less than minimum wage for your time.'),
    tf('The best offer isn’t always the one with the biggest number.', True, 'Time, stress and growth count too.'),
], fmt='call')

negotiate = lesson('jo-negotiate', 'How to Ask for More', 'A polite, specific counteroffer usually helps and rarely hurts.', [
    mc('When do you make a counteroffer?', ['After you get the offer, before you accept', 'After your first year', 'In the first interview'], 0,
       'You have the most leverage between “here’s our offer” and “yes.”',
       context='A [[counteroffer]] is your polite reply asking for more: a higher salary, a bonus, more time off.'),
    order('Put a negotiation in order.',
          ['Thank them and say you’re excited', 'Ask for a specific number, backed by research', 'Listen, and let them answer', 'Get the final offer in writing'],
          'Warm, specific, patient, written.'),
    num('The offer is $52,000. You ask for 6% more. What number do you ask for?', 55120, '$52,000 × 1.06 = $55,120.'),
    mc('They say salary is fixed. What else can you ask about?', ['A signing bonus, more PTO or a later start date', 'Nothing', 'Their salary'], 0,
       'Lots of things bend when salary won’t.'),
    tf('Politely negotiating often gets more, and rarely gets an offer taken back.', True, 'Employers expect it.'),
    num('A starting salary $3,000 higher is worth how much over 5 years, even with no other changes?', 15000, '$3,000 × 5 = $15,000.'),
])

bonus = lesson('jo-signing-bonus', 'Bonuses & Fine Print', 'Signing bonuses are nice. Read the strings attached.', [
    mc('What’s a signing bonus?', ['A one-time payment for saying yes', 'A raise every year', 'A tax refund'], 0, 'Once, not every year.',
       context='A [[signing bonus]] is a one-time payment for accepting an offer. It often comes with a catch: leave too soon and you pay it back.'),
    num('A $3,000 signing bonus is taxed at about 30% when it’s paid. What lands in your account?', 2100, '$3,000 × 0.70 = $2,100.'),
    tf('A signing bonus is usually taxed like regular pay.', True, 'It shows up on your W-2 with everything else.'),
    mc('The letter says you repay the bonus if you leave within 12 months. You might move in 8 months. What do you do?',
       ['Factor in that you might pay it back', 'Ignore the fine print', 'Spend it all on day one'], 0, 'Treat it as a loan until month 12.'),
    mc('Bonus or higher salary: which helps more over time?', ['Higher salary: it repeats every year, and raises build on it', 'The bonus', 'Same'], 0,
       'A salary bump keeps paying.'),
    num('A $2,000 one-time bonus vs. a salary $2,000 higher, over 4 years. How much more does the salary bump pay?', 6000, '$8,000 − $2,000 = $6,000.'),
])

SCAM = doc('bill', 'Remote Data Assistant', [('pay', 'Hourly pay, data entry from home', 32.00), ('training', 'Paid training week', 0.00),
                                              ('kit', 'Starter equipment kit, pay by gift card', -149.00), ('start', 'Start: tomorrow, no interview needed', 0.00)],
           subtitle='“Offer” sent by text message')
red = lesson('jo-red-flags', 'Job Scam Red Flags', 'Real jobs pay you. Fake ones make you pay.', [
    spot('Tap the biggest red flag.', SCAM, 'kit', 'Real employers never make you buy equipment, least of all with gift cards.',
         context='Fake job offers are a common scam. Real employers don’t ask you to pay to start.'),
    mc('They mail you a $2,400 check and ask you to deposit it and send back $1,900 for “equipment.” What happens next?',
       ['The check bounces days later, and your $1,900 is gone', 'You keep $500', 'Nothing'], 0, 'Fake checks take days to bounce. Your transfer is instant.'),
    sort('Red flag or normal?', ['Red flag', 'Normal'],
         [('An offer with no interview at all', 0), ('Asked to pay for a kit with gift cards', 0), ('A background check before you start', 1),
          ('Asked for your bank login', 0), ('An offer letter with salary and start date', 1), ('A video interview with the team', 1)]),
    tf('Giving your Social Security number on official new-hire paperwork is normal.', True,
       'After you’ve accepted a real job, tax and work forms need it. Before an interview? No.'),
    mc('How do you check a company is real?', ['Find its official website and phone number yourself', 'Call the number in the suspicious text', 'You can’t'], 0,
       'Never trust contact details from the message itself.'),
    mc('You think you’ve hit a job scam. Where do you report it?', ['The FTC, at ReportFraud.ftc.gov', 'Nowhere', 'Reply to the scammer'], 0,
       'Reports help warn others.'),
], fmt='spot')

nadia_story = {
    'title': 'One email, $5,500',
    'character': 'Nadia, 25, medical billing specialist',
    'body': 'Nadia got an offer for **$50,000**. Before replying, she looked up similar jobs in her city: most paid **$52,000–$60,000**.\n\n'
            'She thanked them, said she was excited, and asked for **$56,000**, pointing to her research and her two years of experience.\n\n'
            'They came back with **$54,000** plus a **$1,500** signing bonus.',
}
nadia = lesson('jo-nadia', 'Nadia’s Negotiation', 'Research, one polite email, and a better offer.', [
    num('How much more base salary did Nadia get than the first offer?', 4000, '$54,000 − $50,000 = $4,000.'),
    num('In her first year, counting the bonus, how much more did she get?', 5500, '$4,000 + $1,500 = $5,500.'),
    num('Over 3 years, ignoring raises, how much more base salary is that?', 12000, '$4,000 × 3 = $12,000.'),
    mc('Why did Nadia ask for $56,000 instead of $54,000?', ['Asking a bit higher leaves room to meet in the middle', 'To be rude', 'At random'], 0,
       'They met her in the middle, right where she hoped.'),
    tf('Nadia’s research made her ask easier to justify.', True, 'Numbers beat feelings in a negotiation.'),
    mc('What should Nadia do before accepting?', ['Get the new salary and bonus in writing', 'Just say yes on the phone', 'Ask for $70,000'], 0,
       'Written, then signed.'),
], fmt='story', story=nadia_story)

trial_steps = [
    num('Base $45,000, bonus $1,000, 401(k) match $1,350, health insurance employer share $5,000. Total compensation?', 52350,
        '$45,000 + $1,000 + $1,350 + $5,000 = $52,350.'),
    mc('You like an offer but want more money. When do you ask?', ['Now, before you accept', 'After a year on the job', 'Never'], 0, 'Between the offer and your yes.'),
    tf('Real employers may ask you to buy equipment with gift cards.', False, 'That’s a scam, every time.'),
    num('The offer is $60,000 and you ask for 5% more. What number do you ask for?', 63000, '$60,000 × 1.05 = $63,000.'),
]

lessons = [letter, total_comp, research, two, negotiate, bonus, red, nadia, review('jo'), trial('jo', 'Job Offers', trial_steps)]
write_unit('03-job-offers.json', 'job-offers', 3, 'Job Offers & Negotiating', 'Read an offer, compare two, and ask for more without flinching.',
           'The first number is an opening, not a verdict.', terms, lessons, section=S)
