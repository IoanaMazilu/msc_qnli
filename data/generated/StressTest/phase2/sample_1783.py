# Premise: He will be more than 3/3 times as old as Tom 6 years hence.
# Hypothesis: He will be 5/3 times as old as Tom 6 years hence.
# Golden Label: neutral

age_ratio_premise = 3/3
age_ratio_hypothesis = 5/3

# the hypothesis refers to the age ratio between 'he' and Tom mentioned in the premise
if age_ratio_hypothesis <= age_ratio_premise:
    # check if the age ratio in the hypothesis contradicts the estimate of more than 'age_ratio_premise' times as old
    label = "contradiction"
else:
    # the premise gives only an estimate for the age ratio
    # any ratio greater than 'age_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

