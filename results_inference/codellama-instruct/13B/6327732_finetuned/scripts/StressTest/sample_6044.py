distance_premise = 40
distance_hypothesis = 80
speed_maxwell_premise = 4
speed_maxwell_hypothesis = 4
speed_brad_premise = 6
speed_brad_hypothesis = 6

# the hypothesis refers to the distance between their homes and the walking speed of Maxwell, which are also mentioned in the premise
if distance_hypothesis!= distance_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif speed_maxwell_hypothesis!= speed_maxwell_premise:
    # check if the walking speed of Maxwell in the hypothesis contradicts the walking speed in the premise
    label = "contradiction"
elif speed_brad_hypothesis!= speed_brad_premise:
    # check if the running speed of Brad in the hypothesis contradicts the running speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
