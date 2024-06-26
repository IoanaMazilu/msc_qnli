score_premise = {1: 1, 2: 1, 3: 1, 4: 1}
score_hypothesis = {1: 2, 2: 1, 3: 1, 4: 1}

# the hypothesis talks about the scores obtained by Angel in the game, referenced also in the premise
if score_hypothesis <= score_premise:
    # check if the hypothesis value contradicts the estimate of the scores in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the scores
    # any combination of scores less than'score_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
