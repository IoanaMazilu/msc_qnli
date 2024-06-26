rahul_deepak_ratio_premise = 4 / 3
rahul_deepak_ratio_hypothesis = 2 / 3
rahul_future_age_premise = 26
rahul_future_age_hypothesis = 26

# hypothesis talks about the age of Rahul and the ratio between Rahul and Deepak's ages
# the ratio in the hypothesis and premise are mentioned explicitly
# the future age of Rahul in the premise and hypothesis are also given explicitly
if rahul_deepak_ratio_hypothesis != rahul_deepak_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif rahul_future_age_hypothesis != rahul_future_age_premise:
    # check if the future age of Rahul in the hypothesis contradicts the future age of Rahul in the premise
    label = "contradiction"
else:
    # if the values in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
