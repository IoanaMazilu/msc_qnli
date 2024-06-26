distance_premise = 50
distance_hypothesis = 60
relative_speed_premise = 17
relative_speed_hypothesis = 17

# the hypothesis refers to the distance and relative speed mentioned in the premise
if distance_hypothesis < distance_premise or relative_speed_hypothesis != relative_speed_premise:
    # check if the distance estimate in the hypothesis contradicts the distance in the premise
    # or if the relative speed in the hypothesis contradicts the relative speed in the premise
    label = "contradiction"
elif distance_hypothesis == distance_premise and relative_speed_hypothesis == relative_speed_premise:
    # if the hypothesis values and estimates are exactly the same as in the premise, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, but are not exactly the same, it is neutral
    label = "neutral"

print(label)
