speed_to_beach_premise = 80
speed_to_beach_hypothesis = 80
speed_to_home_premise = 70
speed_to_home_hypothesis = 70

# the hypothesis refers to the average speed to the beach and to home mentioned in the premise
if speed_to_beach_hypothesis <= speed_to_beach_premise:
    # check if the estimate of'speed_to_beach_hypothesis' contradicts the speed to the beach in the premise
    label = "contradiction"
elif speed_to_home_hypothesis!= speed_to_home_premise:
    # check if the speed to home in the hypothesis contradicts the speed to home reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
