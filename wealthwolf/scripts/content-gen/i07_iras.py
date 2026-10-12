from lib import *

S = 'investing'
terms = {
    'backdoor-roth': term('Backdoor Roth',
                          'A legal path some high earners use: a nondeductible traditional IRA contribution, then a conversion to a Roth IRA. If you already have pre-tax IRA money, the pro-rata rule can make part of the conversion taxable. This course names it. It does not walk the forms.',
                          'Income is over the Roth IRA limit, so a direct Roth contribution is not allowed.'),
}

what = lesson('ir-what', 'What an IRA Is', 'An account you open yourself.', [
    info('Not the workplace plan',
         'An IRA is an individual retirement account. You open it, not your employer. A [[traditional IRA|traditional-ira]] can give you a tax break now, if you qualify. A [[Roth IRA|roth-ira]] takes the tax break later, on a qualified withdrawal. The 2026 contribution limit is $7,500 for both of them combined, plus $1,100 if you are 50 or older.'),
    mc('Who opens an IRA?',
       ['Only your employer', 'You do', 'The IRS, automatically'], 1,
       'Individual means you. The 401(k) is the workplace one.'),
    num('What is the 2026 IRA contribution limit, in dollars, before the age-50 catch-up?', 7500,
        'The 2026 limit is $7,500 across traditional and Roth IRAs combined.'),
    tf('You can put $7,500 in a traditional IRA and another $7,500 in a Roth IRA in 2026.', False,
       'The $7,500 is the total, split however you like between them. It is not $7,500 each.'),
    mc('How is an IRA different from a 401(k)?',
       ['The IRA is the account you open. The 401(k) comes from the job.', 'They are the same account', 'An IRA cannot hold a fund'], 0,
       'Two containers. The limits are separate. The investments inside can look alike.'),
])

trad = doc('statement', 'Traditional IRA',
           [('in', 'Contribution', 1000), ('save', 'Tax saved this year in the 12% bracket, if you can deduct it', 120)],
           subtitle='The deduction is not automatic')
roth = doc('statement', 'Roth IRA',
           [('in', 'Contribution', 1000), ('save', 'Tax saved this year', 0)],
           subtitle='Qualified withdrawals later are tax-free')

door = lesson('ir-door', 'Roth or Traditional', 'Now or later, and only if you qualify.', [
    info('The same $1,000, two doors',
         'If you can deduct a [[traditional IRA|traditional-ira]] contribution, $1,000 in the 12% bracket saves $120 this year. A [[Roth IRA|roth-ira]] saves $0 this year, and a qualified withdrawal of the earnings later is tax-free. The workplace-plan rules can shrink or erase the traditional deduction. The Roth door has its own income limit.'),
    mc('Which page can lower this year’s tax, if the deduction is allowed?',
         [trad['title'], roth['title']], 0,
         docs=(trad, roth),
         explain='The traditional page is the deduction. $1,000 × 0.12 = $120. The Roth page pays the tax now.'),
    num('If the deduction is allowed, how many dollars of tax does $1,000 save in the 12% bracket?', 120,
        '$1,000 × 0.12 = $120. If the deduction is not allowed, that $120 does not happen.'),
    tf('A Roth IRA contribution lowers this year’s taxable income.', False,
       'Roth money was already taxed. The favor is on a qualified withdrawal later.'),
    mc('You cannot deduct a traditional IRA, and your income is under the Roth limit. Which door is the simple one?',
       ['Traditional, for a deduction you cannot take', 'Roth, since the traditional deduction is worth $0 here', 'Neither, so you skip retirement accounts'], 1,
       'A nondeductible traditional contribution is the awkward one. Under the Roth limit, the Roth door is the direct one.'),
], fmt='call')

limit_doc = doc('statement', '2026 IRA limits',
                [('base', 'Contribution limit, under age 50', 7500),
                 ('extra', 'Catch-up at age 50 or older', 1100)],
                totals=[('Total at age 50 or older', 8600, True)],
                meta=[('Roth phase-out, single', '$153,000 to $168,000'),
                      ('Roth phase-out, married filing jointly', '$242,000 to $252,000')],
                note='A single filer at $168,000 or more cannot make a direct Roth IRA contribution. A joint filer at $252,000 or more cannot. Under the start of the range, the full contribution is allowed.')

