distance_work_premise = 35
distance_work_hypothesis = 45

# the hypothesis refers to the distance from Steve's house to work, same as in the premise
if distance_work_hypothesis != distance_work_premise:
    # check if the distance in the hypothesis contradicts the distance stated in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis matches the one in the premise, we can infer entailment
    label = "entailment"

print(label)
