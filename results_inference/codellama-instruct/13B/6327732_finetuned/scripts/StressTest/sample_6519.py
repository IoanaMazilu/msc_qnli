# define variables for the numerical entities in the premise
distance_1 = 8
speed_1 = 40
time_1 = 14
distance_2 = 20
speed_2 = 60

# define variables for the numerical entities in the hypothesis
distance_total = 5
speed_total = 40
time_total = 14
distance_2_total = 20
speed_2_total = 60

# calculate the total distance traveled by Jerry
distance_total = distance_1 + distance_2

# calculate the total time traveled by Jerry
time_total = time_1 + time_2

# calculate the average speed of Jerry's trip
speed_total = distance_total / time_total

# check if the average speed of Jerry's trip contradicts the hypothesis
if speed_total!= speed_total:
    label = "contradiction"

# check if the total distance traveled by Jerry contradicts the hypothesis
elif distance_total!= distance_total:
    label = "contradiction"

# check if the total time traveled by Jerry contradicts the hypothesis
elif time_total!= time_total:
    label = "contradiction"

# check if the average speed of Jerry's second leg contradicts the hypothesis
elif speed_2_total!= speed_2_total:
    label = "contradiction"

# check if the distance traveled by Jerry in his second leg contradicts the hypothesis
elif distance_2_total!= distance_2_total:
    label = "contradiction"

# if none of the above conditions are met, we can infer entailment
else:
    label = "entailment"

print(label)
