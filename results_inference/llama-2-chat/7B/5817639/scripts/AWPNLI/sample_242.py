weight_premise = 42.0
weight_hypothesis = 14.0

# compare the weight of the books in the hypothesis to the weight of the books in the premise
if weight_hypothesis == weight_premise:
    # if the weight of the books in the hypothesis is the same as the weight of the books in the premise, we can infer entailment
    label = "entailment"
else:
    # if the weight of the books in the hypothesis contradicts the weight of the books in the premise, we can infer contradiction
    label = "contradiction"

print(label)
