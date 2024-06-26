perfect_score_premise = 21
games_premise = 3
points_per_round_hypothesis = 7.0

# the hypothesis refers to the points earned per round, which can be computed from the premise
# compute the points earned per round in the premise
points_per_round_premise = perfect_score_premise / games_premise
if points_per_round_hypothesis!= points_per_round_premise:
    # check if the points earned per round in the hypothesis contradicts the points earned per round from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
