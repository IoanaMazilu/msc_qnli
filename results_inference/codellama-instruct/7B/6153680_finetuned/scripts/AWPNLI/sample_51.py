# Define the variables from the premise
total_fruit_sold = 9792.0
frozen_fruit_sold = 3513.0

# Define the hypothesis variable
fresh_fruit_sold = 6280.0

# Calculate the total fruit sold minus the frozen fruit sold
total_fruit_sold_minus_frozen = total_fruit_sold - frozen_fruit_sold

# Check if the hypothesis value contradicts the premise
if fresh_fruit_sold!= total_fruit_sold_minus_frozen:
    label = "contradiction"
else:
    label = "entailment"

print(label)
