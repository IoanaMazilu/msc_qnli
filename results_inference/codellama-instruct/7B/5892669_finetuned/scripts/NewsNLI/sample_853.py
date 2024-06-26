terrorist_attack_likely_premise = 0.14
terrorist_attack_likely_hypothesis = 0.30

# the hypothesis mentions the percentage of Americans who think an attack is likely, which is also referenced in the premise
# however, the hypothesis refers to a different type of attack (American soil) than the one mentioned in the premise
if terrorist_attack_likely_hypothesis!= terrorist_attack_likely_premise:
    # check if the percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise percentage, we can infer neutrality
    label = "neutral"

print(label)
