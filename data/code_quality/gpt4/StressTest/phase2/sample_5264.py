average_score_premise = 68
average_score_hypothesis = 68

# the hypothesis refers to Scott's average golf score on his first four rounds, mentioned in the premise
if average_score_hypothesis >= average_score_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
