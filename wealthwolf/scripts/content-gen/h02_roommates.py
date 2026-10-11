from lib import *

S = 'home-life'
terms = {
    'roommate-agreement': term('Roommate agreement',
                               'A written note of who pays what, who gets which room, and what happens if someone leaves. It sits next to the lease. It does not replace it.',
                               'Rent is $1,800. The larger room pays $1,200. The smaller room pays $600. Electric and internet are split in half.'),
}

move_doc = doc('statement', 'Moving costs', [
    ('truck', 'Truck rental', 180),
    ('boxes', 'Boxes and supplies', 70),
    ('rent', 'First month’s rent', 1600),
    ('dep', 'Security deposit', 1600),
    ('util', 'Utility start-up', 60),
], totals=[('Cash to move', 3510, True)])
assert 180 + 70 + 1600 + 1600 + 60 == 3510

costs = lesson('mv-costs', 'What Moving Costs', 'The truck is the small line.', [
    info('Add the lines',
         'People remember the truck and forget the deposit. On this move the truck is **$180**. The first month and the [[security deposit]] are **$1,600** each.'),
    num('What is the cash to move on this page?', 3510,
        '$180 + $70 + $1,600 + $1,600 + $60 = $3,510.', doc=move_doc),
    num('How much of that $3,510 is the first month plus the deposit?', 3200,
        '$1,600 + $1,600 = $3,200.', doc=move_doc),
    num('How much is the truck, the boxes, and the utility start, added together?', 310,
        '$180 + $70 + $60 = $310.', doc=move_doc),
    tf('The security deposit on this page is a cost you have spent forever.', False,
         'It is held. If you leave the place undamaged and paid up, it should come back.'),
], fmt='document')

rooms = lesson('mv-rooms', 'Split by Room Size', 'The bigger room pays the bigger share.', [
    info('Use the square feet',
         'The rent is **$1,800**. One room is **400** square feet. The other is **200**. Together that is **600**.\n\nThe larger room is 400 ÷ 600 of the rent. The smaller is 200 ÷ 600.'),
    num('What does the 400-square-foot room pay out of $1,800?', 1200,
        '400 ÷ 600 = 2/3. $1,800 × 2/3 = $1,200.'),
    num('What does the 200-square-foot room pay out of $1,800?', 600,
        '200 ÷ 600 = 1/3. $1,800 × 1/3 = $600.'),
    num('Do those two shares add back to the full rent?', 1800,
        '$1,200 + $600 = $1,800.'),
    tf('Splitting every rent bill in half is fair when one room is twice the other.', False,
       'Half and half ignores the size. Here the fair split is $1,200 and $600.'),
])

bills = lesson('mv-bills', 'Shared Bills', 'Write the split down while you still like each other.', [
    info('Rent is not the only bill',
         'Electric is **$90**. Internet is **$60**. Together that is **$150**.\n\nA [[roommate agreement]] says who pays which share, and when. The [[lease]] still makes each signer responsible to the landlord.'),
    num('Electric is $90 and internet is $60. What is the shared-bill total?', 150,
        '$90 + $60 = $150.'),
    num('Two roommates split that $150 in half. What does each pay?', 75,
        '$150 ÷ 2 = $75.'),
    num('If they split the $150 the way they split the rooms, 2/3 and 1/3, what does the larger room pay?', 100,
        '$150 × 2/3 = $100.'),
    mc('The landlord was not in the room when you agreed. Who can the landlord still ask for the full rent?',
       ['Anyone who signed the lease', 'Only the roommate who took the bigger room', 'Nobody, once you have a roommate agreement'], 0,
       'The agreement splits the bill between you. The lease is what the landlord enforces.'),
])

leaves = lesson('mv-leaves', 'If Someone Leaves', 'The landlord does not take a smaller check.', [
    info('The empty room is still on the lease',
         'Rent is **$1,800**, split **$900** and **$900**. One roommate moves out. The lease still says **$1,800** until a new roommate is approved and added.\n\nYou can chase your former roommate for their share. The landlord can chase you for the whole rent.'),
    num('You were paying $900 of an $1,800 rent. Your roommate leaves. What does the landlord still expect this month?', 1800,
        'The lease amount does not shrink. It is still $1,800.'),
    num('How much more is that than the $900 you had been paying?', 900,
        '$1,800 − $900 = $900.'),
    mc('What belongs in the roommate agreement for this moment?',
       ['Who pays until a new roommate is approved, and how you find one', 'A note that the landlord will cut the rent in half', 'Nothing. A handshake is enough'], 0,
       'Write the plan before anyone is angry.'),
    tf('A roommate agreement lets you pay only your old share after the other person moves out.', False,
       'It can say your roommate still owes you. It cannot force the landlord to accept half the rent.'),
])

utils = lesson('mv-utils', 'Utilities', 'Start the new ones before you end the old ones.', [
    info('A week in the dark is expensive',
         'The start-up charge on this account is **$60**. A typical electric bill after that is **$90**.\n\nTurn the new place on before move-in day. Turn the old place off the day you return the keys, not a month later.'),
    num('The first month is the $60 start-up plus a $90 electric bill. What is that first utility month?', 150,
        '$60 + $90 = $150.'),
    num('After the start-up, you budget $90 a month. What is electric for a 12-month lease, counting the start-up once?', 1140,
        '$90 × 12 + $60 = $1,080 + $60 = $1,140.'),
    mc('You leave the old electric on for an extra month at $90. What did that month buy?',
       ['Power for an apartment you no longer use', 'A discount at the new place', 'A required deposit refund'], 0,
       'Schedule the stop date. An empty apartment still bills you.'),
    tf('The internet account can stay in a roommate’s name after they move out, with no risk to them.', False,
       'The name on the account is the person the company will bill. Put the account with someone who still lives there.'),
])

