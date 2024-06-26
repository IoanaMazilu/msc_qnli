trip_home_premise = 3/2
trip_home_hypothesis = 1/2

# the hypothesis talks about the time difference between the trip home and the trip to the beach, referenced also in the premise
if trip_home_hypothesis >= trip_home_premise:
    # check if the hypothesis value contradicts the estimate of less than 'trip_home_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time difference
    # any time difference less than 'trip_home_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
