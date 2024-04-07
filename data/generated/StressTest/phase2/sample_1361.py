# Premise: John traveled 80% of the way from Yellow-town to Green-fields by train at an average speed of 80 miles per hour.
# Hypothesis: John traveled 20% of the way from Yellow-town to Green-fields by train at an average speed of 80 miles per hour.
# Golden Label: contradiction

travel_distance_premise = 80
travel_distance_hypothesis = 20
average_speed_premise = 80
average_speed_hypothesis = 80

# the hypothesis refers to the percentage of the distance and the average speed of John's travel mentioned in the premise
if travel_distance_premise != travel_distance_hypothesis:
    # check if the 'travel_distance_hypothesis' contradicts the percentage of distance traveled in the premise
    label = "contradiction"
elif average_speed_hypothesis != average_speed_premise:
    # check if the 'average_speed_hypothesis' contradicts the average speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

