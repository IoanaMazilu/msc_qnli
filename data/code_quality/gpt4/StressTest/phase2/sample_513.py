rahul_deepak_ratio_premise = 4/3
rahul_deepak_ratio_hypothesis = 3/3
rahul_age_future_premise = 22
rahul_age_future_hypothesis = 22

# the hypothesis talks about the ratio between Rahul and Deepak's ages and Rahul's future age, both mentioned in the premise
if rahul_deepak_ratio_hypothesis <= rahul_deepak_ratio_premise:
    # check if the hypothesis value contradicts the ratio given in the premise
    label = "contradiction"
elif rahul_age_future_hypothesis != rahul_age_future_premise:
    # check if the future age of Rahul in the hypothesis contradicts the future age of Rahul in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
