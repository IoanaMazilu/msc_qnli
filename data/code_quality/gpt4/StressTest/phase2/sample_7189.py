departure_time_premise = 42
departure_time_hypothesis = 12

# the hypothesis talks about the departure time of a train, referenced also in the premise
if departure_time_hypothesis >= departure_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'departure_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the departure time
    # any departure time less than 'departure_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
