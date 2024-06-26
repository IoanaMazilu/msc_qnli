matthew_wake_premise = "r"
matthew_wake_hypothesis = "y"
johnny_walk_premise = 45
johnny_walk_hypothesis = 85

# the hypothesis refers to the distance walked by Johnny and the direction of the walk
if johnny_walk_hypothesis <= johnny_walk_premise:
    # check if the estimate of 'johnny_walk_hypothesis' contradicts the distance walked in the premise
    label = "contradiction"
elif matthew_wake_hypothesis!= matthew_wake_premise:
    # check if the direction of the walk in the hypothesis contradicts the direction of the walk in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
