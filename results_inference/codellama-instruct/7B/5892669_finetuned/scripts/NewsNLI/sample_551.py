us_goals_premise = 2
slovenia_goals_premise = 2
us_goals_hypothesis = 2
slovenia_goals_hypothesis = 2

# the hypothesis mentions the score of the game and the group ranking, which are also mentioned in the premise
if us_goals_hypothesis!= us_goals_premise:
    # check if the number of US goals in the hypothesis contradicts the number of US goals reported in the premise
    label = "contradiction"
elif slovenia_goals_hypothesis!= slovenia_goals_premise:
    # check if the number of Slovenia goals from the hypothesis contradicts the number of Slovenia goals in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
