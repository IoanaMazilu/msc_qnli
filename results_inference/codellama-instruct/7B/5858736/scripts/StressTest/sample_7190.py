train_leaves_jammu_premise = 12
train_leaves_jammu_hypothesis = 62

# the hypothesis talks about the time of departure of the train, referenced also in the premise
if train_leaves_jammu_hypothesis <= train_leaves_jammu_premise:
    # check if the hypothesis value contradicts the estimate of 'train_leaves_jammu_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time of departure of the train
    # any time of departure greater than 'train_leaves_jammu_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
