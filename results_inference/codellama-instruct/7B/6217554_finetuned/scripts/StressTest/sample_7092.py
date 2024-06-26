ratio_rahul_deepak_premise = 5/2
ratio_rahul_deepak_hypothesis = 8/2
rahul_age_future_premise = 26
rahul_age_future_hypothesis = 26

# the hypothesis refers to the ratio between Rahul and Deepak and Rahul's age in the future, both mentioned in the premise
if ratio_rahul_deepak_hypothesis <= ratio_rahul_deepak_premise:
    # check if the estimate of the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif rahul_age_future_hypothesis!= rahul_age_future_premise:
    # check if the age of Rahul in the future in the hypothesis contradicts the age of Rahul in the future reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
