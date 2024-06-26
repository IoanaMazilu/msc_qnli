butter_weight_premise = 44
butter_weight_hypothesis = 84

# the hypothesis refers to the weight of butter mentioned in the premise
if butter_weight_premise >= butter_weight_hypothesis:
    # check if the weight of butter in the premise contradicts the estimate of less than 'butter_weight_hypothesis'
    label = "contradiction"
else:
    # if the weight of butter in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
# 