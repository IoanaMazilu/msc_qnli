matthew_wake_premise = "t"
matthew_wake_hypothesis = "y"
johnny_walk_premise = "y"
johnny_walk_hypothesis = "t"
distance_premise = 45
distance_hypothesis = 45

# the hypothesis refers to the distance and the direction of the walk, which are also mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance in the premise
    label = "contradiction"
elif johnny_walk_hypothesis!= johnny_walk_premise:
    # check if the direction of the walk in the hypothesis contradicts the direction of the walk reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
