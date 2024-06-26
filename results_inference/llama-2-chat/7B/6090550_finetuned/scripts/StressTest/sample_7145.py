 score_premise = 38
score_hypothesis = 38

# the hypothesis talks about the average golf score on Scott's first four rounds
if score_hypothesis >= score_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than or equal to the premise value, we can infer entailment
    label = "entailment"

print(label)
