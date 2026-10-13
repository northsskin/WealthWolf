from lib import *

S = 'building-wealth'
terms = {
    'donor-advised-fund': term('Donor-advised fund',
                               'An account at a sponsoring charity. You contribute, and you may later recommend grants. The money is no longer yours. This is a description, not a tax worksheet.',
                               'Contributing $2,000 and recommending a grant to a food bank the next year.'),
}

give = lesson('gv-budget', 'Giving Inside the Budget', 'Assign a $3,000 month that includes a gift.', [
    info('A line, not a leftover',
         'Giving belongs in the plan as its own line. This drill is a $3,000 month. Needs are at least $1,800, saving is at least $400, and giving is at least $50. Assign every dollar. The gift comes from the plan, not from the rent.'),
    alloc('Assign all $3,000. Meet each floor.', 3000, 50,
          [{'label': 'Needs', 'min': 1800},
           {'label': 'Saving', 'min': 400},
           {'label': 'Giving', 'min': 50}],
          'The floors are $1,800, $400, and $50, which add to $2,250. The other $750 can land on giving in a simple fill, for $800. A real month can put that extra into saving instead. The drill only requires the floors and a full assignment.'),
    num('How many dollars do the three floors add to?', 2250,
        '$1,800 + $400 + $50 = $2,250.'),
    tf('A gift should come out of rent if the month is tight.', False,
       'The gift is a line you choose. Rent is a need. Skipping rent to donate is not the plan.'),
    mc('Where does a planned gift sit?',
       ['On its own line, after needs are covered', 'Instead of the emergency fund', 'As a secret that the budget does not show'], 0,
       'Its own line. The emergency fund keeps its job.'),
])

check = lesson('gv-check', 'Choosing a Charity', 'A story is not a receipt.', [
    info('Look it up',
         'A qualified charity is an organization the IRS recognizes for deductible gifts. Look it up on the IRS Tax Exempt Organization Search before you give. A photo, a sad story, or a request for gift cards is not that lookup. Churches can qualify even when the search is quirky. If you cannot tell, do not send money that night.'),
    mc('What is the check before you give?',
       ['Whether the organization is a qualified charity', 'Whether the story made you cry', 'Whether a stranger texted you a wallet address'], 0,
       'Qualified organization. Emotion is not a receipt, and a texted wallet is a scam shape you already know.'),
    tf('Gift cards sent to a stranger are a normal way to donate.', False,
       'They are a common scam shape. A real charity can take a traceable gift without a gift-card relay.'),
    mc('A group will not appear clearly as a qualified charity and wants the money tonight. What do you do?',
       ['Wait and verify', 'Send a small amount so you feel kind', 'Empty the emergency fund'], 0,
       'Wait. Kindness survives until morning. A scam does not want you to look the group up.'),
    fill('Look the organization up before you send the ___.',
         ['money', 'will', 'ticker'], 0,
         'The money. The lookup is the point of the pause.'),
])

deduct = lesson('gv-deduct', 'The 2026 Deduction', 'Cash, a cap, and not a gift to a person.', [
    info('What the IRS actually said',
         'For 2026, if you do not itemize, you may deduct up to $1,000 of cash gifts to qualified organizations, or $2,000 if you file jointly. Gifts to individuals are not deductible. This lesson grades those two rules. It does not compute the itemized floor or a partial gift of property.'),
    num('You do not itemize, you file single, and you gave $600 cash to a qualified charity in 2026. How many dollars of that gift fit under the $1,000 cap?', 600,
        'The cap is $1,000. The gift is $600, so all $600 fits. This is the non-itemizer cash rule for 2026.'),
    num('What is the 2026 cash cap, in dollars, for a joint return if you do not itemize?', 2000,
        'The joint cap is $2,000. The single cap is $1,000.'),
    tf('A $500 birthday gift to your brother is a charitable deduction.', False,
       'Gifts to individuals are not deductible. A brother is not a qualified organization.'),
    mc('You do not itemize and you gave $1,400 cash to qualified charities in 2026, filing single. How much of the deduction does this lesson’s cap allow?',
       ['$1,400', '$1,000', '$0, because you did not itemize'], 1,
       'The non-itemizer cap is $1,000. The other $400 does not fit under that cap. Itemizing is a different set of rules this course is not grading.'),
])

