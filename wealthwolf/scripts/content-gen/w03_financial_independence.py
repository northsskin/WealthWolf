from lib import *

S = 'building-wealth'
terms = {
    'savings-rate': term('Savings rate',
                         'The share of your pay that you keep instead of spending. Pay of $60,000 and savings of $15,000 is a 25% savings rate.',
                         'Saving $1,000 of a $4,000 month is 25%.'),
    'four-percent-rule': term('4% rule',
                              'A rule of thumb: in the first retired year, withdraw about 4% of the portfolio, then adjust that dollar amount for inflation. It is a sketch from history, not a promise.',
                              '4% of $1,000,000 is $40,000 in year one.'),
    'fi-number': term('FI number',
                      'The portfolio that could cover your yearly spending under the 4% rule of thumb. It is about 25 times yearly spending.',
                      'Spending $40,000 a year points at a FI number of $1,000,000.'),
    'coast-fi': term('Coast FI',
                     'Having enough invested that, with no more contributions, an example growth rate could reach your FI number by a chosen age. The rate is a guess, not a promise.',
                     'About $100,000 left alone, doubling three times, is about $800,000.'),
}

rate = lesson('fn-rate', 'The Savings Rate', 'The lever you can actually pull.', [
    info('Share of pay',
         'The [[savings rate]] is the share of pay you do not spend. A raise helps. A lower spending number helps more, because the rate is savings divided by pay. Investment returns are a guess. The rate is a choice.'),
    num('Pay is $60,000 and you save $15,000. What is the savings rate, in percent?', 25, unit='%',
        explain='$15,000 ÷ $60,000 = 0.25, which is 25%.'),
    num('A $4,000 month with $1,000 saved is what percent?', 25, unit='%',
        explain='$1,000 ÷ $4,000 = 25%. Same rate, one month.'),
    tf('A higher savings rate requires a higher salary.', False,
       'The rate is a share. Spending less raises it even when pay stays put.'),
    num('Pay stays $60,000 and you save $6,000 instead of $15,000. What is the savings rate, in percent?', 10, unit='%',
        explain='$6,000 ÷ $60,000 = 10%.'),
])

rule = lesson('fn-four', 'The 4% Rule', 'A first-year sketch, with cracks.', [
    info('What the rule actually says',
         'The [[4% rule|four-percent-rule]] says: in year one of retirement, withdraw about 4% of the portfolio, then adjust that dollar amount for [[inflation]] each year. It is a rule of thumb from US history. A very long retirement, a crash in the first years, or fierce inflation can break it. It is not a guarantee, and it is not “spend 4% of whatever is left each year.”'),
    num('What is 4% of a $1,000,000 portfolio, in dollars, for year one?', 40000,
        '$1,000,000 × 0.04 = $40,000.'),
    num('Inflation in the example is 3%. What is the year-two withdrawal if you adjust the $40,000?', 41200,
        '$40,000 × 1.03 = $41,200. You adjust the dollars, you do not take 4% of a smaller pile.'),
    tf('The 4% rule promises the money will last no matter what the first years do.', False,
       'Bad early returns and a very long retirement are the cracks. The rule is a sketch.'),
    mc('Which version matches the rule?',
       ['Always spend 4% of this year’s balance', 'Spend about 4% in year one, then adjust those dollars for inflation', 'Spend the whole gain, every year'], 1,
       'Year one is the 4%. Later years inflate that dollar amount. They do not restart the percent on a shrunken pile.'),
])

sheet = doc('statement', 'A FI sketch',
            [('spend', 'Yearly spending', 40000), ('pile', '25 times that spending', 1000000)],
            subtitle='The 4% rule turned around',
            note='25 times spending is 1 ÷ 0.04. It is a rule of thumb, not a quote.')

