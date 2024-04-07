# Premise: If the distance between their homes is 54 kilometers, Maxwell's walking speed is 4 km/h, and Brad's running speed is 6 km/h.
# Hypothesis: If the distance between their homes is less than 84 kilometers, Maxwell's walking speed is 4 km/h, and Brad's running speed is 6 km/h.
# Golden Label: entailment

distance_homes_premise = 54
distance_homes_hypothesis = 84
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis refers to the distance between homes, Maxwell's walking speed and Brad's running speed mentioned in the premise
if maxwell_speed_premise != maxwell_speed_hypothesis:
    # check if Maxwell's walking speed in hypothesis contradicts the one reported in the premise
    label = "contradiction"
elif brad_speed_premise != brad_speed_hypothesis:
    # check if Brad's running speed in hypothesis contradicts the one reported in the premise
    label = "contradiction"
elif distance_homes_hypothesis < distance_homes_premise:
    # check if the distance between homes in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

