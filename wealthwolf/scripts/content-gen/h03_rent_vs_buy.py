from lib import *

S = 'home-life'
terms = {}

beyond = lesson('rb-beyond', 'More Than the Mortgage', 'The loan payment is one line of owning.', [
    info('Four monthly lines',
         'On this house the [[mortgage]] payment is **$1,400**. Property tax is **$3,000** a year, which is **$250** a month. Insurance is **$1,200** a year, which is **$100** a month. A 1% repair sketch on a **$300,000** home is **$3,000** a year, or **$250** a month.'),
    num('What is the tax bill per month if the year is $3,000?', 250, '$3,000 ÷ 12 = $250.'),
    num('What is the insurance per month if the year is $1,200?', 100, '$1,200 ÷ 12 = $100.'),
    num('What is 1% of a $300,000 home, per year, as a repair sketch?', 3000, '$300,000 × 0.01 = $3,000.'),
    num('Add the mortgage, the monthly tax, the monthly insurance, and a $250 repair set-aside. What is the month?', 2000,
        '$1,400 + $250 + $100 + $250 = $2,000.'),
])

five = lesson('rb-five', 'The 5-Year Sketch', 'Buying has a cover charge. A short stay may not earn it back.', [
    info('A rule of thumb',
         'People often say: if you will move within about five years, renting can win, because buying and selling cost real money up front.\n\nIt is a sketch. A hot market or a cheap rental can flip it. On this purchase, closing costs are **$9,000**.'),
    num('You will stay 3 years. Closing costs are $9,000. How much is that per year of the stay?', 3000,
        '$9,000 ÷ 3 = $3,000 a year.'),
    num('How much is that $9,000 per month over those 36 months?', 250,
        '$9,000 ÷ 36 = $250 a month.'),
    mc('You know the job moves you in two years. What does the 5-year sketch suggest?',
       ['Lean toward renting, and run the closing costs before you buy', 'Buy, because a mortgage is always cheaper than rent', 'Ignore closing costs, since you get them back at the sale'], 0,
       'Two years is inside the window where the cover charge is hard to earn back.'),
    tf('The 5-year sketch is a law that forbids buying if you might move.', False,
       'It is a rule of thumb. The costs, not the slogan, decide it.'),
])

opp = lesson('rb-opp', 'The Down Payment’s Other Job', 'Cash in the house cannot also be your cushion.', [
    info('A dollar has one seat',
         'A [[down payment]] of **$40,000** is no longer an emergency fund, and it is no longer earning interest in savings.\n\nAt an example rate of **4%** a year, that cash would earn **$1,600**. The 4% is an example, not a promise. The [[opportunity cost]] is what you give up by using the money here.'),
    num('What is 4% of a $40,000 down payment for one year, at that example rate?', 1600,
        '$40,000 × 0.04 = $1,600.'),
    num('What is 20% down on a $200,000 home?', 40000, '$200,000 × 0.20 = $40,000.'),
    mc('You have $40,000 and no other savings. You put all of it down. What did you give up?',
       ['A cash cushion for a job loss or a repair', 'The right to live in the house', 'The mortgage payment'], 0,
       'The house got the only cash you had. A broken furnace or a lost job now has nothing to draw on.'),
    tf('A down payment is free money because it lowers the loan.', False,
       'It lowers the loan. It is still your cash, and it cannot do a second job at the same time.'),
])

flex = lesson('rb-flex', 'Flexibility or Equity', 'Renting buys an exit. Buying buys a stake.', [
    info('Two different products',
         'Rent is a service with an end date. A home you own is an asset you must also maintain.\n\nNeither one is morally better. They fit different years of a life.'),
    sort('Sort each fact.',
         ['Renting', 'Buying'],
         [('You can leave when the lease ends', 0),
          ('You are building a stake in the home', 1),
          ('A job in another city is easier to take', 0),
          ('You pay when the roof fails', 1)],
         'Renting keeps the exit open. Buying builds a stake and hands you the repairs.'),
    mc('You want the freedom to move for work next year. Which fact matters most?',
       ['You can leave when the lease ends', 'You are building a stake in the home', 'You pay when the roof fails'], 0,
       'A one-year plan fits an exit more than a stake.'),
    tf('Buying means you can move next month with no extra cost.', False,
       'Selling or renting the place out takes time and money. The lease is the easier exit.'),
    fill('The stake you build by paying down a home is often called ___.',
         ['equity', 'a fee', 'a premium'], 0,
         'Equity is what you own: the value minus what you still owe.'),
], fmt='sort')

rent_doc = doc('statement', 'Keep renting', [
    ('rent', 'Monthly rent', 1800),
], subtitle='One line')
buy_doc = doc('statement', 'Buy this house', [
    ('mort', 'Mortgage payment', 1400),
    ('tax', 'Property tax', 250),
    ('ins', 'Home insurance', 100),
    ('fix', 'Repair set-aside', 250),
], subtitle='Four lines', totals=[('Monthly', 2000, True)])
assert 1400 + 250 + 100 + 250 == 2000 and 2000 - 1800 == 200 and 1800 * 12 == 21600 and 2000 * 12 == 24000

