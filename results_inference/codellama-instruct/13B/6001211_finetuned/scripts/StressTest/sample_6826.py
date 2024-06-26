arun_deepak_ratio_premise = 3/3
arun_deepak_ratio_hypothesis = 4/3

# the hypothesis refers to the age ratio of Arun and Deepak mentioned in the premise
if arun_deepak_ratio_hypothesis <= arun_deepak_ratio_premise:
    # check if the age ratio in the hypothesis contradicts the age ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the age ratio
    # any age ratio greater than 'arun_deepak_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
