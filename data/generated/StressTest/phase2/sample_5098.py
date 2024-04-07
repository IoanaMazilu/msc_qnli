# Premise: Jack took a less than 7-hour bike ride.
# Hypothesis: Jack took a 3-hour bike ride.
# Golden Label: neutral

ride_duration_premise = 7
ride_duration_hypothesis = 3

# the hypothesis talks about the duration of Jack's bike ride, which is also mentioned in the premise
if ride_duration_hypothesis >= ride_duration_premise:
    # check if the hypothesis value contradicts the estimate of less than 'ride_duration_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the duration of the bike ride
    # any duration less than 'ride_duration_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

