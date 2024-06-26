capital_premise = 120
capital_hypothesis = 720

# the hypothesis refers to the capital of Thomas mentioned in the premise
if capital_premise >= capital_hypothesis:
    # check if the estimate of 'capital_premise' contradicts the estimate of 'capital_hypothesis'
    label = "contradiction"
else:
    # the premise gives a specific amount for the capital
    # any amount less than 'capital_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
