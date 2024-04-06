# Premise: Defeat for Cologne leaves them rock bottom with just one point from their opening five games.
# Hypothesis: The defeat leaves Cologne on bottom of the Bundesliga table after five games.
# Golden Label: entailment

points_premise = 1
games_premise = 5
points_hypothesis = 1
games_hypothesis = 5

# the hypothesis mentions the number of points and games for Cologne, which are also mentioned in the premise
if points_hypothesis != points_premise:
    # check if the number of points in the hypothesis contradicts the number of points reported in the premise
    label = "contradiction"
elif games_hypothesis != games_premise:
    # check if the number of games from the hypothesis contradicts the number of games in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

