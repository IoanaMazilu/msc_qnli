distance_premise_1 = 8
distance_premise_2 = 20
distance_hypothesis_1 = 5
distance_hypothesis_2 = 20
speed_premise_1 = 40
speed_premise_2 = 60
speed_hypothesis_1 = 40
speed_hypothesis_2 = 60

# the hypothesis refers to the distance and speed of the journey, which are also mentioned in the premise
if distance_premise_1!= distance_hypothesis_1:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
elif distance_premise_2!= distance_hypothesis_2:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
elif speed_premise_1!= speed_hypothesis_1:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
elif speed_premise_2!= speed_hypothesis_2:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
