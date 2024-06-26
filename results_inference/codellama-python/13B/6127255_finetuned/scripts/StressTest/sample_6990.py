distance_run_premise = 12
distance_run_hypothesis = 52

# the hypothesis refers to the distance run by the sisters mentioned in the premise
if distance_run_hypothesis < distance_run_premise:
    # check if the estimate of 'distance_run_hypothesis' contradicts the distance run in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
