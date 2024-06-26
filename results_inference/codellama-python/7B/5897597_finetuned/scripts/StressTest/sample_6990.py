distance_run_premise = 12
distance_run_hypothesis = 52

# the hypothesis refers to the distance the sisters ran, which is also mentioned in the premise
if distance_run_premise >= distance_run_hypothesis:
    # check if the distance run in the premise contradicts the estimate of less than 'distance_run_hypothesis'
    label = "contradiction"
else:
    # if the premise distance does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
