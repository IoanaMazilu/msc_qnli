# Premise: At DAVOS, Financial Billionaire Schwartzman, who took home over $600 million dollars last year, says he doesn't understand why americans are angry.
# Hypothesis: At Davos, Wall Street Billionaire Mr Schwartzfman, who takes home every year over $500 million dollars, says he doesn't understand why americans are angry.
# Golden Label: entailment

income_premise = 600
income_hypothesis = 500

# the hypothesis and premise mention the money Schwartzman takes home every year
if income_hypothesis > income_premise:
    # check if the income in the hypothesis contradicts the income in the premise
    label = "contradiction"
elif income_hypothesis < income_premise:
    # check if the income in the hypothesis is less than the income in the premise
    # this does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis income is the same as the premise income, we can infer entailment
    label = "entailment"

print(label)

