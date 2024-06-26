age_premise = 88
age_hypothesis = 18

# the hypothesis refers to Molly's age in the future, also mentioned in the premise
if age_hypothesis <= age_premise:
    # check if the hypothesis value contradicts the estimate of more than 'age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Molly's age
    # any age consistent with the premise, but less than 'age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
