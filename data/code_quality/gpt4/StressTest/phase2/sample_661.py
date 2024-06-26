efficiency_premise = 30
efficiency_hypothesis = 40

# the hypothesis refers to the percentage efficiency of Rosy over Mary, as mentioned in the premise
if efficiency_hypothesis <= efficiency_premise:
    # check if the hypothesis value contradicts the estimate of more than 'efficiency_premise'% efficiency
    label = "contradiction"
else:
    # the premise gives only a lower limit for Rosy's efficiency over Mary
    # any efficiency percentage greater than 'efficiency_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
