time_premise = 7 + 1 # 7 days and 1 minute
time_hypothesis = 7 + 1 # 7 days and 1 minute

# the hypothesis refers to the time required by a train to cover the distance between Chennai and Jammu mentioned in the premise
if time_hypothesis <= time_premise:
    # check if the hypothesis time contradicts the time in the premise
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)
