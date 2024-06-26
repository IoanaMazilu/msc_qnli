leaked_oil_premise = 6522.0 - 5165.0
leaked_oil_hypothesis = 1357.0

if leaked_oil_hypothesis!= leaked_oil_premise:
    # check if the number of leaked oil from the hypothesis contradicts the number of leaked oil from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
