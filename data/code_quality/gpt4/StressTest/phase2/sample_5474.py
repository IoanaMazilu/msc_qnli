drive_hours_40mph_premise = 1
drive_hours_40mph_hypothesis = 1
drive_hours_60mph_premise = 3
drive_hours_60mph_hypothesis = 3

# the hypothesis refers to the driving hours at different speeds from the premise
if drive_hours_40mph_hypothesis >= drive_hours_40mph_premise:
    # check if the hypothesis value contradicts the premise value of 1 hour at 40 mph
    label = "contradiction"
elif drive_hours_60mph_hypothesis != drive_hours_60mph_premise:
    # check if the hypothesis value contradicts the premise value of 3 hours at 60 mph
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
