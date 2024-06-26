capital_premise = 300
capital_hypothesis = 600

# the hypothesis refers to the capital of James, which is mentioned in the premise
if capital_premise >= capital_hypothesis:
    # check if the estimate of 'capital_hypothesis' contradicts the capital in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the capital of James
    # any capital less than 'capital_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
