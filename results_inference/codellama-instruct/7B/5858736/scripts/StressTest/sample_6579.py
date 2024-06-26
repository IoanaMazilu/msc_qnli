# Define variables for the weights
sean_weight = 200
package1_weight = 150
package2_weight = 280

# Check if Sean's weight is less than 800 pounds
if sean_weight <= 800:
    # Check if the total weight of the packages is greater than Sean's weight
    if package1_weight + package2_weight > sean_weight:
        # Contradiction: the total weight of the packages is greater than Sean's weight
        label = "contradiction"
    else:
        # Entailment: Sean's weight is less than 800 pounds and the total weight of the packages is less than or equal to Sean's weight
        label = "entailment"
else:
    # Neutral: Sean's weight is greater than 800 pounds and the total weight of the packages is less than or equal to Sean's weight
    label = "neutral"

print(label)
