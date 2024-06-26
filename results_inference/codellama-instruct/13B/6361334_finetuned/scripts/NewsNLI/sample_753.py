# define variables for the numerical entities in the premise and hypothesis
games_lost_premise = 2
games_drawn_premise = 1
games_won_premise = 1
games_lost_hypothesis = 1
games_drawn_hypothesis = 0
games_won_hypothesis = 1

# check if the number of games won in the hypothesis contradicts the number of games won in the premise
if games_won_hypothesis!= games_won_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
