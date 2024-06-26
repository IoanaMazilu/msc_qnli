distance_run_premise = 12
distance_run_hypothesis = 52

# the hypothesis talks about the distance run by the twins sisters, which is also mentioned in the premise
if distance_run_hypothesis <= distance_run_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
