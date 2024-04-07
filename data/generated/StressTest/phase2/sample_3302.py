# Premise: Ratio between Rahul and Deepak is 4:3, After 6 Years Rahul age will be 38 years.
# Hypothesis: Ratio between Rahul and Deepak is more than 4:3, After 6 Years Rahul age will be 38 years.
# Golden Label: contradiction

rahul_deepak_ratio_premise = 4 / 3
rahul_deepak_ratio_hypothesis = 4 / 3
rahul_age_future_premise = 38
rahul_age_future_hypothesis = 38

# the hypothesis talks about the ratio between Rahul and Deepak, and also Rahul's future age, both also referenced in the premise
if rahul_deepak_ratio_hypothesis <= rahul_deepak_ratio_premise:
    # check if the hypothesis ratio contradicts the exact ratio in the premise
    label = "contradiction"
elif rahul_age_future_hypothesis != rahul_age_future_premise:
    # check if the future age of Rahul in the hypothesis contradicts the future age of Rahul in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

