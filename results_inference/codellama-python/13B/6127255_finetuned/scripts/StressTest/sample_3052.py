ride_duration_premise = 1
ride_duration_hypothesis = 3

# the hypothesis talks about the duration of James' bike ride, referenced also in the premise
if ride_duration_hypothesis <= ride_duration_premise:
    # check if the hypothesis value contradicts the estimate of more than 'ride_duration_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the duration of the ride
    # any duration greater than 'ride_duration_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
