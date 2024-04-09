departure_rate_premise = 0.8
departure_rate_hypothesis = 0.7

# the hypothesis talks about the on-time departure rate of flights from Phoenix, referenced also in the premise
if departure_rate_hypothesis <= departure_rate_premise:
    # check if the hypothesis value contradicts the estimate of less than 'departure_rate_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the on-time departure rate
    # any on-time departure rate greater than 'departure_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
