# Define variables for the numerical entities in the premise
fresh_fruit_premise = 9792.0
frozen_fruit_premise = 3513.0
total_fruit_premise = fresh_fruit_premise + frozen_fruit_premise

# Define variables for the numerical entities in the hypothesis
fresh_fruit_hypothesis = 6279.0

# Check if the total number of fresh fruit sold in the hypothesis is greater than or equal to the total number of fresh fruit sold in the premise
if fresh_fruit_hypothesis >= fresh_fruit_premise:
    # Check if the total number of frozen fruit sold in the hypothesis is greater than or equal to the total number of frozen fruit sold in the premise
    if frozen_fruit_hypothesis >= frozen_fruit_premise:
        # If both conditions are true, we can infer entailment
        label = "entailment"
    else:
        # If the total number of frozen fruit sold in the hypothesis is less than the total number of frozen fruit sold in the premise, we can infer contradiction
        label = "contradiction"
else:
    # If the total number of fresh fruit sold in the hypothesis is less than the total number of fresh fruit sold in the premise, we can infer contradiction
    label = "contradiction"

print(label)
