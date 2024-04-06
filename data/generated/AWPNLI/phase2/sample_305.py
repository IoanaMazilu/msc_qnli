# Premise: Paige's team won their dodgeball game and scored 41.0 points total, and Paige scored 11.0 of the points and everyone else scored 6.0 points each.
# Hypothesis: 6.0 players were on her team.
# Golden Label: contradiction

total_points_premise = 41.0
paige_points_premise = 11.0
each_other_points_premise = 6.0
players_hypothesis = 6.0

# the hypothesis talks about the number of players in Paige's team, which can be inferred from the premise
# compute the total points scored by the others in the premise
other_points_premise = total_points_premise - paige_points_premise

# compute the number of other players in the premise
other_players_premise = other_points_premise / each_other_points_premise

# add Paige to get the total number of players in the premise
total_players_premise = other_players_premise + 1

if players_hypothesis != total_players_premise:
    # check if the number of players in the hypothesis contradicts the number of players from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

