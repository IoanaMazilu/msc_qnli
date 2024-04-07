# Premise: 380 and Andrew's share is Rs.
# Hypothesis: 780 and Andrew's share is Rs.
# Golden Label: contradiction

andrew_share_premise = 380
andrew_share_hypothesis = 780

# the hypothesis refers to Andrew's share mentioned in the premise
if andrew_share_hypothesis == andrew_share_premise:
    # check if the value of 'andrew_share_hypothesis' matches the value of Andrew's share in the premise
    label = "entailment"
elif andrew_share_hypothesis < andrew_share_premise:
    # check if the value of 'andrew_share_hypothesis' contradicts the value of Andrew's share in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not match or contradict the premise value, the relation is neutral
    label = "neutral"

print(label)

