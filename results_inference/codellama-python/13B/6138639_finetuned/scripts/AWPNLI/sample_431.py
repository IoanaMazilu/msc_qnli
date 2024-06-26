leaked_oil_premise = 6522.0 - 5165.0
leaked_oil_hypothesis = 1358.0

# the hypothesis refers to the amount of oil leaked, which is also mentioned in the premise
# check if the amount of oil leaked in the hypothesis contradicts the amount of oil leaked from the premise
if leaked_oil_hypothesis!= leaked_oil_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
