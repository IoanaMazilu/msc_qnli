drive_hours_50mph_premise = 1
drive_hours_50mph_hypothesis = 7
drive_hours_60mph_premise = 3
drive_hours_60mph_hypothesis = 3

# the hypothesis refers to the driving hours at 50 mph and 60 mph mentioned in the premise
if drive_hours_50mph_premise!= drive_hours_50mph_hypothesis:
    # check if the driving hours at 50 mph in the hypothesis contradicts the driving hours at 50 mph reported in the premise
    label = "contradiction"
elif drive_hours_60mph_premise!= drive_hours_60mph_hypothesis:
    # check if the driving hours at 60 mph in the hypothesis contradicts the driving hours at 60 mph reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)