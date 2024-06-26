average_score_premise = 38
average_score_hypothesis = 38

# the hypothesis refers to the average score of Scott's first four rounds mentioned in the premise
if average_score_hypothesis >= average_score_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_score_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
