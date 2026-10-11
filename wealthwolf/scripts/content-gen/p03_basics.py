from lib import *

S = 'protecting'
terms = {
    'insurance': term('Insurance',
                      'You pay a smaller, regular amount so a pool of people can cover a big loss you could not pay alone.',
                      'A $100 monthly premium sits in the pool. A $20,000 surgery does not come only out of your pocket.'),
    'deductible': term('Deductible',
                       'The amount you pay on a covered loss before insurance starts paying.',
                       'A $1,000 deductible on a $4,000 claim means you pay $1,000 and the plan pays the rest, up to the limit.'),
    'coverage-limit': term('Coverage limit',
                           'The most the policy will pay for a covered loss.',
                           'A $300,000 limit does not pay the part of a loss above $300,000.'),
    'exclusion': term('Exclusion',
                      'A loss the policy says it will not pay, even if everything else is in force.',
                      'A standard home policy often excludes flood. The water can be real and still not covered.'),
}

pool = lesson('ib-pool', 'What Insurance Is', 'You buy a share of a pool, not a promise that nothing bad will happen.', [
    mc('What is insurance, in plain terms?',
       ['A pool that pays big losses in exchange for a smaller regular payment', 'A savings account that never goes down', 'A fine you pay after an accident'], 0,
       'The premium is the share. The pool is there for the loss you could not cover alone.',
       context='[[Insurance]] is that pool. The [[premium]] is what you pay to keep the policy active, whether or not you use it.'),
    num('The premium is $80 a month. What is that for a year?', 960, '$80 × 12 = $960.'),
    tf('Paying the premium means the insurer will cover every loss you ever have.', False,
       'The policy pays what it covers, up to the limit, after the deductible. Not every misfortune.'),
    mc('Who is the premium for?',
       ['The pool, so covered losses can be paid', 'A savings jar with your name on it', 'A tax on safe drivers only'], 0,
       'You may not claim this year. Someone in the pool will.'),
    fill('The regular price of keeping insurance active is the ___.',
         ['premium', 'deductible', 'exclusion'], 0,
         'You pay it even in a quiet year.'),
])

parts = lesson('ib-parts', 'Premium, Deductible, Limit', 'Three numbers. They are not the same job.', [
    mc('What is a deductible?',
       ['What you pay on a covered loss before the insurer pays', 'The most the policy will ever pay', 'The monthly price of the policy'], 0,
       'You cover the first part. Then the pool steps in.',
       context='A [[deductible]] comes off the loss. A [[coverage limit]] is the ceiling on what the policy pays.'),
    num('A covered claim is $4,000. The deductible is $1,000. How much do you pay toward that claim?', 1000,
        'The deductible is the first $1,000.'),
    num('How much of that $4,000 does insurance pay, if it is under the limit?', 3000,
        '$4,000 − $1,000 = $3,000.'),
    num('The coverage limit is $300,000. A covered loss is $20,000, after a $1,000 deductible. Does the limit block the payment? How much of the $20,000 is above $300,000?',
        0, '$20,000 is under $300,000, so none of it is past the limit.'),
    tf('A higher coverage limit means the insurer will pay past that limit.', False,
       'The limit is the ceiling.'),
])

policy_lines = [
    ('prem', 'Premium for the year', 1200),
    ('ded', 'Deductible', 1000),
    ('limit', 'Coverage limit', 300000),
]
POLICY = doc('statement', 'Policy summary', policy_lines, subtitle='Sample renters policy',
             meta=[('Policy number', 'R-20418'), ('Term', '12 months')],
             note='This is a summary, not the whole contract.')
summary = lesson('ib-summary', 'A Policy Summary', 'Three lines tell you the price, the first dollars, and the ceiling.', [
    num('What is the yearly premium on this summary?', 1200, 'The premium line is $1,200.',
        context='Read the summary before you read the ads.', doc=POLICY),
    num('What is the deductible?', 1000, 'The deductible line is $1,000.', doc=POLICY),
    num('A covered loss is $4,000. Using this deductible, how much does the insurer pay?', 3000,
        '$4,000 − $1,000 = $3,000. The limit is $300,000, so it does not cut this claim.', doc=POLICY),
    mc('Which line is the most the policy will pay?',
       ['The coverage limit', 'The premium', 'The deductible'], 0,
       'The limit is the ceiling. The premium is the price. The deductible is your first part.'),
    tf('The one-page summary is the entire legal contract.', False,
       'The summary is the map. The contract is longer, and the exclusions live there.'),
], fmt='document')

