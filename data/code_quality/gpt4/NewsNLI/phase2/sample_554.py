scores_premise = [6, 1, 6, 1]
scores_hypothesis = [6, 1, 6, 1]

# the hypothesis mentions the match scores, which are also mentioned in the premise
if scores_hypothesis != scores_premise:
    # check if the match scores in the hypothesis contradict the match scores reported in the premise
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)
