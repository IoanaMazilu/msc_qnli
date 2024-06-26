weight_premise = 40000
weight_sand_premise = 0.85
length_hypothesis = 160

# the hypothesis mentions the length of the slab, which is not referenced in the premise
# the premise mentions the weight of the slab, but does not provide a specific value
# the premise also mentions the percentage of sand in the weight, but does not provide a specific value
# thus, we cannot infer the length of the slab from the premise, and the premise does not contradict the hypothesis
label = "neutral"

print(label)
