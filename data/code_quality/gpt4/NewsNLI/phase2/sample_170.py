cost_percentage_premise = 0.25
cost_percentage_hypothesis = 0.25

# the hypothesis mentions the percentage of the ticket cost charged by Fixed, which is also mentioned in the premise
if cost_percentage_hypothesis != cost_percentage_premise:
    # check if the percentage cost in the hypothesis contradicts the percentage cost reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
