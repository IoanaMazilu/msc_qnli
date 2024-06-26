drive_time_46mph_premise = 7
drive_time_46mph_hypothesis = 1
drive_time_60mph_premise = 3
drive_time_60mph_hypothesis = 3

# the hypothesis talks about driving time at two different speeds, referenced also in the premise
if drive_time_46mph_hypothesis >= drive_time_46mph_premise:
    # check if 'drive_time_46mph_hypothesis' contradicts the estimate of less than 'drive_time_46mph_premise' in the premise
    label = "contradiction"
elif drive_time_60mph_hypothesis != drive_time_60mph_premise:
    # check if 'drive_time_60mph_hypothesis' contradicts the exact 'drive_time_60mph_premise' in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the driving time at 46 mph, but a precise time at 60 mph
    # the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
