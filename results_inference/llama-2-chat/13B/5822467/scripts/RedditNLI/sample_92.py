fine_premise = 1400000000
settlement_hypothesis = 140000000

# the premise and hypothesis mention a fine and a settlement in billion dollars
if fine_premise!= settlement_hypothesis:
    # check if the amount of the fine in the hypothesis contradicts the amount of the fine in the premise
    label = "contradiction"
elif settlement_hypothesis > fine_premise:
    # check if the amount of the settlement in the hypothesis contradicts the premise estimate of only $14 billion
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of the fine
    # any amount of the settlement in the hypothesis greater or equal to $14 billion is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
