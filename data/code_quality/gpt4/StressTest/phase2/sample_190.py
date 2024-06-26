neelam_age_ratio_premise = 1/3
shaan_age_ratio_premise = 1/2
shaan_age_premise = 6

neelam_age_ratio_hypothesis = 1/3
shaan_age_ratio_hypothesis = 1/2
shaan_age_hypothesis = 5

# the hypothesis refers to the ratio of Neelam's age and Shaan's age mentioned in the premise
if neelam_age_ratio_hypothesis != neelam_age_ratio_premise or shaan_age_ratio_hypothesis != shaan_age_ratio_premise:
    # check if the ratio for Neelam's age or Shaan's age in the hypothesis contradict the ratios in the premise
    label = "contradiction"
elif shaan_age_hypothesis >= shaan_age_premise:
    # check if Shaan's age in the hypothesis contradicts the age in the premise
    label = "contradiction"
else:
    # if the ratios and ages in the hypothesis do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
