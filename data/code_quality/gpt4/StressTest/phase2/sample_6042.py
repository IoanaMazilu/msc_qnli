distance_premise = 40
distance_hypothesis = 10
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis refers to the same properties as the premise: distance, Maxwell's speed and Brad's speed
if distance_premise <= distance_hypothesis:
    # check if the estimate of 'distance_hypothesis' contradicts the distance reported in the premise
    label = "contradiction"
elif maxwell_speed_premise != maxwell_speed_hypothesis:
    # check if Maxwell's speed in the hypothesis contradicts Maxwell's speed reported in the premise
    label = "contradiction"
elif brad_speed_premise != brad_speed_hypothesis:
    # check if Brad's speed in the hypothesis contradicts Brad's speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
