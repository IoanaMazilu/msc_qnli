age_ratio_premise = 5 / 3
age_ratio_hypothesis = 5 / 3

# the hypothesis refers to the age ratio mentioned in the premise
if age_ratio_hypothesis <= age_ratio_premise:
    # check if the age ratio in the hypothesis contradicts the age ratio in the premise
    label = "contradiction"
else:
    # the premise gives an exact age ratio
    # any age ratio greater than 'age_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
