trip_premise = 0.5
trip_hypothesis = 7.0/2.0

# the hypothesis talks about the time difference between two trips, referenced also in the premise
if trip_hypothesis <= trip_premise:
    # check if the hypothesis value contradicts the estimate of 'trip_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time difference
    # any time difference less than 'trip_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
