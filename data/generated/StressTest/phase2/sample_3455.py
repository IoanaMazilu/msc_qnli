# Premise: Ratio between Rahul and Deepak is 4:3, After 6 Years Rahul age will be 26 years.
# Hypothesis: Ratio between Rahul and Deepak is 3:3, After 6 Years Rahul age will be 26 years.
# Golden Label: contradiction

rahul_deepak_ratio_premise = 4/3
rahul_deepak_ratio_hypothesis = 3/3
rahul_age_future_premise = 26
rahul_age_future_hypothesis = 26

# the hypothesis talks about the ratio between Rahul and Deepak's ages and Rahul's future age, all referenced in the premise
if rahul_deepak_ratio_hypothesis != rahul_deepak_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif rahul_age_future_hypothesis != rahul_age_future_premise:
    # check if the future age of Rahul in the hypothesis contradicts the future age of Rahul in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

