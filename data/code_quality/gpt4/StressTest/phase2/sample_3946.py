drive_hours_premise = 1
drive_hours_hypothesis = 7
drive_rate_premise = 30
drive_rate_hypothesis = 30

# the hypothesis talks about the driving time from Town A to Town C, also mentioned in the premise
# the hypothesis also mentions the driving rate which is the same as in the premise
if drive_hours_hypothesis <= drive_hours_premise:
    # check if the driving time in the hypothesis contradicts the estimate of more than 'drive_hours_premise'
    label = "contradiction"
elif drive_rate_hypothesis != drive_rate_premise:
    # check if the driving rate in the hypothesis contradicts the driving rate mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the driving time
    # any driving time greater than 'drive_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
