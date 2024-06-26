rahul_deepak_ratio_premise = 4/3
rahul_deepak_ratio_hypothesis = 5/3
rahul_future_age_premise = 26
rahul_future_age_hypothesis = 26

# the hypothesis talks about the ratio between Rahul and Deepak and Rahul's future age, both referenced in the premise
if rahul_deepak_ratio_premise != rahul_deepak_ratio_hypothesis:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif rahul_future_age_premise != rahul_future_age_hypothesis:
    # check if Rahul's future age in the hypothesis contradicts Rahul's future age in the premise
    label = "contradiction"
else:
    # if the ratio and future age in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