limits = lesson('ir-limits', 'The 2026 IRA Limits', 'The dollar cap, then the income cap.', [
    info('Two different gates',
         'The dollar gate: $7,500 in 2026, or $8,600 at age 50 or older. The income gate is for Roth IRAs. A single filer with modified AGI under $153,000 can make a full Roth contribution. At $168,000 or more, a direct Roth contribution is not allowed. Married filing jointly: full under $242,000, and none at $252,000 or more. This course will not compute a partial phase-out in between.'),
    num('How many dollars can someone under 50 contribute to IRAs in 2026?', 7500,
        doc=limit_doc,
        explain='The base limit is $7,500, traditional and Roth combined.'),
    num('How many dollars is the total at age 50 or older in 2026?', 8600,
        doc=limit_doc,
        explain='$7,500 + $1,100 = $8,600.'),
    tf('A single filer with modified AGI of $170,000 can make a direct Roth IRA contribution in 2026.', False,
       '$170,000 is over $168,000. The direct Roth contribution is not allowed. A partial amount between $153,000 and $168,000 is a real thing, and this course does not grade that math.'),
    tf('A single filer with modified AGI of $100,000 is under the 2026 Roth IRA income limit.', True,
       '$100,000 is under $153,000, so the full Roth contribution is allowed, up to the $7,500 dollar cap and up to earned income.'),
], fmt='document')

open_it = lesson('ir-open', 'Opening One', 'Four steps, then leave it alone.', [
    info('The order',
         'You need earned income, such as wages. You check the limit that applies to you. Then you open the IRA, link a bank account, pick a [[fund]], and set an automatic transfer. The account is the container. The fund is what you own inside it.'),
    order('Put the opening in order.',
          ['Check that you have earned income and that the limit allows it',
           'Open the IRA',
           'Link your bank account',
           'Choose a fund and set the automatic transfer'],
          'The limit first, so you do not contribute money you are not allowed to. The fund is last, and then the transfer repeats.'),
    mc('What do you actually own inside the IRA?',
       ['The IRA itself is the investment', 'The fund, or other investments, you buy in it', 'Your employer’s match'], 1,
       'The IRA is the container. A broad, cheap fund is a solid thing to put in it.'),
    tf('You can contribute more than you earned from work.', False,
       'The IRA contribution cannot top your earned income, and it cannot top the yearly dollar limit.'),
    num('Maya earned $28,000 from work in 2026 and is under 50. What is the most she can contribute to IRAs, in dollars?', 7500,
        'Her wages are over $7,500, and she is under 50, so the dollar cap is the binding one: $7,500.'),
])

both = lesson('ir-both', 'A 401(k) and an IRA', 'The limits are separate.', [
    info('Both, if the rules allow',
         'The 2026 employee [[401(k)|401k]] limit is $24,500. The IRA limit is a separate $7,500. Using the workplace plan does not by itself ban an IRA. It can affect whether a traditional IRA contribution is deductible. A Roth IRA still has its income limit.'),
    num('In 2026, a 30-year-old puts $24,500 in a 401(k) and $7,500 in a Roth IRA. How many dollars went into retirement accounts?', 32000,
        '$24,500 + $7,500 = $32,000. The two limits are separate, so this is allowed if the Roth income test is met and the person earned enough.'),
    num('Someone puts $2,000 in a Roth IRA and wants the rest of the 2026 IRA limit in a traditional IRA. How many dollars are left?', 5500,
        '$7,500 − $2,000 = $5,500. The cap is shared.'),
    tf('Maxing a 401(k) uses up the IRA limit too.', False,
       'They are different limits. $24,500 at work does not reduce the $7,500 IRA cap.'),
    mc('You have a 401(k) at work and your income is under the Roth IRA limit. What can you also do?',
       ['Nothing. The 401(k) blocks every IRA.', 'Contribute to a Roth IRA, up to the IRA limit', 'Skip the employer match so the IRA is allowed'], 1,
       'The match stays. The IRA is an extra container, inside its own limit.'),
])

back = lesson('ir-back', 'The Backdoor, Named Only', 'A high earner’s path. Not a worksheet.', [
    info('What the name means',
         'If your income is over the [[Roth IRA|roth-ira]] limit, a direct Roth contribution is not allowed. A [[backdoor Roth|backdoor-roth]] is a nondeductible contribution to a [[traditional IRA|traditional-ira]], followed by a conversion into a Roth IRA. If you already have pre-tax money in any traditional IRA, the pro-rata rule can tax part of that conversion. This lesson names the path. The forms and the tax math belong with the IRS or a tax pro, not in a quiz.'),
    mc('Who is a backdoor Roth even about?',
       ['Someone under the Roth income limit', 'Someone whose income is too high for a direct Roth IRA contribution', 'Someone opening a 401(k)'], 1,
       'Under the limit, you just contribute to the Roth. The backdoor is for the person who cannot.'),
    tf('A backdoor Roth is a way to skip taxes entirely, even if you have a large pre-tax IRA.', False,
       'The pro-rata rule can make part of the conversion taxable when pre-tax IRA money already exists.'),
    mc('What will this course not do?',
       ['Name the path', 'Walk the forms and compute a partial conversion', 'Mention the pro-rata rule'], 1,
       'Naming it is the lesson. The worksheet is not.'),
    fill('The rule that can tax part of the conversion when other traditional IRA money exists is the ___ rule.',
         ['pro-rata', 'ticker', 'coupon'], 0,
         'Pro-rata. It looks at all your traditional IRAs, not only the new dollars.'),
])

