premise_train_time = 12
hypothesis_train_time = 82

# the hypothesis refers to the train time mentioned in the premise
if premise_train_time <= hypothesis_train_time:
    # check if the estimate of 'hypothesis_train_time' contradicts the train time in the premise
    label = "contradiction"
elif hypothesis_train_time!= premise_train_time:
    # check if the train time in the hypothesis contradicts the train time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
