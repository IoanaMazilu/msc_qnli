distance_run_premise = 2
distance_run_hypothesis = 3

# the hypothesis talks about the distance the twins ran, which is also mentioned in the premise
if distance_run_hypothesis <= distance_run_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
