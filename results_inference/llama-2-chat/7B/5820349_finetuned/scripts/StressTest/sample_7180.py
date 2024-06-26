drive_hours_42mph_premise = 5
drive_hours_42mph_hypothesis = 1
drive_hours_60mph_premise = 3
drive_hours_60mph_hypothesis = 3

# the hypothesis refers to the driving time at different speeds mentioned in the premise
if drive_hours_42mph_hypothesis >= drive_hours_42mph_premise:
    # check if the driving time at 42mph in the hypothesis contradicts the estimate of less than 'drive_hours_42mph_premise'
    label = "contradiction"
elif drive_hours_60mph_hypothesis!= drive_hours_60mph_premise:
    # check if the driving time at 60mph in the hypothesis contradicts the driving time at 60mph reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the driving time at 42mph
    # any driving time less than 'drive_hours_42mph_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
