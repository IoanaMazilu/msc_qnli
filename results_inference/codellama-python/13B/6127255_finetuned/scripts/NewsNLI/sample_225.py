scores_premise = [5, 0]
scores_hypothesis = [5, 0]

# the hypothesis mentions the scores of the game, which are also mentioned in the premise
if scores_hypothesis!= scores_premise:
    # check if the scores in the hypothesis contradicts the scores reported in the premise
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)
