# Premise: Ratio between Rahul and Deepak is less than 7:3, After 6 Years Rahul age will be 26 years.
# Hypothesis: Ratio between Rahul and Deepak is 4:3, After 6 Years Rahul age will be 26 years.
# Golden Label: neutral

rahul_deepak_ratio_premise = 7/3
rahul_deepak_ratio_hypothesis = 4/3
rahul_age_future_premise = 26
rahul_age_future_hypothesis = 26

# the hypothesis refers to the same ratio and future age for Rahul as mentioned in the premise
if rahul_deepak_ratio_premise <= rahul_deepak_ratio_hypothesis:
    # check if the ratio in the hypothesis contradicts the ratio described in the premise
    label = "contradiction"
elif rahul_age_future_hypothesis != rahul_age_future_premise:
    # check if the future age of Rahul in the hypothesis contradicts the future age of Rahul reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

