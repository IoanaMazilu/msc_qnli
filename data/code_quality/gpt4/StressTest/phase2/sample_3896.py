# define variables for the ratios and Rahul's future age
ratio_premise_rahul = 4
ratio_premise_deepak = 3
ratio_hypothesis_rahul = 1
ratio_hypothesis_deepak = 3
rahul_future_age_premise = 30
rahul_future_age_hypothesis = 30

# the hypothesis refers to the ratio between Rahul and Deepak's ages and Rahul's future age, all mentioned in the premise
if ratio_premise_rahul != ratio_hypothesis_rahul or ratio_premise_deepak != ratio_hypothesis_deepak:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif rahul_future_age_premise != rahul_future_age_hypothesis:
    # check if Rahul's future age in the hypothesis contradicts Rahul's future age in the premise
    label = "contradiction"
else:
    # if the ratios and Rahul's future age in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)
