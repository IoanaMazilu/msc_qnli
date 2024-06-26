initial_oil_premise = 6522.0
leaked_oil_premise = 5165.0
leaked_oil_hypothesis = 1358.0

# the hypothesis refers to the amount of oil leaked, which is also mentioned in the premise
# compute the leaked oil from the premise
leaked_oil_premise = initial_oil_premise - leaked_oil_premise
if leaked_oil_hypothesis!= leaked_oil_premise:
    # check if the amount of leaked oil in the hypothesis contradicts the amount of leaked oil from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
