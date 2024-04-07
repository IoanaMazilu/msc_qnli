# Premise: A train leaves Delhi at 11 a.
# Hypothesis: A train leaves Delhi at more than 11 a.
# Golden Label: contradiction

train_departure_premise = 11
train_departure_hypothesis = 11

# the hypothesis refers to the departure time of a train from Delhi, which is also mentioned in the premise
if train_departure_hypothesis > train_departure_premise:
    # check if the hypothesis value contradicts the exact departure time mentioned in the premise
    label = "contradiction"
elif train_departure_hypothesis == train_departure_premise:
    # if the departure time in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"
else:
    # the departure time in the hypothesis is less than the one in the premise
    label = "contradiction"

print(label)

