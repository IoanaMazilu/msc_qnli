lewis_age_ratio_premise = 1
brown_age_ratio_premise = 2
lewis_age_ratio_hypothesis = 1
brown_age_ratio_hypothesis = 2

# the hypothesis refers to the age ratio of Lewis and Brown mentioned in the premise
if lewis_age_ratio_hypothesis >= lewis_age_ratio_premise:
    # check if the estimate of 'lewis_age_ratio_hypothesis' contradicts the age ratio of Lewis in the premise
    label = "contradiction"
elif brown_age_ratio_hypothesis >= brown_age_ratio_premise:
    # check if the estimate of 'brown_age_ratio_hypothesis' contradicts the age ratio of Brown in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
