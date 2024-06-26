deals_cost_premise = 1
deals_cost_hypothesis = 1

# the hypothesis mentions the cost of the investigation to Hernandez, which is also mentioned in the premise
if deals_cost_hypothesis!= deals_cost_premise:
    # check if the number of deals cost in the hypothesis contradicts the number of deals cost reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
