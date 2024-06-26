# defining variables for premise
drive_time_48mph_premise = 1
drive_time_60mph_premise = 3

# defining variables for hypothesis
drive_time_48mph_hypothesis = 5
drive_time_60mph_hypothesis = 3

# the hypothesis talks about the driving time at different speeds, mentioned in the premise
if drive_time_48mph_hypothesis < drive_time_48mph_premise:
    # check if the hypothesis estimate contradicts the drive time at 48 mph in the premise
    label = "contradiction"
elif drive_time_60mph_hypothesis != drive_time_60mph_premise:
    # check if the drive time at 60 mph in the hypothesis contradicts the drive time at 60 mph in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
