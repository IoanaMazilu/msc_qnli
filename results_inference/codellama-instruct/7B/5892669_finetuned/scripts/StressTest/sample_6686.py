steps_climbed_premise = 60
steps_climbed_hypothesis = 80
climbing_time_premise = 40
climbing_time_hypothesis = 40

# the hypothesis refers to the number of steps climbed and the time taken, both mentioned in the premise
if steps_climbed_hypothesis!= steps_climbed_premise:
    # check if the number of steps climbed in the hypothesis contradicts the number of steps climbed reported in the premise
    label = "contradiction"
elif climbing_time_hypothesis!= climbing_time_premise:
    # check if the time taken to climb in the hypothesis contradicts the time taken reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
