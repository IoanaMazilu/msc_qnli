distance_traveled_premise = 0.80
distance_traveled_hypothesis = 0.80
speed_premise = 80
speed_hypothesis = 80

# the hypothesis refers to the distance and speed of John's travel mentioned in the premise
if distance_traveled_hypothesis >= distance_traveled_premise:
    # check if the estimate of 'distance_traveled_hypothesis' contradicts the distance traveled in the premise
    label = "contradiction"
elif speed_hypothesis != speed_premise:
    # check if the speed of travel in the hypothesis contradicts the speed of travel reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
