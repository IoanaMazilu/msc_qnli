departure_time_premise = 12
departure_time_hypothesis = 82

# the hypothesis refers to the departure time of the train mentioned in the premise
if departure_time_hypothesis <= departure_time_premise:
    # check if the hypothesis value contradicts the departure time in the premise
    label = "contradiction"
else:
    # the premise gives the exact departure time
    # any departure time less than 'departure_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
