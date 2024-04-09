percentage_shrinkage_premise = 1.0
dollar_amount_hypothesis = 6000

# the premise gives the percentage change in the Saudi central bank's net foreign assets
# the hypothesis gives a specific dollar amount change
if percentage_shrinkage_premise!= dollar_amount_hypothesis:
    # check if the dollar amount in the hypothesis contradicts the percentage change in the premise
    label = "contradiction"
else:
    # if the dollar amount in the hypothesis is consistent with the percentage change in the premise, we can infer entailment
    label = "entailment"

print(label)
