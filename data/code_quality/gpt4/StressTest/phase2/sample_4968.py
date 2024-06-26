butter_weight_premise = 34
butter_weight_hypothesis = 44

# the hypothesis refers to the weight of butter mentioned in the premise
if butter_weight_hypothesis <= butter_weight_premise:
    # check if the estimate of 'butter_weight_hypothesis' contradicts the weight of butter in the premise
    label = "contradiction"
elif butter_weight_premise >= butter_weight_hypothesis:
    # check if the weight of butter in the premise contradicts the estimate of 'butter_weight_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
