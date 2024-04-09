birds_premise = 6.0
nests_premise = 3.0
birds_hypothesis = 9.0

# compare the number of birds in the hypothesis to the number of birds in the premise
if birds_hypothesis == birds_premise:
    # if the number of birds in the hypothesis is equal to the number of birds in the premise, we can infer entailment
    label = "entailment"
else:
    # if the number of birds in the hypothesis is greater than the number of birds in the premise, we can infer contradiction
    label = "contradiction"

# compare the number of nests in the hypothesis to the number of nests in the premise
if birds_hypothesis == nests_premise:
    # if the number of nests in the hypothesis is equal to the number of nests in the premise, we can infer entailment
    label = "entailment"
else:
    # if the number of nests in the hypothesis is greater than the number of nests in the premise, we can infer contradiction
    label = "contradiction"

print(label)
