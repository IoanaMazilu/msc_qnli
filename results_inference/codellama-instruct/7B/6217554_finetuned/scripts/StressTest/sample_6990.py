distance_run_premise = 12
distance_run_hypothesis = 52

# the hypothesis talks about the distance run by the twins sisters, referenced also in the premise
if distance_run_hypothesis >= distance_run_premise:
    # check if the hypothesis value contradicts the distance run in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
