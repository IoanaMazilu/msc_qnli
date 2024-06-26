# define variables for the numerical entities in the premise
karen_speed_premise = 80
tom_speed_premise = 45
distance_premise = 100

# define variables for the numerical entities in the hypothesis
karen_speed_hypothesis = 60
tom_speed_hypothesis = 45
distance_hypothesis = 100

# calculate the time taken by Karen to drive the distance in the premise
time_premise = distance_premise / karen_speed_premise

# calculate the time taken by Tom to drive the distance in the hypothesis
time_hypothesis = distance_hypothesis / tom_speed_hypothesis

# calculate the time difference between the two
time_difference = time_hypothesis - time_premise

# check if the time difference contradicts the premise
if time_difference < 0:
    label = "contradiction"
else:
    label = "neutral"

print(label)
