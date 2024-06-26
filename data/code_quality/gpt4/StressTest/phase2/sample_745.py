departure_rate_premise = 40
departure_rate_hypothesis = 70

# the hypothesis talks about the on-time departure rate from Phoenix,
# which is also mentioned in the premise
if departure_rate_hypothesis <= departure_rate_premise:
    # check if the on-time departure rate in the hypothesis contradicts the rate in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the on-time departure rate
    # any rate higher than 'departure_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