low_lines = [
    ('prem', 'Yearly premium', 1800),
    ('ded', 'Deductible', 500),
]
high_lines = [
    ('prem', 'Yearly premium', 1080),
    ('ded', 'Deductible', 2000),
]
assert 1800 - 1080 == 720 and 2000 - 500 == 1500
LOW = doc('statement', 'Plan Low', low_lines, subtitle='Lower deductible')
HIGH = doc('statement', 'Plan High', high_lines, subtitle='Higher deductible')
call = lesson('ib-deductible-call', 'Higher Deductible, Lower Premium', 'You trade a cheaper year for a bigger bill when something breaks.', [
    num('How much less premium does Plan High charge per year?', 720, '$1,800 − $1,080 = $720.',
        context='Same kind of policy. The deductible and the premium moved in opposite directions.',
        docs=[LOW, HIGH]),
    num('How much higher is Plan High’s deductible?', 1500, '$2,000 − $500 = $1,500.', docs=[LOW, HIGH]),
    mc('You expect no claim this year. Which plan costs less if that comes true?',
       ['Plan High', 'Plan Low', 'They cost the same'], 0,
       'With no claim you only pay the premium. $1,080 is less than $1,800.'),
    mc('A covered loss is $2,000. You also pay the premium. Which plan has you pay less in total that year?',
       ['Plan Low', 'Plan High', 'They match to the dollar'], 0,
       'Plan Low: $500 + $1,800 = $2,300. Plan High: $2,000 + $1,080 = $3,080.',
       why=['$2,300 against $3,080.', 'The bigger deductible swallows the whole loss.', 'The totals are $780 apart.']),
    tf('The cheaper premium is always the better plan.', False,
       'It is better in a quiet year. A big claim can erase the savings.'),
], fmt='call')

choose = lesson('ib-insure-what', 'What to Insure', 'Insure the loss that would wreck you. Skip the one you can replace.', [
    sort('Insure it, or you could probably skip it?',
         ['Insure it', 'You could skip it'],
         [('A fire that destroys the place you live', 0),
          ('A lawsuit after someone is hurt', 0),
          ('A $40 toaster’s extended warranty', 1),
          ('A phone you could replace from savings', 1),
          ('A car crash that injures another person', 0)],
         'Insure the big loss. The small stuff can come from cash you already have.'),
    mc('Why skip insurance on a loss you could pay from savings?',
       ['The premium can cost more than the risk is worth to you', 'Small losses are illegal to pay yourself', 'Insurers refuse any policy under $1,000'], 0,
       'Insurance is for the hit you cannot absorb.'),
    tf('If you can replace it next paycheck, it is the first thing to insure.', False,
       'That is the loss you can skip. Insure the one you cannot.'),
    mc('Which loss is the clearest case for insurance?',
       ['A hospital bill big enough to wipe out your savings', 'A $15 charging cable', 'A snack you did not like'], 0,
       'Size is the test. Could you write the check?'),
    fill('Insure the loss you could not ___ from savings.',
         ['cover', 'enjoy', 'advertise'], 0,
         'That is the job of the pool.'),
], fmt='sort')

exclude = lesson('ib-exclusions', 'Exclusions', 'The loss can be real and still not covered.', [
    mc('What is an exclusion?',
       ['A loss the policy says it will not pay', 'The monthly premium', 'A bonus for filing no claims'], 0,
       'The damage can be obvious. The contract can still say no.',
       context='An [[exclusion]] is a no, written in advance.'),
    tf('If a policy excludes flood, a flood is still covered because water is an accident.', False,
       'An exclusion is the exception. The accident is not enough.'),
    mc('Where do you look before you count on a policy?',
       ['The exclusions, not only the friendly summary', 'The advertisement', 'The font on the logo'], 0,
       'The summary sells. The exclusions decide.'),
    mc('A policy covers theft and excludes earthquakes. An earthquake breaks the windows. What happens?',
       ['The earthquake exclusion can block the claim', 'Theft coverage pays, because glass is missing', 'Every broken window is theft'], 0,
       'The cause is the earthquake. That cause is excluded.'),
    fill('An exclusion is a loss the policy will not ___.',
         ['pay', 'mention', 'count'], 0,
         'Read it before you need it.'),
])

