trip_premise = 3/2
trip_hypothesis = 1/2

# the hypothesis talks about the time it took Carl to drive to the beach and back
if trip_hypothesis <= trip_premise:
    # check if the hypothesis value contradicts the estimate of 'trip_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the time it took Carl to drive to the beach and back
    # any time that is less than or equal to 'trip_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
