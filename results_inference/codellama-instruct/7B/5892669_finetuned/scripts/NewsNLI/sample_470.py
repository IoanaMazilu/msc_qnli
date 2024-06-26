score_premise = 2
score_hypothesis = 2

# the hypothesis mentions the score of the game and the fact that Manchester City faced a replay, which are also mentioned in the premise
if score_hypothesis!= score_premise:
    # check if the score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
