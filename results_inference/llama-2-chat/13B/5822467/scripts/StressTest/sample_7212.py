roslin_scores_premise = [1, 2, 3, 4, 5]
roslin_scores_hypothesis = [less than 8, 2, 3, 4, 5]

# the hypothesis refers to the number of scores obtained by Roslin in the game
if all(score in roslin_scores_hypothesis for score in roslin_scores_premise):
    # check if the hypothesis values are consistent with the premise values
    label = "neutral"
elif any(score not in roslin_scores_hypothesis for score in roslin_scores_premise):
    # check if the premise values contradict the hypothesis values
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
