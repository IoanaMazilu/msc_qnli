drive_time_40mph_premise = 5
drive_time_40mph_hypothesis = 1
drive_time_60mph_premise = 3
drive_time_60mph_hypothesis = 3

# the hypothesis talks about the driving time at 40 mph and 60 mph, referenced also in the premise
if drive_time_40mph_hypothesis >= drive_time_40mph_premise:
    # check if the hypothesis value contradicts the estimate of less than 'drive_time_40mph_premise'
    label = "contradiction"
elif drive_time_60mph_hypothesis!= drive_time_60mph_premise:
    # check if the driving time at 60 mph in the hypothesis contradicts the driving time at 60 mph reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the driving time at 40 mph
    # any driving time less than 'drive_time_40mph_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
