scott_avg_score_premise = 38
scott_avg_score_hypothesis = 38

# the hypothesis refers to the same average golf score of Scott as in the premise
if scott_avg_score_hypothesis >= scott_avg_score_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than or equal to the premise value, we can infer entailment
    label = "entailment"

print(label)
