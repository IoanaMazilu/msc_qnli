first_distance_premise = 240
first_distance_hypothesis = 140
second_distance_premise = 120
second_distance_hypothesis = 120

# the hypothesis refers to the distances driven at the same speed, mentioned in the premise
if first_distance_hypothesis!= first_distance_premise:
    # check if the first distance in the hypothesis contradicts the first distance reported in the premise
    label = "contradiction"
elif second_distance_hypothesis!= second_distance_premise:
    # check if the second distance in the hypothesis contradicts the second distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
