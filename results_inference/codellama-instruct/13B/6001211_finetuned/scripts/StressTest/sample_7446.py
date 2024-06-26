rahul_deepak_ratio_premise = 4/3
rahul_deepak_ratio_hypothesis = 1/3
rahul_age_future_premise = 26
rahul_age_future_hypothesis = 26

# the hypothesis refers to the ratio between Rahul and Deepak's ages and Rahul's future age, both mentioned in the premise
if rahul_deepak_ratio_premise <= rahul_deepak_ratio_hypothesis:
    # check if the estimate of 'rahul_deepak_ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
elif rahul_age_future_hypothesis!= rahul_age_future_premise:
    # check if the future age of Rahul in the hypothesis contradicts the future age of Rahul reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
