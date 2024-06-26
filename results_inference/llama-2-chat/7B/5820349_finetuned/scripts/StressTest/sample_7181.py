drive_hours_42mph_premise = 1
drive_hours_42mph_hypothesis = 7
drive_hours_60mph_premise = 3
drive_hours_60mph_hypothesis = 3

# the hypothesis refers to the driving hours at 42mph and 60mph mentioned in the premise
if drive_hours_42mph_hypothesis!= drive_hours_42mph_premise:
    # check if the driving hours at 42mph in the hypothesis contradicts the driving hours at 42mph reported in the premise
    label = "contradiction"
elif drive_hours_60mph_hypothesis!= drive_hours_60mph_premise:
    # check if the driving hours at 60mph in the hypothesis contradicts the driving hours at 60mph reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
