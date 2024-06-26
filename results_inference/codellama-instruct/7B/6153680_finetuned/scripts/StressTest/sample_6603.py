investment_multiplier = 2
hypothesis_investment_multiplier = 3

# the hypothesis refers to the investment multiplier mentioned in the premise
if investment_multiplier >= hypothesis_investment_multiplier:
    # check if the investment multiplier in the hypothesis contradicts the investment multiplier in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
