from lib import *

S = 'protecting'
terms = {
    'renters-insurance': term('Renters insurance',
                              'A policy for a renter’s belongings, their liability, and sometimes a hotel if the place cannot be lived in. The landlord’s policy does not cover the renter’s stuff.',
                              'A $192 policy. A fire takes $6,000 of furniture the landlord’s insurance will not replace.'),
    'replacement-cost': term('Replacement cost',
                             'The insurer pays what it costs to buy a similar item new, minus the deductible, instead of what the old item would sell for.',
                             'A stolen laptop costs $1,200 to replace. Replacement cost starts from $1,200, not from a pawn-shop price.'),
    'actual-cash-value': term('Actual cash value',
                              'Replacement cost minus wear and age. The check is for what the used item was worth, not for a new one.',
                              'That $1,200 laptop is worth $400 used. Actual cash value starts from $400.'),
}

why = lesson('hi-why', 'Why Renters Need It', 'The landlord’s policy covers the building. It does not cover your couch.', [
    mc('Whose policy covers a renter’s furniture after a fire?',
       ['The renter’s own policy, if they have one', 'The landlord’s policy, automatically', 'The city’s policy'], 0,
       'The landlord insured the building. The couch was yours.',
       context='[[Renters insurance]] covers your belongings and, typically, your [[liability coverage|liability-coverage]]. The landlord’s policy does not.'),
    tf('If you rent, the landlord’s insurance replaces your clothes after a fire.', False,
       'Their policy is for their building. Your clothes need your policy.'),
    mc('A guest is hurt in your apartment and sues. Which policy is built for that?',
       ['Your renters liability coverage', 'Your auto collision coverage', 'The landlord’s roof coverage'], 0,
       'Liability coverage on a renters policy faces that lawsuit.'),
    num('A renters policy costs $16 a month. What is that per year?', 192, '$16 × 12 = $192.'),
    mc('You own almost nothing expensive. Is that a full reason to skip renters insurance?',
       ['No. Liability and a hotel stay can dwarf the value of the couch', 'Yes. Renters policies only cover jewelry', 'Yes, because landlords must cover guests'], 0,
       'The belongings are only one part. The lawsuit is the other.'),
])

covers = lesson('hi-covers', 'What It Covers', 'Your things, a lawsuit, and a place to sleep.', [
    mc('Which is a usual piece of renters coverage?',
       ['A hotel if the apartment cannot be lived in', 'Flood water from the river', 'The landlord’s roof'], 0,
       'That hotel piece is often called loss of use. Flood is a different policy.',
       context='A typical [[renters insurance]] policy has three jobs: belongings, liability, and extra living costs.'),
    num('The hotel limit is $3,000. Four nights at $150 would be how much?', 600, '$150 × 4 = $600.'),
    num('How much of that $3,000 hotel limit is left after $600?', 2400, '$3,000 − $600 = $2,400.'),
    tf('Renters insurance rebuilds the apartment building.', False,
       'The building is the landlord’s. Your policy is for you.'),
    fill('Loss of use helps pay for a ___ if you cannot stay home.',
         ['hotel', 'new car', 'stock trade'], 0,
         'It is shelter, not a shopping spree.'),
])

value = lesson('hi-value', 'Replacement Cost or Cash Value', 'New price, or used price. The policy picks one.', [
    mc('What is replacement cost?',
       ['What a similar new item costs now', 'What a used item would sell for', 'The deductible'], 0,
       'New for old, minus the deductible.',
       context='[[Replacement cost]] buys a similar new item. [[Actual cash value]] pays the used price.'),
    num('A laptop costs $1,200 to replace and is worth $400 used. How much more does replacement cost start from?', 800,
        '$1,200 − $400 = $800.'),
    num('Replacement cost, $250 deductible. How much do you receive for that laptop?', 950,
        '$1,200 − $250 = $950.'),
    num('Actual cash value, same $250 deductible. How much do you receive?', 150,
        '$400 − $250 = $150.'),
    tf('Actual cash value and replacement cost pay the same check.', False,
       'Age comes out of actual cash value. That is the gap.'),
])

pol_lines = [
    ('stuff', 'Belongings limit', 15000),
    ('liab', 'Liability coverage limit', 100000),
    ('use', 'Loss of use limit', 3000),
    ('prem', 'Premium for the year', 192),
]
POL = doc('statement', 'Renters policy', pol_lines, subtitle='Declarations',
          meta=[('Deductible', '$250'), ('Belongings', 'Replacement cost')],
          note='Flood is not in this policy.')
page = lesson('hi-page', 'Reading the Policy', 'Four lines. Know which loss each one answers.', [
    num('What is the belongings limit?', 15000, 'That line says $15,000.',
        context='Match the loss to the line. A lawsuit is not the belongings limit.', doc=POL),
    num('What is the liability limit?', 100000, 'That line says $100,000.', doc=POL),
    num('The yearly premium is $192. What is that per month?', 16, '$192 ÷ 12 = $16.', doc=POL),
    mc('A guest sues for $40,000. Which line is the one that applies?',
       ['Liability coverage, $100,000', 'Belongings, $15,000', 'The $192 premium'], 0,
       'A lawsuit is liability. $40,000 is under the $100,000 limit.'),
    tf('This page includes flood coverage because the note says flood is not in the policy.', False,
       'The note is the warning. Flood is absent.'),
], fmt='document')

