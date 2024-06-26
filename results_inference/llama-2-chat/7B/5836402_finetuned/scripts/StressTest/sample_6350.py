investment_premise = 90000
investment_hypothesis = 90000

# the hypothesis refers to the amount of investment mentioned in the premise
if investment_hypothesis!= investment_premise:
    # check if the amount of investment in the hypothesis contradicts the amount of investment reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
