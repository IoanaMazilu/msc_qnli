# Premise: Ratio between Rahul and Deepak is less than 8:2, After 6 Years Rahul age will be 26 years.
# Hypothesis: Ratio between Rahul and Deepak is 5:2, After 6 Years Rahul age will be 26 years.
# Golden Label: neutral

ratio_rahul_deepak_premise = 8/2
ratio_rahul_deepak_hypothesis = 5/2
rahul_future_age_premise = 26
rahul_future_age_hypothesis = 26

# the hypothesis refers to the ratio between Rahul and Deepak as well as Rahul's future age, both mentioned in the premise
if ratio_rahul_deepak_hypothesis >= ratio_rahul_deepak_premise:
    # check if the ratio in the hypothesis contradicts the ratio estimate in the premise
    label = "contradiction"
elif rahul_future_age_hypothesis != rahul_future_age_premise:
    # check if Rahul's future age in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

