john_frank_age_difference_premise = 8
john_frank_age_difference_hypothesis = 5

# the hypothesis refers to the age difference between John and Frank mentioned in the premise
if john_frank_age_difference_hypothesis >= john_frank_age_difference_premise:
    # check if the age difference in the hypothesis contradicts the estimate of less than 'john_frank_age_difference_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the age difference
    # any age difference less than 'john_frank_age_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
