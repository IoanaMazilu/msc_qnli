# Premise: A perfect score is 21.0 points.
# Hypothesis: You would have 63.0 points after 3.0 perfect games in a row.
# Golden Label: entailment

perfect_score_premise = 21.0
perfect_games_hypothesis = 3.0
total_points_hypothesis = 63.0

# the hypothesis refers to the total points after a number of perfect games, which can be computed from the premise
# compute the total points from the premise
total_points_premise = perfect_score_premise * perfect_games_hypothesis
if total_points_hypothesis != total_points_premise:
    # check if the total points in the hypothesis contradicts the total points from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

