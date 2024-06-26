mary_age_ratio_premise = 2
mary_age_ratio_hypothesis = 5
betty_age_ratio_premise = 4
betty_age_ratio_hypothesis = 4

# the hypothesis refers to Albert's age relative to Mary's and Betty's, as mentioned in the premise
if mary_age_ratio_premise > mary_age_ratio_hypothesis:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif betty_age_ratio_hypothesis != betty_age_ratio_premise:
    # check if the ratio of Albert's age to Betty's age in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values and ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
