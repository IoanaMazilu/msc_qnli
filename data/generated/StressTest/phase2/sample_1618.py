# Premise: At present, the ratio between the ages of Arun and Deepak is more than 2:3.
# Hypothesis: At present, the ratio between the ages of Arun and Deepak is 4:3.
# Golden Label: neutral

arun_deepak_ratio_premise = 2/3
arun_deepak_ratio_hypothesis = 4/3

# the hypothesis refers to the ratio of ages of Arun and Deepak mentioned in the premise
if arun_deepak_ratio_hypothesis <= arun_deepak_ratio_premise:
    # check if the ratio in 'arun_deepak_ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of ages
    # any ratio greater than 'arun_deepak_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

