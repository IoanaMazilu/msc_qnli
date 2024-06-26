distance_premise1 = 340
distance_premise2 = 120
speed_premise1 = 60
speed_premise2 = 40
distance_hypothesis1 = 240
distance_hypothesis2 = 120
speed_hypothesis1 = 60
speed_hypothesis2 = 40

# the hypothesis refers to the distance and speed of Joe's drives mentioned in the premise
if distance_hypothesis1!= distance_premise1 or distance_hypothesis2!= distance_premise2 or speed_hypothesis1!= speed_premise1 or speed_hypothesis2!= speed_premise2:
    # check if the distance or speed in the hypothesis contradicts the ones in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
