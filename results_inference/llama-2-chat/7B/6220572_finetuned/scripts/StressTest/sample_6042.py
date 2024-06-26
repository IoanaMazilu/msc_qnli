distance_premise = 40
distance_hypothesis = 10
speed_maxwell_premise = 4
speed_maxwell_hypothesis = 4
speed_brad_premise = 6
speed_brad_hypothesis = 6

# the hypothesis refers to the distance and speeds mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the distance estimate in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif speed_maxwell_hypothesis!= speed_maxwell_premise or speed_brad_hypothesis!= speed_brad_premise:
    # check if the speeds in the hypothesis contradict the speeds reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
