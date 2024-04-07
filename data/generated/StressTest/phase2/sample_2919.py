# Premise: Ratio between Rahul and Deepak is 4:2, After 6 Years Rahul age will be 22 years.
# Hypothesis: Ratio between Rahul and Deepak is less than 8:2, After 6 Years Rahul age will be 22 years.
# Golden Label: entailment

rahul_deepak_ratio_premise = 4/2
rahul_deepak_ratio_hypothesis = 8/2
rahul_age_future_premise = 22
rahul_age_future_hypothesis = 22

# the hypothesis refers to the ratio between Rahul and Deepak's ages and Rahul's future age mentioned in the premise
if rahul_deepak_ratio_hypothesis <= rahul_deepak_ratio_premise:
    # check if the 'rahul_deepak_ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
elif rahul_age_future_hypothesis != rahul_age_future_premise:
    # check if Rahul's future age in the hypothesis contradicts Rahul's future age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

