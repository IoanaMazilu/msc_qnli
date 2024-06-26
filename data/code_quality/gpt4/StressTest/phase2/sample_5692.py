rahul_deepak_ratio_premise = 1/3
rahul_deepak_ratio_hypothesis = 4/3
rahul_age_future_premise = 18
rahul_age_future_hypothesis = 18

# the hypothesis talks about the ratio between Rahul and Deepak and Rahul's future age, both mentioned in the premise
if rahul_deepak_ratio_hypothesis <= rahul_deepak_ratio_premise:
    # check if the ratio in the hypothesis contradicts the estimate of more than 'rahul_deepak_ratio_premise'
    label = "contradiction"
elif rahul_age_future_hypothesis != rahul_age_future_premise:
    # check if the future age of Rahul in the hypothesis contradicts the future age reported in the premise
    label = "contradiction"
else:
    # the ratio in the premise gives only an estimate,
    # any ratio greater than 'rahul_deepak_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
