rahul_deepak_ratio_premise = 6/3
rahul_deepak_ratio_hypothesis = 4/3
rahul_age_future_premise = 34
rahul_age_future_hypothesis = 34

# the hypothesis refers to the ratio between Rahul and Deepak and Rahul's future age, both mentioned in the premise
if rahul_deepak_ratio_hypothesis >= rahul_deepak_ratio_premise:
    # check if the ratio in the hypothesis contradicts the premise's estimate of less than 'rahul_deepak_ratio_premise'
    label = "contradiction"
elif rahul_age_future_hypothesis!= rahul_age_future_premise:
    # check if Rahul's future age in the hypothesis contradicts Rahul's future age reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio between Rahul and Deepak
    # any ratio less than 'rahul_deepak_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
