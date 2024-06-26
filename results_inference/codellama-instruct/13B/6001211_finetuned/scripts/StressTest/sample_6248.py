investment_premise = 100000
investment_hypothesis = 100000

# the hypothesis refers to the amount invested by Raviraj, mentioned also in the premise
if investment_hypothesis >= investment_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
