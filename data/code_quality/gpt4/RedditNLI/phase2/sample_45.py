percentage_income_gains_premise = 95
percentage_income_gains_hypothesis = 95

# the hypothesis and premise mention the percentage of income gains captured by the top 1%
if percentage_income_gains_premise != percentage_income_gains_hypothesis:
    # check if the percentage of income gains in the hypothesis contradicts the percentage of income gains in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
