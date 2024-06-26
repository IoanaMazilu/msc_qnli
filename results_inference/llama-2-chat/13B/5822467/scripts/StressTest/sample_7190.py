train_leaving_time_premise = 12
train_leaving_time_hypothesis = 62

# the hypothesis refers to the time at which the train leaves Jammu
if train_leaving_time_hypothesis <= train_leaving_time_premise:
    # check if the estimate of 'train_leaving_time_hypothesis' contradicts the time reported in the premise
    label = "contradiction"
elif train_leaving_time_hypothesis > train_leaving_time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
