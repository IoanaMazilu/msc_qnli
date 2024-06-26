# define variables for the distances and ratio
distance_AB = 4
distance_BC = 2
ratio = 3/2

# calculate the average speed
average_speed = distance_AB / ratio

# check if the average speed contradicts the hypothesis
if average_speed!= distance_BC:
    label = "contradiction"
else:
    label = "entailment"

print(label)
