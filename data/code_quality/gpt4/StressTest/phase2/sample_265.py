rahul_deepak_ratio_premise = 1 / 3
rahul_deepak_ratio_hypothesis = 4 / 3
rahul_age_future_premise = 26
rahul_age_future_hypothesis = 26

# the hypothesis refers to the ratio between Rahul and Deepak's age and Rahul's future age mentioned in the premise
if rahul_age_future_hypothesis != rahul_age_future_premise:
    # check if the future age of Rahul in the hypothesis contradicts the future age of Rahul reported in the premise
    label = "contradiction"
elif rahul_deepak_ratio_hypothesis <= rahul_deepak_ratio_premise:
    # check if the ratio between Rahul and Deepak in the hypothesis contradicts the ratio between Rahul and Deepak in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio between Rahul and Deepak
    # any ratio greater than 'rahul_deepak_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
