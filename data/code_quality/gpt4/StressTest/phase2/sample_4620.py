time_spent_premise = 6
time_spent_hypothesis = 1

# the hypothesis refers to the time spent on the roads, mentioned in the premise
if time_spent_premise <= time_spent_hypothesis:
    # check if the estimate of 'time_spent_hypothesis' contradicts the time spent in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