daf = lesson('gv-daf', 'Donor-Advised Funds', 'You give it away, then you recommend.', [
    info('No longer yours',
         'A [[donor-advised fund]] is an account at a sponsoring charity. You contribute, and later you recommend grants. The money is no longer yours. Any deduction follows the rules for that kind of gift and that tax year. This is the shape of the tool, not a reason to open one.'),
    mc('After you contribute to a donor-advised fund, whose money is it?',
       ['Still yours, like a savings account', 'The sponsoring charity’s', 'The Federal Reserve’s'], 1,
       'You recommended later gifts. You do not own the balance the way you own a brokerage.'),
    tf('A donor-advised fund is a trick that lets a gift to a friend become deductible.', False,
       'Grants go to charities. A gift to a person is still not a charitable deduction.'),
    mc('What is the honest one-line description?',
       ['Contribute now, recommend grants later, and the money has left you', 'A second emergency fund', 'A kind of margin loan'], 0,
       'Contribute, then recommend. It is not cash you can spend on rent.'),
    fill('The account at a sponsoring charity is a donor-advised ___.',
         ['fund', 'will', 'rate'], 0,
         'Fund. The sponsor holds it.'),
])

hours = lesson('gv-time', 'Time or Money', 'Hours count as giving. They do not count as a deduction.', [
    info('The hours are real',
         'Four hours at a food bank is giving. The IRS does not let you deduct the value of your time. Out-of-pocket costs are a different, fussier rule this lesson will not grade. If the month cannot spare cash, time is the honest gift. Pretending the hours are a $200 deduction is not.'),
    num('You volunteer 4 hours. How many of those hours are a cash deduction in this lesson?', 0, unit=None,
        explain='Zero. Time is not a charitable deduction for the value of the hours.'),
    tf('Volunteer hours are worthless because they are not deductible.', False,
       'They are real help. They are just not a deduction for the value of your time.'),
    mc('The month cannot spare cash. What is the clean gift?',
       ['Time you actually have', 'Rent money', 'A deduction you invent for the hours'], 0,
       'Time. The rent stays. The invented deduction is not a rule.'),
    num('A friend says your 4 hours are “worth” $25 each, so you should deduct $100. How many dollars of that hour-value does this lesson allow as a deduction?', 0,
        'The value of your time is not the deduction. $0 of that $100 story is allowed here.'),
])

person = doc('statement', 'Gift to your sister',
             [('gift', 'Cash you handed her', 200)],
             subtitle='A person, not an organization')
org = doc('statement', 'Gift to a qualified food bank',
          [('gift', 'Cash to the charity', 200)],
          subtitle='A qualified organization')

family = lesson('gv-family', 'Family or a Charity', 'Kindness is not the same as a deduction.', [
    info('Both can be right',
         'Giving $200 to your sister can be the right family choice. It is not a charitable deduction. Giving $200 to a qualified food bank can be. The 2026 non-itemizer rule is about qualified organizations, not relatives. Do the kind thing. Do not call the sister a charity.'),
    mc('Which page can be a charitable deduction, if the other rules are met?',
       [person['title'], org['title']], 1,
       docs=(person, org),
       explain='The food bank is the qualified organization. The sister is a person. Gifts to individuals are not deductible.'),
    num('How many dollars on the sister’s page are a charitable deduction?', 0,
        'Zero. Kindness to a person is not a charitable deduction.'),
    tf('Calling the gift a donation on a note to your sister makes it deductible.', False,
       'The recipient has to be a qualified organization. A note does not change who she is.'),
    mc('When is the gift to your sister still a good idea?',
       ['When you want to help her and you are not pretending it is a tax move', 'When you need a deduction and nothing else', 'When the Fed cuts rates'], 0,
       'Help is allowed. The tax story is the part that is not true.'),
], fmt='call')

