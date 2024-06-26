drive_time_40mph_premise = 5
drive_time_60mph_premise = 3
drive_time_40mph_hypothesis = 1
drive_time_60mph_hypothesis = 3

# the hypothesis refers to the time Andrew drove at 40 and 60 mph, which are also mentioned in the premise
if drive_time_40mph_hypothesis!= drive_time_40mph_premise or drive_time_60mph_hypothesis!= drive_time_60mph_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
