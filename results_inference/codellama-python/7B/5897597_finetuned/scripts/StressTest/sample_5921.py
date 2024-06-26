speed_to_beach_premise = 80
speed_to_beach_hypothesis = 80
speed_home_premise = 70
speed_home_hypothesis = 70

# the hypothesis refers to the speeds of Carl's driving to the beach and back home, mentioned in the premise
if speed_to_beach_hypothesis <= speed_to_beach_premise:
    # check if the hypothesis value contradicts the premise value of'speed_to_beach_premise'
    label = "contradiction"
elif speed_home_hypothesis!= speed_home_premise:
    # check if the speed home in the hypothesis contradicts the speed home reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
