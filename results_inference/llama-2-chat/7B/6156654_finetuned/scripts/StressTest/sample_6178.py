rahul_deepak_ratio_premise = 6/3
rahul_deepak_ratio_hypothesis = 4/3
rahul_age_premise = 34
rahul_age_hypothesis = 34

# the hypothesis refers to the ratio of Rahul and Deepak, which is also mentioned in the premise
if rahul_deepak_ratio_hypothesis!= rahul_deepak_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif rahul_age_hypothesis!= rahul_age_premise:
    # check if the age in the hypothesis contradicts the age in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
