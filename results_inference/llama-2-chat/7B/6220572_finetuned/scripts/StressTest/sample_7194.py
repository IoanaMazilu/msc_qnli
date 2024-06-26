distance_train_premise = 7 * 24 + 1
distance_train_hypothesis = 6 * 24 + 1

# the hypothesis refers to the time required by a train to cover the distance mentioned in the premise
if distance_train_hypothesis <= distance_train_premise:
    # check if the hypothesis value contradicts the exact time reported in the premise
    label = "contradiction"
else:
    # the premise gives an exact time for the distance
    # any time greater than 'distance_train_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
