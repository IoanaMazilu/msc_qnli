age_ratio_premise = 3
age_ratio_hypothesis = 4

# the hypothesis talks about the ratio of the ages of two people, referenced also in the premise
if age_ratio_hypothesis <= age_ratio_premise:
    # check if the hypothesis value contradicts the estimate of more than 'age_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of the ages
    # any ratio of more than 'age_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
