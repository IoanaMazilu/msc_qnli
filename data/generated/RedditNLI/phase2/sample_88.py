# Premise: Goldman to Pay Up to $5 Billion to Settle Claims of Faulty Mortgages.
# Hypothesis: Goldman Sachs to pay $5.1 billion to settle toxic mortgage probe.
# Golden Label: contradiction

settlement_premise = 5
settlement_hypothesis = 5.1

# The hypothesis and premise mention the settlement Goldman will pay
if settlement_hypothesis > settlement_premise:
    # Check if the settlement amount in the hypothesis contradicts the maximum settlement amount in the premise
    label = "contradiction"
elif settlement_hypothesis <= settlement_premise:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

