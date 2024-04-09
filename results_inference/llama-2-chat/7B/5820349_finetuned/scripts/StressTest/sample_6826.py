arun_deepak_ratio_premise = 3/3
arun_deepak_ratio_hypothesis = 4/3

# the hypothesis talks about the ratio between the ages of Arun and Deepak, referenced also in the premise
if arun_deepak_ratio_hypothesis <= arun_deepak_ratio_premise:
    # check if the hypothesis value contradicts the estimate of more than 'arun_deepak_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio
    # any ratio greater than 'arun_deepak_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
