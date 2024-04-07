# Premise: Jon had an average score of more than 75 on his first five quizzes.
# Hypothesis: Jon had an average score of 85 on his first five quizzes.
# Golden Label: neutral

average_score_premise = 75
average_score_hypothesis = 85

# the hypothesis talks about the average score for Jon's first five quizzes, also mentioned in the premise
if average_score_hypothesis <= average_score_premise:
    # check if the hypothesis value contradicts the premise estimate of more than 'average_score_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average score
    # any average score greater than 'average_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

