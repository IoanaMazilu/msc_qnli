# Premise: Mary played the game, getting at least one score of each of 1, 2, 3 and 4 and never getting the same score in consecutive steps.
# Hypothesis: Mary played the game, getting at least one score of each of more than 1, 2, 3 and 4 and never getting the same score in consecutive steps.
# Golden Label: contradiction

# Scores in premise
score_1_premise = 1
score_2_premise = 2
score_3_premise = 3
score_4_premise = 4

# Scores in hypothesis
score_1_hypothesis = 1
score_2_hypothesis = 2
score_3_hypothesis = 3
score_4_hypothesis = 4

# The hypothesis refers to the scores Mary got in the game, which is also mentioned in the premise
if score_1_hypothesis <= score_1_premise or score_2_hypothesis <= score_2_premise or score_3_hypothesis <= score_3_premise or score_4_hypothesis <= score_4_premise:
    # Check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # Since the hypothesis scores are greater than the premise ones, it cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)

