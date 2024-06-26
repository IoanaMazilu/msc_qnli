average_score_premise = 70
average_score_hypothesis = 60

# the hypothesis refers to Gary's average score for the first four quizzes mentioned in the premise
if average_score_premise <= average_score_hypothesis:
    # check if the 'average_score_hypothesis' contradicts the average score in the premise
    label = "contradiction"
else:
    # if the average score in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
