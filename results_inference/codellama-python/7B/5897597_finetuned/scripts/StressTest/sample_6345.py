investment_premise = 50000
investment_hypothesis = 10000

# the hypothesis refers to the amount of money Mr Sharad invested, which is also mentioned in the premise
if investment_premise <= investment_hypothesis:
    # check if the amount of investment in the premise contradicts the estimate of 'investment_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
