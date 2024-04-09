score_premise = [1, 2, 3, 4, 5]
score_hypothesis = [1, 2, 3, 4, 5]

# the hypothesis talks about the scores obtained by Roslin in the game, which is also referred to in the premise
if any(score_hypothesis[i] <= score_premise[i] for i in range(len(score_hypothesis))):
    # check if the hypothesis value contradicts the estimate of scores in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the scores, any sequence of scores that is consistent with the premise is consistent with the hypothesis
    label = "neutral"

print(label)
