drive_time_at_44mph_premise = 1
drive_time_at_44mph_hypothesis = 2
drive_time_at_60mph_premise = 3
drive_time_at_60mph_hypothesis = 3

# the hypothesis talks about the driving time at different speeds from city A to city B, also mentioned in the premise
if drive_time_at_44mph_hypothesis <= drive_time_at_44mph_premise:
    # check if the driving time at 44 mph in the hypothesis contradicts the driving time at 44 mph in the premise
    label = "contradiction"
elif drive_time_at_60mph_hypothesis != drive_time_at_60mph_premise:
    # check if the driving time at 60 mph in the hypothesis contradicts the driving time at 60 mph in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
