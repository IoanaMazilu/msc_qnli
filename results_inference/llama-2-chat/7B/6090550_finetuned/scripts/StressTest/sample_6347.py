investment_premise = 50000
investment_hypothesis = 50000

# the hypothesis talks about the investment amount, which is also mentioned in the premise
if investment_hypothesis >= investment_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
