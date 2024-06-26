fine_premise = 14
fine_hypothesis = 14

# the hypothesis and premise mention the amount of the fine
if fine_premise!= fine_hypothesis:
    # check if the amount of the fine in the hypothesis contradicts the amount of the fine in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of the fine
    # any estimate of the amount in the hypothesis greater or equal to 'fine_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
