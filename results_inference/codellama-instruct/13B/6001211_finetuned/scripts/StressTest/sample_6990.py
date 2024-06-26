distance_run_premise = 12
distance_run_hypothesis = 52

# the hypothesis refers to the distance run by the sisters mentioned in the premise
if distance_run_premise >= distance_run_hypothesis:
    # check if the estimate of 'distance_run_hypothesis' contradicts the distance run in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
