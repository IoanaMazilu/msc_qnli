# Premise: Andrea played the game, getting at least one score of each of less than 6, 2, 3, 4, and 5, and never getting the same score in consecutive steps.
# Hypothesis: Andrea played the game, getting at least one score of each of 1, 2, 3, 4, and 5, and never getting the same score in consecutive steps.
# Golden Label: neutral

lowest_score_premise = 6
lowest_score_hypothesis = 1

# the hypothesis refers to the scores obtained by Andrea in a game, which are also mentioned in the premise
if lowest_score_hypothesis >= lowest_score_premise:
    # check whether the lowest score in the hypothesis contradicts the value mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

