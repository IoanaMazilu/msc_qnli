efficiency_premise = 35
efficiency_hypothesis = 25

# the hypothesis refers to the efficiency of Suresh compared to Kamal mentioned in the premise
if efficiency_hypothesis >= efficiency_premise:
    # check if the hypothesis value contradicts the estimate of less than 'efficiency_premise'
    label = "contradiction"
elif efficiency_hypothesis < efficiency_premise:
    # the premise gives only an estimate for the efficiency of Suresh
    # any efficiency less than 'efficiency_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
