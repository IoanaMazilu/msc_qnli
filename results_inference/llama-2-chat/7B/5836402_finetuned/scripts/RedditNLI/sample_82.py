investment_premise = 1
investment_hypothesis = 1

# the hypothesis and premise mention the amount of investment from General Motors
if investment_hypothesis!= investment_premise:
    # check if the amount of investment in the hypothesis contradicts the amount of investment in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
