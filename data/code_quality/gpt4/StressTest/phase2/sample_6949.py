arun_deepak_ratio_premise = 1/4
arun_deepak_ratio_hypothesis = 5/4

# the hypothesis refers to the ratio of ages between Arun and Deepak as mentioned in the premise
if arun_deepak_ratio_hypothesis <= arun_deepak_ratio_premise:
    # check if the hypothesis ratio contradicts the premise ratio
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio
    # a ratio higher than 'arun_deepak_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
