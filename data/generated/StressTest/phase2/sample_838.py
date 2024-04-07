# Premise: Vijay bought less than 760 shirts at the rate of Rs.
# Hypothesis: Vijay bought 160 shirts at the rate of Rs.
# Golden Label: neutral

shirts_bought_premise = 760
shirts_bought_hypothesis = 160

# the hypothesis refers to the number of shirts bought by Vijay mentioned in the premise
if shirts_bought_hypothesis >= shirts_bought_premise:
    # check if the number of 'shirts_bought_hypothesis' contradicts the number of shirts in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shirts
    # any number of shirts less than 'shirts_bought_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

