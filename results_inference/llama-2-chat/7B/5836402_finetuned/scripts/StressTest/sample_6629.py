scores_premise = [1, 2, 3]
scores_hypothesis = [1, 2, 3]

# the hypothesis refers to the scores mentioned in the premise
if scores_hypothesis >= scores_premise:
    # check if the estimate of'scores_hypothesis' contradicts the scores in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
