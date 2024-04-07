# Premise: At present, the ratio between the ages of Arun and Deepak is less than 5:3.
# Hypothesis: At present, the ratio between the ages of Arun and Deepak is 4:3.
# Golden Label: neutral

arun_deepak_ratio_premise = 5 / 3
arun_deepak_ratio_hypothesis = 4 / 3

# the hypothesis talks about the ratio of ages of Arun and Deepak, mentioned also in the premise
if arun_deepak_ratio_hypothesis >= arun_deepak_ratio_premise:
    # check if the hypothesis value contradicts the estimate of less than 'arun_deepak_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of ages
    # any ratio less than 'arun_deepak_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

