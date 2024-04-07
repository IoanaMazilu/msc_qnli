# Premise: Vijay bought less than 560 shirts at the rate of Rs.
# Hypothesis: Vijay bought 160 shirts at the rate of Rs.
# Golden Label: neutral

shirts_bought_premise = 560
shirts_bought_hypothesis = 160

# the hypothesis refers to the number of shirts Vijay bought, which is also mentioned in the premise
if shirts_bought_hypothesis >= shirts_bought_premise:
    # check if the hypothesis value contradicts the estimate of less than 'shirts_bought_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shirts
    # any number of shirts less than 'shirts_bought_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

