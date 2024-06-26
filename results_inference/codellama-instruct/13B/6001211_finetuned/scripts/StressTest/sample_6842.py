investment_duration_premise = 6
investment_amount_premise = 20000
investment_duration_hypothesis = 6
investment_amount_hypothesis = 20000

# the hypothesis refers to the duration and amount of investment mentioned in the premise
if investment_duration_hypothesis <= investment_duration_premise:
    # check if the duration of investment in the hypothesis contradicts the duration of investment in the premise
    label = "contradiction"
elif investment_amount_hypothesis!= investment_amount_premise:
    # check if the amount of investment in the hypothesis contradicts the amount of investment in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)