distance_run_premise = 8
distance_run_hypothesis = 8

# the hypothesis is a statement about the distance the sisters ran, which is also in the premise
if distance_run_hypothesis >= distance_run_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
