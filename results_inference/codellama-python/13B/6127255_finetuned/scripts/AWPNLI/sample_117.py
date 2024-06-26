jogged_distance_premise = 25.0
jogged_speed_premise = 5.0
jogged_time_hypothesis = 4.0

# the hypothesis refers to the time Teresa jogged, which can be computed from the premise
# compute the time jogged in the premise
jogged_time_premise = jogged_distance_premise / jogged_speed_premise
if jogged_time_hypothesis!= jogged_time_premise:
    # check if the time in the hypothesis contradicts the time computed from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
