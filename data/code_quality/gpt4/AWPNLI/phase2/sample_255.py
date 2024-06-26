goals_last_season_premise = 156.0
goals_this_season_premise = 187.0
total_goals_hypothesis = 341.0

# the hypothesis refers to the total number of goals, which are also mentioned in the premise
# compute the total number of goals in the premise
total_goals_premise = goals_last_season_premise + goals_this_season_premise
if total_goals_hypothesis != total_goals_premise:
    # check if the total number of goals in the hypothesis contradicts the total number of goals from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
