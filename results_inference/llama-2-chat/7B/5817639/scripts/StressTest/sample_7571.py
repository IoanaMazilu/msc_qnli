dist_premise = 35
dist_hypothesis = 35

# the hypothesis refers to the distance between Fred and Sam, which is also mentioned in the premise
if dist_hypothesis == dist_premise:
    # if the distance in the hypothesis is equal to the distance in the premise, we can infer entailment
    label = "entailment"
elif dist_hypothesis > dist_premise:
    # if the distance in the hypothesis is greater than the distance in the premise, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis and premise provide the same distance information, but the hypothesis provides a different estimate, we can infer neutrality
    label = "neutral"

print(label)