number = lesson('fn-number', 'Your FI Number', 'Twenty-five times spending.', [
    info('Turn the rule around',
         'If year one is 4% of the pile, the pile is 25 times spending. That portfolio is your [[FI number]]. Spending of $40,000 points at $1,000,000. Spend less, and the number shrinks. The market still has to cooperate. The number is a target, not a balance you have.'),
    num('Yearly spending is $40,000. What is 25 times that, in dollars?', 1000000,
        doc=sheet,
        explain='25 × $40,000 = $1,000,000.'),
    num('Spending is $30,000 a year. What is the FI number?', 750000,
        '25 × $30,000 = $750,000. A lower life has a lower target.'),
    tf('The FI number is the salary you need to earn forever.', False,
       'It is a portfolio target, about 25 times spending. Pay is how you feed it. Spending is what sets it.'),
    num('How many dollars of yearly spending does a $500,000 FI number describe, at 4%?', 20000,
        '$500,000 × 0.04 = $20,000, which is the same as $500,000 ÷ 25.'),
], fmt='document')

lean = lesson('fn-lean', 'Lean or Regular', 'The number is the spending.', [
    info('Two targets, one person',
         'Regular FI uses the spending you actually want. Lean FI uses a smaller life on purpose. Neither is more virtuous. A lean [[FI number]] is just a smaller multiple. If regular spending is $40,000, the target is $1,000,000. Lean spending of $25,000 is $625,000.'),
    num('What is the lean FI number on $25,000 of yearly spending?', 625000,
        '25 × $25,000 = $625,000.'),
    num('How many fewer dollars is that than the $1,000,000 regular target?', 375000,
        '$1,000,000 − $625,000 = $375,000. The gap is the spending you agreed to skip.'),
    tf('Lean FI means the 4% rule no longer has cracks.', False,
       'A smaller pile can still be hit by a bad early retirement. Lean changes the target, not the uncertainty.'),
    mc('What actually changed between the two numbers?',
       ['The law of inflation', 'How much life you are asking the portfolio to buy', 'The federal funds rate'], 1,
       'Spending sets the number. Lean is a smaller ask.'),
])

coast = lesson('fn-coast', 'Coast FI', 'Enough that the example could finish the job.', [
    info('Stop adding, on paper',
         '[[Coast FI]] means the pile you already have could reach the [[FI number]] by a chosen age if you never add another dollar. This sketch uses an example 8% rate. The [[rule of 72]] says that doubles in about 9 years. Three doubles is 27 years, and 2 × 2 × 2 = 8. So $100,000 might become about $800,000. The 8% is an example, not a promise.'),
    num('At an example 8%, about how many years does the rule of 72 give for one doubling?', 9, unit='years',
        explain='72 ÷ 8 = 9 years. About, and only at that example rate.'),
    num('$100,000 doubles three times. About how many dollars is that?', 800000,
        '$100,000 × 2 × 2 × 2 = $800,000. Three example doubles, no new deposits.'),
    tf('Coast FI means you can stop saving and the result is guaranteed.', False,
       'The doubling is an example rate. A lower rate, or spending that creeps up, moves the finish line.'),
    mc('What are you allowed to stop, in the coast idea?',
       ['New contributions, on paper', 'Having an emergency fund', 'Paying rent'], 0,
       'Contributions. The life, the cash pile, and the guess about returns are still there.'),
])

ordinary = lesson('fn-ordinary', 'An Ordinary Income', 'The number follows spending, not a job title.', [
    info('A teacher-sized life',
         'Financial independence is not a fortune reserved for a huge salary. A household that can live on $30,000 a year is aiming at about $750,000 under the [[4% rule|four-percent-rule]]. A household that spends $80,000 is aiming at $2,000,000. The salary helps you save. The spending writes the target.'),
    num('What is the FI number for $30,000 of yearly spending?', 750000,
        '25 × $30,000 = $750,000.'),
    num('What is the FI number for $80,000 of yearly spending?', 2000000,
        '25 × $80,000 = $2,000,000.'),
    tf('A modest salary makes a FI number impossible.', False,
       'The number is 25 times spending. A modest life is a smaller number, and the savings rate is the lever.'),
    mc('Which change shrinks the FI number?',
       ['A higher spending target', 'A lower spending target', 'A scarier headline'], 1,
       'Lower spending, smaller multiple. The headline does not rewrite the formula.'),
])

