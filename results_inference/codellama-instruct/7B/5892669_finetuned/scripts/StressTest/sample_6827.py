arun_deepak_ratio_premise = 4/3
arun_deepak_ratio_hypothesis = 1/3

# the hypothesis refers to the ratio of ages of Arun and Deepak mentioned in the premise
if arun_deepak_ratio_hypothesis!= arun_deepak_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)
