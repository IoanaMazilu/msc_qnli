investment_premise = 1
investment_hypothesis = 1

# the hypothesis and premise mention the amount of investment by General Motors in the US
if investment_hypothesis < investment_premise:
    # check if the investment amount in the hypothesis contradicts the investment amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
