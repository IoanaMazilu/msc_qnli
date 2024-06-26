distance_premise = 50
distance_hypothesis = 10
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis refers to the distance between their homes, Maxwell's walking speed and Brad's running speed mentioned in the premise
if distance_premise <= distance_hypothesis:
    # check if the estimate of 'distance_hypothesis' contradicts the distance between their homes in the premise
    label = "contradiction"
elif maxwell_speed_premise != maxwell_speed_hypothesis:
    # check if the walking speed of Maxwell in the hypothesis contradicts the walking speed of Maxwell in the premise
    label = "contradiction"
elif brad_speed_premise != brad_speed_hypothesis:
    # check if the running speed of Brad in the hypothesis contradicts the running speed of Brad in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
