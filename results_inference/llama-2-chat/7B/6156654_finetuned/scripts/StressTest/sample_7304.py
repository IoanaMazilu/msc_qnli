scott_avg_score_premise = 58
scott_avg_score_hypothesis = 78

# the hypothesis refers to the average golf score of Scott on his first four rounds, which is also mentioned in the premise
if scott_avg_score_premise!= scott_avg_score_hypothesis:
    # check if the average score in the hypothesis contradicts the average score in the premise
    label = "contradiction"
else:
    # if the average score in the hypothesis is equal to the average score in the premise, we can infer entailment
    label = "entailment"

print(label)
