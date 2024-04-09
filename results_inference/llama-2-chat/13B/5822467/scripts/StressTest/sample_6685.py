step_premise = 80
step_hypothesis = 60
time_premise = 40
time_hypothesis = 40

# the hypothesis refers to the number of steps climbed and the time taken, both mentioned in the premise
if step_hypothesis <= step_premise:
    # check if the estimate of'step_hypothesis' contradicts the number of steps climbed in the premise
    label = "contradiction"
elif time_hypothesis!= time_premise:
    # check if the time taken in the hypothesis contradicts the time taken in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
