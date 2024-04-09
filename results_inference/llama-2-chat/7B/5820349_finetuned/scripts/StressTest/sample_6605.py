investment_return_premise = 2
investment_return_hypothesis = 2

# the hypothesis refers to the return on investment mentioned in the premise
if investment_return_hypothesis >= investment_return_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
