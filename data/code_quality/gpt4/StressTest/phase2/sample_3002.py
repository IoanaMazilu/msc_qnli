arun_deepak_ratio_premise = 4 / 3
arun_deepak_ratio_hypothesis = 4 / 3

# The hypothesis refers to the age ratio of Arun and Deepak mentioned in the premise
if arun_deepak_ratio_hypothesis >= arun_deepak_ratio_premise:
    # check if the age ratio in the hypothesis contradicts the age ratio reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
