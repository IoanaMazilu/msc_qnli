# Premise: James took a more than 2-hour bike ride.
# Hypothesis: James took a 3-hour bike ride.
# Golden Label: neutral

bike_ride_duration_premise = 2
bike_ride_duration_hypothesis = 3

# the hypothesis talks about the duration of a bike ride, referenced also in the premise
if bike_ride_duration_hypothesis <= bike_ride_duration_premise:
    # check if the hypothesis value contradicts the estimate of more than 'bike_ride_duration_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the bike ride duration
    # any duration greater than 'bike_ride_duration_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

