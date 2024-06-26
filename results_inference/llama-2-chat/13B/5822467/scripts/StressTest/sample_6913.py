departure_rate_premise = 80
departure_rate_hypothesis = 70

# the hypothesis refers to the on-time departure rate of subsequent flights from Phoenix
if departure_rate_hypothesis <= departure_rate_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif departure_rate_premise < departure_rate_hypothesis:
    # check if the hypothesis value entails the premise value
    label = "entailment"
else:
    # the premise gives a minimum requirement for the on-time departure rate
    # any on-time departure rate higher than the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
