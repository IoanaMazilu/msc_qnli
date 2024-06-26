from math import sqrt

# define variables for the numerical entities in the premise
west_town_speed = 4
east_town_speed = 1

# define variables for the numerical entities in the hypothesis
west_town_speed_hypothesis = 7
east_town_speed_hypothesis = 1

# calculate the distance between the two towns
distance = sqrt((west_town_speed - east_town_speed) ** 2 + (west_town_speed_hypothesis - east_town_speed_hypothesis) ** 2)

# check if the distance is less than or equal to the sum of the speeds
if distance <= (west_town_speed + east_town_speed):
    # check if the hypothesis values contradict the premise values
    if west_town_speed_hypothesis <= west_town_speed and east_town_speed_hypothesis <= east_town_speed:
        # if the hypothesis values do not contradict the premise values, we can infer entailment
        label = "entailment"
    else:
        # if the hypothesis values contradict the premise values, we can infer contradiction
        label = "contradiction"
else:
    # if the distance is greater than the sum of the speeds, we can infer neutral
    label = "neutral"

print(label)
