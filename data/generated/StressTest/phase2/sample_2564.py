# Premise: If Tim received $800 more than Jim did, what was the profit made by their business in that year?
# Hypothesis: If Tim received $700 more than Jim did, what was the profit made by their business in that year?
# Golden Label: contradiction

profit_tim_premise = 800
profit_tim_hypothesis = 700

# The hypothesis is talking about the profit that Tim made over Jim, which is also mentioned in the premise.
if profit_tim_premise != profit_tim_hypothesis:
    # Check if the profit made by Tim in the hypothesis contradicts the profit mentioned in the premise.
    label = "contradiction"
else:
    # If the profits are the same, then it's an entailment.
    label = "entailment"

print(label)

