from lib import *

S = 'taxes'
terms = {
    'capital-gain': term('Capital gain',
                         'Profit from selling an investment for more than your cost basis. Held a year or less, it is short-term. Held more than a year, it is long-term.',
                         'Bought at $2,000, sold at $2,600. The gain is $600.'),
    'cost-basis': term('Cost basis',
                       'What you paid for an investment, including commissions you cannot ignore. The gain is the sale minus this number.',
                       'Eight shares at $25 each have a cost basis of $200.'),
}

gain = lesson('vt-gain', 'A Capital Gain', 'The profit is the sale minus what you paid.', [
    info('Two prices',
         'A [[capital gain]] is the sale price minus your [[cost basis]]. Bought at **$2,000**, sold at **$2,600**, the gain is **$600**.\n\nA loss is the same math when the sale is lower. This unit is education, not a reason to buy or sell.'),
    num('What is the gain on a $2,000 purchase sold for $2,600?', 600,
        '$2,600 − $2,000 = $600.'),
    num('The same investment is sold for $1,700. What is the loss?', 300,
        '$2,000 − $1,700 = $300.'),
    mc('What is cost basis, in this example?',
       ['The $2,000 you paid', 'The $2,600 sale', 'The tax rate'], 0,
       'Basis is what you paid. The sale is what you received.'),
    tf('A gain is taxed as if the whole sale price were profit.', False,
       'Only the $600 above the $2,000 basis is the gain.'),
])

term_len = lesson('vt-term', 'Short or Long', 'More than a year changes the rate in this example.', [
    info('Eleven months, or a year and a day',
         'Held a year or less, the **$600** gain is short-term and taxed as ordinary income. This example puts it in a **22%** ordinary rate, so the tax is **$132**.\n\nHeld more than a year, it is long-term. This example uses a stated **15%** long-term rate, so the tax is **$90**. The 0%, 15%, and 20% cutoffs depend on income. This lesson does not invent those cutoffs. Waiting saves **$42** in this example.'),
    num('The $600 short-term gain is taxed at the stated 22%. What is the tax?', 132,
        '$600 × 0.22 = $132.'),
    num('The $600 long-term gain is taxed at the stated 15%. What is the tax?', 90,
        '$600 × 0.15 = $90.'),
    num('How much less tax is the long-term result in this example?', 42,
        '$132 − $90 = $42.'),
    tf('Selling after 11 months gets the long-term rate.', False,
       'Eleven months is a year or less. Long-term means more than a year.'),
])

divs = lesson('vt-div', 'Dividends', 'Qualified is not the same word as ordinary.', [
    info('Two names on the form',
         'A dividend is a payment from a stock or a fund you still hold. **Qualified** dividends can be taxed at the long-term rates. **Ordinary** dividends are taxed as ordinary income.\n\nIn this example, **$400** of qualified dividends at a stated **15%** cost **$60**. **$100** of ordinary dividends at a stated **22%** cost **$22**. Not every dividend is qualified.'),
    num('What is 15% of $400 of qualified dividends, at that stated rate?', 60,
        '$400 × 0.15 = $60.'),
    num('What is 22% of $100 of ordinary dividends, at that stated rate?', 22,
        '$100 × 0.22 = $22.'),
    num('What is the tax on both dividends in this example?', 82,
        '$60 + $22 = $82.'),
    tf('Every dividend is qualified and taxed at the long-term rate.', False,
       'Ordinary dividends are taxed as ordinary income. The form tells you which is which.'),
])

basis = lesson('vt-basis', 'Cost Basis', 'The shares remember what you paid.', [
    info('Count the shares',
         'Eight shares at **$25** each have a [[cost basis]] of **$200**. Sold at **$40** each, the proceeds are **$320**. The [[capital gain]] is **$120**.\n\nReinvested dividends can raise the basis. Ignoring them makes the gain look bigger than it is.'),
    num('What is the cost basis of 8 shares at $25?', 200, '8 × $25 = $200.'),
    num('What are the proceeds of those 8 shares at $40?', 320, '8 × $40 = $320.'),
    num('What is the gain?', 120, '$320 − $200 = $120.'),
    tf('The gain is $320, because that is what the buyer paid you.', False,
       'The gain is $120. The other $200 is your own basis coming back.'),
])

harvest = lesson('vt-harvest', 'Tax-Loss Harvesting', 'A loss can cancel a gain. A quick buyback can cancel the loss.', [
    info('Net them',
         'Tax-loss harvesting means selling an investment that is down so the loss can offset a gain. A **$500** gain and a **$200** loss leave a **$300** net gain.\n\nA wash sale can disallow the loss if you buy the same investment within **30 days** before or after the sale. This is the common rule, at a high level. It is not a trading plan.'),
    num('A $500 gain and a $200 loss. What is the net gain?', 300,
        '$500 − $200 = $300.'),
    num('How much of the $500 gain did the loss offset?', 200,
        'The loss is $200, so $200 of the gain is offset.'),
    mc('What can disallow the loss?',
       ['Buying the same investment back within 30 days', 'Waiting more than a year to sell', 'Keeping the shares and never selling'], 0,
       'That quick buyback is the wash-sale problem. Holding is not a sale, so there is no loss to claim yet.'),
    tf('A loss you have not sold is a deduction this year.', False,
       'The loss is real on paper only until you sell. Unsold shares have not produced a deductible loss.'),
])

