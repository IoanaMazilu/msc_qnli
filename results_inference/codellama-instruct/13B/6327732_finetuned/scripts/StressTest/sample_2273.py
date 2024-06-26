# define variables for the distances and ratio
distance_AB = 2
distance_BC = 3
ratio = 8

# calculate the average speed based on the ratio and distances
average_speed = (distance_AB + distance_BC) / ratio

# check if the average speed contradicts the hypothesis
if average_speed!= 8:
    label = "contradiction"
else:
    label = "entailment"

print(label)
