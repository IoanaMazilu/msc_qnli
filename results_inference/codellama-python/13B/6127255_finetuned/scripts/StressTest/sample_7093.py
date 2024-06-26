rahul_deepak_ratio_premise = 8/2
rahul_deepak_ratio_hypothesis = 5/2
rahul_age_future_premise = 26
rahul_age_future_hypothesis = 26

# the hypothesis talks about the ratio between Rahul and Deepak's ages and Rahul's future age, both referenced in the premise
if rahul_age_future_hypothesis!= rahul_age_future_premise:
    # check if the future age of Rahul in the hypothesis contradicts the future age of Rahul in the premise
    label = "contradiction"
elif rahul_deepak_ratio_hypothesis >= rahul_deepak_ratio_premise:
    # check if the ratio between Rahul and Deepak in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio between Rahul and Deepak
    # any ratio less than 'rahul_deepak_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
