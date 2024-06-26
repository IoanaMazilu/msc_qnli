 score_premise = 88
score_hypothesis = 58

# the hypothesis talks about the average score of Scott's first four rounds, which is also mentioned in the premise
if score_hypothesis >= score_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
