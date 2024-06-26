cost_reduction_premise = 25
cost_reduction_hypothesis = 25

# the hypothesis talks about the cost reduction in Indonesia's tin industry, which is also mentioned in the premise
if cost_reduction_hypothesis!= cost_reduction_premise:
    # check if the cost reduction percentage in the hypothesis contradicts the cost reduction percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
