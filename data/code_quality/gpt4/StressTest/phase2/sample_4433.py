average_score_premise = 85
average_score_hypothesis = 45

# the hypothesis talks about Jon's average score on his first five quizzes, referenced also in the premise
if average_score_hypothesis == average_score_premise:
    # check if the average score in the hypothesis matches the average score reported in the premise
    label = "entailment"
else:
    # the reported average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"

print(label)
