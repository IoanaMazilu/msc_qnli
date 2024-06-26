trip_home_premise = 3/2
trip_beach_premise = 1/2

# the hypothesis refers to the time difference between the trip home and the trip to the beach
if trip_home_hypothesis <= trip_beach_premise:
    # check if the estimate of 'trip_home_hypothesis' contradicts the time difference in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time difference
    # any time difference greater than 'trip_beach_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
