lowest_score_premise = 1
lowest_score_hypothesis = 8

# the hypothesis talks about the lowest score Roslin got in the game, referenced also in the premise
if lowest_score_hypothesis < lowest_score_premise:
    # check if the hypothesis value contradicts the premise stating that the lowest score was 'lowest_score_premise'
    label = "contradiction"
elif lowest_score_hypothesis == lowest_score_premise:
    # if 'lowest_score_hypothesis' equals 'lowest_score_premise', the hypothesis can be fully and explicitly entailed from the premise
    label = "entailment"
else:
    # the premise gives only a lower limit for the lowest score
    # any score greater than 'lowest_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
