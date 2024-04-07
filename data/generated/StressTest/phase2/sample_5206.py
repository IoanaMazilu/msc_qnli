# Premise: Ratio between Rahul and Deepak is less than 7:3, After 4 Years Rahul age will be 32 years.
# Hypothesis: Ratio between Rahul and Deepak is 4:3, After 4 Years Rahul age will be 32 years.
# Golden Label: neutral

rahul_deepak_ratio_premise = 7/3
rahul_deepak_ratio_hypothesis = 4/3
rahul_age_future_premise = 32
rahul_age_future_hypothesis = 32

# the hypothesis refers to the ratio between Rahul and Deepak and Rahul's future age, both mentioned in the premise
if rahul_deepak_ratio_hypothesis >= rahul_deepak_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
elif rahul_age_future_hypothesis != rahul_age_future_premise:
    # check if Rahul's future age in the hypothesis contradicts the future age given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

