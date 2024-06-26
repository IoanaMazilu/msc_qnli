import math

bottle_capacity_premise = 1000 * math.pi
bottle_capacity_hypothesis = 1000 * math.pi

# The hypothesis mentions the capacity of Emily's water bottle that is also mentioned in the premise.
if bottle_capacity_hypothesis >= bottle_capacity_premise:
    # Check if the hypothesis value contradicts the premise of 'bottle_capacity_premise'
    label = "contradiction"
else:
    # If the hypothesis value is less than the premise, we can infer entailment
    label = "entailment"

print(label)
