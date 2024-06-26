drive_hours_premise = 8
drive_hours_hypothesis = 1
drive_speed_premise = 50
drive_speed_hypothesis = 50
drive_hours_60mph_premise = 3
drive_hours_60mph_hypothesis = 3

# the hypothesis talks about the driving time and speed from city A to B, also referenced in the premise
if drive_hours_hypothesis > drive_hours_premise:
    # check if the driving hours in the hypothesis contradicts the estimate of less than 'drive_hours_premise' hours
    label = "contradiction"
elif drive_speed_hypothesis != drive_speed_premise:
    # check if the driving speed in the hypothesis contradicts the driving speed in the premise
    label = "contradiction"
elif drive_hours_60mph_hypothesis != drive_hours_60mph_premise:
    # check if the driving hours at 60mph in the hypothesis contradicts the driving hours at 60mph in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the driving hours at 50mph
    # any driving hours less than 'drive_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
