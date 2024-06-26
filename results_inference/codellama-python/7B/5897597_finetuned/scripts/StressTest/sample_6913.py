departure_rate_premise = 80
departure_rate_hypothesis = 70

# the hypothesis refers to the on-time departure rate mentioned in the premise
if departure_rate_hypothesis >= departure_rate_premise:
    # check if the hypothesis value contradicts the premise value of less than 'departure_rate_premise'
    label = "contradiction"
elif departure_rate_hypothesis < departure_rate_premise:
    # the premise gives an upper limit for the on-time departure rate
    # any rate less than 'departure_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
