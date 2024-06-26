bottle_capacity_premise = 1000
bottle_capacity_hypothesis = 6000

# The hypothesis refers to the capacity of Emily's water bottle, which is also mentioned in the premise
if bottle_capacity_hypothesis < bottle_capacity_premise:
    # Check if the capacity value in the hypothesis contradicts the one in the premise
    label = "contradiction"
elif bottle_capacity_hypothesis > bottle_capacity_premise:
    # The hypothesis value does not contradict the premise, but cannot be explicitly entailed from it either
    label = "neutral"
else:
    # If the capacity value in the hypothesis matches exactly the one in the premise, we can infer entailment
    label = "entailment"

print(label)
