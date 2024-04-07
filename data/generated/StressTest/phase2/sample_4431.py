# Premise: Jon had an average score of 85 on his first five quizzes.
# Hypothesis: Jon had an average score of more than 75 on his first five quizzes.
# Golden Label: entailment

average_score_premise = 85
average_score_hypothesis = 75

# the hypothesis refers to the average score of Jon's first five quizzes mentioned in the premise
if average_score_premise <= average_score_hypothesis:
    # check if the estimate of 'average_score_hypothesis' contradicts the average score in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

