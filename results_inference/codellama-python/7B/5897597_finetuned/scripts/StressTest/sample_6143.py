average_score_premise = 18
average_score_hypothesis = 38

# the hypothesis refers to Scott's average golf score on his first four rounds, mentioned in the premise
if average_score_hypothesis!= average_score_premise:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
