female_prisoners_ratio_premise = 3
female_prisoners_ratio_hypothesis = 3

# the hypothesis mentions the ratio of female prisoners to male prisoners, which is also referenced in the premise
if female_prisoners_ratio_hypothesis!= female_prisoners_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio reported in the premise
    label = "contradiction"
else:
    # if the hypothesis ratio does not contradict the premise ratio, we can infer entailment
    label = "entailment"

print(label)
