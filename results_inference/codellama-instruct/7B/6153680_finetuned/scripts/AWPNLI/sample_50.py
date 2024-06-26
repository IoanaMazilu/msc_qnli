# Define the variables for the premise
total_fruit_sold = 9792.0
frozen_fruit_sold = 3513.0

# Define the variables for the hypothesis
fresh_fruit_sold = 6279.0

# Calculate the total fruit sold in the premise
total_fruit_sold_premise = total_fruit_sold - frozen_fruit_sold

# Check if the total fruit sold in the hypothesis contradicts the total fruit sold in the premise
if fresh_fruit_sold!= total_fruit_sold_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
