sameer_age_ratio_premise = 5/4
anand_age_ratio_premise = 5/4
sameer_age_ratio_hypothesis = 3/4
anand_age_ratio_hypothesis = 3/4

# the hypothesis refers to the ratio of the ages of Sameer and Anand mentioned in the premise
if sameer_age_ratio_hypothesis <= sameer_age_ratio_premise:
    # check if the estimate of'sameer_age_ratio_hypothesis' contradicts the ratio of ages in the premise
    label = "contradiction"
elif anand_age_ratio_hypothesis!= anand_age_ratio_premise:
    # check if the ratio of ages in the hypothesis contradicts the ratio of ages reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
