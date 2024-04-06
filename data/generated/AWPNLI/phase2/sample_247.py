# Premise: A perfect score is 21.0 points.
# Hypothesis: You would have 62.0 points after 3.0 perfect games in a row.
# Golden Label: contradiction

perfect_score_premise = 21.0
points_hypothesis = 62.0
games_hypothesis = 3.0

# the hypothesis refers to the total points which are calculated from the perfect score from the premise
# compute the total points in the premise
total_points_premise = perfect_score_premise * games_hypothesis
if points_hypothesis != total_points_premise:
    # check if the total points in the hypothesis contradicts the total points from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

