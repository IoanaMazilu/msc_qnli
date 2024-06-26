peak_weight_premise = 405
peak_weight_hypothesis = 405

# the hypothesis mentions the peak weight of the person, which is also mentioned in the premise
if peak_weight_hypothesis != peak_weight_premise:
    # check if the peak weight in the hypothesis contradicts the peak weight reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
