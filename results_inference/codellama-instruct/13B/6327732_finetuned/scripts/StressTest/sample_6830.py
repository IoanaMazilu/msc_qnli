arun_age_premise = 6
arun_age_hypothesis = 3

# the hypothesis refers to the number of years after which Arun's age will be 26 years
if arun_age_hypothesis <= arun_age_premise:
    # check if the estimate of 'arun_age_hypothesis' contradicts the number of years in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years greater than 'arun_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
