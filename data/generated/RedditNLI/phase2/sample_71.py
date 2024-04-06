# Premise: Goldman Sachs to pay $5.1 billion to settle toxic mortgage probe.
# Hypothesis: Goldman to Pay Up to $5 Billion to Settle Claims of Faulty Mortgages.
# Golden Label: contradiction

settlement_amount_premise = 5.1
settlement_amount_hypothesis = 5

# the hypothesis and premise mention the settlement amount Goldman Sachs has to pay
if settlement_amount_hypothesis > settlement_amount_premise:
    # check if the settlement amount in the hypothesis contradicts the settlement amount in the premise
    label = "contradiction"
elif settlement_amount_hypothesis < settlement_amount_premise:
    # check if the settlement amount in the hypothesis is less than the settlement amount in the premise
    label = "entailment"
else:
    # if the hypothesis value does not contradict or entail the premise one, we can infer neutrality
    label = "neutral"

print(label)

