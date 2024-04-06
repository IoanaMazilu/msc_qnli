# Premise: The money would bring the running tab for both conflicts to about $947 billion, according to figures from the Congressional Research Service.
# Hypothesis: Funds would bring tab for Iraq and Afghanistan wars to $947 billion.
# Golden Label: neutral

conflicts_cost_premise = 947000000000
conflicts_cost_hypothesis = 947000000000

# the hypothesis mentions the total cost for the wars, which is also referenced in the premise
if conflicts_cost_hypothesis != conflicts_cost_premise:
    # check if the total cost in the hypothesis contradicts the total cost reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

