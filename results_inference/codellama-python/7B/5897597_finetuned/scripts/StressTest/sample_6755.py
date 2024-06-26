ana_departure_premise = 8
ana_departure_hypothesis = 8

# the hypothesis refers to Ana's departure time mentioned in the premise
if ana_departure_hypothesis < ana_departure_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives an exact departure time
    # any departure time less than 'ana_departure_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
