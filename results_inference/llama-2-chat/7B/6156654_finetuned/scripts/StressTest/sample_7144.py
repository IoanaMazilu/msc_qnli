scott_avg_score_premise = 48
scott_avg_score_hypothesis = 38

# the hypothesis talks about the average golf score of Scott on his first four rounds, which is also mentioned in the premise
if scott_avg_score_hypothesis > scott_avg_score_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
