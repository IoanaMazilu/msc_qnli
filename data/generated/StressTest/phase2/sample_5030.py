# Premise: Gary had an average score of 70 on his first four quizzes.
# Hypothesis: Gary had an average score of less than 70 on his first four quizzes.
# Golden Label: contradiction

average_score_premise = 70
average_score_hypothesis_less = 70

# the hypothesis refers to the average score of Gary's first four quizzes mentioned in the premise
if average_score_premise < average_score_hypothesis_less:
    # check if the premise value contradicts the estimate of less than 'average_score_hypothesis_less'
    label = "contradiction"
elif average_score_premise == average_score_hypothesis_less:
    # check if the premise value contradicts the estimate of less than 'average_score_hypothesis_less'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)

