investment_premise = 100000
investment_hypothesis = 100000

# the hypothesis refers to the amount of money invested by Raviraj, which is also mentioned in the premise
if investment_hypothesis >= investment_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
