# Define the variables for the premise and hypothesis
rahul_deepak_ratio_premise = 2 / 3
rahul_deepak_ratio_hypothesis = 4 / 3
rahul_future_age_premise = 26
rahul_future_age_hypothesis = 26

# Check if the age of Rahul in the future is the same in both the premise and hypothesis
if rahul_future_age_premise != rahul_future_age_hypothesis:
    # If the future age of Rahul in the hypothesis contradicts the future age in the premise, label as contradiction
    label = "contradiction"
elif rahul_deepak_ratio_hypothesis <= rahul_deepak_ratio_premise:
    # If the ratio of Rahul and Deepak in the hypothesis contradicts the ratio in the premise, label as contradiction
    label = "contradiction"
else:
    # If the ratio in the hypothesis is more than the ratio in the premise but does not contradict it, label as neutral
    label = "neutral"

print(label)
