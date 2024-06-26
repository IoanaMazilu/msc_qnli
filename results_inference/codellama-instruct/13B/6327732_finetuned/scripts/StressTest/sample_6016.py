age_premise = 40
age_hypothesis = 20

# the hypothesis refers to the age at which Jane started baby-sitting, which is also mentioned in the premise
if age_hypothesis >= age_premise:
    # check if the hypothesis value contradicts the estimate of less than 'age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the age at which Jane started baby-sitting
    # any age less than 'age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
