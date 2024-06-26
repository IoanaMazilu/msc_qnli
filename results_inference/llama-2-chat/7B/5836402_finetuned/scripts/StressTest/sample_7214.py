min_scores_premise = [1, 2, 3, 4, 5]
min_scores_hypothesis = [1, 2, 3, 4, 5]

# the hypothesis talks about the minimum scores Roslin could get in the game, which is also referenced in the premise
for i in range(min_scores_premise[0], min_scores_premise[-1] + 1):
    if min_scores_hypothesis[0] <= i:
        # check if the hypothesis value contradicts the estimate of at least 'i' in the premise
        label = "contradiction"
    else:
        # the premise gives only an estimate for the minimum score
        # any number of scores less than'min_scores_premise[0]' is consistent with the premise, but cannot be explicitly entailed from the premise
        label = "neutral"

print(label)
