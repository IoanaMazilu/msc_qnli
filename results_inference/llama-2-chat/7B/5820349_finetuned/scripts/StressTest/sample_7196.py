train_time_premise = 7 * 24 + 1
train_time_hypothesis = 7 * 24 + 1

# the hypothesis refers to the time required by a train to cover a certain distance, also mentioned in the premise
if train_time_hypothesis <= train_time_premise:
    # check if the hypothesis value contradicts the exact time given in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
