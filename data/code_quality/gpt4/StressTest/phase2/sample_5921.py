speed_to_beach_premise = 80
speed_to_beach_hypothesis = 80
speed_home_premise = 70
speed_home_hypothesis = 70

# the hypothesis refers to the same speeds of the premise
if speed_to_beach_hypothesis <= speed_to_beach_premise:
    # check if the hypothesis value contradicts the premise speed to the beach
    label = "contradiction"
elif speed_home_hypothesis != speed_home_premise:
    # check if the hypothesis value contradicts the premise speed to home
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
