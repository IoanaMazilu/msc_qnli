rahul_deepak_ratio_premise = 5/2
rahul_deepak_ratio_hypothesis = 8/2
rahul_age_premise = 26
rahul_age_hypothesis = 26

# the hypothesis refers to the ratio of Rahul and Deepak, and Rahul's age, which are also mentioned in the premise
if rahul_deepak_ratio_hypothesis <= rahul_deepak_ratio_premise:
    # check if the hypothesis ratio contradicts the premise ratio
    label = "contradiction"
elif rahul_age_hypothesis!= rahul_age_premise:
    # check if Rahul's age in the hypothesis contradicts Rahul's age in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
