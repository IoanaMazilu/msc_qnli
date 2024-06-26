future_age_premise = 18
past_age_premise = 6
future_age_hypothesis = 18
past_age_hypothesis = 6

# the hypothesis refers to Molly's age in the future and in the past, mentioned in the premise
if future_age_hypothesis <= future_age_premise:
    # check if the hypothesis value contradicts the estimate of more than 'future_age_premise'
    label = "contradiction"
elif past_age_hypothesis!= past_age_premise:
    # check if the past age in the hypothesis contradicts the past age reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the future age
    # any future age greater than 'future_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
