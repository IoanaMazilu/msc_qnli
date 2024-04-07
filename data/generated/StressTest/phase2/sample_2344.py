# Premise: James took a less than 8-hour bike ride.
# Hypothesis: James took a 3-hour bike ride.
# Golden Label: neutral

bike_ride_premise = 8
bike_ride_hypothesis = 3

# the hypothesis talks about the duration of a bike ride, which is also referenced in the premise
if bike_ride_hypothesis >= bike_ride_premise:
    # check if the hypothesis value contradicts the estimate of less than 'bike_ride_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the duration of the bike ride
    # any duration less than 'bike_ride_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

