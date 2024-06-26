miles_traveled_premise = 8
speed_premise = 40
time_premise = 11
miles_traveled_hypothesis = 6
speed_hypothesis = 40
time_hypothesis = 11

# the hypothesis refers to the same journey as the premise
# compute the total distance traveled in the hypothesis
total_distance_hypothesis = miles_traveled_hypothesis + miles_traveled_hypothesis

# compute the average speed in the hypothesis
average_speed_hypothesis = total_distance_hypothesis / (time_hypothesis + time_hypothesis)

# the premise provides the total distance traveled and the average speed
if miles_traveled_hypothesis!= miles_traveled_premise or speed_hypothesis!= speed_premise or time_hypothesis!= time_premise:
    label = "contradiction"
elif average_speed_hypothesis!= average_speed_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
