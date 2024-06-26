investment_duration_premise = 6
investment_duration_hypothesis = 7

# the hypothesis refers to the duration of investment mentioned in the premise
if investment_duration_hypothesis < investment_duration_premise:
    # check if the estimate of 'investment_duration_hypothesis' contradicts the duration of investment in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
