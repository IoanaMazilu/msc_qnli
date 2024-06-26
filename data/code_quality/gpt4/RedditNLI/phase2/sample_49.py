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
