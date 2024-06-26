lowest_score_premise = 6
lowest_score_hypothesis = 1

# the hypothesis refers to the scores obtained by Andrea in a game, which are also mentioned in the premise
if lowest_score_hypothesis >= lowest_score_premise:
    # check whether the lowest score in the hypothesis contradicts the value mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
