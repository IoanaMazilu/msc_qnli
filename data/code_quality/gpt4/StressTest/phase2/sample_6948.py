arun_deepak_ratio_premise = 5/4
arun_deepak_ratio_hypothesis = 1/4

# the hypothesis talks about the ratio between the ages of Arun and Deepak, referenced also in the premise
if arun_deepak_ratio_hypothesis >= arun_deepak_ratio_premise:
    # check if the hypothesis value contradicts the premise ratio
    label = "contradiction"
elif arun_deepak_ratio_hypothesis < arun_deepak_ratio_premise:
    # the premise gives a specific ratio for the ages of Arun and Deepak
    # any ratio less than 'arun_deepak_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the ratio in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
