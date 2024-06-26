matthew_wake_premise = "r"
matthew_wake_hypothesis = "y"
johnny_walk_premise = "y"
johnny_walk_hypothesis = "r"

# the hypothesis refers to the distance and the direction of the walk
if matthew_wake_premise == matthew_wake_hypothesis:
    # check if the hypothesis value contradicts the direction of the walk in the premise
    label = "contradiction"
elif johnny_walk_premise == johnny_walk_hypothesis:
    # check if the hypothesis value contradicts the direction of the walk in the premise
    label = "contradiction"
elif johnny_walk_premise == matthew_wake_premise:
    # check if the hypothesis value contradicts the direction of the walk in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance and the direction of the walk
    # any distance and direction of the walk greater than '35 km' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
