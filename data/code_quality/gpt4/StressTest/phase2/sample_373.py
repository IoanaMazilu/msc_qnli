distance_run_premise = 20
distance_run_hypothesis = 10

# the hypothesis speaks about the distance run by the sisters in the premise
if distance_run_hypothesis > distance_run_premise:
    # check if the distance run in the hypothesis contradicts the premise
    label = "contradiction"
elif distance_run_hypothesis < distance_run_premise:
    # the premise gives only an estimate for the distance run
    # any distance less than 'distance_run_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis distance matches exactly the premise distance, we can infer entailment
    label = "entailment"

print(label)
