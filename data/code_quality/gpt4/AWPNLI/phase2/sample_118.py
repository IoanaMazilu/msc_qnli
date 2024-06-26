distance_premise = 80.0
speed_premise = 10.0
time_hypothesis = 8.0

# the hypothesis refers to the time Benjamin skated, which can be computed from the premise
# compute the time Benjamin skated in the premise
time_premise = distance_premise / speed_premise
if time_hypothesis != time_premise:
    # check if the time in the hypothesis contradicts the time computed from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
