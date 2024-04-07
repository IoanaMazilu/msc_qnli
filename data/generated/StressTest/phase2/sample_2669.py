# Premise: A train leaves Delhi at 9 a.
# Hypothesis: A train leaves Delhi at more than 9 a.
# Golden Label: contradiction

train_departure_premise = 9
train_departure_hypothesis = 9

# The hypothesis refers to the departure time of a train mentioned in the premise.
if train_departure_hypothesis > train_departure_premise:
    # Check if the departure time in the hypothesis contradicts the departure time in the premise
    label = "contradiction"
elif train_departure_hypothesis < train_departure_premise:
    # Check if the departure time in the hypothesis contradicts the departure time in the premise
    label = "contradiction"
else:
    # If the departure time in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"

print(label)

