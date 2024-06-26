speed_home_to_beach_premise = 80
speed_home_to_beach_hypothesis = 60
speed_beach_to_home_premise = 70
speed_beach_to_home_hypothesis = 70

# the hypothesis refers to the average speed of the journey from home to the beach and back, which are also mentioned in the premise
if speed_home_to_beach_hypothesis!= speed_home_to_beach_premise:
    # check if the speed of the journey from home to the beach in the hypothesis contradicts the speed in the premise
    label = "contradiction"
elif speed_beach_to_home_hypothesis!= speed_beach_to_home_premise:
    # check if the speed of the journey from the beach to home in the hypothesis contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
