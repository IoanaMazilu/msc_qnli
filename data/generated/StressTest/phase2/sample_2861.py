# Premise: Andrea played the game, getting at least one score of each of 1, 2, 3, 4, and 5, and never getting the same score in consecutive steps.
# Hypothesis: Andrea played the game, getting at least one score of each of more than 1, 2, 3, 4, and 5, and never getting the same score in consecutive steps.
# Golden Label: contradiction

# defining the minimum scores Andrea got in the game according to the premise and the hypothesis
min_scores_premise = [1, 2, 3, 4, 5]
min_scores_hypothesis = [2, 2, 3, 4, 5]

# the hypothesis refers to the scores Andrea got in the game, which are also mentioned in the premise
for score_p, score_h in zip(min_scores_premise, min_scores_hypothesis):
    if score_h <= score_p:
        # check if the hypothesis value contradicts the estimate of 'score_p'
        label = "contradiction"
        break
else:
    # the premise gives only an estimate for the minimum scores
    # any estimate of minimum score greater than 'min_scores_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

