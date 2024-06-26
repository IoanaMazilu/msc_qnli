# driving time at 50 mph
driving_time_50mph_premise = 1
driving_time_50mph_hypothesis = 7

# driving time at 60 mph
driving_time_60mph_premise = 3
driving_time_60mph_hypothesis = 3

# the hypothesis refers to the driving time at different speeds from the premise
if driving_time_50mph_hypothesis!= driving_time_50mph_premise:
    # check if the driving time at 50 mph in the hypothesis contradicts the driving time at 50 mph reported in the premise
    label = "contradiction"
elif driving_time_60mph_hypothesis!= driving_time_60mph_premise:
    # check if the driving time at 60 mph in the hypothesis contradicts the driving time at 60 mph reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
