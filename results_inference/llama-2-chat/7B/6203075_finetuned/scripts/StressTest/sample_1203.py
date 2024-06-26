speed_home_to_beach_premise = 80
speed_home_to_beach_hypothesis = 40
speed_beach_to_home_premise = 70
speed_beach_to_home_hypothesis = 70

# the hypothesis refers to the average speed of Carl's journey from home to the beach and back
if speed_home_to_beach_premise <= speed_home_to_beach_hypothesis:
    # check if the hypothesis speed contradicts the premise speed
    label = "contradiction"
elif speed_beach_to_home_premise!= speed_beach_to_home_hypothesis:
    # check if the speed of the return journey from the beach to home in the hypothesis contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
