from lib import *

S = 'home-life'
terms = {
    'lease': term('Lease',
                  'The contract that says how long you can live there, what you pay, and what you and the landlord each must do.',
                  'A 12-month lease at $1,150 a month, with a $1,150 security deposit due at signing.'),
    'security-deposit': term('Security deposit',
                             'Money you pay up front that the landlord holds against unpaid rent or damage beyond ordinary wear. The unused part should come back.',
                             'A $1,150 deposit. $200 of real damage is kept. $950 comes back.'),
}

afford = lesson('rn-afford', 'How Much Rent', 'A sketch, not a law: about 30% of gross pay.', [
    info('The 30% sketch',
         'Gross pay is your pay before taxes. A common sketch says housing should stay near **30%** of that.\n\nOn **$4,000** of gross pay, 30% is **$1,200**. It is a warning light, not a rule that fits every city.'),
    num('Gross pay is $4,000. What is 30% of it?', 1200, '$4,000 × 0.30 = $1,200.'),
    num('The listing is $1,350 and your 30% sketch is $1,200. How far over is the listing?', 150,
        '$1,350 − $1,200 = $150.'),
    num('Gross pay is $3,000. What is 30% of it?', 900, '$3,000 × 0.30 = $900.'),
    tf('The 30% sketch is a law that caps every renter’s rent.', False,
       'It is a rule of thumb. Your city, your debts, and your other bills can push the real number lower.'),
])

listing = lesson('rn-listing', 'Read the Listing', 'The rent line is not the whole month.', [
    info('What the ad leaves out',
         'A listing can show the rent and skip the power bill, the fee to apply, and the parking.\n\nRent **$1,350**. The electric estimate is **$90**. The application fee is **$40**.'),
    num('Rent is $1,350 and electric is about $90. What is a truer monthly cost?', 1440,
        '$1,350 + $90 = $1,440.'),
    num('That $1,440 monthly cost is how far over a $1,200 sketch?', 240,
        '$1,440 − $1,200 = $240.'),
    mc('The ad says “utilities not included.” What does that mean for your budget?',
       ['You add the power, heat, and internet on top of the rent', 'The landlord pays every bill', 'The rent already includes electric'], 0,
       '“Not included” means those bills are still yours.'),
    tf('An application fee is the same thing as a security deposit.', False,
       'The fee pays for the screening. You do not get it back. A deposit is held against damage or unpaid rent.'),
])

fees = lesson('rn-fees', 'Fees and Screening', 'Each application can ask for a fee and a credit check.', [
    mc('What is an application fee usually paying for?',
       ['The screening, such as a credit check', 'Your security deposit', 'The first month of rent'], 0,
       'It is the cost of looking at you. It is not rent, and it usually does not come back.',
       context='A landlord may check your [[credit score]] before offering a lease.'),
    num('Each application costs $40. You apply to 3 places. What do the fees add up to?', 120,
        '$40 × 3 = $120.'),
    num('You apply to 2 places at $40 each, and only one says yes. How much of those fees comes back?', 0,
        'Application fees are spent either way. $40 × 2 = $80, and $0 of it returns.'),
    mc('A screening looks at your credit. What is the careful move before you apply everywhere?',
       ['Apply where you would actually live, so you do not pay fee after fee', 'Apply to ten places the same day', 'Pay a company that promises to hide your credit'], 0,
       'Each fee is real money. Start with the places that fit the budget.'),
    tf('A landlord who checks your credit is always running a scam.', False,
       'A credit check is a normal part of many rentals. The scam version is a stranger who wants the fee with no real apartment.'),
])

lease_doc = doc('statement', 'Move-in charges', [
    ('rent', 'First month’s rent', 1150),
    ('dep', 'Security deposit', 1150),
    ('pet', 'Pet deposit', 200),
    ('park', 'Parking, first month', 75),
], subtitle='12-month lease', totals=[('Due at signing', 2575, True)])
assert 1150 + 1150 + 200 + 75 == 2575

lease = lesson('rn-lease', 'Read the Lease', 'The cash due at signing is more than one month.', [
    info('What you are signing',
         'A [[lease]] is the contract: the rent, the length, and the rules. The [[security deposit]] is the cash they hold against damage, not this month’s rent.\n\nThis one is 12 months. The monthly rent is **$1,150**. The page below is what they want before you get the keys.'),
    num('How much is due at signing on this page?', 2575,
        '$1,150 + $1,150 + $200 + $75 = $2,575.', doc=lease_doc),
    num('After the first month, the pet deposit and the security deposit are not monthly bills. What is rent plus parking?', 1225,
        '$1,150 + $75 = $1,225.', doc=lease_doc),
    mc('Which line is held against damage, not spent as this month’s rent?',
       ['Security deposit', 'First month’s rent', 'Parking, first month'], 0,
       'A [[security deposit]] comes back if the rent is paid and the damage is only ordinary wear.',
       doc=lease_doc),
    tf('Once you sign, the rent on this lease can change next month because the landlord feels like it.', False,
       'A fixed-term lease holds the rent for the term. A raise waits for a renewal, unless the lease itself says otherwise.'),
], fmt='document')

deposit = lesson('rn-deposit', 'Get the Deposit Back', 'Photos and a clean place do the work.', [
    info('Ordinary wear is not a bill',
         'The [[security deposit]] covers unpaid rent and damage past ordinary wear. Scuffs from a chair are wear. A hole in the door is damage.\n\nPhotograph every room when you move in and when you move out.'),
    num('The deposit is $1,150. The landlord keeps $200 for a broken door. How much should come back?', 950,
        '$1,150 − $200 = $950.'),
    num('The deposit is $1,150 and the place is clean, with only ordinary wear. How much should come back?', 1150,
        'Nothing was damaged and the rent was paid, so the whole $1,150 comes back.'),
    mc('What helps you if the landlord keeps too much?',
       ['Move-in and move-out photos, plus the written list of damages', 'A verbal promise that they will “take care of it”', 'Paying the next tenant’s fee'], 0,
       'The photos show the condition. The list shows what they charged.'),
    tf('A landlord may keep the deposit for ordinary wear and tear.', False,
       'Ordinary wear is the cost of having a tenant. The deposit is for damage and unpaid rent.'),
])

