# Premise: At Davos, Wall Street Billionaire Steven Schwartzfman, who takes home every year around $700 million dollars, says he doesn't understand why americans are angry.
# Hypothesis: At DAVOS, Financial Billionaire Schwartzman, who took home over $600 million dollars last year, says he doesn't understand why americans are angry.
# Golden Label: entailment

annual_income_premise = 700
annual_income_hypothesis = 600

# the hypothesis and premise mention the annual income of Steven Schwartzman
if annual_income_hypothesis > annual_income_premise:
    # check if the annual income in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the annual income in the hypothesis is less or equal to the amount in the premise, it is consistent with the premise but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

