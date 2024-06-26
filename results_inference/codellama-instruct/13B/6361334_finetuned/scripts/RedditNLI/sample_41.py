surplus_premise = 4.61
surplus_hypothesis = 7.01

# the hypothesis and premise mention the amount of surplus added to the economy
if surplus_hypothesis < surplus_premise:
    # check if the amount of surplus in the hypothesis contradicts the amount of surplus in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of surplus
    # any estimate of the amount in the hypothesis greater or equal to'surplus_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
