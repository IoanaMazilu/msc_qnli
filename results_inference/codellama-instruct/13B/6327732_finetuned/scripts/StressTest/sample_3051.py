ride_time_premise = 3
ride_time_hypothesis = 1

# the hypothesis refers to the duration of the bike ride mentioned in the premise
if ride_time_hypothesis <= ride_time_premise:
    # check if the estimate of 'ride_time_hypothesis' contradicts the duration of the bike ride in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the duration of the bike ride
    # any duration greater than 'ride_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
