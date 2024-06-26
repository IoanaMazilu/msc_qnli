oil_leaked_premise = 6522.0 - 5165.0
oil_leaked_hypothesis = 1357.0

# the hypothesis refers to the amount of oil leaked, which is also mentioned in the premise
# compute the total amount of oil leaked from the premise
total_oil_leaked_premise = oil_leaked_premise
if total_oil_leaked_premise!= oil_leaked_hypothesis:
    # check if the amount of oil leaked in the hypothesis contradicts the amount of oil leaked from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
