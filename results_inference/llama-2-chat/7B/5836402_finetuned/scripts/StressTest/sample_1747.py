sameer_age_ratio_premise = 1/4
anand_age_ratio_premise = 1/4
sameer_age_ratio_hypothesis = 5/4
anand_age_ratio_hypothesis = 5/4

# the hypothesis refers to the ratio of Sameer and Anand's ages mentioned in the premise
if sameer_age_ratio_hypothesis <= sameer_age_ratio_premise or \
   anand_age_ratio_hypothesis <= anand_age_ratio_premise:
    # check if the ratio of Sameer and Anand's ages in the hypothesis contradicts the ratio of their ages in the premise
    label = "contradiction"
else:
    # if the ratio of Sameer and Anand's ages in the hypothesis does not contradict the ratio of their ages in the premise, we can infer entailment
    label = "entailment"

print(label)
