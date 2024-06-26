bike_ride_duration_premise = 3
bike_ride_duration_hypothesis = 3

# the hypothesis refers to the duration of the bike ride mentioned in the premise
if bike_ride_duration_hypothesis != bike_ride_duration_premise:
    # check if the bike ride duration in the hypothesis contradicts the bike ride duration in the premise
    label = "contradiction"
else:
    # the premise clearly specifies the bike ride duration
    # any bike ride duration equal to 'bike_ride_duration_premise' can be explicitly entailed from the premise
    label = "entailment"

print(label)
