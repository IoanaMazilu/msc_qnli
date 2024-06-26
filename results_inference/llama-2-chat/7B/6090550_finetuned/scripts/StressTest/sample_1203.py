speed_home_to_beach_premise = 80
speed_home_to_beach_hypothesis = 40
speed_beach_to_home_premise = 70
speed_beach_to_home_hypothesis = 70

# the hypothesis refers to the average speeds from home to the beach and from the beach to home
if speed_home_to_beach_premise <= speed_home_to_beach_hypothesis:
    # check if the estimate of'speed_home_to_beach_hypothesis' contradicts the speed in the premise
    label = "contradiction"
elif speed_beach_to_home_hypothesis!= speed_beach_to_home_premise:
    # check if the speed from the beach to home in the hypothesis contradicts the speed from the beach to home in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
