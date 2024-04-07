# Premise: Roslin played the game, getting at least one score of each of less than 8, 2, 3, 4, and 5, and never getting the same score in consecutive steps.
# Hypothesis: Roslin played the game, getting at least one score of each of 1, 2, 3, 4, and 5, and never getting the same score in consecutive steps.
# Golden Label: neutral

low_score_premise = 8
low_score_hypothesis = 1

# the hypothesis talks about the lowest score that Roslin got in the game, referenced also in the premise
if low_score_hypothesis >= low_score_premise:
    # check if the hypothesis value contradicts the premise which states that the lowest score was less than 'low_score_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the lowest score
    # any lowest score less than 'low_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

