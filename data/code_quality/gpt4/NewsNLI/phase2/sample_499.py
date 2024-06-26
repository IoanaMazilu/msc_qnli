round_score_premise = -10
leaderboard_score_premise = -13
round_score_hypothesis = -10
leaderboard_score_hypothesis = -13

# the hypothesis mentions the round score and the leaderboard score of the Englishman, which are also mentioned in the premise
if round_score_hypothesis != round_score_premise:
    # check if the round score in the hypothesis contradicts the round score reported in the premise
    label = "contradiction"
elif leaderboard_score_hypothesis != leaderboard_score_premise:
    # check if the leaderboard score from the hypothesis contradicts the leaderboard score in the premise
    label = "contradiction"
else:
    # if the hypothesis values and scores do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
