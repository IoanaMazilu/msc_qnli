capital_premise = 600
capital_hypothesis = 300

# the premise gives a range of values for James' capital, while the hypothesis gives a single value
if capital_hypothesis <= capital_premise:
    # check if the hypothesis value contradicts the estimate of less than 'capital_premise'
    label = "contradiction"
else:
    # the premise gives a range of values, and any value within that range is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
