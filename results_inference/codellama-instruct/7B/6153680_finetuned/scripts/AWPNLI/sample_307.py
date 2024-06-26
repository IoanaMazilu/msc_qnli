# Define variables for the premise
candy_received = 108.0
candy_eaten = 36.0
candy_left = candy_received - candy_eaten

# Define variables for the hypothesis
piles_possible = 4.0

# Calculate the number of piles Sarah could make based on the premise
piles_calculated = candy_left / 9.0

# Check if the number of piles in the hypothesis contradicts the number of piles calculated from the premise
if piles_possible!= piles_calculated:
    label = "contradiction"
else:
    label = "entailment"

print(label)
