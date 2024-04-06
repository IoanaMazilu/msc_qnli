# Premise: Global Debt Has Soared By $57 Trillion Since The 2007-08 Financial Crisis.
# Hypothesis: Global debt up $57 TRILLION since crisis: Report.
# Golden Label: entailment

debt_increase_premise = 57
debt_increase_hypothesis = 57

# the hypothesis and premise mention the increase in global debt since the 2007-08 financial crisis
if debt_increase_hypothesis != debt_increase_premise:
    # check if the debt increase in the hypothesis contradicts the debt increase in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

