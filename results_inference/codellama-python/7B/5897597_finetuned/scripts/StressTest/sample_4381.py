drive_time_50mph_premise = 8
drive_time_50mph_hypothesis = 1
drive_time_60mph_premise = 3
drive_time_60mph_hypothesis = 3

# the hypothesis refers to the driving time at different speeds from city A to city B mentioned in the premise
if drive_time_50mph_hypothesis >= drive_time_50mph_premise:
    # check if the hypothesis value contradicts the estimate of less than 'drive_time_50mph_premise'
    label = "contradiction"
elif drive_time_60mph_hypothesis!= drive_time_60mph_premise:
    # check if the driving time at 60mph in the hypothesis contradicts the driving time at 60mph reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the driving time at 50mph
    # any driving time less than 'drive_time_50mph_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
