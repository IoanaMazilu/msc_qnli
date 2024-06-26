amount_premise = 5.1
amount_hypothesis = 5.1

# the hypothesis and premise mention the same amount of money for the deal
if amount_premise!= amount_hypothesis:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the amount in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