low = doc('statement', 'Save 10%',
          [('save', 'Saved from $60,000 of pay', 6000)],
          subtitle='A $6,000 year')
high = doc('statement', 'Save 25%',
           [('save', 'Saved from $60,000 of pay', 15000)],
           subtitle='A $15,000 year')

paths = lesson('fn-paths', 'Two Paths', 'Same pay. Different share.', [
    info('The gap is the rate',
         'Both pages start from $60,000 of pay. One saves 10%, which is $6,000. The other saves 25%, which is $15,000. Returns are not on the page. The only difference is the [[savings rate]].'),
    mc('Which page puts more dollars to work this year?',
       [low['title'], high['title']], 1,
       docs=(low, high),
       explain='25% is $15,000. 10% is $6,000. Same pay, $9,000 more saved on the higher rate.'),
    num('How many more dollars does the 25% page save this year?', 9000,
        '$15,000 − $6,000 = $9,000.'),
    tf('The 10% page will catch up automatically, because returns are required to be higher for people who save less.', False,
       'Nothing promises a higher return for a lower rate. The deposit gap is real every year.'),
    num('Over 10 years, before any growth, how many more dollars does the 25% path deposit?', 90000,
        '10 × $9,000 = $90,000. Growth, if it comes, is on top of a larger pile.'),
], fmt='call')

dana = lesson('fn-dana', 'Dana’s 15-Year Plan', 'The target is a million. The deposits are not.', [
    info('Meet Dana',
         'Dana is 32 and a nurse. She can live on $40,000 a year, so her [[FI number]] under the 4% rule is $1,000,000. She saves $15,000 a year, a 25% rate on $60,000 of pay.\n\nFifteen years of those deposits, before any growth, are $225,000. The rest of the million would have to come from growth. She writes that down so the plan does not pretend the deposits alone finish the job.',
         ),
    num('What is Dana’s FI number?', 1000000,
        '25 × $40,000 = $1,000,000.'),
    num('How many dollars does she deposit in 15 years, before growth?', 225000,
        '15 × $15,000 = $225,000.'),
    num('How many dollars of the $1,000,000 are not covered by those deposits alone?', 775000,
        '$1,000,000 − $225,000 = $775,000. That gap is what growth would have to cover, and growth is not a promise.'),
    tf('Dana is guaranteed to reach $1,000,000 in 15 years because she has a plan.', False,
       'The deposits are $225,000. The rest depends on returns and on her spending staying near $40,000.'),
], fmt='story', story={
    'title': 'Fifteen years, written down',
    'character': 'Dana, 32, nurse',
    'body': 'Dana can live on **$40,000** a year, so her FI number is **$1,000,000**. She saves **$15,000** a year.\n\nFifteen years of deposits, before growth, are **$225,000**. She writes down the gap so the plan stays honest.',
})

write_unit('03-financial-independence.json', 'financial-independence', 3, 'Financial Independence',
           'The savings rate, the 4% sketch, and the number 25 times spending.',
           'Spending writes the target. The savings rate is the lever.',
           terms, [rate, rule, number, lean, coast, ordinary, paths, dana, review('fn'), trial('fn', 'Financial Independence', [
               num('You save $12,000 of $48,000 pay. What is the savings rate, in percent?', 25, unit='%',
                   explain='$12,000 ÷ $48,000 = 25%.'),
               num('Spending is $50,000 a year. What is the FI number under the 25-times sketch?', 1250000,
                   '25 × $50,000 = $1,250,000.'),
               tf('The 4% rule means you spend 4% of whatever balance is left, every year.', False,
                  'Year one is about 4%. Later years adjust those dollars for inflation. They do not restart the percent.'),
               num('$50,000 doubles three times at an example rate. About how many dollars is that?', 400000,
                   '$50,000 × 2 × 2 × 2 = $400,000. The rate that produced the doubles is still an example.'),
           ])],
           section=S)
