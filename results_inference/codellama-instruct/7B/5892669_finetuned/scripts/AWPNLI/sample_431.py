oil_leaked_premise = 6522.0
oil_leaked_hypothesis = 1358.0

# the hypothesis refers to the amount of oil leaked, which is also mentioned in the premise
# compute the amount of oil leaked in the premise
oil_leaked_premise -= oil_leaked_hypothesis
if oil_leaked_premise < 0:
    # check if the amount of oil leaked in the hypothesis contradicts the amount of oil leaked from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
