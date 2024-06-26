distance_premise = 520
distance_hypothesis = 120
average_speed_premise = 50
average_speed_hypothesis = 50

# the hypothesis refers to the distance and speed of a train journey mentioned in the premise
if distance_hypothesis > distance_premise:
    # check if the distance in the hypothesis contradicts the estimate of less than 'distance_premise' miles
    label = "contradiction"
elif average_speed_hypothesis != average_speed_premise:
    # check if the average speed in the hypothesis contradicts the average speed reported in the premise
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # the hypothesis distance is less than the premise distance, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
