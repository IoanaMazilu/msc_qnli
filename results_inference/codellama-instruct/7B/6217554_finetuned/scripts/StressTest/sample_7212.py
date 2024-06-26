# define variables for the scores Roslin got in the game
scores_premise = [1, 2, 3, 4, 5]
scores_hypothesis = [8, 2, 3, 4, 5]

# check if the hypothesis scores contradict the premise ones
if any(score_hypothesis in scores_premise for score_hypothesis in scores_hypothesis):
    # if any of the hypothesis scores is also in the premise ones, we have a contradiction
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
