age_premise = 84
age_hypothesis = 14

# the hypothesis refers to the age difference between Frank and John, mentioned in the premise
if age_hypothesis <= age_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives an exact value for the age difference
    # any age difference less than 'age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
