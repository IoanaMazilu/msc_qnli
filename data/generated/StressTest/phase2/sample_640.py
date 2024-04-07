# Premise: Jerry had an average score of more than 15 on his first eight quizzes.
# Hypothesis: Jerry had an average score of 85 on his first eight quizzes.
# Golden Label: neutral

average_score_premise = 15
average_score_hypothesis = 85

# the hypothesis states a specific average score for the same number of quizzes in the premise
if average_score_hypothesis <= average_score_premise:
    # check if the hypothesis value contradicts the premise estimate of more than 'average_score_premise'
    label = "contradiction"
else:
    # the premise only gives an estimate for the average score
    # any average score greater than 'average_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

