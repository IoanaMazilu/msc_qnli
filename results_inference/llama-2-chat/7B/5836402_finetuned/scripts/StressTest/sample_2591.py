sameer_age_ratio_premise = 5/4
sameer_age_ratio_hypothesis = 5/4

# the hypothesis refers to the ratio of the ages of Sameer and Anand mentioned in the premise
if sameer_age_ratio_premise >= sameer_age_ratio_hypothesis:
    # check if the ratio of ages in the hypothesis contradicts the ratio of ages in the premise
    label = "contradiction"
else:
    # if the ratio of ages in the hypothesis does not contradict the ratio of ages in the premise, we can infer entailment
    label = "entailment"

print(label)
