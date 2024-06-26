drive_time_44mph_premise = 1
drive_time_44mph_hypothesis = 1
drive_time_60mph_premise = 3
drive_time_60mph_hypothesis = 3

# the hypothesis refers to the driving time at different speeds from the premise
if drive_time_44mph_hypothesis >= drive_time_44mph_premise:
    # check if the hypothesis value contradicts the premise value for 44 mph
    label = "contradiction"
elif drive_time_60mph_hypothesis!= drive_time_60mph_premise:
    # check if the hypothesis value contradicts the premise value for 60 mph
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
