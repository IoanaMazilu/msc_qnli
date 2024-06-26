southward_distance_premise = 20
southward_distance_hypothesis = 80
right_distance_premise = 10
right_distance_hypothesis = 10
second_right_distance_premise = 20
second_right_distance_hypothesis = 20
left_distance_premise = 20
left_distance_hypothesis = 20

# the hypothesis refers to the same journey as the premise, with distances cycled in each direction
if southward_distance_hypothesis != southward_distance_premise:
    # check if the southward distance in the hypothesis contradicts the southward distance reported in the premise
    label = "contradiction"
elif right_distance_hypothesis != right_distance_premise:
    # check if the rightward distance in the hypothesis contradicts the rightward distance reported in the premise
    label = "contradiction"
elif second_right_distance_hypothesis != second_right_distance_premise:
    # check if the second rightward distance in the hypothesis contradicts the second rightward distance reported in the premise
    label = "contradiction"
elif left_distance_hypothesis != left_distance_premise:
    # check if the leftward distance in the hypothesis contradicts the leftward distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