apt_a = doc('statement', 'Apartment A', [
    ('rent', 'Rent', 1500),
    ('util', 'Utilities, your estimate', 180),
], subtitle='Nothing included', totals=[('Monthly', 1680, True)])
apt_b = doc('statement', 'Apartment B', [
    ('rent', 'Rent', 1750),
    ('net', 'Internet, the rest is included', 60),
], subtitle='Heat and water included', totals=[('Monthly', 1810, True)])
assert 1500 + 180 == 1680 and 1750 + 60 == 1810 and 1810 - 1680 == 130

compare = lesson('mv-compare', 'Two Apartments', 'Compare the month, not the rent line.', [
    num('What is Apartment A per month, rent plus utilities?', 1680,
        '$1,500 + $180 = $1,680.', docs=[apt_a, apt_b]),
    num('What is Apartment B per month, rent plus the internet you still pay?', 1810,
        '$1,750 + $60 = $1,810.', docs=[apt_a, apt_b]),
    num('How much less is A than B, once both pages are included?', 130,
        '$1,810 − $1,680 = $130.', docs=[apt_a, apt_b]),
    mc('You care only about the monthly cash. Which page wins?',
       ['Apartment A', 'Apartment B', 'They cost the same'], 0,
       'A is $1,680. B is $1,810. A is $130 less.',
       why=['$1,680 is the lower full month.', 'B’s rent looks higher because heat and water are inside it, and the total is still higher.', 'The totals differ by $130.'],
       docs=[apt_a, apt_b]),
    tf('The lower rent line is always the cheaper apartment.', False,
       'B’s rent is higher and its full month is higher here. On another pair, a higher rent can still be cheaper once utilities are added.'),
], fmt='call')

ben_story = {
    'title': 'Ben and Ola',
    'character': 'Ben, 23',
    'body': 'Ben is 23 and works in a warehouse. Ola is 24 and teaches. Their rent is **$1,800**. Ben’s room is **200** square feet. Ola’s is **400**.\n\nThey split the rent by size: **$600** for Ben and **$1,200** for Ola. Electric is **$90** and internet is **$60**, and those they split in half.\n\nThey write a [[roommate agreement]] the same week they sign the [[lease]].',
}
ben = lesson('mv-ben', 'Ben and Ola', 'The rooms are not equal, so the rent is not either.', [
    num('What is Ben’s rent share on the 200-square-foot room?', 600,
        '200 ÷ 600 = 1/3. $1,800 × 1/3 = $600.'),
    num('What is Ola’s rent share on the 400-square-foot room?', 1200,
        '400 ÷ 600 = 2/3. $1,800 × 2/3 = $1,200.'),
    num('Electric and internet are $150. Split in half, what does Ben add?', 75,
        '$90 + $60 = $150. $150 ÷ 2 = $75.'),
    num('What does Ben pay in a normal month, rent share plus his half of the bills?', 675,
        '$600 + $75 = $675.'),
    num('What does Ola pay in that same month?', 1275,
        '$1,200 + $75 = $1,275. Together: $675 + $1,275 = $1,950, which is the $1,800 rent plus the $150 bills.'),
], fmt='story', story=ben_story)

checklist = lesson('mv-checklist', 'Moving Checklist', 'Do them in an order that does not leave you paying two rents.', [
    info('Four beats',
         'Notice, then the truck, then the utilities, then the photos and the keys.\n\nSkipping the notice can cost a fee. Skipping the photos can cost the [[security deposit]].'),
    order('Put the move in order.',
          ['Give written notice on time',
           'Book the truck and the helpers',
           'Start the new utilities and stop the old ones',
           'Photograph every room and return the keys'],
          'Notice protects you from a penalty. The truck and the power make the day work. The photos are the last word on the deposit.'),
    mc('Why do the photos come after the place is empty?',
       ['They show the condition you actually left', 'The landlord prefers a furnished photo', 'Photos replace the written notice'], 0,
       'The deposit argument is about the day you hand over the keys.'),
    tf('You should stop the old electric a month before you move out, to save money.', False,
       'You still live there. Stop it the day you return the keys.'),
    fill('The paper that tells the landlord you are leaving is written ___.',
         ['notice', 'a new lease', 'a gift'], 0,
         'Notice, on time, in writing.'),
], fmt='concept')

trial_steps = [
    num('A move has a $200 truck, a $1,500 deposit, and $1,500 of first month’s rent. What is that trio?', 3200,
        '$200 + $1,500 + $1,500 = $3,200.'),
    mc('One roommate moves out. The lease rent is $2,000. What can the landlord still require?',
       ['The full $2,000', 'Only the remaining roommate’s old half', 'Nothing until a new roommate signs'], 0,
       'The lease amount stays until the lease changes.'),
    num('Rooms are 300 and 100 square feet. Rent is $2,000. What does the 300-square-foot room pay?', 1500,
        '300 ÷ 400 = 3/4. $2,000 × 3/4 = $1,500.'),
    tf('A roommate agreement replaces the lease.', False,
       'It splits duties between roommates. The landlord still uses the lease.'),
]

lessons = [costs, rooms, bills, leaves, utils, compare, ben, checklist,
           review('mv'), trial('mv', 'Moving & Roommates', trial_steps)]
write_unit('02-moving-roommates.json', 'moving-roommates', 2, 'Moving & Roommates',
           'The real cost of a move, a fair split, and a plan for the day someone leaves.',
           'Write the split down before you share a fridge.', terms, lessons, section=S)
