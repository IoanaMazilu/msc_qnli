oil_leaked_premise = 6522.0
oil_leaked_hypothesis = 1357.0

# the hypothesis refers to the amount of oil leaked, which is also mentioned in the premise
# compute the amount of oil leaked in the premise
oil_leaked_premise = oil_leaked_premise - oil_leaked_hypothesis
if oil_leaked_premise!= oil_leaked_hypothesis:
    # check if the amount of oil leaked from the hypothesis contradicts the amount of oil leaked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
