distance_premise = 40
distance_hypothesis = 10
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis refers to the distance between their homes and the walking and running speeds of Maxwell and Brad
if distance_hypothesis >= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance between their homes in the premise
    label = "contradiction"
elif maxwell_speed_hypothesis!= maxwell_speed_premise:
    # check if the walking speed of Maxwell in the hypothesis contradicts the walking speed reported in the premise
    label = "contradiction"
elif brad_speed_hypothesis!= brad_speed_premise:
    # check if the running speed of Brad in the hypothesis contradicts the running speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
