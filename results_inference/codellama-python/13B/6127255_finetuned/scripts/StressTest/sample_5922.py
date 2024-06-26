trip_home_premise = 0.5
trip_home_hypothesis = 3.5

# the hypothesis refers to the duration of the trip home, which is also mentioned in the premise
if trip_home_hypothesis < trip_home_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives a specific duration for the trip home
    # any duration less than or equal to 'trip_home_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
