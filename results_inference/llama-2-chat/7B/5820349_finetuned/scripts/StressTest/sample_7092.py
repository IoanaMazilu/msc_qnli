ratio_premise = 5/2
ratio_hypothesis = 8/2
rahul_future_age_premise = 26
rahul_future_age_hypothesis = 26

# the hypothesis refers to the ratio between Rahul and Deepak and Rahul's future age, both mentioned in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the estimate of 'ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
elif rahul_future_age_hypothesis!= rahul_future_age_premise:
    # check if Rahul's future age in the hypothesis contradicts Rahul's future age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
