time_at_50mph_premise = 1
time_at_50mph_hypothesis = 4
time_at_60mph_premise = 3
time_at_60mph_hypothesis = 3

# the hypothesis refers to the driving time at two different speeds from city A to city B mentioned in the premise
if time_at_50mph_hypothesis != time_at_50mph_premise:
    # check if the driving time at 50 mph in the hypothesis contradicts the driving time at 50 mph reported in the premise
    label = "contradiction"
elif time_at_60mph_hypothesis != time_at_60mph_premise:
    # check if the driving time at 60 mph in the hypothesis contradicts the driving time at 60 mph reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