short = doc('statement', 'Sold at 11 months', [
    ('gain', 'Short-term gain', 600),
    ('tax', 'Tax at the stated 22%', 132),
])
long = doc('statement', 'Sold after more than a year', [
    ('gain', 'Long-term gain', 600),
    ('tax', 'Tax at the stated 15%', 90),
])
assert 600 * 0.22 == 132 and 600 * 0.15 == 90 and 132 - 90 == 42

year = lesson('vt-year', 'Why the Year Matters', 'Same gain. The rate on this pair is the whole difference.', [
    num('What is the tax on the 11-month page?', 132,
        '$600 × 0.22 = $132.',
        context='Both pages are the same **$600** [[capital gain]]. The holding period is the only change.',
        docs=[short, long]),
    num('What is the tax on the long-term page?', 90,
        '$600 × 0.15 = $90.', docs=[short, long]),
    num('How much tax does waiting past a year save in this example?', 42,
        '$132 − $90 = $42.', docs=[short, long]),
    mc('Which page has the smaller tax, on these stated rates?',
       ['The long-term sale', 'The 11-month sale', 'They match'], 0,
       'Long-term is $90. Eleven months is $132.',
       why=['$90 is the smaller tax.', '11 months is still short-term here.', 'The taxes differ by $42.'],
       docs=[short, long]),
    tf('The long-term page has a smaller gain.', False,
       'Both gains are $600. The rate changed, not the gain.'),
], fmt='call')

elena_story = {
    'title': 'Elena’s savings interest',
    'character': 'Elena, 44',
    'body': 'Elena is 44 and a teacher. Her savings account paid **$80** of interest. She left it in the account.\n\nThe bank will report it on Form 1099-INT. The **$80** is taxable even though she did not withdraw it. It is not a [[capital gain]]. She did not sell anything.\n\nShe also still holds a fund. Unsold, it has no gain to report this year, whatever the screen says it is “worth.”',
}
elena = lesson('vt-elena', 'Interest, Even If You Leave It', 'Form 1099-INT does not wait for a withdrawal.', [
    num('How much interest did the savings account pay?', 80, 'The story’s figure is $80.'),
    mc('Why is the $80 taxable this year?',
       ['Interest is income when it is paid, even if it stays in the account', 'Only withdrawn cash is income', 'Interest is a long-term capital gain'], 0,
       'Leaving it in the account does not defer it. A sale is a different event.'),
    tf('The unsold fund produces a capital gain this year because the price went up on the screen.', False,
       'The gain waits for a sale. An unsold fund is still hers.'),
    mc('Which form reports the bank interest?',
       ['Form 1099-INT', 'Form W-4', 'Schedule C'], 0,
       '1099-INT is the interest form. The W-4 is withholding. Schedule C is a business.'),
    fill('Interest left in the account is still ___.',
         ['taxable', 'a capital loss', 'a standard deduction'], 0,
         'Taxable. The withdrawal is not what makes it income.'),
], fmt='story', story=elena_story)

slip = doc('statement', 'Brokerage summary', [
    ('proceeds', 'Proceeds from the sale', 2600),
    ('basis', 'Cost basis', 2000),
    ('qual', 'Qualified dividends', 400),
    ('interest', 'Interest', 80),
], subtitle='These lines are not one total')
assert 2600 - 2000 == 600

broker = lesson('vt-1099', 'A Brokerage 1099', 'Read the gain from two lines, not from their sum.', [
    info('Four different facts',
         'Proceeds **$2,600**. [[Cost basis]] **$2,000**. Qualified dividends **$400**. Interest **$80**.\n\nAdding all four lines is not a tax. The gain is proceeds minus basis.'),
    num('What is the capital gain on this page?', 600,
        '$2,600 − $2,000 = $600.', doc=slip),
    num('What is the interest on this page?', 80, 'The interest line is $80.', doc=slip),
    num('Qualified dividends are $400. At a stated 15% rate, what is the tax on that line alone?', 60,
        '$400 × 0.15 = $60. That rate is the example’s stated rate, not a cutoff this page computed.',
        doc=slip),
    tf('The four lines should be added together and called the gain.', False,
       'The gain is $600. Dividends and interest are their own income.'),
], fmt='document')

trial_steps = [
    num('Cost basis is $900. The sale is $1,200. What is the gain?', 300, '$1,200 − $900 = $300.'),
    num('A $1,000 short-term gain is taxed at a stated 24%. What is the tax?', 240, '$1,000 × 0.24 = $240.'),
    tf('A sale after 400 days is still short-term.', False,
       'More than a year is long-term. 400 days is more than a year.'),
    mc('Interest of $50 posted to a savings account and left there is:',
       ['Taxable interest', 'A capital gain', 'Invisible until you withdraw it'], 0,
       'It is interest income for the year it was paid.'),
]

lessons = [gain, term_len, divs, basis, harvest, year, elena, broker,
           review('vt'), trial('vt', 'Taxes on Investments', trial_steps)]
write_unit('06-investment-taxes.json', 'investment-taxes', 6, 'Taxes on Investments',
           'Gains, dividends, basis, and the year that changes the rate in the example.',
           'The gain is the sale minus the basis. The year decides which rate this example uses.', terms, lessons, section=S)
