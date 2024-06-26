average_speed_to_beach_premise = 80
average_speed_to_beach_hypothesis = 20
average_speed_from_beach_premise = 70
average_speed_from_beach_hypothesis = 70

# the hypothesis refers to the same journey Carl took, as mentioned in the premise
if average_speed_to_beach_premise != average_speed_to_beach_hypothesis:
    # check if the average speed to the beach in the hypothesis contradicts the average speed to the beach mentioned in the premise
    label = "contradiction"
elif average_speed_from_beach_premise != average_speed_from_beach_hypothesis:
    # check if the average speed from the beach in the hypothesis contradicts the average speed from the beach mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
