age_frank_premise = 14
age_frank_hypothesis = 54

# the hypothesis refers to the age difference between Frank and John
if age_frank_hypothesis <= age_frank_premise:
    # check if the estimate of 'age_frank_hypothesis' contradicts the age difference in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the age difference
    # any age difference greater than 'age_frank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
