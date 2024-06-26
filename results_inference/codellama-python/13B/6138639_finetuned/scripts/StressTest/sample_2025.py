john_age_difference_premise = 3
john_age_difference_hypothesis = 5

# the hypothesis refers to the age difference between John and Tom mentioned in the premise
if john_age_difference_hypothesis >= john_age_difference_premise:
    # check if the hypothesis value contradicts the age difference in the premise
    label = "contradiction"
else:
    # the premise gives an exact age difference
    # any age difference less than 'john_age_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
