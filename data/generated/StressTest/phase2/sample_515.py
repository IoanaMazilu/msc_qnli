# Premise: Ratio between Rahul and Deepak is 4:3, After 6 Years Rahul age will be 22 years.
# Hypothesis: Ratio between Rahul and Deepak is 2:3, After 6 Years Rahul age will be 22 years.
# Golden Label: contradiction

rahul_deepak_ratio_premise = 4/3
rahul_deepak_ratio_hypothesis = 2/3
rahul_age_future_premise = 22
rahul_age_future_hypothesis = 22

# The hypothesis refers to the ratio between Rahul and Deepak and Rahul's future age mentioned in the premise
if rahul_deepak_ratio_premise != rahul_deepak_ratio_hypothesis:
    # check if the ratio between Rahul and Deepak in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif rahul_age_future_premise != rahul_age_future_hypothesis:
    # check if Rahul's future age in the hypothesis contradicts Rahul's future age in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

