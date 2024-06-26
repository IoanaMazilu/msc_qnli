efficiency_premise = 25
efficiency_hypothesis = 35

# the hypothesis refers to the difference in efficiency between Suresh and Kamal
if efficiency_hypothesis <= efficiency_premise:
    # check if the hypothesis value contradicts the estimate of more than 'efficiency_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the difference in efficiency
    # any difference in efficiency greater than 'efficiency_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
