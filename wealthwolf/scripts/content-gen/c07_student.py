from lib import *

S = 'credit-debt'
terms = {
    'subsidized-loan': term('Subsidized loan', 'A federal student loan where the government pays the interest while you are in school at least half time, and during the grace period.',
                            'A $3,500 subsidized loan sits through four years of school and adds $0 of interest while you are enrolled.'),
    'unsubsidized-loan': term('Unsubsidized loan', 'A federal student loan where interest starts while you are still in school. You can pay it as you go, or let it be added to the balance.',
                              '$3,500 unsubsidized at 6% adds about $210 of interest in one year of school.'),
    'income-driven-repayment': term('Income-driven repayment', 'A federal plan that sets the monthly payment from your income and family size, instead of a fixed amount that clears the loan in 10 years.',
                                    'A standard plan might ask $180. An income-driven plan might ask $70 while your pay is low. The names and rules depend on when the loan was made.'),
}

fed = lesson('sl-federal-private', 'Federal or Private', 'Federal loans come with rules a bank loan does not have to offer.', [
    mc('Which loan is made through the federal student-aid program?',
       ['A federal student loan', 'A private loan from a bank', 'A credit card'], 0,
       'Federal loans are the ones with the government rulebook.',
       context='A federal student loan comes through the U.S. student-aid program. A private student loan comes from a bank or other lender. Federal loans can offer income-based payments and other protections. Private loans often start charging interest immediately and set their own rules.'),
    tf('A private student loan has to offer the same repayment plans as a federal loan.', False,
       'Private lenders set their own terms. Read them.'),
    mc('You are offered both. Which one do people usually use first?',
       ['The federal loan, and only then consider private', 'The private loan, because the ads are bigger', 'A credit card for tuition'], 0,
       'Federal loans first. Private loans fill a gap, they do not replace the safer option.'),
    mc('Where do you check which federal plans your loan can use?',
       ['studentaid.gov', 'Your bank’s website', 'The lender’s ads'], 0,
       'The official site. Plan names change, and 2026 is not 2019.'),
    match('Match the lender to the loan.',
          [('U.S. student-aid program', 'Federal student loan'), ('A bank', 'Private student loan'), ('A card issuer', 'Not a student loan at all')]),
    tf('Putting tuition on a credit card is the same as a federal student loan.', False,
       'A card has none of the federal protections, and a much higher rate.'),
])

sub = lesson('sl-subsidized', 'Subsidized or Not', 'One loan waits. The other starts the meter in the classroom.', [
    mc('Who pays the interest on a subsidized loan while you are in school at least half time?',
       ['The government', 'You, every month', 'Your employer'], 0,
       'That is the subsidy.',
       context='On a [[subsidized loan]], the government pays the interest while you are in school at least half time. On an [[unsubsidized loan]], interest starts right away. You can pay that interest while you study, or let it join the balance later.'),
    tf('An unsubsidized loan charges no interest until you graduate.', False, 'The interest starts in school.'),
    mc('Both loans are $3,500. Which one can grow while you are still in class?',
       ['The unsubsidized loan', 'The subsidized loan', 'Neither'], 0,
       'Unsubsidized interest does not wait for graduation.'),
    mc('You can pay the unsubsidized interest while you are in school. Why bother?',
       ['So it is not added to the balance you repay later', 'Because the school requires it', 'It raises the subsidized rate'], 0,
       'Interest you let pile up becomes principal.'),
    fill('The government covers in-school interest on a ___ loan.', ['subsidized', 'unsubsidized', 'private'], 0, 'Subsidized.'),
    tf('Subsidized loans are limited. Not every student, and not every dollar, qualifies.', True,
       'There are caps. Anything above them is often unsubsidized.'),
])

amina_story = {
    'title': 'Two loans, one year',
    'character': 'Amina, 20, community-college student',
    'body': 'Amina takes **$3,500** in a subsidized loan and **$3,500** in an unsubsidized loan for the year. The unsubsidized rate is **6%**.\n\n'
            'She works part time and can spare **$20** a month. She wants to know what the unsubsidized loan costs if she lets the interest sit for this one year of school.',
}
assert round(3500 * 0.06) == 210 and 20 * 12 == 240
amina = lesson('sl-amina', 'Amina’s Year in School', 'Same dollar amount. Only one of the loans grows.', [
    num('Using simple interest, how much interest does the unsubsidized $3,500 add in one year at 6%?', 210,
        '$3,500 × 0.06 × 1 = $210. Real loans compound, so treat this as the clean estimate.'),
    num('How much interest does the subsidized $3,500 add during that same year in school?', 0,
        '$0. The government covers it while she is enrolled at least half time.'),
    num('If she pays $20 a month toward the unsubsidized interest, how much does she pay in a year?', 240, '$20 × 12 = $240.'),
    mc('Her $240 of payments against $210 of simple interest. What is true?',
       ['She covered that year’s interest and a little more', 'She still owes all $210 on top', 'The subsidized loan also grew by $210'], 0,
       '$240 − $210 = $30 to the good, on this simple estimate.'),
    tf('Letting the $210 sit means she repays it later, with interest on a bigger balance.', True,
       'Unpaid interest can be added to the principal.'),
    mc('What is the careful habit for the unsubsidized loan?',
       ['Pay the interest while she is in school, if the $20 fits', 'Ignore it until the bill is huge', 'Move it onto a credit card'], 0,
       'Small payments now beat a larger balance later.'),
], fmt='story', story=amina_story)

