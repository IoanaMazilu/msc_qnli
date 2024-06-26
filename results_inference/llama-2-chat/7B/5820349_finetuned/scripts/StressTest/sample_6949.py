arun_deepak_ratio_premise = 1/4
arun_deepak_ratio_hypothesis = 5/4

# the hypothesis refers to the age ratio of Arun and Deepak mentioned in the premise
if arun_deepak_ratio_hypothesis <= arun_deepak_ratio_premise:
    # check if the age ratio in the hypothesis contradicts the estimate of more than 'arun_deepak_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the age ratio
    # any age ratio greater than 'arun_deepak_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)