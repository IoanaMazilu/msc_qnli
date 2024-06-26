drive_time_at_40mph_premise = 5
drive_time_at_40mph_hypothesis = 1
drive_time_at_60mph_premise = 3
drive_time_at_60mph_hypothesis = 3

# The hypothesis refers to the time John drove at 40 mph and 60 mph, also mentioned in the premise
if drive_time_at_40mph_hypothesis >= drive_time_at_40mph_premise:
    # Check if the time John drove at 40 mph in the hypothesis contradicts the premise
    label = "contradiction"
elif drive_time_at_60mph_hypothesis != drive_time_at_60mph_premise:
    # Check if the time John drove at 60 mph in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
