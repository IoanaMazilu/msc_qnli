departure_rate_premise = 20
departure_rate_hypothesis = 60

# the hypothesis refers to the on-time departure rate mentioned in the premise
if departure_rate_hypothesis <= departure_rate_premise:
    # check if the 'departure_rate_hypothesis' contradicts the departure rate in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the departure rate
    # any departure rate greater than 'departure_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
