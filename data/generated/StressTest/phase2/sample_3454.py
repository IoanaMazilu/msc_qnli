# Premise: Ratio between Rahul and Deepak is less than 8:3, After 6 Years Rahul age will be 26 years.
# Hypothesis: Ratio between Rahul and Deepak is 4:3, After 6 Years Rahul age will be 26 years.
# Golden Label: neutral

rahul_deepak_ratio_premise = 8/3
rahul_deepak_ratio_hypothesis = 4/3
rahul_future_age_premise = 26
rahul_future_age_hypothesis = 26

# the hypothesis refers to the age ratio between Rahul and Deepak, and Rahul's future age, both mentioned in the premise
if rahul_deepak_ratio_hypothesis >= rahul_deepak_ratio_premise:
    # check if the ratio between Rahul and Deepak in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif rahul_future_age_hypothesis != rahul_future_age_premise:
    # check if Rahul's future age in the hypothesis contradicts Rahul's future age in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

