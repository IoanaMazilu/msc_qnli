sameer_anand_ratio_premise = 5/4
sameer_anand_ratio_hypothesis = 5/4

# the hypothesis refers to the ratio of ages of Sameer and Anand mentioned in the premise
if sameer_anand_ratio_hypothesis >= sameer_anand_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis is less than the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)
