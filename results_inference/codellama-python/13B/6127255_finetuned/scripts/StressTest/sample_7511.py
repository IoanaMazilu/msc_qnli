#drive_time_50mph_premise = 1
#drive_time_50mph_hypothesis = 7
#drive_time_60mph_premise = 3
#drive_time_60mph_hypothesis = 3

# the hypothesis refers to the driving times at different speeds mentioned in the premise
# if the driving times at 50 mph or 60 mph in the hypothesis contradict the driving times at the same speeds in the premise
if drive_time_50mph_hypothesis!= drive_time_50mph_premise:
    label = "contradiction"
elif drive_time_60mph_hypothesis!= drive_time_60mph_premise:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
#