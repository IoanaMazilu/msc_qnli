arsenal_score_premise = 4
galatasaray_score_premise = 1
hat_trick_premise = 1

arsenal_score_hypothesis = 4
galatasaray_score_hypothesis = 1

# the hypothesis mentions the score of the game and the fact that Danny Welbeck scored a hat-trick, which are also mentioned in the premise
if arsenal_score_hypothesis!= arsenal_score_premise or galatasaray_score_hypothesis!= galatasaray_score_premise:
    # check if the score of the game in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
