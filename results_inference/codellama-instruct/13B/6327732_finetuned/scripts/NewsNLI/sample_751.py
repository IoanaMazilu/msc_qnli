# define variables for the numerical entities in the premise and hypothesis
premise_sets_won = 2
hypothesis_sets_won = 2
premise_games_won = 6
hypothesis_games_won = 7

# check if the number of sets won in the hypothesis contradicts the number of sets won in the premise
if hypothesis_sets_won!= premise_sets_won:
    label = "contradiction"
# check if the number of games won in the hypothesis contradicts the number of games won in the premise
elif hypothesis_games_won!= premise_games_won:
    label = "contradiction"
# if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
else:
    label = "entailment"

print(label)
