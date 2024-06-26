train_departure_premise = 9
train_departure_hypothesis = 1

# the hypothesis talks about the train departure time, referenced also in the premise
if train_departure_hypothesis!= train_departure_premise:
    # check if the train departure time in the hypothesis contradicts the train departure time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)