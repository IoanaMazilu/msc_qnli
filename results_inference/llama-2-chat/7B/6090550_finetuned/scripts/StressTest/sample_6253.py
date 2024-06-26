scores_premise = [7, 2, 3, 4]
scores_hypothesis = [1, 2, 3, 4]

# the hypothesis refers to the scores Angel got, which are also mentioned in the premise

if scores_hypothesis >= scores_premise:
    # check if the hypothesis scores contradict the premise scores
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)
