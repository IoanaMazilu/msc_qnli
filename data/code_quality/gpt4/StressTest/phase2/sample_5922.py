trip_home_premise = 0.5
trip_home_hypothesis = 1.5

# the hypothesis refers to the duration of the trip home mentioned in the premise
if trip_home_hypothesis >= trip_home_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives the exact duration of the trip home
    # any duration less than 'trip_home_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
