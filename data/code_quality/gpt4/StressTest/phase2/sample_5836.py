departure_rate_premise = 20
departure_rate_hypothesis = 80

# the hypothesis talks about the on-time departure rate, which is also mentioned in the premise
if departure_rate_hypothesis <= departure_rate_premise:
    # check if the value of 'departure_rate_hypothesis' contradicts the 'departure_rate_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the departure rate
    # any departure rate higher than 'departure_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
