departure_rate_premise = 20
departure_rate_hypothesis = 60

# the hypothesis talks about the on-time departure rate from Phoenix, referenced also in the premise
if departure_rate_hypothesis <= departure_rate_premise:
    # check if the hypothesis value contradicts the estimate of more than 'departure_rate_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the on-time departure rate
    # any rate higher than 'departure_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
