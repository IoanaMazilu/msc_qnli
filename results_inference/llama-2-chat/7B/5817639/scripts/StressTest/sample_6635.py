departure_time_premise = 9
departure_time_hypothesis = 1

# the hypothesis talks about the departure time of a train, referenced also in the premise
if departure_time_hypothesis <= departure_time_premise:
    # check if the hypothesis value contradicts the estimate of the departure time in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the departure time
    # any departure time greater than 'departure_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
