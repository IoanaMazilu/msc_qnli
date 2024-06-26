matthew_wake_premise = "r"
matthew_wake_hypothesis = "y"
johnny_walk_premise = "y"
johnny_walk_hypothesis = "r"

# the hypothesis refers to the same road and the same distance as the premise
if matthew_wake_hypothesis!= matthew_wake_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif johnny_walk_hypothesis!= johnny_walk_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance and the same road
    # any distance greater than 'distance_premise' and the same road as the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
