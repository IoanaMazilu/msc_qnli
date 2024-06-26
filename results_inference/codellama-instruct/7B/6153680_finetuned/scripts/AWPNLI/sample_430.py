oil_leaked_premise = 6522.0 - 5165.0
oil_leaked_hypothesis = 1357.0

# the hypothesis refers to the amount of oil leaked, which is also mentioned in the premise
if oil_leaked_hypothesis!= oil_leaked_premise:
    # check if the amount of oil leaked in the hypothesis contradicts the amount of oil leaked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and the premise values are the same, we can infer entailment
    label = "entailment"

print(label)
