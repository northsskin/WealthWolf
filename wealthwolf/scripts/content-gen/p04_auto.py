from lib import *

S = 'protecting'
terms = {
    'liability-coverage': term('Liability coverage',
                               'Auto insurance that pays others when you cause their injuries or damage. It does not fix your own car.',
                               'You cause a crash. Liability coverage helps pay the other driver’s medical bills, up to the limit.'),
    'collision-coverage': term('Collision coverage',
                               'Pays to repair your car after a crash with another car or object, after your deductible.',
                               'A $1,800 repair and a $500 collision deductible: you pay $500, collision pays $1,300.'),
    'comprehensive-coverage': term('Comprehensive coverage',
                                   'Pays for your car from something other than a crash, such as theft, hail, or a broken windshield, after the deductible.',
                                   'Hail dents the hood. Comprehensive is the coverage that fits, not collision.'),
    'uninsured-motorist': term('Uninsured motorist coverage',
                               'Pays you when a driver who has little or no insurance hurts you or, on many policies, your car.',
                               'The other driver has no insurance and a $9,000 hospital bill is yours. This coverage is built for that gap.'),
}

kinds = lesson('ai-kinds', 'Three Kinds of Coverage', 'One pays them. One fixes your crash. One covers the hail.', [
    sort('Which coverage fits?',
         ['Liability coverage', 'Collision', 'Comprehensive'],
         [('You injure another driver', 0),
          ('You hit a fence and dent your own car', 1),
          ('Someone steals your car', 2),
          ('Hail ruins the roof of your car', 2),
          ('You cause damage to another person’s car', 0)],
         'Liability pays them. Collision fixes a crash. Comprehensive covers theft, hail, and similar losses.',
         context='[[Liability coverage|liability-coverage]] pays other people. [[Collision coverage]] fixes your car after a crash. [[Comprehensive coverage]] covers theft, hail, and a lot of non-crash damage.'),
    mc('Collision coverage pays to fix whose car after you hit a pole?',
       ['Yours, after the deductible', 'The pole’s owner only', 'Nobody. Poles are excluded from every policy'], 0,
       'The pole is an object. Collision is the crash coverage for your car.'),
    tf('Liability coverage repairs your own bumper.', False,
       'Liability faces outward. Your bumper is collision, if you bought it.'),
    mc('A tree branch smashes the windshield in a storm. Which coverage is the usual fit?',
       ['Comprehensive', 'Liability coverage', 'A renters policy'], 0,
       'It is not a crash with a vehicle. Comprehensive is the one to check.'),
    fill('Coverage that pays other people you hurt is ___ coverage.',
         ['liability', 'collision', 'comprehensive'], 0,
         'Their injuries and their car. Not your own paint.'),
], fmt='sort')

minimums = lesson('ai-minimums', 'State Minimums', 'Legal and enough are not the same word.', [
    info('The floor is not the roof',
         'Every state sets a legal minimum for auto liability. Drive below it and you can be breaking the law.\n\nThat minimum is often far too small for a serious injury. A hospital bill can pass the legal floor in an afternoon. The rest can land on you.'),
    mc('What is a state minimum?',
       ['The least liability the law lets you drive with', 'The most any crash can cost', 'The price of collision coverage'], 0,
       'It is a legal floor, not a guess at a real injury.'),
    tf('Meeting the legal minimum means a serious injury will always be fully covered.', False,
       'The law’s floor and a hospital’s bill are set by different people.'),
    mc('You cause a crash. Medical bills for the other driver run past your liability limit. Who is exposed to the rest?',
       ['You are', 'The state, automatically', 'No one. Bills stop at the minimum'], 0,
       'The limit is a ceiling on the insurer, not on the injury.'),
    mc('Why do people buy more than the minimum?',
       ['A serious injury costs more than the legal floor', 'The state pays you a bonus for it', 'Collision is illegal at the minimum'], 0,
       'The extra limit is there for the bill the floor cannot hold.'),
])

