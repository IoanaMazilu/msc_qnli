distance_run_premise = 2
distance_run_hypothesis = 3

# the hypothesis refers to the distance that the sisters ran, which is also mentioned in the premise
if distance_run_premise!= distance_run_hypothesis:
    # check if the distance run in the hypothesis contradicts the distance run reported in the premise
    label = "contradiction"
else:
    # if the distance run in the hypothesis does not contradict the distance run in the premise, we can infer entailment
    label = "entailment"

print(label)
