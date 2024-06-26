time_premise = 7
time_hypothesis = 7

# the hypothesis refers to the time required by a train to cover the distance between Chennai and Jammu
if time_hypothesis <= time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif time_hypothesis > time_premise:
    # check if the hypothesis value is more than the premise value
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, we can infer entailment
    label = "entailment"

print(label)
