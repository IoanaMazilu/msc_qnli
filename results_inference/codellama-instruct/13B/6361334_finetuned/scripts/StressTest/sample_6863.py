matthew_wake_premise = "r to y"
matthew_wake_hypothesis = "r to y"
johnny_walk_premise = 45
johnny_walk_hypothesis = 85

# the hypothesis refers to the same event as the premise, but with different distances
if matthew_wake_hypothesis!= matthew_wake_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif johnny_walk_hypothesis <= johnny_walk_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance greater than 'johnny_walk_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
