future_age_premise = 88
future_age_hypothesis = 18

# the hypothesis refers to Molly's future age, which is also mentioned in the premise
if future_age_hypothesis >= future_age_premise:
    # check if the hypothesis value contradicts the premise's estimate of less than 'future_age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Molly's future age
    # any number of years less than 'future_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
