premise_trip_home = 7/2
hypothesis_trip_home = 1/2

# the hypothesis refers to the time difference between the trip to the beach and the trip home
if hypothesis_trip_home <= premise_trip_home:
    # check if the estimate of 'hypothesis_trip_home' contradicts the time difference in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time difference
    # any time difference greater than 'premise_trip_home' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
