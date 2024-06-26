weight_premise = 40000
weight_hypothesis = 160

# the hypothesis mentions the length of the slab, which is not referenced in the premise
# the premise mentions the weight of the slab, but the weight is not directly related to the length of the slab
# the premise also mentions the percentage of sand, shells and water in the slab, but this information is not directly related to the length of the slab
# the premise and hypothesis do not contradict each other, but the hypothesis cannot be fully and explicitly entailed from the premise
label = "neutral"

print(label)
