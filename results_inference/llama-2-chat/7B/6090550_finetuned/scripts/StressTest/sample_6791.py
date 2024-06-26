distance_premise = 50
distance_hypothesis = 50
maxwell_speed = 4
brad_speed = 6

# the hypothesis refers to the distance between their homes and the speed of Maxwell and Brad
if distance_hypothesis <= distance_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "entailment"
elif maxwell_speed!= 4 or brad_speed!= 6:
    # check if the speed of Maxwell or Brad in the hypothesis contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
