home_beach_speed_premise = 80
home_beach_speed_hypothesis = 60
return_speed_premise = 70
return_speed_hypothesis = 70

# the hypothesis refers to the speed of the trip from home to the beach and the return trip mentioned in the premise
if home_beach_speed_hypothesis!= home_beach_speed_premise:
    # check if the speed of the trip from home to the beach in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
elif return_speed_hypothesis!= return_speed_premise:
    # check if the speed of the return trip in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
