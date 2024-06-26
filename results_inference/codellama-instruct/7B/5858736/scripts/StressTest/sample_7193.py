train_leaves_chennai_premise = 12
train_leaves_chennai_hypothesis = 11

# the hypothesis refers to the time of departure of the train, mentioned in the premise
if train_leaves_chennai_hypothesis >= train_leaves_chennai_premise:
    # check if the estimate of 'train_leaves_chennai_hypothesis' contradicts the time of departure in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time of departure
    # any time of departure less than 'train_leaves_chennai_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
