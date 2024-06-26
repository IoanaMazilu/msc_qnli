lowest_score_premise = 7
lowest_score_hypothesis = 1

# the hypothesis talks about the lowest score Mary got in the game, referenced also in the premise
if lowest_score_hypothesis >= lowest_score_premise:
    # check if the value of the lowest score in the hypothesis contradicts the premise value of less than 'lowest_score_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the lowest score
    # any score less than 'lowest_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
