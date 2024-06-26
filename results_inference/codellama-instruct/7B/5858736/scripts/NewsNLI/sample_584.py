premise_wins = 7
premise_losses = 6
premise_sets = 5
premise_games = 6
premise_break_points = 4
premise_break_points_won = 3
premise_games_won = 6
premise_games_lost = 0

hypothesis_wins = 7
hypothesis_losses = 6
hypothesis_sets = 5
hypothesis_games = 6
hypothesis_break_points = 4
hypothesis_break_points_won = 3
hypothesis_games_won = 6
hypothesis_games_lost = 0

# check if the hypothesis values and estimates do not contradict the premise values
if hypothesis_wins!= premise_wins:
    label = "contradiction"
elif hypothesis_losses!= premise_losses:
    label = "contradiction"
elif hypothesis_sets!= premise_sets:
    label = "contradiction"
elif hypothesis_games!= premise_games:
    label = "contradiction"
elif hypothesis_break_points!= premise_break_points:
    label = "contradiction"
elif hypothesis_break_points_won!= premise_break_points_won:
    label = "contradiction"
elif hypothesis_games_won!= premise_games_won:
    label = "contradiction"
elif hypothesis_games_lost!= premise_games_lost:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
