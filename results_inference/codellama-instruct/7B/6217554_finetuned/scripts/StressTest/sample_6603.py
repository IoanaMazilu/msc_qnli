investment_multiplier_premise = 2
investment_multiplier_hypothesis = 3

# the hypothesis talks about the investment multiplier mentioned in the premise
if investment_multiplier_hypothesis >= investment_multiplier_premise:
    # check if the hypothesis value contradicts the investment multiplier in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
