ride_time_premise = 1
ride_time_hypothesis = 3

# the hypothesis refers to the exact number of hours in the bike ride, while the premise mentions a more than 1-hour ride
if ride_time_hypothesis <= ride_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'ride_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ride time
    # any number of hours greater than 'ride_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
