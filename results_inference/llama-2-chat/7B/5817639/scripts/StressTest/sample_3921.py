train_leaves_premise = 9
train_leaves_hypothesis = 4

# the hypothesis talks about the time of departure of a train, referenced also in the premise
if train_leaves_hypothesis >= train_leaves_premise:
    # check if the hypothesis value contradicts the estimate of the time of departure in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time of departure
    # any time of departure greater than 'train_leaves_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
