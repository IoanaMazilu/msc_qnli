matthew_wake_premise = "r"
matthew_wake_hypothesis = "y"
johnny_walk_premise = "y"
johnny_walk_hypothesis = "r"

# the hypothesis refers to the distance traveled by Johnny and the direction of his walk
if johnny_walk_hypothesis!= johnny_walk_premise:
    # check if the direction of Johnny's walk contradicts the direction mentioned in the premise
    label = "contradiction"
elif matthew_wake_hypothesis!= matthew_wake_premise:
    # check if the direction of Matthew's wake contradicts the direction mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
