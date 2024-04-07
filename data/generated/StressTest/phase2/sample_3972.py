# Premise: Ratio between Rahul and Deepak is 4:3, After 2 Years Rahul age will be 26 years.
# Hypothesis: Ratio between Rahul and Deepak is less than 7:3, After 2 Years Rahul age will be 26 years.
# Golden Label: entailment

rahul_to_deepak_ratio_premise = 4/3
rahul_to_deepak_ratio_hypothesis = 7/3
rahul_future_age_premise = 26
rahul_future_age_hypothesis = 26

# the hypothesis refers to the ratio between Rahul and Deepak's ages and Rahul's future age, also mentioned in the premise
if rahul_to_deepak_ratio_hypothesis >= rahul_to_deepak_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif rahul_future_age_hypothesis != rahul_future_age_premise:
    # check if Rahul's future age in the hypothesis contradicts Rahul's future age in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

