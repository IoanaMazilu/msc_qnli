bicycle_distance_premise = 40.0
bicycle_speed_premise = 8.0
bicycle_time_hypothesis = 3.0

# the hypothesis refers to the time spent bicycling, which is also mentioned in the premise
# compute the total distance bicycled in the premise
total_distance_premise = bicycle_distance_premise / bicycle_speed_premise
if bicycle_time_hypothesis >= total_distance_premise:
    # check if the time from the hypothesis is greater than or equal to the total distance bicycled in the premise
    label = "entailment"
else:
    # if the time from the hypothesis is less than the total distance bicycled in the premise, we can infer contradiction
    label = "contradiction"

print(label)
