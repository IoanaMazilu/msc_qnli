investment_return_premise = 2
investment_return_hypothesis = 3

# the hypothesis refers to the return on investment mentioned in the premise
if investment_return_hypothesis <= investment_return_premise:
    # check if the estimate of 'investment_return_hypothesis' contradicts the return on investment in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
