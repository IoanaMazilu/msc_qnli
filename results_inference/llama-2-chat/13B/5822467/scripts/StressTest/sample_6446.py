age_premise = 14
age_hypothesis = 54

# the hypothesis refers to the age difference between Frank and John, which is also mentioned in the premise
if age_hypothesis <= age_premise:
    # check if the hypothesis value contradicts the estimate of 'age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the age difference
    # any age difference greater than 'age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
