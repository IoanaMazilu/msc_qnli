distance_run_premise = 2
distance_run_hypothesis = 3

# the hypothesis refers to the distance run by the sisters mentioned in the premise
if distance_run_premise!= distance_run_hypothesis:
    # check if the distance run in the hypothesis contradicts the distance run reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