grace = lesson('sl-after-school', 'Before the First Bill', 'Federal loans usually give you months after school, not a bill on graduation day.', [
    mc('Most federal student loans give you about how long after leaving school before payments start?',
       ['6 months', '6 weeks', '6 days'], 0,
       'About six months. Use them. Do not spend them by accident.',
       context='After you leave school, most federal loans wait about six months before the first bill. Interest on an unsubsidized loan still exists. A subsidized loan’s interest break usually covers this wait too. Confirm the date on studentaid.gov so it does not surprise you.'),
    tf('An unsubsidized loan stops charging interest during those six months.', False,
       'The payment waits. The interest on an unsubsidized loan does not.'),
    num('Using half a year of 6% on the original $3,500, about how much interest builds in those 6 months?', 105,
        'Half of 6% is 3%. $3,500 × 0.03 = $105.'),
    mc('What should you do during the six months?',
       ['Find the servicer, set a payment method, and pick a plan before the first due date', 'Throw the mail away', 'Assume the loan ended with the classes'], 0,
       'The pause is for getting ready, not for forgetting.'),
    tf('You can apply for an income-driven plan before the first payment is due.', True,
       'Doing it early means the first bill is the one you actually chose.'),
    mc('Who tells you the real due date?',
       ['Your loan servicer, and studentaid.gov', 'A classmate', 'The college admissions office'], 0,
       'The servicer is the company that collects the payments.'),
])

plans = lesson('sl-plans', 'Repayment Plans', 'One plan is a fixed payoff. Another follows your paycheck. The list changes, so check it.', [
    info('Plans change. Check the official list',
         'A standard plan uses a fixed payment meant to clear the loan in about 10 years. An [[income-driven repayment]] plan sets the payment from your income instead.\n\n'
         'The Saving on a Valuable Education (SAVE) plan was blocked by the courts, and Congress voted in 2025 to phase it out. It isn’t open to new borrowers. Which other plans you can use depends on when your loan was made. Check studentaid.gov before you pick.'),
    mc('What does a standard plan try to do?',
       ['Pay the loan off on a fixed schedule, often about 10 years', 'Set the payment from your income', 'Erase the loan at graduation'], 0,
       'Fixed payment, fixed clock.'),
    mc('What does an income-driven plan look at?',
       ['Your income and family size', 'Only the school’s ranking', 'Your credit score'], 0,
       'The payment follows the paycheck. A lower payment can mean more interest over time.'),
    tf('In 2026, new borrowers should enroll in the SAVE plan.', False,
       'SAVE isn’t open to new borrowers. Use the plans studentaid.gov lists for your loan.'),
    mc('A lower monthly payment under an income-driven plan can mean…',
       ['You pay for longer, and you may pay more interest', 'The loan is free', 'The principal vanishes'], 0,
       'Smaller is not the same as cheaper.'),
    mc('Some balances can be forgiven after many years of qualifying payments. What is the careful take?',
       ['Treat it as possible, and confirm the current rules on studentaid.gov before you count on a dollar', 'It is guaranteed for every loan', 'Forgiveness happens automatically after 12 months'], 0,
       'Programs exist. The details move. Education, not a promise.'),
])

sum_lines = [
    ('prin', 'Principal', 15000),
    ('accr', 'Interest already accrued', 800),
    ('pay', 'Standard-plan payment', 180),
]
assert 180 * 120 == 21600 and 21600 - 15800 == 5800 and 15000 + 800 == 15800
SUMMARY = doc('statement', 'Federal loan summary', sum_lines, subtitle='Servicer: example · 2026',
              meta=[['Repayment term on the standard plan', '10 years']],
              totals=[('Balance to repay before future interest', 15800, True)],
              note='The $180 payment is the standard plan. 120 payments of $180 include future interest.')
summary = lesson('sl-summary', 'The Loan Summary', 'Principal, interest already added, and the payment they are asking.', [
    num('What is the principal?', 15000, 'The amount borrowed: $15,000.',
        context='A loan summary shows what you borrowed, interest already added, and the payment of the plan you are on.',
        doc=SUMMARY),
    num('How much interest has already been added?', 800, 'The accrued line: $800.', doc=SUMMARY),
    num('What is the balance before any future interest?', 15800, '$15,000 + $800 = $15,800.', doc=SUMMARY),
    num('The standard payment is $180 for 10 years (120 months). How much do you pay in total on that plan?', 21600,
        '$180 × 120 = $21,600.', doc=SUMMARY),
    num('How much of that $21,600 is interest, above the $15,800 you owe today?', 5800, '$21,600 − $15,800 = $5,800.'),
    tf('The $180 payment includes only the $15,800. Future interest is extra on top of the $21,600.', False,
       'The $21,600 already includes the interest inside those 120 payments.'),
], fmt='document')

