driven_time_premise = 1 + 3 = 4
driven_speed_premise = 40
driven_speed_hypothesis = 60

# the hypothesis talks about the speed and time of driving, referenced also in the premise
if driven_speed_hypothesis <= driven_speed_premise:
    # check if the hypothesis value contradicts the estimate of 'driven_speed_premise'
    label = "contradiction"
elif driven_time_hypothesis < 5:
    # check if the hypothesis value contradicts the estimate of 'driven_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the driving time and speed
    # any driving time and speed combination greater than 'driven_time_premise' and 'driven_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
