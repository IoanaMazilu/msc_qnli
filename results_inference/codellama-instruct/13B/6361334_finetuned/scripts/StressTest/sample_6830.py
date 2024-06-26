arun_age_premise = 6
arun_age_hypothesis = 3

# the hypothesis refers to the number of years after which Arun's age will be 26 years
# the premise gives an estimate for the number of years after which Arun's age will be 26 years
if arun_age_hypothesis <= arun_age_premise:
    # check if the hypothesis value contradicts the estimate of more than 'arun_age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years after which Arun's age will be 26 years
    # any number of years greater than 'arun_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
