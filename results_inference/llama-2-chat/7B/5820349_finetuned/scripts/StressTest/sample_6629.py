lowest_score_premise = 1
lowest_score_hypothesis = 1

# the hypothesis refers to the lowest score Mary got in the game, mentioned also in the premise
if lowest_score_hypothesis >= lowest_score_premise:
    # check if the estimate of 'lowest_score_hypothesis' contradicts the lowest score in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
