bike_ride_duration_premise = 1
bike_ride_duration_hypothesis = 3

# the hypothesis refers to the duration of James' bike ride mentioned in the premise
if bike_ride_duration_hypothesis <= bike_ride_duration_premise:
    # check if the duration of the bike ride in the hypothesis contradicts the estimate of more than 'bike_ride_duration_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the duration of the bike ride
    # any duration greater than 'bike_ride_duration_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
