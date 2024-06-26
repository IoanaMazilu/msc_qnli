trip_home_premise = 1/2
trip_home_hypothesis = 4/2

# the hypothesis talks about the time difference between the trip home and the trip to the beach, referenced also in the premise
if trip_home_hypothesis!= trip_home_premise:
    # check if the time difference in the hypothesis contradicts the time difference reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time difference
    # the time difference in the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
