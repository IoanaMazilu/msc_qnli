train_leave_time_premise = 12
train_leave_time_hypothesis = 12

# the hypothesis talks about the time of departure of the train, referenced also in the premise
if train_leave_time_hypothesis >= train_leave_time_premise:
    # check if the time of departure in the hypothesis contradicts the time of departure reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