filing = lesson('ib-claim', 'Filing a Claim', 'Safety first. Then the record. Then the company.', [
    order('Put a claim in order.',
          ['Make sure people are safe and call for help if someone is hurt',
           'Write down what happened and take photos',
           'Tell your insurance company',
           'Keep receipts for costs you had to pay'],
          'People first. The record second. The company third. The receipts prove the extra costs.'),
    tf('You should throw away receipts once you have told the insurer.', False,
       'Receipts are how you show what you spent.'),
    mc('Why take photos?',
       ['They show the damage as it was', 'They raise the deductible', 'They replace the policy'], 0,
       'Memory fades. The photo does not.'),
    mc('Someone is hurt. What comes before the paperwork?',
       ['Getting them help', 'Comparing premiums', 'Posting about it'], 0,
       'The claim can wait a few minutes. An injury cannot.'),
    fill('Keep the ___ for costs you paid out of pocket.',
         ['receipts', 'excuses', 'ads'], 0,
         'A receipt is the proof.'),
])

sam_story = {
    'title': 'The window under the deductible',
    'character': 'Sam, 41, line cook',
    'body': 'A storm breaks Sam’s apartment window. The glass shop wants **$900**. His policy’s deductible is **$1,000**, and the yearly premium is **$240**. He files anyway, because he wants to know.\n\nThe insurer agrees the break is covered. The payout is still **$0**, because $900 never clears a $1,000 deductible. A second storm later puts a **$2,400** hole in the same kind of glass.',
}
rates = lesson('ib-rates', 'Claims and Your Rates', 'A claim can cost more than the check.', [
    num('How much does insurance pay on the $900 window?', 0,
        '$900 is under the $1,000 deductible, so the payout is $0.'),
    num('How much would insurance pay on the later $2,400 break, same deductible?', 1400,
        '$2,400 − $1,000 = $1,400.'),
    mc('Why might Sam still think twice before filing a small claim?',
       ['A claim can raise what he pays later, even when the payout is tiny', 'Filing is illegal under $1,000', 'The premium disappears if he never files'], 0,
       'The check is not the only cost. The next premium can move.'),
    tf('A covered loss under the deductible still produces a payout.', False,
       'The deductible is the hurdle. Under it, the insurer pays nothing.'),
    mc('He pays the $240 premium and gets $0 for the $900 window. What did the premium buy that year?',
       ['Coverage for a bigger loss, not a refund of the premium', 'A promise the window would not break', 'The $900, paid in secret'], 0,
       'The pool was there. This particular loss never reached it.'),
], fmt='story', story=sam_story)

trial_steps = [
    num('Premium $60 a month. What is the yearly premium?', 720, '$60 × 12 = $720.'),
    mc('A covered $6,000 loss has a $1,000 deductible and a huge limit. How much do you pay toward the loss?',
       ['$1,000', '$6,000', '$0'], 0,
       'The deductible is your first $1,000. The limit is not the issue.'),
    tf('An exclusion is a loss the policy agrees to pay extra for.', False,
       'An exclusion is a loss the policy will not pay.'),
    num('Plan A’s premium is $2,000. Plan B’s is $1,250. How much less is B?', 750,
        '$2,000 − $1,250 = $750.'),
]

lessons = [pool, parts, summary, call, choose, exclude, filing, rates,
           review('ib'), trial('ib', 'Insurance Basics', trial_steps)]
write_unit('03-insurance-basics.json', 'insurance-basics', 3, 'Insurance Basics',
           'The pool, the deductible, the limit, and the losses a policy will not touch.',
           'Read the no before you trust the yes.', terms, lessons, section=S)
