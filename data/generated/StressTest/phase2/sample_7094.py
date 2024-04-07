# Premise: Ratio between Rahul and Deepak is 5:2, After 6 Years Rahul age will be 26 years.
# Hypothesis: Ratio between Rahul and Deepak is less than 5:2, After 6 Years Rahul age will be 26 years.
# Golden Label: contradiction

rahul_deepak_ratio_premise = 5 / 2
rahul_deepak_ratio_hypothesis = 5 / 2

rahul_age_future_premise = 26
rahul_age_future_hypothesis = 26

# The hypothesis refers to the ratio between Rahul and Deepak's ages and Rahul's future age, both mentioned in the premise
if rahul_deepak_ratio_hypothesis >= rahul_deepak_ratio_premise:
    # Check if the estimate of 'rahul_deepak_ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
elif rahul_age_future_hypothesis != rahul_age_future_premise:
    # Check if the future age of Rahul in the hypothesis contradicts the future age of Rahul stated in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

