deal_premise = 5.1e9
deal_hypothesis = 5.1e9

# the hypothesis and premise mention the same deal amount for the acquisition of Costa Coffee by Coke
if deal_hypothesis!= deal_premise:
    # check if the deal amount in the hypothesis contradicts the deal amount in the premise
    label = "contradiction"
else:
    # if the deal amount in the hypothesis matches the deal amount in the premise, we can infer entailment
    label = "entailment"

print(label)
