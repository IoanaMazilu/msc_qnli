distance_homes_premise = 54
distance_homes_hypothesis = 44
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis refers to the distances and the speeds of Maxwell and Brad mentioned in the premise
if distance_homes_hypothesis != distance_homes_premise:
    # check if the distance in the hypothesis contradicts the distance stated in the premise
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
