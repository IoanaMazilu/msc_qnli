minimum_wage_premise = 190
minimum_wage_hypothesis = 190

# the hypothesis and premise mention the same amount of money in labour costs
if minimum_wage_premise!= minimum_wage_hypothesis:
    # check if the amount of money in the hypothesis contradicts the amount of money in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
