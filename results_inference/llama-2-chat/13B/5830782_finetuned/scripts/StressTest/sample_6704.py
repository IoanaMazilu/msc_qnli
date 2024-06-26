age_difference_premise = 7
age_difference_hypothesis = 7

# the hypothesis refers to the age difference between Kiran and Bineesh mentioned in the premise
if age_difference_hypothesis >= age_difference_premise:
    # check if the hypothesis value contradicts the age difference in the premise
    label = "contradiction"
else:
    # the premise gives the exact age difference
    # any age difference less than 'age_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
