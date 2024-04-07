# Premise: He will be more than 1/3 times as old as Tom 6 years hence.
# Hypothesis: He will be 5/3 times as old as Tom 6 years hence.
# Golden Label: neutral

age_ratio_premise = 1/3
age_ratio_hypothesis = 5/3

# the hypothesis references the age ratio between 'he' and Tom, which is also mentioned in the premise
if age_ratio_hypothesis <= age_ratio_premise:
    # check if the hypothesis' age ratio contradicts the premise's estimate of more than 'age_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the age ratio
    # any age ratio greater than 'age_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

