# Premise: Angel played the game, getting at least one score of each of less than 7, 2, 3, and 4, and never getting the same score in consecutive steps.
# Hypothesis: Angel played the game, getting at least one score of each of 1, 2, 3, and 4, and never getting the same score in consecutive steps.
# Golden Label: neutral

lowest_score_premise = 7
lowest_score_hypothesis = 1

# the hypothesis refers to the minimum score Angel got in the game, mentioned also in the premise
if lowest_score_hypothesis >= lowest_score_premise:
    # check if the 'lowest_score_hypothesis' contradicts the premise's estimate of less than 'lowest_score_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the lowest score
    # any number less than 'lowest_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

