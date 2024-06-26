avg_speed_premise = 80
avg_speed_hypothesis = 30
second_trip_speed_premise = 60
second_trip_speed_hypothesis = 60

# the hypothesis refers to the average speed of the first and second part of the trip mentioned in the premise
if avg_speed_hypothesis >= avg_speed_premise:
    # check if the 'avg_speed_hypothesis' contradicts the average speed in the premise
    label = "contradiction"
elif second_trip_speed_hypothesis != second_trip_speed_premise:
    # check if the second trip speed in the hypothesis contradicts the second trip speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
