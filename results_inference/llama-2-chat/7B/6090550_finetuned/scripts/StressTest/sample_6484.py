distance_premise = 80
distance_hypothesis = 20
maxwell_speed = 4
brad_speed = 6

# the hypothesis talks about the distance between their homes, Maxwell's walking speed and Brad's running speed, which are also mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the distance in the hypothesis contradicts the premise
    label = "contradiction"
elif maxwell_speed!= 4 or brad_speed!= 6:
    # check if the speeds in the hypothesis contradict the speeds in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
