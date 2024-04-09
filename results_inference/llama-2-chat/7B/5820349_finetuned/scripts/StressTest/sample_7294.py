capital_premise = 600
capital_hypothesis = 300

# the hypothesis refers to the capital of James mentioned in the premise
if capital_hypothesis >= capital_premise:
    # check if the value of 'capital_hypothesis' contradicts the estimate of less than 'capital_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the capital
    # any value of 'capital_hypothesis' less than 'capital_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
