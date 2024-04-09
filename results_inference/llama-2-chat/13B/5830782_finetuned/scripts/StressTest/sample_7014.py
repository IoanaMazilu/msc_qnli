ratio_premise = 1/2
ratio_hypothesis = 6/2

# the hypothesis refers to the ratio of ages of Lewis and Brown mentioned in the premise
if ratio_premise >= ratio_hypothesis:
    # check if the ratio in the premise contradicts the estimate of 'less than ratio_hypothesis'
    label = "contradiction"
else:
    # if the ratio in the premise does not contradict the ratio in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
