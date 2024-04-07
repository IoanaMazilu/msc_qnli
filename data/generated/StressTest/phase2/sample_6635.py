# Premise: A train leaves Delhi at 9 a.
# Hypothesis: A train leaves Delhi at 1 a.
# Golden Label: contradiction

train_departure_time_premise = 9
train_departure_time_hypothesis = 1

# the hypothesis talks about the train departure time, referenced also in the premise
if train_departure_time_hypothesis != train_departure_time_premise:
    # check if the departure time in the hypothesis contradicts the departure time reported in the premise
    label = "contradiction"
else:
    # if the departure time in the hypothesis is the same as the one in the premise, we can infer entailment
    label = "entailment"

print(label)

