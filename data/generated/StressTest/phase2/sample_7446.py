# Premise: Ratio between Rahul and Deepak is 4:3, After 6 Years Rahul age will be 26 years.
# Hypothesis: Ratio between Rahul and Deepak is more than 1:3, After 6 Years Rahul age will be 26 years.
# Golden Label: entailment

rahul_deepak_ratio_premise = 4 / 3
rahul_deepak_ratio_hypothesis = 1 / 3
rahul_age_future_premise = 26
rahul_age_future_hypothesis = 26

# The hypothesis refers to the ratio between Rahul's and Deepak's ages, and to Rahul's future age, both mentioned in the premise
if rahul_deepak_ratio_hypothesis >= rahul_deepak_ratio_premise:
    # Check if the 'rahul_deepak_ratio_hypothesis' contradicts the ratio between Rahul's and Deepak's ages in the premise
    label = "contradiction"
elif rahul_age_future_hypothesis != rahul_age_future_premise:
    # Check if Rahul's future age in the hypothesis contradicts Rahul's future age in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

