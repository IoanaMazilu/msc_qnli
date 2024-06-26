sameer_age_premise = 1
anand_age_premise = 4
sameer_age_hypothesis = 5
anand_age_hypothesis = 4

# the hypothesis refers to the ratio of ages of Sameer and Anand mentioned in the premise
if sameer_age_hypothesis!= sameer_age_premise or anand_age_hypothesis!= anand_age_premise:
    # check if the ratio of ages in the hypothesis contradicts the ratio of ages reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
