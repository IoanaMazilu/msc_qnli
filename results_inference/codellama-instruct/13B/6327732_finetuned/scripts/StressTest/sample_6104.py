age_premise = 18
age_hypothesis = 58

# the hypothesis refers to the age at which Jane started baby-sitting, which is mentioned in the premise
if age_hypothesis <= age_premise:
    # check if the estimate of 'age_hypothesis' contradicts the age mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the age at which Jane started baby-sitting
    # any age greater than 'age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
