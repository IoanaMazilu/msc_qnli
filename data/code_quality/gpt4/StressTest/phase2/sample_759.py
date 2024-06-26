distance_homes_premise = 30
distance_homes_hypothesis = 20
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis refers to the distance between homes, Maxwell's speed and Brad's speed mentioned in the premise
if distance_homes_premise <= distance_homes_hypothesis:
    # check if the number of 'distance_homes_hypothesis' contradicts the distance between homes in the premise
    label = "contradiction"
elif maxwell_speed_hypothesis != maxwell_speed_premise:
    # check if Maxwell's speed in the hypothesis contradicts Maxwell's speed in the premise
    label = "contradiction"
elif brad_speed_hypothesis != brad_speed_premise:
    # check if Brad's speed in the hypothesis contradicts Brad's speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
