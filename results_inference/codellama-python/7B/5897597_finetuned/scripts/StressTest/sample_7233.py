distance_run_premise = 2
distance_run_hypothesis = 3

# the hypothesis refers to the distance the sisters ran, which is also mentioned in the premise
if distance_run_hypothesis <= distance_run_premise:
    # check if the hypothesis value contradicts the distance run in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
