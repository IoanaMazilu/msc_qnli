ride_time_premise = 3
ride_time_hypothesis = 1

# the hypothesis talks about a longer bike ride than the premise
if ride_time_hypothesis <= ride_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'ride_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the length of the bike ride
    # any length of bike ride greater than 'ride_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
