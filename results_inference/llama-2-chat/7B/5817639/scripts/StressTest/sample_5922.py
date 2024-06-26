trip_premise = 1/2
trip_hypothesis = 3/2

# the hypothesis talks about the duration of a trip, referenced also in the premise
if trip_hypothesis <= trip_premise:
    # check if the hypothesis value contradicts the estimate of 'trip_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the duration of the trip
    # any duration shorter than 'trip_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
