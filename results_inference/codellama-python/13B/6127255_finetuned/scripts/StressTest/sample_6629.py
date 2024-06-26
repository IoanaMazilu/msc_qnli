#scores_premise = [1, 2, 3]
#scores_hypothesis = [0, 2, 3]

# the hypothesis refers to the scores Mary got in a game, which is also mentioned in the premise
# we check if the scores in the hypothesis are less than the scores in the premise
if any(score_hypothesis >= score_premise for score_hypothesis, score_premise in zip(scores_hypothesis, scores_premise)):
    # if the hypothesis score is not less than the premise score, we have a contradiction
    label = "contradiction"
else:
    # the premise gives only an estimate for the minimum score
    # any score less than the minimum score is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
