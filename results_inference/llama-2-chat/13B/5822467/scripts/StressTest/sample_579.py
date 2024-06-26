alice_leaves_premise = 30
bob_leaves_premise = 0
alice_leaves_hypothesis = -60

# the hypothesis refers to the time difference between Alice and Bob's departure
if alice_leaves_hypothesis > bob_leaves_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif alice_leaves_hypothesis < bob_leaves_premise:
    # check if the hypothesis value is consistent with the premise
    label = "neutral"
else:
    # the premise only gives an estimate for the time difference
    # any time difference less than 60 minutes is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
