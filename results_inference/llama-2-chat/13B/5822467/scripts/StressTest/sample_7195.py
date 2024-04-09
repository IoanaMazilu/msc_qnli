train_distance_premise = 6 * 24 * 60 + 60
train_distance_hypothesis = 7 * 24 * 60 + 60

# the hypothesis refers to the time required to cover the distance between Chennai and Jammu
if train_distance_hypothesis <= train_distance_premise:
    # check if the hypothesis value contradicts the estimate of more than 'train_distance_premise'
    label = "contradiction"
elif train_distance_hypothesis > train_distance_premise:
    # the hypothesis value is greater than the premise value, so we can infer entailment
    label = "entailment"
else:
    # the premise gives only an estimate for the time required
    # any time greater than 'train_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
