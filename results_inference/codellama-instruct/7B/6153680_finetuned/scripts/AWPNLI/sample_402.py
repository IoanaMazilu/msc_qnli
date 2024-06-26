# Define variables for the premise
picked_pears = 42.0
sold_pears = 17.0

# Define variables for the hypothesis
left_pears = 25.0

# Calculate the total number of pears
total_pears = picked_pears - sold_pears

# Check if the hypothesis value contradicts the total number of pears
if left_pears!= total_pears:
    # If the hypothesis value contradicts the total number of pears, then the relation is contradiction
    relation = "contradiction"
else:
    # If the hypothesis value does not contradict the total number of pears, then the relation is entailment
    relation = "entailment"

print(relation)
