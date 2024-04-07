# Premise: Gary had an average score of more than 60 on his first four quizzes.
# Hypothesis: Gary had an average score of 70 on his first four quizzes.
# Golden Label: neutral

average_score_premise = 60
average_score_hypothesis = 70

# the hypothesis refers to Gary's average score on the first four quizzes, which is also mentioned in the premise
if average_score_hypothesis <= average_score_premise:
    # check if the hypothesis value contradicts the premise's estimate of more than 'average_score_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average score
    # any average score greater than 'average_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

