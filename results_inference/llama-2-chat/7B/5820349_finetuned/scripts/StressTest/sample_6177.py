rahul_deepak_ratio_premise = 4 / 3
rahul_deepak_ratio_hypothesis = 6 / 3
rahul_age_future_premise = 34
rahul_age_future_hypothesis = 34

# the hypothesis refers to the ratio between Rahul and Deepak and Rahul's future age, both mentioned in the premise
if rahul_deepak_ratio_hypothesis <= rahul_deepak_ratio_premise:
    # check if the estimate of 'rahul_deepak_ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
elif rahul_age_future_hypothesis!= rahul_age_future_premise:
    # check if the future age of Rahul in the hypothesis contradicts the future age of Rahul reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
