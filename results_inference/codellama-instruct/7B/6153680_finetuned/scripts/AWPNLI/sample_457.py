# Define the variables from the premise
original_algal_plants = 3263.0
current_algal_plants = 809.0
total_algal_plants = 4074.0

# Calculate the difference in algal plants between the premise and the hypothesis
difference_algal_plants = total_algal_plants - (original_algal_plants + current_algal_plants)

# The hypothesis states that there are 4074.0 algal plants in Milford Lake now
if difference_algal_plants!= 0:
    # Check if the difference in algal plants between the premise and the hypothesis contradicts the premise
    label = "contradiction"
else:
    # If the difference in algal plants is 0, it means that the premise and the hypothesis are consistent
    label = "entailment"

print(label)
