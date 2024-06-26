steps_premise = 60
steps_hypothesis = 80
time_premise = 40
time_hypothesis = 40

# the hypothesis refers to the number of steps climbed by Vinod and the time taken, both mentioned in the premise
if steps_hypothesis!= steps_premise:
    # check if the number of steps in the hypothesis contradicts the number of steps reported in the premise
    label = "contradiction"
elif time_hypothesis!= time_premise:
    # check if the time taken in the hypothesis contradicts the time taken reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)