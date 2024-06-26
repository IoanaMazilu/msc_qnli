investment_premise = 90000
investment_hypothesis = 90000

# the hypothesis refers to the investment amount mentioned in the premise
if investment_hypothesis >= investment_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
