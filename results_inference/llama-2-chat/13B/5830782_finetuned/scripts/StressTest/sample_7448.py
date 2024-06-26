rahul_deepak_ratio_premise = 4 / 3
rahul_deepak_ratio_hypothesis = 2 / 3
rahul_future_age_premise = 26
rahul_future_age_hypothesis = 26

# the hypothesis refers to the ratio between Rahul and Deepak's ages and Rahul's future age
if rahul_deepak_ratio_hypothesis!= rahul_deepak_ratio_premise:
    # check if the ratio between Rahul and Deepak's ages in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
elif rahul_future_age_hypothesis!= rahul_future_age_premise:
    # check if Rahul's future age in the hypothesis contradicts Rahul's future age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
