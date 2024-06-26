amount_premise = 7.2
amount_hypothesis = 7.15

# the premise and hypothesis mention the amount of money involved in the transaction
if amount_hypothesis!= amount_premise:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the amounts in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
