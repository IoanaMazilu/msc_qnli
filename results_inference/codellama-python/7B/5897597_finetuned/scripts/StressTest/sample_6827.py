arun_deepak_ratio_premise = 4/3
arun_deepak_ratio_hypothesis = 1/3

# the hypothesis refers to the ratio of ages of Arun and Deepak mentioned in the premise
if arun_deepak_ratio_premise!= arun_deepak_ratio_hypothesis:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)