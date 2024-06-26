distance_run_premise = 12
distance_run_hypothesis = 52

# the hypothesis refers to the distance run by the sisters, which is also mentioned in the premise
if distance_run_hypothesis < distance_run_premise:
    # check if the hypothesis value contradicts the distance run in the premise
    label = "contradiction"
elif distance_run_hypothesis > distance_run_premise:
    # check if the hypothesis value is greater than the distance run in the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the distance run in the premise, we can infer entailment
    label = "entailment"

print(label)
