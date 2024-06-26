games_per_month_premise = 13.0
months_per_season_premise = 14.0
total_games_hypothesis = 177.0

# the hypothesis refers to the total number of games in a season, which can be computed from the premise
# compute the total number of games in the premise
total_games_premise = games_per_month_premise * months_per_season_premise
if total_games_hypothesis != total_games_premise:
    # check if the total number of games in the hypothesis contradicts the total number of games from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
