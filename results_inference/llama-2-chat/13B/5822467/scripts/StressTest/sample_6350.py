investment_premise = 90000
investment_hypothesis = 100000
months_premise = 4

# the hypothesis refers to the amount of investment and the time period mentioned in the premise
if investment_hypothesis <= investment_premise:
    # check if the estimate of 'investment_hypothesis' contradicts the amount of investment in the premise
    label = "contradiction"
elif months_premise!= months_hypothesis:
    # check if the time period in the hypothesis contradicts the time period reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
