marbles_premise = float(16.0)
marbles_hypothesis = float(9.0)

# compare the number of marbles in the hypothesis to the number of marbles in the premise
if marbles_hypothesis <= marbles_premise:
    # if the number of marbles in the hypothesis does not exceed the number of marbles in the premise, we can infer entailment
    label = "entailment"
elif marbles_hypothesis > marbles_premise:
    # if the number of marbles in the hypothesis exceeds the number of marbles in the premise, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis and premise values are equal or within a reasonable range of each other, we can infer neutrality
    label = "neutral"

print(label)
