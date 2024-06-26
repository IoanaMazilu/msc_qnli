# Define variables for the distances between A and B, and B and C
distance_AB = 4
distance_BC = 2

# Calculate the average speed of Murali from A to C
average_speed = distance_AB / 2

# Check if the ratio of distances between A to B and B to C is more than 1:2
if distance_AB / distance_BC > 1:
    # The hypothesis is entailed from the premise
    label = "entailment"
else:
    # The hypothesis is not entailed from the premise
    label = "contradiction"

print(label)
