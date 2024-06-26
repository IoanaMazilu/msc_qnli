sameer_age_ratio_premise = 3/4
anand_age_ratio_premise = 3/4
sameer_age_ratio_hypothesis = 5/4
anand_age_ratio_hypothesis = 5/4

# the hypothesis refers to the ratio of the ages of Sameer and Anand mentioned in the premise
if sameer_age_ratio_hypothesis!= sameer_age_ratio_premise:
    # check if the ratio of Sameer's age in the hypothesis contradicts the ratio of Sameer's age in the premise
    label = "contradiction"
elif anand_age_ratio_hypothesis!= anand_age_ratio_premise:
    # check if the ratio of Anand's age in the hypothesis contradicts the ratio of Anand's age in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
