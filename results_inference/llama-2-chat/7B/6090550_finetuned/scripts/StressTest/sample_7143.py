 score_premise = 38
score_hypothesis = 48

# the hypothesis refers to Scott's average golf score on his first four rounds, also mentioned in the premise
if score_hypothesis <= score_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
