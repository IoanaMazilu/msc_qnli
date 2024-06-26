investment_premise = 50000
investment_hypothesis = 50000

# the hypothesis refers to the investment made by Mr Sharad mentioned in the premise
if investment_hypothesis >= investment_premise:
    # check if the estimate of 'investment_hypothesis' contradicts the investment in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
