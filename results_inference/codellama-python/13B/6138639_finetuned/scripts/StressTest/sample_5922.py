trip_home_premise = 1/2
trip_home_hypothesis = 3/2

# the hypothesis refers to the time difference between the trip home and the trip to the beach mentioned in the premise
if trip_home_hypothesis <= trip_home_premise:
    # check if the hypothesis value contradicts the estimate of more than 'trip_home_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time difference
    # any time difference greater than 'trip_home_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)