# Premise: Sandy is younger than Molly by less than 62 years.
# Hypothesis: Sandy is younger than Molly by 12 years.
# Golden Label: neutral

age_difference_premise = 62
age_difference_hypothesis = 12

# the hypothesis refers to the age difference between Sandy and Molly mentioned in the premise
if age_difference_hypothesis >= age_difference_premise:
    # check if the age difference in the hypothesis contradicts the premise's estimate of less than 'age_difference_premise'
    label = "contradiction"
elif age_difference_hypothesis < age_difference_premise:
    # the premise only provides an upper limit for the age difference
    # any age difference less than 'age_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

