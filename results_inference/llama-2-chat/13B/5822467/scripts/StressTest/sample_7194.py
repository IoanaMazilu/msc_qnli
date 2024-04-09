train_time_premise = 7 * 24 * 60 + 60
train_time_hypothesis = 7 * 24 * 60 + 120

# the hypothesis refers to the time required to cover the distance between Chennai and Jammu
if train_time_hypothesis <= train_time_premise:
    # check if the hypothesis value contradicts the estimate of 'train_time_premise'
    label = "contradiction"
elif train_time_premise!= train_time_hypothesis:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives a specific value for the time required to cover the distance
    # any time greater than 'train_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
