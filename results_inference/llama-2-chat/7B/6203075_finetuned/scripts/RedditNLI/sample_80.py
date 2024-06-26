deal_premise = 5.1e9
deal_hypothesis = 5.1e9

# the hypothesis and premise mention the deal value for Costa Coffee
if deal_hypothesis!= deal_premise:
    # check if the deal value in the hypothesis contradicts the deal value in the premise
    label = "contradiction"
else:
    # if the deal values are the same, we can infer entailment
    label = "entailment"

print(label)
