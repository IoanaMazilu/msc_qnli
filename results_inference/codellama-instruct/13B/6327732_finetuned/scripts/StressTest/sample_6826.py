age_ratio_premise = 3
age_ratio_hypothesis = 4

# the hypothesis refers to the ratio between the ages of Arun and Deepak mentioned in the premise
if age_ratio_hypothesis <= age_ratio_premise:
    # check if the estimate of 'age_ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio
    # any ratio greater than 'age_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
