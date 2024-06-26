cost_increase_premise = 190
cost_increase_hypothesis = 190

# the hypothesis and premise mention the increase in labour costs for Loblaw due to higher minimum wage rules
if cost_increase_premise!= cost_increase_hypothesis:
    # check if the cost increase in the hypothesis contradicts the cost increase in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)