distance_premise = 100
distance_hypothesis = 100
speed_premise = 60
speed_hypothesis = 70

# the hypothesis refers to the distance and speed mentioned in the premise
if distance_premise!= distance_hypothesis:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif speed_hypothesis!= speed_premise:
    # check if the speed in the hypothesis contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
