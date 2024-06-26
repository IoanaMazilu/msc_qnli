train_leave_time_premise = 12
train_leave_time_hypothesis = 12

# the hypothesis talks about the train leaving Chennai bound for Jammu at a specific time, which is also mentioned in the premise
if train_leave_time_hypothesis >= train_leave_time_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
