# Premise: If the distance between their homes is less than 610 kilometers, Maxwell's walking speed is 4 km/h, and Brad's running speed is 7 km/h, what is the distance traveled by Brad?
# Hypothesis: If the distance between their homes is 110 kilometers, Maxwell's walking speed is 4 km/h, and Brad's running speed is 7 km/h, what is the distance traveled by Brad?
# Golden Label: neutral

distance_home_premise = 610
distance_home_hypothesis = 110
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 7
brad_speed_hypothesis = 7

# the hypothesis refers to the distance between homes, and the speed of Maxwell and Brad mentioned in the premise
if distance_home_hypothesis >= distance_home_premise:
    # check if the distance between homes in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif maxwell_speed_hypothesis != maxwell_speed_premise:
    # check if Maxwell's speed in the hypothesis contradicts Maxwell's speed in the premise
    label = "contradiction"
elif brad_speed_hypothesis != brad_speed_premise:
    # check if Brad's speed in the hypothesis contradicts Brad's speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we infer entailment
    label = "entailment"

print(label)

