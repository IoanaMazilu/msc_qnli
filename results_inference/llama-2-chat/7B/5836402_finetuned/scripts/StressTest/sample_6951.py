future_age_premise = 40
future_age_hypothesis = 40
future_years_hypothesis = 2

# the hypothesis refers to Arun's future age, which is also mentioned in the premise
if future_age_hypothesis <= future_age_premise:
    # check if the hypothesis value contradicts the estimate of more than 'future_age_premise' years in the future
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years in the future
    # any number of years greater than 'future_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
