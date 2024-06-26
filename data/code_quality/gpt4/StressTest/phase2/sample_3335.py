rahul_deepak_ratio_premise = 4 / 3
rahul_deepak_ratio_hypothesis = 4 / 3
rahul_age_future_premise = 26
rahul_age_future_hypothesis = 26

# hypothesis talks about the ages of Rahul and Deepak and their ratio
if rahul_deepak_ratio_hypothesis <= rahul_deepak_ratio_premise:
    # check if the ratio in the hypothesis contradicts the one in the premise
    label = "contradiction"
elif rahul_age_future_hypothesis != rahul_age_future_premise:
    # check if the future age of Rahul in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
