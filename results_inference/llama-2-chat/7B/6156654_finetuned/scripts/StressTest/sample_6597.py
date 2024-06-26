distance_efrida_frazer_premise = 15
distance_efrida_frazer_hypothesis = 35

# the hypothesis refers to the distance between Efrida and Frazer's homes, which is also mentioned in the premise
if distance_efrida_frazer_hypothesis < distance_efrida_frazer_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
