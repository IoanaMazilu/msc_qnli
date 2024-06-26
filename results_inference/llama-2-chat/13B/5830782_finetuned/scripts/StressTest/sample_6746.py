flora_departure_premise = 2
flora_departure_hypothesis = 2

# the hypothesis refers to the time Flora leaves City A, which is also mentioned in the premise
if flora_departure_hypothesis <= flora_departure_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an exact time for Flora's departure
    # any departure time greater than 'flora_departure_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
