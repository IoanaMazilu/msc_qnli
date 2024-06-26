# Define variables for the distances between A and B, and B and C
distance_AB = 10
distance_BC = 15

# Define the ratio of distances between A and B to B and C
ratio = 2/3

# Calculate the average speed of Murali from A to C
average_speed = distance_AB / ratio

# Check if the hypothesis value contradicts the premise
if average_speed > distance_BC:
    label = "contradiction"
else:
    # The hypothesis value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
