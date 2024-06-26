distance_run_premise = 12
distance_run_hypothesis = 52

# The hypothesis refers to the distance run by Sita and Geeta mentioned in the premise
if distance_run_premise > distance_run_hypothesis:
    # Check if the distance run in the premise contradicts the estimate of 'less than distance_run_hypothesis'
    label = "contradiction"
elif distance_run_premise != distance_run_hypothesis:
    # Check if the distance run in the hypothesis contradicts the distance run reported in the premise
    label = "neutral"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
