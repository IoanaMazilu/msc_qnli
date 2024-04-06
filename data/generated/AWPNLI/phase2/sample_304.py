# Premise: Paige's team won their dodgeball game and scored 41.0 points total, and Paige scored 11.0 of the points and everyone else scored 6.0 points each.
# Hypothesis: 5.0 players were on her team.
# Golden Label: entailment

total_points_premise = 41.0
paige_points_premise = 11.0
each_other_player_points_premise = 6.0
team_size_hypothesis = 5.0

# the hypothesis talks about the size of the team, which can be inferred from the premise
# compute the total points scored by the other players in the premise
other_players_points_premise = total_points_premise - paige_points_premise
# compute the size of the team in the premise
team_size_premise = 1 + other_players_points_premise / each_other_player_points_premise

if team_size_hypothesis != team_size_premise:
    # check if the size of the team in the hypothesis contradicts the size of the team from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

