amount_premise = 5.1
amount_hypothesis = 5.1

# the hypothesis and premise mention the amount of money involved in the deal for Costa Coffee
if amount_hypothesis!= amount_premise:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
