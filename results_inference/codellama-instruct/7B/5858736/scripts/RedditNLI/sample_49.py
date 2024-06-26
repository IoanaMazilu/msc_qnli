debt_premise = 570000000000
debt_hypothesis = 570000000000

# the hypothesis and premise mention the same amount of global debt
if debt_hypothesis!= debt_premise:
    # check if the amount of global debt in the hypothesis contradicts the amount of global debt in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
