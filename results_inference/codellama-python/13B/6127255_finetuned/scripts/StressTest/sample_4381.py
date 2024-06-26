drive_hours_50mph_premise = 8
drive_hours_50mph_hypothesis = 1
drive_hours_60mph_premise = 3
drive_hours_60mph_hypothesis = 3

# the hypothesis talks about the driving hours at 50 mph and 60 mph, referenced also in the premise
if drive_hours_50mph_hypothesis >= drive_hours_50mph_premise:
    # check if the hypothesis value contradicts the estimate of less than 'drive_hours_50mph_premise'
    label = "contradiction"
elif drive_hours_60mph_hypothesis!= drive_hours_60mph_premise:
    # check if the driving hours at 60 mph in the hypothesis contradicts the driving hours at 60 mph reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the driving hours at 50 mph
    # any number of driving hours less than 'drive_hours_50mph_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
