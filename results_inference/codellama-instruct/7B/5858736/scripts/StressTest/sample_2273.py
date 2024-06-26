# Define variables for the distances between A and B, and B and C
distance_AB = 2
distance_BC = 3

# Define variables for the average speed of Murali from A to C
average_speed_AC = 10

# Calculate the ratio of distances between A to B and B to C
ratio_AB_to_BC = distance_AB / distance_BC

# Calculate the average speed of Murali from A to C given the ratio of distances
average_speed_AC_given_ratio = average_speed_AC * ratio_AB_to_BC

# Compare the calculated average speed with the given hypothesis
if average_speed_AC_given_ratio == 15:
    label = "entailment"
elif average_speed_AC_given_ratio!= 15:
    label = "contradiction"
else:
    label = "neutral"

print(label)
