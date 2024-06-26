future_age_premise = 4
future_age_hypothesis = 6

# the hypothesis talks about Sandy's future age, which is also referenced in the premise
if future_age_hypothesis <= future_age_premise:
    # check if the hypothesis value contradicts the estimate of more than 'future_age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the future age
    # any number of years greater than 'future_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
