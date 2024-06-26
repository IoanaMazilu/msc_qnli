investment_premise = 50000
investment_hypothesis = 50000

# the hypothesis refers to the investment made by Mr Sharad, which is also mentioned in the premise
if investment_hypothesis >= investment_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