um = lesson('ai-uninsured', 'Uninsured Drivers', 'Their missing policy can become your bill.', [
    mc('What is uninsured motorist coverage for?',
       ['When another driver has little or no insurance and hurts you', 'When you want a cheaper premium', 'When your own car needs an oil change'], 0,
       'It fills the hole their missing policy left.',
       context='[[Uninsured motorist coverage|uninsured-motorist]] pays you when the other driver cannot.'),
    tf('If the other driver has no insurance, your liability coverage pays your hospital bill.', False,
       'Liability pays people you hurt. It does not pay you.'),
    mc('You are hurt. The other driver is uninsured. Which coverage do you look at on your own policy?',
       ['Uninsured motorist', 'Only your collision deductible', 'A life insurance beneficiary form'], 0,
       'This is the coverage built for their empty policy.'),
    mc('Why does this coverage exist?',
       ['Plenty of drivers are on the road with little or no insurance', 'It replaces state inspection', 'It pays your parking tickets'], 0,
       'You cannot control what they bought. You can buy a backstop.'),
    fill('Uninsured motorist coverage responds when the other driver has too ___ insurance.',
         ['little', 'much', 'new'], 0,
         'Their gap becomes your problem unless you covered it.'),
])

price = lesson('ai-price', 'What Changes the Price', 'The car, the driver, the miles, and the deductible.', [
    mc('Which change often raises an auto premium?',
       ['A recent at-fault crash', 'Parking in a legal spot', 'Reading the policy'], 0,
       'The insurer prices the risk it thinks you bring.'),
    tf('A higher deductible usually means a higher premium.', False,
       'You take more of the loss, so the premium often drops. You felt this trade on other policies.'),
    mc('Which is a lever you can actually pull?',
       ['The deductible, the car you drive, and how much you drive', 'The weather in your state', 'Other people’s crashes'], 0,
       'You do not control the pool. You do control the car and the deductible.'),
    mc('Why might a sports car cost more to insure than a used sedan?',
       ['It costs more to repair and may be stolen more often', 'Sedans are illegal to insure', 'Sports cars are exempt from liability'], 0,
       'Price follows the size of the possible claim.'),
    num('Quote A is $140 a month. Quote B is $95. How much less is B per month?', 45,
        '$140 − $95 = $45.'),
])

a_lines = [
    ('prem', 'Premium for the year', 1560),
    ('ded', 'Collision deductible', 500),
]
b_lines = [
    ('prem', 'Premium for the year', 1080),
    ('ded', 'Collision deductible', 1000),
]
assert 1560 - 1080 == 480
QUOTE_A = doc('statement', 'Quote A', a_lines, subtitle='Same liability limits')
QUOTE_B = doc('statement', 'Quote B', b_lines, subtitle='Same liability limits')
quotes = lesson('ai-quotes', 'Two Quotes', 'The cheaper year can mean a bigger deductible.', [
    num('What is Quote A’s yearly premium?', 1560, 'The premium line is $1,560.',
        context='Same liability limits. The premium and the collision deductible are what moved.',
        docs=[QUOTE_A, QUOTE_B]),
    num('How much less is Quote B’s yearly premium?', 480, '$1,560 − $1,080 = $480.', docs=[QUOTE_A, QUOTE_B]),
    num('A $2,000 crash repair. Using Quote A, how much of the repair do you pay as the deductible?', 500,
        'Quote A’s collision deductible is $500.', docs=[QUOTE_A, QUOTE_B]),
    num('Using Quote B, how much of that same $2,000 repair do you pay?', 1000,
        'Quote B’s deductible is $1,000.', docs=[QUOTE_A, QUOTE_B]),
    mc('You have a solid emergency fund and you want the lower yearly price. Which quote fits that preference?',
       ['Quote B', 'Quote A', 'Neither. The premiums match'], 0,
       'B saves $480 a year and asks you to hold a $1,000 deductible.',
       why=['$1,080 is the lower premium.', 'A is the lower deductible, not the lower premium.', 'They differ by $480.']),
    tf('The lower premium is the whole comparison.', False,
       'The deductible moved too. Read both lines.'),
], fmt='call')

