min_wage_premise = 15
min_wage_hypothesis = 15

# the hypothesis and premise mention the same minimum wage value
if min_wage_premise!= min_wage_hypothesis:
    # check if the minimum wage in the hypothesis contradicts the minimum wage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
