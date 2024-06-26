efficiency_premise = 10
efficiency_hypothesis = 10

# the hypothesis refers to the efficiency of Rosy compared to Mary
if efficiency_hypothesis >= efficiency_premise:
    # check if the hypothesis value contradicts the estimate of 'efficiency_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the efficiency of Rosy compared to Mary
    # any value less than 'efficiency_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
