distance_homes_premise = 40
distance_homes_hypothesis = 10
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis refers to the distance between homes, Maxwell's walking speed and Brad's running speed mentioned in the premise
if distance_homes_premise <= distance_homes_hypothesis:
    # check if the estimate of 'distance_homes_hypothesis' contradicts the distance between homes in the premise
    label = "contradiction"
elif maxwell_speed_premise!= maxwell_speed_hypothesis:
    # check if Maxwell's walking speed in the hypothesis contradicts Maxwell's walking speed reported in the premise
    label = "contradiction"
elif brad_speed_premise!= brad_speed_hypothesis:
    # check if Brad's running speed in the hypothesis contradicts Brad's running speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
