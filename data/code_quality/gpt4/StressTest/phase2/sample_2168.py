distance_premise = 700
distance_hypothesis = 500
speed_premise = 18
speed_hypothesis = 18

# the hypothesis refers to the distance covered by Sandy and the speed at which Sandy runs, which are both mentioned in the premise
if distance_premise != distance_hypothesis:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif speed_premise != speed_hypothesis:
    # check if the speed in the hypothesis contradicts the speed in the premise
    label = "contradiction"
else:
    # if the distance and speed in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)
