# Premise: Global Debt Has Soared By $57 Trillion Since The 2007-08 Financial Crisis.
# Hypothesis: Global debt has grown by $57 trillion in seven years following the financial crisis.
# Golden Label: entailment

debt_increase_premise = 57
debt_increase_hypothesis = 57

# the hypothesis and premise mention the increase in global debt
if debt_increase_hypothesis != debt_increase_premise:
    # check if the amount of debt increase in the hypothesis contradicts the amount of debt increase in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