rights = lesson('rn-rights', 'Who Does What', 'The lease splits the jobs. Local rules add more.', [
    info('Read yours, then your city',
         'A lease says who fixes what, how much notice a visit needs, and when the rent is late.\n\nCities and states add their own rules. This sort is the usual split, not a law degree.'),
    sort('Sort each job.',
         ['Yours', 'The landlord’s'],
         [('Pay the rent on the date in the lease', 0),
          ('Keep the heat and the plumbing working', 1),
          ('Give notice before a non-emergency visit', 1),
          ('Report a leak in writing', 0)],
         'You pay and you report. They maintain the building and they do not walk in unannounced for a casual look.'),
    mc('The heat fails in January. What is the useful first step?',
       ['Tell the landlord in writing and keep a copy', 'Stop paying rent that day with no record', 'Fix it and never mention it'], 0,
       'A written report starts the clock and gives you a record.'),
    tf('You can be asked to pay the rent even while you are waiting on a repair.', True,
       'A repair dispute and the rent are often separate. Skipping rent can put you in breach. Ask a local tenant office before you withhold anything.'),
    fill('A visit that is not an emergency should come with ___ first.',
         ['notice', 'a new deposit', 'a guest fee'], 0,
         'Notice is the usual rule. The lease, and your city, say how much.'),
], fmt='sort')

bad = doc('statement', 'Clause to question', [
    ('rent', 'Monthly rent', 1400),
    ('last', 'Last month’s rent, due now', 1400),
    ('bad', 'Nonrefundable “security deposit”', 1400),
    ('park', 'Parking', 50),
])
spot = lesson('rn-spot', 'A Bad Clause', 'A deposit you can never see again is a fee with a nicer name.', [
    info('Read the words next to the dollar',
         'A real [[security deposit]] is held and then returned, minus real damage. A line that says nonrefundable is not that.\n\nOn this page, one line uses the word deposit and then takes the money for good.'),
    spot('Which line is the clause to question before you sign?', bad, 'bad',
         'Nonrefundable means it does not come back. That is a fee, not a deposit you can recover.'),
    num('If you treat that nonrefundable line as gone, how much of the $1,400 will you not see again?', 1400,
        'The line itself says it does not come back. All $1,400 of it is spent.'),
    mc('What should you do with a clause like that?',
       ['Ask to have it changed, or walk away', 'Sign fast so nobody else takes the apartment', 'Pay it and call it a deposit anyway'], 0,
       'The time to argue is before your name is on the lease.'),
    tf('Adding the word “deposit” makes a nonrefundable fee refundable.', False,
       'The word nonrefundable is the part that matters. A deposit you cannot get back is a fee.'),
], fmt='spot')

kayla_story = {
    'title': 'Kayla’s first lease',
    'character': 'Kayla, 26',
    'body': 'Kayla is 26. She is a medical receptionist, and her gross pay is **$4,000** a month. A common rent sketch is 30% of that, which is **$1,200**.\n\nShe finds a one-bedroom for **$1,150**. Two applications cost **$40** each. The lease wants the first month and a **$1,150** [[security deposit]] at signing.\n\nShe has **$2,500** saved for the move. The fees, the first month, and the deposit use almost all of it.',
}
kayla = lesson('rn-kayla', 'Kayla’s First Lease', 'The rent fits. The cash at the door is the hard part.', [
    num('What is 30% of Kayla’s $4,000 gross pay?', 1200, '$4,000 × 0.30 = $1,200.'),
    num('Her rent is $1,150. How much under that $1,200 sketch is she?', 50,
        '$1,200 − $1,150 = $50.'),
    num('Two applications at $40. What do the fees cost?', 80, '$40 × 2 = $80.'),
    num('She has $2,500. Fees are $80. First month and deposit are $1,150 + $1,150. How much is left?', 120,
        '$2,500 − $80 − $1,150 − $1,150 = $120.'),
    mc('The place at $1,150 fits the sketch, and a nicer one would empty her savings. What fits this story?',
       ['Take the $1,150 lease and keep the $120 as a thin cushion', 'Spend the cushion on a higher rent the same day', 'Skip the deposit because she likes the place'], 0,
       'The rent is inside the sketch. The $120 is all that stands between her and an empty account.'),
], fmt='story', story=kayla_story)

trial_steps = [
    num('Gross pay is $5,000. What is 30% of it, as a rent sketch?', 1500, '$5,000 × 0.30 = $1,500.'),
    mc('Which payment usually comes back if you leave the place undamaged?',
       ['The security deposit', 'The application fee', 'A nonrefundable move-in fee'], 0,
       'A deposit is held. A fee is spent.'),
    tf('“Utilities not included” means you can ignore the power bill.', False,
       'It means the power bill is extra.'),
    num('A $1,200 deposit has $300 of damage kept back. How much comes back?', 900,
        '$1,200 − $300 = $900.'),
]

lessons = [afford, listing, fees, lease, deposit, rights, spot, kayla,
           review('rn'), trial('rn', 'Renting', trial_steps)]
write_unit('01-renting.json', 'renting', 1, 'Renting',
           'What you can afford, what the lease actually says, and how to get the deposit back.',
           'The rent is the headline. The cash at signing is the story.', terms, lessons, section=S)
