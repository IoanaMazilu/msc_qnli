ride_time_premise = 1
ride_time_hypothesis = 3

# the hypothesis refers to the ride time mentioned in the premise
if ride_time_hypothesis <= ride_time_premise:
    # check if the estimate of 'ride_time_hypothesis' contradicts the number of hours in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ride time
    # any ride time greater than 'ride_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
