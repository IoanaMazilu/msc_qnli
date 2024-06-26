future_age_premise = 88
future_age_hypothesis = 18
past_age = 7

# the hypothesis refers to Molly's age in the future and in the past, as mentioned in the premise
if future_age_hypothesis >= future_age_premise:
    # check if the future age in the hypothesis contradicts the estimate of less than 'future_age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the future age
    # any future age less than 'future_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
