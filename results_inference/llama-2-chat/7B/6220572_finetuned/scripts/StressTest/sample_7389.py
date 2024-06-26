efficiency_premise = 10
efficiency_hypothesis = 30

if efficiency_hypothesis >= efficiency_premise:
    # check if the hypothesis value contradicts the estimate of less than 'efficiency_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the efficiency difference
    # any efficiency difference greater than 'efficiency_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
