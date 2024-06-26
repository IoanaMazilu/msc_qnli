justification_premise = 100
justification_hypothesis = 100

# the hypothesis mentions the justification percentage given by the officer's lawyer, which is also mentioned in the premise
if justification_hypothesis != justification_premise:
    # check if the justification percentage in the hypothesis contradicts the justification percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
