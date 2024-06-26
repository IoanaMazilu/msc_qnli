distance_premise = 3.0
speed_premise = 2.0
time_hypothesis = 2.7

# the hypothesis refers to the time spent wandering, which can be inferred from the distance and speed in the premise
# compute the time spent wandering in the premise
time_premise = distance_premise / speed_premise
if time_hypothesis != time_premise:
    # check if the time in the hypothesis contradicts the time from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)