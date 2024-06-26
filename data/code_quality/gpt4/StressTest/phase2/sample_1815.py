distance_premise = 80
distance_hypothesis = 70
maxwell_speed = 4
brad_speed = 6

# the hypothesis refers to the distance between homes, Maxwell's walking speed and Brad's running speed mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance in the premise
    label = "contradiction"
elif maxwell_speed != maxwell_speed or brad_speed != brad_speed:
    # check if the speeds in the hypothesis contradict the speeds reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
