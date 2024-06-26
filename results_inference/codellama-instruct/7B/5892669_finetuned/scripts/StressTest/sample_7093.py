rahul_deepak_ratio_premise = 8/2
rahul_deepak_ratio_hypothesis = 5/2
rahul_age_future_premise = 26
rahul_age_future_hypothesis = 26

# the hypothesis refers to the ratio between Rahul and Deepak and Rahul's future age, both mentioned in the premise
if rahul_deepak_ratio_hypothesis >= rahul_deepak_ratio_premise:
    # check if the ratio in the hypothesis contradicts the estimate of less than 'rahul_deepak_ratio_premise'
    label = "contradiction"
elif rahul_age_future_hypothesis!= rahul_age_future_premise:
    # check if Rahul's future age in the hypothesis contradicts the future age reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio between Rahul and Deepak
    # any ratio less than 'rahul_deepak_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
