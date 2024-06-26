ana_departure_premise = 8
ana_departure_hypothesis = 8

# the hypothesis refers to the time Ana departs, which is also mentioned in the premise
if ana_departure_hypothesis >= ana_departure_premise:
    # check if the hypothesis time contradicts the premise time
    label = "contradiction"
else:
    # the premise gives an exact time for Ana's departure
    # any time less than 'ana_departure_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
