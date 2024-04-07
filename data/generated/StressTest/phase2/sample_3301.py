# Premise: Ratio between Rahul and Deepak is less than 8:3, After 6 Years Rahul age will be 38 years.
# Hypothesis: Ratio between Rahul and Deepak is 4:3, After 6 Years Rahul age will be 38 years.
# Golden Label: neutral

ratio_premise = 8/3
ratio_hypothesis = 4/3
rahul_age_future_premise = 38
rahul_age_future_hypothesis = 38

# The hypothesis refers to the age of Rahul in the future and the ratio between Rahul and Deepak, both referenced in the premise
if ratio_hypothesis >= ratio_premise:
    # Check if the ratio in the hypothesis contradicts the estimate of less than 'ratio_premise'
    label = "contradiction"
elif rahul_age_future_hypothesis != rahul_age_future_premise:
    # Check if the future age of Rahul in the hypothesis contradicts the future age of Rahul reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