call = lesson('rb-call', 'Two Pages, One Month', 'Put the rent next to the full cost of owning.', [
    num('What is a year of the $1,800 rent?', 21600, '$1,800 × 12 = $21,600.', docs=[rent_doc, buy_doc]),
    num('What is the buy page per month?', 2000,
        '$1,400 + $250 + $100 + $250 = $2,000.', docs=[rent_doc, buy_doc]),
    num('What is a year of that $2,000 owning cost?', 24000, '$2,000 × 12 = $24,000.', docs=[rent_doc, buy_doc]),
    num('How much more is owning than renting, per month, on these two pages?', 200,
        '$2,000 − $1,800 = $200.', docs=[rent_doc, buy_doc]),
    mc('These two pages, and only these two pages. Which costs less each month?',
       ['Renting, at $1,800', 'Owning, at $2,000', 'They match'], 0,
       'Rent is $200 less on this pair. Owning may still win over a long stay because some of the mortgage builds equity. This month’s cash does not show that.',
       docs=[rent_doc, buy_doc]),
], fmt='call')

wins = lesson('rb-wins', 'When Renting Wins', 'A short stay, a thin cushion, or a job that moves.', [
    info('Three good reasons',
         'Renting fits when you will not stay long, when the down payment would empty your savings, or when the job can send you to another city.\n\nOn the pair you just saw, rent is **$1,800** and the full owning cost is **$2,000**.'),
    mc('Your emergency fund would have to become the down payment. What is the careful read?',
       ['Rent until the down payment is extra money, not your only money', 'Buy, and hope nothing breaks', 'Borrow the emergency fund from a credit card'], 0,
       'A house with no cash behind it is a fragile win.'),
    num('Owning is $200 more per month than renting. Over 12 months, how much more cash is that?', 2400,
        '$200 × 12 = $2,400.'),
    tf('Renting is the better cash-flow choice on these pages for a one-year stay.', True,
       'You pay $1,800 instead of $2,000, and you do not pay closing costs for a year you will not keep.'),
    fill('If the down payment is your only savings, buying spends your ___.',
         ['cushion', 'rent', 'credit score'], 0,
         'The cushion is what a job loss or a repair draws on. Do not spend the last of it to get the keys.'),
])

myth = lesson('rb-myth', '“Throwing Money Away”', 'Rent buys a home for the month. Owning wastes money too.', [
    info('Count the money that does not build a stake',
         'Rent of **$1,800** buys the month. It does not build equity. That part of the proverb is true.\n\nIt skips the owner’s leaks. In this sketch the **$1,400** mortgage sends **$1,000** to [[interest]] and **$400** to [[principal]]. Tax **$250**, insurance **$100**, and repairs **$250** build no equity either.'),
    num('In this sketch, how much of the owner’s month does not build equity?', 1600,
        '$1,000 interest + $250 tax + $100 insurance + $250 repairs = $1,600.'),
    num('Rent is $1,800. The owner’s non-equity costs are $1,600. How much more is the rent than those costs?', 200,
        '$1,800 − $1,600 = $200. Close, not “all rent is wasted.”'),
    mc('What is wrong with “rent is throwing money away”?',
       ['It ignores interest, tax, insurance, and repairs', 'Rent does not buy you a place to live', 'Owners never pay interest'], 0,
       'Both paths spend money that builds nothing. The proverb only counts one of them.'),
    tf('In this sketch, every dollar of the $1,400 mortgage builds equity.', False,
       'Only the $400 of principal does. The $1,000 of interest is the cost of borrowing.'),
])

sam_story = {
    'title': 'Sam’s two-year contract',
    'character': 'Sam, 29',
    'body': 'Sam is 29 and a nurse. The contract that brought him here ends in **two years**. Closing costs on the house he likes are **$8,400**.\n\nRent nearby is **$1,800** a month. The down payment would be **$40,000**, and that is most of what he has saved.\n\nHe runs the cover charge across the stay he actually has, not across a stay he hopes for.',
}
sam = lesson('rb-sam', 'Sam’s Decision', 'A two-year contract is a renter’s calendar.', [
    num('Sam’s closing costs are $8,400 over 24 months. How much is that per month?', 350,
        '$8,400 ÷ 24 = $350.'),
    num('What is two years of his $1,800 rent?', 43200, '$1,800 × 24 = $43,200.'),
    mc('He will leave in two years, and the $40,000 is most of his savings. What fits the story?',
       ['Rent, and keep the $40,000 as savings', 'Buy, because rent is throwing money away', 'Empty the savings so the mortgage is smaller'], 0,
       'The stay is short, and the down payment is his cushion. The 5-year sketch points at renting.'),
    tf('Sam gets the $8,400 of closing costs back automatically when he sells in two years.', False,
       'Closing costs are spent. A sale has its own costs on top.'),
    fill('Sam should judge the house against a stay of ___, the length he actually has.',
         ['two years', 'thirty years', 'one month'], 0,
         'A 30-year loan does not mean he will stay 30 years.'),
], fmt='story', story=sam_story)

trial_steps = [
    num('Tax is $2,400 a year. What is that per month?', 200, '$2,400 ÷ 12 = $200.'),
    mc('You will move in 18 months and closing costs are several thousand dollars. What does the 5-year sketch lean toward?',
       ['Renting', 'Buying and selling again next spring', 'Ignoring the closing costs'], 0,
       'A short stay rarely earns back the cover charge.'),
    num('A $20,000 down payment at an example 4% would earn how much in a year?', 800,
        '$20,000 × 0.04 = $800. The rate is an example.'),
    tf('On a fair comparison, you line the rent up against the mortgage payment alone.', False,
       'Owning also has tax, insurance, and repairs.'),
]

lessons = [beyond, five, opp, flex, call, wins, myth, sam,
           review('rb'), trial('rb', 'Rent vs. Buy', trial_steps)]
write_unit('03-rent-vs-buy.json', 'rent-vs-buy', 3, 'Rent vs. Buy',
           'The full cost of owning, the 5-year sketch, and the proverb that only counts rent.',
           'Rent buys the month. Owning buys a stake, and a list of bills.', terms, lessons, section=S)
