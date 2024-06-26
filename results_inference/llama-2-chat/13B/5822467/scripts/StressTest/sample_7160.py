age_premise = 38
age_hypothesis = 38

# the hypothesis refers to the age of Sandy after 4 years, mentioned in the premise
if age_hypothesis <= age_premise:
    # check if the estimate of 'age_hypothesis' contradicts the age of Sandy reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the age of Sandy after 4 years
    # any age consistent with the premise cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
