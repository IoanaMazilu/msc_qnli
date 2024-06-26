matthew_wake_premise = "r"
matthew_wake_hypothesis = "y"
johnny_walk_premise = "y"
johnny_walk_hypothesis = "r"

# the hypothesis refers to the same road and the same distance as the premise
if matthew_wake_hypothesis == matthew_wake_premise and johnny_walk_hypothesis == johnny_walk_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    if distance_hypothesis <= distance_premise:
        label = "contradiction"
    else:
        label = "entailment"
else:
    label = "neutral"

print(label)
