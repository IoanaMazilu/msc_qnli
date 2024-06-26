distance_run_premise = 2
distance_run_hypothesis = 3

# the hypothesis refers to the distance run by the sisters, mentioned in the premise
if distance_run_premise >= distance_run_hypothesis:
    # check if the distance run in the premise contradicts the estimate of less than 'distance_run_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
