efficient_premise = 35
efficient_hypothesis = 25

# the hypothesis refers to the efficiency of Suresh compared to Kamal mentioned in the premise
if efficient_hypothesis >= efficient_premise:
    # check if the hypothesis value contradicts the estimate of less than 'efficient_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the efficiency
    # any efficiency less than 'efficient_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
