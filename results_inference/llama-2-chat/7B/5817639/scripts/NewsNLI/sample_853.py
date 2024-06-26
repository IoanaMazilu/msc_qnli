likely_attack_premise = 0.14
likely_attack_hypothesis = 0.3

# check if the percentage of people thinking an attack is likely in the hypothesis contradicts the percentage in the premise
if likely_attack_hypothesis!= likely_attack_premise:
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
