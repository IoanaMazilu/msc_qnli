weight_premise = 40000
weight_hypothesis = 160 # in feet

# the hypothesis mentions the length of a slab, which is not referenced in the premise
# the premise mentions the weight of a slab, which is not referenced in the hypothesis
# there is no numerical information in the premise that can contradict or be entailed by the hypothesis
# there is no numerical information in the hypothesis that can contradict or be entailed by the premise
label = "neutral"

print(label)
