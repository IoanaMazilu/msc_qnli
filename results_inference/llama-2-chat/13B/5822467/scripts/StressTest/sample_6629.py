mary_scores_premise = [1, 2, 3]
mary_scores_hypothesis = [less than 1, 2, 3]

# the hypothesis refers to the scores Mary got in the game, as reported in the premise
if all(score in mary_scores_hypothesis for score in mary_scores_premise):
    # the hypothesis values are consistent with the premise values, so we can infer entailment
    label = "entailment"
elif any(score not in mary_scores_hypothesis for score in mary_scores_premise):
    # the hypothesis values contradict at least one premise value
    label = "contradiction"
else:
    # the premise only gives an estimate of the scores, so we cannot infer entailment or contradiction
    label = "neutral"

print(label)
