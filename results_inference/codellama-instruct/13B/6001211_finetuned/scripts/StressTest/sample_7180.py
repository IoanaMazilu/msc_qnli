drive_time_42mph_premise = 5
drive_time_42mph_hypothesis = 1
drive_time_60mph_premise = 3
drive_time_60mph_hypothesis = 3

# the hypothesis refers to the driving time at different speeds from the premise
if drive_time_42mph_hypothesis >= drive_time_42mph_premise:
    # check if the drive time at 42 mph in the hypothesis contradicts the estimate of less than 'drive_time_42mph_premise'
    label = "contradiction"
elif drive_time_60mph_hypothesis!= drive_time_60mph_premise:
    # check if the drive time at 60 mph in the hypothesis contradicts the drive time at 60 mph reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the drive time at 42 mph
    # any drive time less than 'drive_time_42mph_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
