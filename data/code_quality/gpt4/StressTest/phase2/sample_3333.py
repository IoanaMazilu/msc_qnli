# defining variables
rahul_deepak_ratio_premise = 4 / 3
rahul_deepak_ratio_hypothesis = 6 / 3
rahul_age_premise = 26
rahul_age_hypothesis = 26

# the hypothesis refers to the ratio between Rahul and Deepak and Rahul's age after 22 years
if rahul_deepak_ratio_hypothesis >= rahul_deepak_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif rahul_age_hypothesis != rahul_age_premise:
    # check if the age in the hypothesis contradicts the age in the premise
    label = "contradiction"
else:
    # if the hypothesis values does not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
