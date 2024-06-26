investment_premise = 8000
investment_hypothesis = 2000

# the hypothesis refers to the amount of money invested by Sachi, mentioned in the premise
if investment_hypothesis!= investment_premise:
    # check if the amount of investment in the hypothesis contradicts the amount of investment reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
