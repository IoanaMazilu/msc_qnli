ratio_rahul_deepak_premise = 4/3
ratio_rahul_deepak_hypothesis = 6/3
rahul_age_future_premise = 26
rahul_age_future_hypothesis = 26

# the hypothesis talks about the ratio of Rahul to Deepak's age and Rahul's future age, both referenced in the premise
if ratio_rahul_deepak_hypothesis != ratio_rahul_deepak_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif rahul_age_future_hypothesis != rahul_age_future_premise:
    # check if Rahul's future age in the hypothesis contradicts the future age in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
