investment_premise = 20000
investment_hypothesis = 20000
months_premise = 7
months_hypothesis = 6

# the hypothesis refers to the amount invested and the duration of investment mentioned in the premise
if investment_hypothesis!= investment_premise:
    # check if the investment amount in the hypothesis contradicts the investment amount reported in the premise
    label = "contradiction"
elif months_hypothesis >= months_premise:
    # check if the duration of investment in the hypothesis contradicts the duration of investment reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
