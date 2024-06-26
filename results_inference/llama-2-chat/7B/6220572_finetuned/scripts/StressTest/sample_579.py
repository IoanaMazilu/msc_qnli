alice_leaves_premise = 30
alice_leaves_hypothesis = 60

# the hypothesis refers to the time Alice leaves City A after Bob, also mentioned in the premise
if alice_leaves_hypothesis <= alice_leaves_premise:
    # check if the estimate of 'alice_leaves_hypothesis' contradicts the time Alice leaves City A in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Alice leaves City A
    # any time greater than 'alice_leaves_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
