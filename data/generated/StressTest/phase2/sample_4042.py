# Premise: If the distance between their homes is less than 84 kilometers, Maxwell's walking speed is 4 km/h, and Brad's running speed is 6 km/h.
# Hypothesis: If the distance between their homes is 54 kilometers, Maxwell's walking speed is 4 km/h, and Brad's running speed is 6 km/h.
# Golden Label: neutral

distance_premise = 84
distance_hypothesis = 54
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis refers to the distance between homes, Maxwell's walking speed and Brad's running speed mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the distance in the hypothesis contradicts the premise
    label = "contradiction"
elif maxwell_speed_hypothesis != maxwell_speed_premise:
    # check if Maxwell's speed in the hypothesis contradicts the premise
    label = "contradiction"
elif brad_speed_hypothesis != brad_speed_premise:
    # check if Brad's speed in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

