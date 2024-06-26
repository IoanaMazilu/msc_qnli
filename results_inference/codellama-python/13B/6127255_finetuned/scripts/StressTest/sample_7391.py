efficiency_difference_premise = 10
efficiency_difference_hypothesis = 10

# the hypothesis refers to the efficiency difference between Rosy and Mary mentioned in the premise
if efficiency_difference_hypothesis >= efficiency_difference_premise:
    # check if the hypothesis value contradicts the efficiency difference in the premise
    label = "contradiction"
else:
    # the premise gives an exact efficiency difference
    # any efficiency difference less than 'efficiency_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
