train_distance_premise = 7 * 24 * 60 + 60
train_distance_hypothesis = 7 * 24 * 60 + 60 + 1

# the hypothesis refers to the distance between Chennai and Jammu mentioned in the premise
if train_distance_hypothesis <= train_distance_premise:
    # check if the hypothesis value contradicts the exact distance in the premise
    label = "contradiction"
elif train_distance_hypothesis > train_distance_premise + 1:
    # check if the hypothesis value is more than the exact distance in the premise plus one minute
    label = "entailment"
else:
    # if the hypothesis value falls within the exact distance in the premise plus one minute, it is neutral
    label = "neutral"

print(label)
