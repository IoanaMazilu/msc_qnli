speed_premise = 9
speed_hypothesis = 6
distance_premise = 300
distance_hypothesis = 300

# the hypothesis talks about the speed of running and the distance to the park, referenced also in the premise
if speed_hypothesis > speed_premise:
    # check if the speed in the hypothesis contradicts the speed in the premise
    label = "contradiction"
elif distance_hypothesis != distance_premise:
    # check if the distance to the park in the hypothesis contradicts the distance in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
