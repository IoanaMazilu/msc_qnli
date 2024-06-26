arun_deepak_ratio_premise = 4/3
arun_deepak_ratio_hypothesis = 1/3

# the hypothesis refers to the age ratio of Arun and Deepak mentioned in the premise
if arun_deepak_ratio_hypothesis!= arun_deepak_ratio_premise:
    # check if the age ratio in the hypothesis contradicts the age ratio in the premise
    label = "contradiction"
else:
    # if the age ratios in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
