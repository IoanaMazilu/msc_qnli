drive_hours_60mph_premise = 7
drive_hours_60mph_hypothesis = 1
drive_hours_90mph_premise = 3
drive_hours_90mph_hypothesis = 3

# the hypothesis refers to the hours David drove at 60 mph and 90 mph, which are also mentioned in the premise
if drive_hours_60mph_hypothesis >= drive_hours_60mph_premise:
    # check if the hours of driving at 60 mph in the hypothesis contradicts the estimate of less than 'drive_hours_60mph_premise'
    label = "contradiction"
elif drive_hours_90mph_hypothesis != drive_hours_90mph_premise:
    # check if the hours of driving at 90 mph in the hypothesis contradicts the hours of driving at 90 mph in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours driving at 60 mph
    # an exact number of hours less than 'drive_hours_60mph_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
