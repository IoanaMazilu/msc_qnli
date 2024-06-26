weight_premise = 40000
weight_hypothesis = 160 * 12 # 160 feet x 12 inches per foot

# the hypothesis mentions the length of the slab, which is not mentioned in the premise
# therefore, we cannot entail or contradict the premise
label = "neutral"

print(label)
