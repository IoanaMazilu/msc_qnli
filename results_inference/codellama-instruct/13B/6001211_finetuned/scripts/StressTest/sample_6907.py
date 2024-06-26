drive_time_44mph_premise = 2
drive_time_44mph_hypothesis = 1
drive_time_60mph_premise = 3
drive_time_60mph_hypothesis = 3

# the hypothesis refers to the driving time at different speeds mentioned in the premise
if drive_time_44mph_hypothesis >= drive_time_44mph_premise:
    # check if the drive time at 44 mph in the hypothesis contradicts the estimate of less than 'drive_time_44mph_premise'
    label = "contradiction"
elif drive_time_60mph_hypothesis!= drive_time_60mph_premise:
    # check if the drive time at 60 mph in the hypothesis contradicts the drive time at 60 mph reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the drive time at 44 mph
    # any drive time less than 'drive_time_44mph_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
