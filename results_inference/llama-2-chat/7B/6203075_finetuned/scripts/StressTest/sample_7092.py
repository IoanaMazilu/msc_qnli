rahul_deepak_ratio_premise = 5/2
rahul_deepak_ratio_hypothesis = 8/2
rahul_age_premise = 26
rahul_age_hypothesis = 26

# the hypothesis refers to the ratio of Rahul and Deepak's age and the age of Rahul after 6 years, both mentioned in the premise
if rahul_deepak_ratio_hypothesis <= rahul_deepak_ratio_premise:
    # check if the hypothesis value contradicts the ratio in the premise
    label = "contradiction"
elif rahul_age_hypothesis!= rahul_age_premise:
    # check if the age of Rahul in the hypothesis contradicts the age of Rahul in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
