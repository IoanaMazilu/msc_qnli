goals_premise = 10
games_premise = 2
score_premise = 4 - 1

goals_hypothesis = 10
games_hypothesis = 2
score_hypothesis = 4 - 1

# the hypothesis mentions the number of goals Arsenal made in two games and the score of the match against Portsmouth, which are also mentioned in the premise
if goals_hypothesis != goals_premise:
    # check if the number of goals in the hypothesis contradicts the number of goals reported in the premise
    label = "contradiction"
elif games_hypothesis != games_premise:
    # check if the number of games from the hypothesis contradicts the number of games in the premise
    label = "contradiction"
elif score_hypothesis != score_premise:
    # check if the match score from the hypothesis contradicts the match score in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
