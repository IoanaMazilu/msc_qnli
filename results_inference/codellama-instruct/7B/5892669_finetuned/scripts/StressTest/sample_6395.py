oil_premise = 8
oil_hypothesis = 8

# the hypothesis refers to the amount of oil used in George's car, mentioned in the premise
if oil_hypothesis <= oil_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
