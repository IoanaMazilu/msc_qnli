# define variables for the numerical entities in the premise
karen_speed_premise = 60
tom_speed_premise = 45
distance_premise = 100

# define variables for the numerical entities in the hypothesis
karen_speed_hypothesis = 70
tom_speed_hypothesis = 45
distance_hypothesis = 100

# calculate the time taken by Karen to drive the distance in the premise
time_premise = distance_premise / karen_speed_premise

# calculate the time taken by Tom to drive the distance in the hypothesis
time_hypothesis = distance_hypothesis / tom_speed_hypothesis

# calculate the difference in time between the two scenarios
time_diff = time_hypothesis - time_premise

# check if the difference in time contradicts the premise
if time_diff < 0:
    # if the difference in time is negative, it contradicts the premise
    label = "contradiction"
else:
    # if the difference in time is positive or zero, it does not contradict the premise
    label = "neutral"

print(label)
