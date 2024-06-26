drive_time_premise = 3
drive_time_hypothesis = 1
mph_premise = 40
mph_hypothesis = 60

# the hypothesis talks about the speed and time of driving, referenced also in the premise
if drive_time_hypothesis <= drive_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'drive_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the driving time
    # any driving time greater than 'drive_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
