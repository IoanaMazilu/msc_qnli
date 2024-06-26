investment_premise = 50000
investment_hypothesis = 10000

# the hypothesis refers to the investment amount mentioned in the premise
if investment_premise <= investment_hypothesis:
    # check if the estimate of 'investment_hypothesis' contradicts the investment amount in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)