spot_doc = doc('statement', 'A plea in your texts',
               [('story', 'Story about a sick child', 0),
                ('cards', 'Gift cards they want sent tonight', 150)],
               subtitle='No organization you can look up')

fake = lesson('gv-spot', 'A Plea That Is Not a Charity', 'The gift-card line is the problem.', [
    info('You have seen this shape',
         'A real charity can wait while you look it up. This message has a story and a demand for $150 in gift cards tonight, and no organization you can check. The story line can be true or invented. The gift-card line is the scam shape.'),
    spot('Which line is the problem?', spot_doc, 'cards',
         'Gift cards, tonight, to a sender you cannot look up. That is the line to refuse. The story is the bait.'),
    num('How many dollars do they want in gift cards?', 150,
        'The ask is $150. You do not send it.'),
    tf('Sending half, $75, is a safe compromise.', False,
       'Half of a scam is still the scam. The pause is to look the group up, or to walk away.'),
    mc('What would a careful gift look like instead?',
       ['A traceable gift to an organization you looked up', 'Gift cards to a number in a text', 'Your emergency fund, wired tonight'], 0,
       'Look it up. Then give in a way you can trace. Not gift cards to a stranger.'),
], fmt='spot')

priya = lesson('gv-priya', 'Priya’s Giving Plan', 'Fifty dollars, after the lookup.', [
    info('Meet Priya',
         'Priya is 26 and a graphic designer. She gives $50 a month, which is $600 a year, to a food bank she looked up. She does not itemize. The 2026 single cash cap is $1,000, so the $600 fits under it.\n\nShe does not give the rent, and she does not give from the emergency fund. The $50 is a line in the month.',
         ),
    num('How many dollars a year is Priya’s $50 a month?', 600,
        '12 × $50 = $600.'),
    num('How many dollars of room are left under the $1,000 single cap after that $600?', 400,
        '$1,000 − $600 = $400. She does not have to use it.'),
    tf('Priya should skip the lookup because $50 is too small to be a scam.', False,
       'Small gifts are how gift-card scams start. The lookup takes a minute at any size.'),
    mc('Which pile does the $50 not come from?',
       ['The giving line in her budget', 'The rent', 'Money left after needs and saving'], 1,
       'Not the rent. The giving line is the one she planned.'),
], fmt='story', story={
    'title': 'Fifty dollars, looked up',
    'character': 'Priya, 26, graphic designer',
    'body': 'Priya gives **$50** a month, **$600** a year, to a food bank she looked up. She does not itemize. The 2026 single cash cap is **$1,000**.\n\nThe $50 is a budget line. It is not the rent.',
})

write_unit('08-giving.json', 'giving', 8, 'Giving & Philanthropy',
           'A budget line, a real charity, and the 2026 cash cap.',
           'Look the organization up. Then give from the line you planned.',
           terms, [give, check, deduct, daf, hours, family, fake, priya, review('gv'), trial('gv', 'Giving & Philanthropy', [
               num('You do not itemize and you file jointly in 2026. What is the cash charitable cap, in dollars?', 2000,
                   'The joint cap is $2,000. The single cap is $1,000.'),
               tf('A cash gift to your cousin is a charitable deduction.', False,
                  'Gifts to individuals are not deductible. A cousin is not a qualified organization.'),
               num('You volunteer 6 hours and someone values them at $20 each. How many dollars of that hour-value are a deduction here?', 0,
                   'The value of your time is not a charitable deduction. The answer is $0.'),
               mc('A text wants gift cards tonight and will not name an organization you can look up. What do you do?',
                  ['Send the cards', 'Do not send them', 'Wire the emergency fund'], 1,
                  'Gift cards to an unnamed sender are the scam shape. Look a real charity up, or give nothing tonight.'),
           ])],
           section=S)
