sameer_anand_ratio_premise = 5/4
sameer_anand_ratio_hypothesis = 3/4

# the hypothesis refers to the ratio of ages of Sameer and Anand mentioned in the premise
if sameer_anand_ratio_hypothesis >= sameer_anand_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis ratio does not contradict the premise ratio, we can infer entailment
    label = "entailment"

print(label)
