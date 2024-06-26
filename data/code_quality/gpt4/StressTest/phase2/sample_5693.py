ratio_premise = [4, 3]
ratio_hypothesis = [5, 3]
rahul_future_age_premise = 18
rahul_future_age_hypothesis = 18

# the hypothesis refers to the age ratios and future ages of Rahul and Deepak mentioned in the premise
if ratio_premise != ratio_hypothesis:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif rahul_future_age_premise != rahul_future_age_hypothesis:
    # check if Rahul's future age in the hypothesis contradicts Rahul's future age in the premise
    label = "contradiction"
else:
    # if the hypothesis values and ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
