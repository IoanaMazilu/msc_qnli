trip_home_longer_premise = 7/2
trip_home_longer_hypothesis = 1/2

# the hypothesis refers to the time difference between the trip to the beach and the trip home mentioned in the premise
if trip_home_longer_hypothesis <= trip_home_longer_premise:
    # check if the hypothesis value contradicts the estimate of less than 'trip_home_longer_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time difference
    # any time difference less than 'trip_home_longer_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
