arun_deepak_ratio_premise = 5/4
arun_deepak_ratio_hypothesis = 1/4

# the hypothesis refers to the ratio of ages of Arun and Deepak mentioned in the premise
if arun_deepak_ratio_hypothesis >= arun_deepak_ratio_premise:
    # check if the estimate of 'arun_deepak_ratio_hypothesis' contradicts the ratio of ages in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
