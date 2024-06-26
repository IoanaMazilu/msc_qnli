rahul_deepak_ratio_premise = 4/3
rahul_deepak_ratio_hypothesis = 6/3
rahul_future_age_premise = 50
rahul_future_age_hypothesis = 50

# the hypothesis refers to the age ratio between Rahul and Deepak and to Rahul's future age, mentioned in the premise
if rahul_deepak_ratio_hypothesis != rahul_deepak_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
elif rahul_future_age_hypothesis != rahul_future_age_premise:
    # check if Rahul's future age in the hypothesis contradicts the one given in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
