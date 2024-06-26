scott_avg_score_premise = 18
scott_avg_score_hypothesis = 38

# the hypothesis talks about the average golf score of Scott on his first four rounds, which is also mentioned in the premise
if scott_avg_score_hypothesis!= scott_avg_score_premise:
    # check if the average score in the hypothesis contradicts the average score in the premise
    label = "contradiction"
else:
    # if the average score in the hypothesis matches the average score in the premise, we can infer entailment
    label = "entailment"

print(label)
