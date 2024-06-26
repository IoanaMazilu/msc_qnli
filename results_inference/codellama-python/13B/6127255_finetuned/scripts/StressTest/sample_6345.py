investment_premise = 50000
investment_hypothesis = 10000

# the hypothesis refers to the amount of money Mr Sharad invested in his business, which is also mentioned in the premise
if investment_premise <= investment_hypothesis:
    # check if the investment amount in the premise contradicts the hypothesis of more than 'investment_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
