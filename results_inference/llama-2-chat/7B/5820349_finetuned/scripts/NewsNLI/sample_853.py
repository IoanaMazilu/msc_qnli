likely_attack_premise = 0.14
likely_attack_hypothesis = 0.30

# the hypothesis mentions the percentage of Americans who think an attack is likely, which is also referenced in the premise
if likely_attack_hypothesis!= likely_attack_premise:
    # check if the percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise percentage, we can infer entailment
    label = "entailment"

print(label)
