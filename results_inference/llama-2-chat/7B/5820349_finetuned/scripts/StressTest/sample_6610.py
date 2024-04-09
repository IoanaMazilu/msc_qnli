future_age_premise = 88
future_age_hypothesis = 18
past_age = 7

# the hypothesis refers to Molly's age in the future and the past, mentioned also in the premise
if future_age_hypothesis >= future_age_premise:
    # check if the hypothesis value contradicts the estimate of less than 'future_age_premise'
    label = "contradiction"
elif past_age!= 7:
    # check if the past age in the hypothesis contradicts the past age reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Molly's future age
    # any future age less than 'future_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
