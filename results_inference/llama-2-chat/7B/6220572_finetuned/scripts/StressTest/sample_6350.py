investment_premise = 90000
investment_hypothesis = 90000

# the hypothesis refers to the amount of investment mentioned in the premise
if investment_hypothesis == investment_premise:
    # check if the hypothesis value contradicts the investment amount in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
