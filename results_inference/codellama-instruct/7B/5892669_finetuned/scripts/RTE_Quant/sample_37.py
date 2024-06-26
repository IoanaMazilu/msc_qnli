production_cost_reduction_premise = 25
production_cost_reduction_hypothesis = 25

# the hypothesis talks about the production cost reduction in Indonesia, which is also mentioned in the premise
if production_cost_reduction_hypothesis!= production_cost_reduction_premise:
    # check if the production cost reduction percentage in the hypothesis contradicts the production cost reduction percentage from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
