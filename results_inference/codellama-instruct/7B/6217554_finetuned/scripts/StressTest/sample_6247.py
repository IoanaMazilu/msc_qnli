investment_premise = 600000
investment_hypothesis = 100000

# the hypothesis talks about the investment amount mentioned in the premise
if investment_hypothesis >= investment_premise:
    # check if the investment amount in the hypothesis contradicts the estimate of less than 'investment_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
