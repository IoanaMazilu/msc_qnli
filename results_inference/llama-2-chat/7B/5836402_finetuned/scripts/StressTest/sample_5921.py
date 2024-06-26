home_to_beach_speed_premise = 80
home_to_beach_speed_hypothesis = 80
return_speed_premise = 70
return_speed_hypothesis = 70

# the hypothesis refers to the average speed of the journey from home to the beach and return, mentioned in the premise
if home_to_beach_speed_premise <= home_to_beach_speed_hypothesis:
    # check if the estimate of 'home_to_beach_speed_hypothesis' contradicts the speed of the journey from home to the beach in the premise
    label = "contradiction"
elif return_speed_hypothesis!= return_speed_premise:
    # check if the return speed in the hypothesis contradicts the return speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
