napoli_ranking_premise = 7
napoli_ranking_hypothesis = 7
score_premise = 1
score_hypothesis = 1

# the hypothesis mentions Napoli's ranking, the score of the game and the fact that the goal was scored late, which are also mentioned in the premise
if napoli_ranking_hypothesis != napoli_ranking_premise:
    # check if Napoli's ranking in the hypothesis contradicts the ranking reported in the premise
    label = "contradiction"
elif score_hypothesis != score_premise:
    # check if the game score from the hypothesis contradicts the game score in the premise
    label = "contradiction"
else:
    # if the hypothesis values and facts do not contradict the premise values and facts, we can infer entailment
    label = "entailment"

print(label)