after = lesson('ai-after', 'After a Crash', 'Help first. Then the record. Then the insurers.', [
    order('Put the aftermath in order.',
          ['Check for injuries and call for help if someone is hurt',
           'Move to safety if you can, and call the police when the law or the damage calls for it',
           'Exchange names, insurance, and photos of the cars',
           'Call your insurer and keep the repair estimates'],
          'People first. The record next. Your insurer after you can tell them what happened.'),
    tf('You should leave the scene once you have said sorry, even if someone is hurt.', False,
       'Injuries and the law come before the drive home.'),
    mc('Why photograph both cars?',
       ['The pictures show the damage before it is repaired or forgotten', 'Photos lower your deductible', 'The police require a filter'], 0,
       'The estimate comes later. The photo is from the day.'),
    mc('The other driver asks you to skip insurance and pay them cash tonight. What is the careful move?',
       ['Go through the insurers. A cash deal in the moment is how details disappear', 'Empty your wallet so they will not call', 'Post their license plate and go'], 0,
       'A calm claim beats a roadside bargain.'),
    fill('Exchange insurance information. Do not only exchange ___.',
         ['first names', 'policies', 'photos'], 0,
         'A first name will not pay a repair.'),
])

dec_lines = [
    ('liab', 'Liability coverage limit, per person', 100000),
    ('coll', 'Collision deductible', 500),
    ('comp', 'Comprehensive deductible', 250),
    ('prem', 'Premium for six months', 780),
]
DEC = doc('statement', 'Declarations page', dec_lines, subtitle='Your auto policy',
          meta=[('Car', '2018 sedan'), ('Term', '6 months')],
          note='The declarations page is the cover sheet of what you bought.')
dec = lesson('ai-declarations', 'The Declarations Page', 'This page is the policy in four lines.', [
    num('What is the liability limit per person on this page?', 100000,
        'That line says $100,000.',
        context='The declarations page lists the limits and deductibles you actually bought.', doc=DEC),
    num('What is the collision deductible?', 500, 'The collision line says $500.', doc=DEC),
    num('What is the comprehensive deductible?', 250, 'That line says $250.', doc=DEC),
    num('The six-month premium is $780. What is that per month?', 130, '$780 ÷ 6 = $130.', doc=DEC),
    tf('The declarations page is a bill for a crash you already had.', False,
       'It is the summary of the coverage you bought, before a crash.'),
], fmt='document')

theo_story = {
    'title': 'The parking-lot bumper',
    'character': 'Theo, 28, night-shift nurse',
    'body': 'Theo backs into a pole in the hospital garage. The bumper repair is **$1,800**. His collision deductible is **$500**. Nobody else is hurt, and no other car is involved.\n\nHis six-month premium was **$780**. He wants the car fixed before his next stretch of shifts.',
}
theo = lesson('ai-theo', 'Theo’s Fender-Bender', 'The pole does not file a claim. His collision coverage does.', [
    num('How much of the $1,800 repair does Theo pay as the deductible?', 500,
        'The collision deductible is $500.'),
    num('How much does collision coverage pay?', 1300, '$1,800 − $500 = $1,300.'),
    mc('Which coverage pays his bumper?',
       ['Collision', 'Liability coverage', 'Uninsured motorist'], 0,
       'He hit an object. That is collision, not a payment to another person.'),
    tf('Liability coverage is what fixes Theo’s bumper.', False,
       'Liability would matter if he had hurt someone else.'),
    mc('He has the $500 in savings. What is the sensible use of it here?',
       ['Pay the deductible and let collision cover the other $1,300', 'Skip insurance and put the $1,800 on a credit card', 'Ask the pole’s owner to pay'], 0,
       'The deductible is the part he agreed to hold.'),
], fmt='story', story=theo_story)

trial_steps = [
    mc('Hail destroys the hood. Which coverage do you look at?',
       ['Comprehensive', 'Liability coverage', 'The state minimum only'], 0,
       'Hail is not a crash and it is not a payment to another person.'),
    num('A repair is $2,400. The collision deductible is $400. How much does insurance pay?', 2000,
        '$2,400 − $400 = $2,000.'),
    tf('The legal minimum is always enough for a serious injury.', False,
       'It is a legal floor. Hospital bills do not stop there.'),
    mc('After a crash, what comes before arguing about fault?',
       ['Checking for injuries and getting help', 'Posting a video', 'Shopping for a new deductible'], 0,
       'People first.'),
]

lessons = [kinds, minimums, um, price, quotes, after, dec, theo,
           review('ai'), trial('ai', 'Auto Insurance', trial_steps)]
write_unit('04-auto-insurance.json', 'auto-insurance', 4, 'Auto Insurance',
           'Liability, collision, comprehensive, and the quote behind the monthly price.',
           'The legal minimum is a floor. Injury does not care.', terms, lessons, section=S)
