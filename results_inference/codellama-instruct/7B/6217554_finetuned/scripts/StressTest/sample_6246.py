investment_premise = 100000
investment_hypothesis = 600000

# the hypothesis talks about the investment amount mentioned in the premise
if investment_hypothesis >= investment_premise:
    # check if the investment amount in the hypothesis contradicts the investment amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value contradicts the premise one, we can infer entailment
    label = "entailment"

print(label)
