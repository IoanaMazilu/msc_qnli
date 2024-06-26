average_score_premise = 48
average_score_hypothesis = 38

# the hypothesis refers to the average score of Scott's first four rounds mentioned in the premise
if average_score_premise >= average_score_hypothesis:
    # check if the estimate of 'average_score_hypothesis' contradicts the average score in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
