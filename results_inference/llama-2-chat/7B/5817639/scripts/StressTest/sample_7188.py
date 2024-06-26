train_leaves_premise = "12 noon"
train_leaves_hypothesis = "less than 42 noon"

# the hypothesis talks about the time of departure of a train, referenced also in the premise
if train_leaves_hypothesis <= train_leaves_premise:
    # check if the hypothesis value contradicts the estimate of the time of departure in the premise
    label = "contradiction"
else:
    # the premise gives a specific time of departure, while the hypothesis gives a more general time range
    # any time of departure within the range of the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