floods = lesson('hi-floods', 'Floods and Earthquakes', 'The usual policy has a hole where the water and the ground are.', [
    sort('Usually in a standard home or renters policy, or a separate policy?',
         ['Usually included', 'Needs its own policy'],
         [('Theft of a laptop', 0),
          ('A kitchen fire', 0),
          ('A river flood', 1),
          ('An earthquake', 1),
          ('Wind that tears off roof shingles', 0)],
         'Flood and earthquake are the famous holes. Fire, theft, and wind are the usual yes.',
         context='An [[exclusion]] is a loss the main policy will not pay. Flood and earthquake are classic ones.'),
    tf('A standard renters policy quietly includes river flood.', False,
       'Flood is sold separately. The summary will not sneak it in.'),
    mc('You live where hurricanes push water into streets. What do you ask?',
       ['Whether you need a separate flood policy', 'Whether collision coverage handles a flood', 'Whether the deductible disappears in a storm'], 0,
       'Name the water. Then see if this policy even speaks to it.'),
    mc('An earthquake policy is separate. Your standard policy excludes earthquakes. The ground shakes and breaks the dishes. What pays?',
       ['Only the earthquake policy, if you bought it', 'The standard policy, because dishes are belongings', 'Auto comprehensive'], 0,
       'The cause is the earthquake. The exclusion follows the cause.'),
    fill('Flood and earthquake usually need ___ policy.',
         ['their own', 'no', 'an auto'], 0,
         'The main contract stepped aside.'),
], fmt='sort')

inventory = lesson('hi-inventory', 'A Home Inventory', 'After a fire you will not remember the blender.', [
    info('Write it down before you need it',
         'A home inventory is a list of what you own, with photos and roughly what it cost.\n\nKeep a copy outside the apartment. A list that burns with the couch cannot replace the couch.'),
    mc('Why make the list before a loss?',
       ['After a fire you will not remember every item or its price', 'The insurer writes the list for you', 'Lists lower the deductible to zero'], 0,
       'Memory is a bad filing cabinet.'),
    num('You list a bike at $450, a laptop at $1,200, and a bed at $800. What is the total?', 2450,
        '$450 + $1,200 + $800 = $2,450.'),
    tf('The only copy of the inventory should live in the apartment it describes.', False,
       'Store a copy somewhere the fire cannot reach.'),
    mc('What belongs on the list besides the name of the item?',
       ['A photo and about what it cost', 'Your Social Security number', 'Your bank password'], 0,
       'The photo and the price help the claim. The password helps a thief.'),
])

home = lesson('hi-home', 'Home Insurance Basics', 'Owners insure the building and the things inside it.', [
    mc('How is a home policy different from a renters policy?',
       ['It also helps rebuild the building you own', 'It only covers cars in the driveway', 'It replaces flood for free'], 0,
       'You own the walls, so the policy has to know about the walls.',
       context='Home insurance is the owner’s version: the building, the belongings, liability, and often extra living costs.'),
    tf('Owning a home means flood is included automatically.', False,
       'Flood is still usually separate. Owning the house does not close that hole.'),
    num('A dwelling limit is $250,000. A rebuild estimate is $310,000. How much of the estimate is above the limit?', 60000,
        '$310,000 − $250,000 = $60,000.'),
    mc('Why compare the dwelling limit to a rebuild estimate?',
       ['The limit, not the sale price, is what the insurer will pay toward rebuilding', 'The sale price is always the limit', 'A higher sale price lowers the premium to zero'], 0,
       'You insure the cost to rebuild, not the price a buyer would pay for the land.'),
    fill('The dwelling limit needs to cover the cost to ___, not only the price you paid.',
         ['rebuild', 'decorate', 'advertise'], 0,
         'Lumber and labor set that number.'),
])

priya_story = {
    'title': 'The night the hallway filled with smoke',
    'character': 'Priya, 26, graphic designer',
    'body': 'A fire two floors down fills Priya’s apartment with smoke. She rents. Her landlord’s insurer will look at the building. Her couch, her clothes, and her laptop are hers.\n\nHer renters policy uses replacement cost. Belongings come to **$6,000**. Four hotel nights at **$150** come to **$600**. The deductible is **$500**.',
}
priya = lesson('hi-priya', 'Priya’s Apartment Fire', 'The building was the landlord’s. The laptop was hers.', [
    num('What do the hotel nights cost?', 600, '$150 × 4 = $600.'),
    num('Belongings plus hotel, before the deductible. What is the total?', 6600,
        '$6,000 + $600 = $6,600.'),
    num('After the $500 deductible, how much does the policy pay if both losses are covered?', 6100,
        '$6,600 − $500 = $6,100.'),
    mc('Why doesn’t the landlord’s policy write that check?',
       ['It covers the building, not her belongings', 'Renters are banned from filing claims', 'Smoke is an exclusion on every policy'], 0,
       'Different owner, different policy.'),
    tf('She should keep the hotel receipts.', True,
       'Loss of use is paid from proof, not from memory.'),
], fmt='story', story=priya_story)

trial_steps = [
    mc('A renter’s clothes burn. Whose policy is supposed to cover the clothes?',
       ['The renter’s policy', 'The landlord’s building policy', 'The neighbor’s auto policy'], 0,
       'The clothes were not part of the building.'),
    num('Replacement cost $900. Actual cash value $300. How much bigger is replacement cost?', 600,
        '$900 − $300 = $600.'),
    tf('A standard renters policy includes earthquake coverage.', False,
       'Earthquake is a separate policy.'),
    num('Loss of use limit $2,000. You spend $1,250 on a hotel. How much of the limit is left?', 750,
        '$2,000 − $1,250 = $750.'),
]

lessons = [why, covers, value, page, floods, inventory, home, priya,
           review('hi'), trial('hi', 'Renters & Home', trial_steps)]
write_unit('05-home-insurance.json', 'home-insurance', 5, 'Renters & Home Insurance',
           'Your belongings, the building if you own it, and the disasters a standard policy skips.',
           'The landlord insured the walls. You insure what is inside them.', terms, lessons, section=S)
