departure_rate_premise = 50
departure_rate_hypothesis = 10

# the hypothesis refers to the on-time departure rate mentioned in the premise
if departure_rate_hypothesis >= departure_rate_premise:
    # check if the hypothesis value contradicts the premise one
    label = "contradiction"
else:
    # the premise gives a specific departure rate
    # any departure rate less than 'departure_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
