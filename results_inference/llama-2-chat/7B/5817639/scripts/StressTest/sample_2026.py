old_age_premise = 5
old_age_hypothesis = 6

# the hypothesis refers to the age difference between John and Tom mentioned in the premise
if old_age_hypothesis <= old_age_premise:
    # check if the estimate of 'old_age_hypothesis' contradicts the age difference in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the age difference
    # any age difference greater than 'old_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
