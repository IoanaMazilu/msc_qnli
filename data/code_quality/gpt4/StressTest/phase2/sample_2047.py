age_difference_premise = 78
age_difference_hypothesis = 18

# the hypothesis refers to the age difference between Sandy and Molly as stated in the premise
if age_difference_hypothesis >= age_difference_premise:
    # check if the hypothesis age difference contradicts the premise
    label = "contradiction"
elif age_difference_hypothesis < age_difference_premise:
    # the premise gives only an estimate for the age difference
    # any age difference less than 'age_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
