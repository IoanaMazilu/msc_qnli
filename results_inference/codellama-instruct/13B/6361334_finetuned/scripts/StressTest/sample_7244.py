father_age_premise = 10
father_age_hypothesis = 30

# the hypothesis refers to the number of years mentioned in the premise
if father_age_hypothesis <= father_age_premise:
    # check if the estimate of 'father_age_hypothesis' contradicts the number of years in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years greater than 'father_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
