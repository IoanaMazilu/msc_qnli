time_drive_42mph_premise = 1
time_drive_42mph_hypothesis = 5
time_drive_60mph_premise = 3
time_drive_60mph_hypothesis = 3

# the hypothesis talks about the time Andrew drove at different speeds between city A and city B, as mentioned in the premise
if time_drive_42mph_hypothesis >= time_drive_42mph_premise:
    # check if the hypothesis value contradicts the time Andrew drove at 42 mph in the premise
    label = "contradiction"
elif time_drive_60mph_hypothesis != time_drive_60mph_premise:
    # check if the time Andrew drove at 60 mph as per the hypothesis contradicts the time he drove at 60 mph as per the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
