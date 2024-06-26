average_score_premise = 38
average_score_hypothesis = 38

# the hypothesis refers to Scott's average golf score on his first four rounds mentioned in the premise
if average_score_hypothesis >= average_score_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
