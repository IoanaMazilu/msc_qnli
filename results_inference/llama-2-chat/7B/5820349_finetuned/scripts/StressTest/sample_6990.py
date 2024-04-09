distance_run_premise = 12
distance_run_hypothesis = 52

# the hypothesis refers to the distance the sisters ran, which is also mentioned in the premise
if distance_run_premise >= distance_run_hypothesis:
    # check if the premise value contradicts the hypothesis estimate of less than 'distance_run_hypothesis'
    label = "contradiction"
elif distance_run_premise < distance_run_hypothesis:
    # if the premise value is less than the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
