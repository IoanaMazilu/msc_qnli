distance_premise = 500
distance_hypothesis = 800
speed_premise = 15
speed_hypothesis = 15

# the hypothesis refers to the distance and speed mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif speed_hypothesis!= speed_premise:
    # check if the speed in the hypothesis contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
