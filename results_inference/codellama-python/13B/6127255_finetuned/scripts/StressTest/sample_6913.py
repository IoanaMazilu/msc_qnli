departure_rate_premise = 80
departure_rate_hypothesis = 70

# the hypothesis refers to the on-time departure rate mentioned in the premise
if departure_rate_hypothesis >= departure_rate_premise:
    # check if the 'departure_rate_hypothesis' contradicts the departure rate in the premise
    label = "contradiction"
else:
    # if the departure rate in the hypothesis is less than the one in the premise, it does not contradict the premise, but cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
