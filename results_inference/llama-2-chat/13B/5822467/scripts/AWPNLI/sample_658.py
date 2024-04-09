points_premise = 21
games_premise = 3
points_hypothesis = 7.0

# the hypothesis refers to the average points earned per round, which is also mentioned in the premise
# compute the total points earned in the premise
total_points_premise = points_premise * games_premise

if points_hypothesis >= total_points_premise:
    # check if the average points earned in the hypothesis contradicts the total points earned in the premise
    label = "contradiction"
elif points_hypothesis < total_points_premise:
    # check if the average points earned in the hypothesis is less than the total points earned in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