early = lesson('ir-early', 'Taking Money Out Early', 'Contributions and earnings are not the same.', [
    info('Roth contributions are the flexible part',
         'You can usually withdraw your own [[Roth IRA|roth-ira]] contributions at any time, without tax or penalty. The earnings are the restricted part: generally tax-free only after age 59½ and a five-year clock, with some exceptions this course will not list as a plan. A [[traditional IRA|traditional-ira]] withdrawal before 59½ is usually income tax plus a 10% penalty.'),
    num('You contributed $2,000 to a Roth IRA. It is now worth $2,500. How many dollars are contributions you can usually take out?', 2000,
        'The $2,000 is contributions. The other $500 is earnings, and those have the extra rules.'),
    num('How many dollars of that account are earnings?', 500,
        '$2,500 − $2,000 = $500.'),
    tf('A traditional IRA withdrawal at age 40 is usually tax-free.', False,
       'Before 59½ it is usually income tax plus a 10% penalty. The Roth contribution rule does not apply to it.'),
    mc('Which pile inside a Roth IRA is the one you can usually take out early without tax or penalty?',
       ['The earnings', 'The contributions', 'The whole account, always'], 1,
       'Contributions. Earnings wait on the age and five-year rules, aside from exceptions you should not build a budget on.'),
])

maya = lesson('ir-maya', 'Maya Opens a Roth', 'Under the limit, so the direct door.', [
    info('Meet Maya',
         'Maya is 22 and a library assistant. She earned $28,000 this year, which is under the 2026 Roth IRA income limit for a single filer. She has no IRA yet.\n\nShe opens a Roth IRA and puts in $1,500, then buys a broad [[index fund]]. She does not need a backdoor. $1,500 is under the $7,500 cap.'),
    tf('Maya’s $28,000 income blocks a 2026 Roth IRA contribution.', False,
       '$28,000 is far under $153,000. She can contribute, up to $7,500 and up to what she earned.'),
    num('How many dollars under the $7,500 cap is Maya’s $1,500 contribution?', 6000,
        '$7,500 − $1,500 = $6,000 of room left. She does not have to fill it.'),
    mc('What does Maya buy inside the new IRA?',
       ['The IRA, and nothing else', 'A broad index fund', 'Her employer’s stock, because the fee is zero'], 1,
       'The Roth IRA is the container. The fund is the investment.'),
    order('Put Maya’s afternoon in order.',
          ['Check that $28,000 is under the Roth income limit',
           'Open the Roth IRA',
           'Transfer the $1,500',
           'Buy the broad index fund'],
          'The limit check first. Then the account, the money, and the fund.'),
], fmt='story', story={
    'title': 'The direct door',
    'character': 'Maya, 22, library assistant',
    'body': 'Maya earned **$28,000** this year. That is under the 2026 Roth IRA income limit for a single filer.\n\nShe opens a Roth IRA, contributes **$1,500**, and buys a broad index fund. A backdoor is not her situation.',
})

write_unit('07-iras.json', 'iras', 7, 'IRAs: Roth vs Traditional',
           'The account you open yourself, the dollar cap, and the income cap.',
           'Under the limit, use the front door.',
           terms, [what, door, limits, open_it, both, back, early, maya, review('ir'), trial('ir', 'IRAs: Roth vs Traditional', [
               num('At age 50 in 2026, what is the total IRA contribution limit including the catch-up?', 8600,
                   '$7,500 + $1,100 = $8,600.'),
               tf('Roth IRA contributions and Roth IRA earnings follow the same early-withdrawal rule.', False,
                  'Contributions can usually come out. Earnings generally wait on age 59½ and the five-year clock.'),
               mc('A direct Roth IRA contribution is not allowed for a single filer in 2026 once modified AGI reaches what?',
                  ['$7,500', '$168,000', '$24,500'], 1,
                  '$168,000 or more blocks the direct contribution. $7,500 is the dollar cap. $24,500 is the 401(k) employee cap.'),
               num('You put $3,000 in a Roth IRA in 2026 and you are under 50. How many dollars of IRA room are left?', 4500,
                   '$7,500 − $3,000 = $4,500, shared with any traditional IRA contribution.'),
           ])],
           section=S)