school_a = [
    ('loan', 'Loans at graduation', 18000),
]
school_b = [
    ('loan', 'Loans at graduation', 40000),
]
assert 40000 - 18000 == 22000
SCH_A = doc('statement', 'School A', school_a, subtitle='Same career goal', totals=[('Debt at graduation', 18000, True)])
SCH_B = doc('statement', 'School B', school_b, subtitle='Same career goal', totals=[('Debt at graduation', 40000, True)])
school = lesson('sl-school-cost', 'Choose the School with the Cost', 'The job can be the same. The debt will not be.', [
    num('How much more does School B cost in loans than School A?', 22000, '$40,000 − $18,000 = $22,000.',
        context='If two schools lead to the same work, the cheaper debt is the stronger start. Run the loans, not the brochure.',
        docs=[SCH_A, SCH_B]),
    mc('The likely job is the same. Which leaving debt is easier to live with?',
       ['$18,000', '$40,000', 'They are equal because the job title matches'], 0,
       '$22,000 less to repay.',
       why=['Less principal, less interest.', 'More than double the debt.', 'The title matches. The bill does not.']),
    num('School A at a rough $200 a month would take how many months to pay $18,000, ignoring interest?', 90,
        '$18,000 ÷ $200 = 90 months, which is 7 years and 6 months. Interest makes it longer.', unit='months'),
    tf('A more expensive school is worth it whenever the campus is nicer.', False,
       'Worth it depends on the pay you can earn and the debt you can carry.'),
    mc('What belongs in the comparison?',
       ['Loans at graduation, not just this year’s tuition sticker', 'Only this year’s tuition', 'The school’s ranking alone'], 0,
       'The number you repay is the one that matters.'),
    mc('You can work a year and cut School B’s loans by $8,000. What is the new gap versus School A’s $18,000?',
       ['$14,000 more than School A', '$8,000 more', 'School B becomes cheaper'], 0,
       '$40,000 − $8,000 = $32,000. $32,000 − $18,000 = $14,000 still more.'),
], fmt='call')

trial_steps = [
    mc('Interest on which federal loan starts while you are still in school?',
       ['Unsubsidized', 'Subsidized', 'Neither'], 0, 'Unsubsidized interest does not wait.'),
    num('$4,000 unsubsidized at 5% simple interest for 2 years in school. How much interest?', 400, '$4,000 × 0.05 × 2 = $400.'),
    tf('New borrowers could still sign up for the SAVE repayment plan in 2026.', False, 'Courts blocked SAVE and a 2025 law is phasing it out. studentaid.gov lists the plans open to you.'),
    num('A summary shows $200 a month for 10 years. What do those payments add up to?', 24000, '$200 × 120 = $24,000.'),
]

lessons = [fed, sub, amina, grace, plans, summary, school,
           lesson('sl-cap', 'Borrow Less Than They Offer', 'The school can offer more than the degree is worth to you.', [
               mc('The aid letter offers $12,000. Your budget says you need $9,000. What can you do?',
                  ['Borrow the $9,000', 'You must take the full $12,000', 'Borrow $20,000 to be safe'], 0,
                  'You can take less than the offer.',
                  context='An aid offer is a maximum, not a target. Every extra dollar is [[principal]] you repay with [[interest]].'),
               num('You decline $3,000 of the offer. At 5% simple interest for 4 years in school, about how much unsubsidized interest do you avoid?',
                   600, '$3,000 × 0.05 × 4 = $600, before any interest after graduation.'),
               tf('Taking the maximum loan is required if you want the classes.', False, 'Borrow what you need. Leave the rest.'),
               num('Those $3,000, repaid later as $75 a month, take how many months if you ignore interest?', 40,
                   '$3,000 ÷ $75 = 40 months.', unit='months'),
               mc('What is a practical way to need less?',
                  ['A cheaper term, a scholarship, or working a few shifts', 'A second private loan', 'Skipping the bill'], 0,
                  'Fewer dollars borrowed is the only guaranteed forgiveness.'),
               fill('An aid offer is a ___, not a bill you must borrow in full.', ['maximum', 'minimum', 'fine'], 0, 'You can borrow less.'),
           ]),
           review('sl'), trial('sl', 'Student Loans', trial_steps)]
write_unit('07-student-loans.json', 'student-loans', 7, 'Student Loans',
           'Federal and private, subsidized and not, and what the payment becomes.',
           'The school ends. The loan does not. Know which kind you signed.', terms, lessons, section=S)
