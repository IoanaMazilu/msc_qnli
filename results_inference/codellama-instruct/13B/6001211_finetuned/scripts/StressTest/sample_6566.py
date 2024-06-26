speed_to_beach_premise = 80
speed_to_beach_hypothesis = 60
speed_home_premise = 70
speed_home_hypothesis = 70

# the hypothesis refers to the average speeds of driving to the beach and back home, mentioned in the premise
if speed_to_beach_premise!= speed_to_beach_hypothesis:
    # check if the speed to the beach in the hypothesis contradicts the speed to the beach reported in the premise
    label = "contradiction"
elif speed_home_premise!= speed_home_hypothesis:
    # check if the speed home in the hypothesis contradicts the speed home reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
