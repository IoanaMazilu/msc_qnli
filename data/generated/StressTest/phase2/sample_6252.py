# Premise: Angel played the game, getting at least one score of each of 1, 2, 3, and 4, and never getting the same score in consecutive steps.
# Hypothesis: Angel played the game, getting at least one score of each of less than 7, 2, 3, and 4, and never getting the same score in consecutive steps.
# Golden Label: entailment

lowest_score_premise = 1
lowest_score_hypothesis = 7

# the hypothesis refers to the range of scores Angel got in the game mentioned in the premise
if lowest_score_hypothesis < lowest_score_premise:
    # check if the lowest score in the hypothesis contradicts the lowest score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

