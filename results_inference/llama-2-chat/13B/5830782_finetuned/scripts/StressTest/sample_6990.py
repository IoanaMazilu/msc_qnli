distance_run_premise = 12
distance_run_hypothesis = 52

# the hypothesis refers to the distance run by the sisters mentioned in the premise
if distance_run_premise > distance_run_hypothesis:
    # check if the distance run in the premise contradicts the estimate of less than 'distance_run_hypothesis'
    label = "contradiction"
elif distance_run_premise < distance_run_hypothesis:
    # check if the distance run in the premise is less than the distance run in the hypothesis
    label = "entailment"
else:
    # if the distance run in the premise equals the distance run in the hypothesis, we can infer neutrality
    label = "neutral"

print(label)
