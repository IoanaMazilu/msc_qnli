borussia_dortmund_score_premise = 5
moenchengladbach_score_premise = 0
borussia_dortmund_rank_premise = 3
borussia_dortmund_score_hypothesis = 5
moenchengladbach_score_hypothesis = 0
borussia_dortmund_rank_hypothesis = 3

# the hypothesis mentions the score of the game, the rank of Borussia Dortmund and the score of Moenchengladbach, which are also mentioned in the premise
if borussia_dortmund_score_hypothesis!= borussia_dortmund_score_premise:
    # check if the score of Borussia Dortmund in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif moenchengladbach_score_hypothesis!= moenchengladbach_score_premise:
    # check if the score of Moenchengladbach from the hypothesis contradicts the score in the premise
    label = "contradiction"
elif borussia_dortmund_rank_hypothesis!= borussia_dortmund_rank_premise:
    # check if the rank of Borussia Dortmund from the hypothesis contradicts the rank in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
