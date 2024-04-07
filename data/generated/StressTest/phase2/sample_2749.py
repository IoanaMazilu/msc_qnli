# Premise: Sandy is younger than Molly by less than 26 years.
# Hypothesis: Sandy is younger than Molly by 16 years.
# Golden Label: neutral

age_difference_premise = 26
age_difference_hypothesis = 16

# the hypothesis refers to the age difference between Sandy and Molly, also mentioned in the premise
if age_difference_hypothesis >= age_difference_premise:
    # check if the age difference in the hypothesis contradicts the age difference in the premise
    label = "contradiction"
elif age_difference_hypothesis < age_difference_premise:
    # the premise gives only an estimate for the age difference
    # any difference less than 'age_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

