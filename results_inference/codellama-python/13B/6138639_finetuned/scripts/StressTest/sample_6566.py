speed_to_beach_premise = 80
speed_to_beach_hypothesis = 60
speed_to_home_premise = 70
speed_to_home_hypothesis = 70

# the hypothesis refers to the speed of Carl's trip to the beach and back home, mentioned in the premise
if speed_to_beach_hypothesis > speed_to_beach_premise:
    # check if the speed to the beach in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
elif speed_to_home_hypothesis!= speed_to_home_premise:
    # check if the speed to return home in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
