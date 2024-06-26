average_score_premise = 85
average_score_hypothesis = 15
quiz_count = 8

# the hypothesis refers to Jerry's average score over the first eight quizzes
if average_score_premise <= average_score_hypothesis:
    # check if the hypothesis estimate contradicts Jerry's average score in the premise
    label = "contradiction"
else:
    # if the hypothesis estimate is less than the average score in the premise, we can infer entailment
    label = "entailment"

print(label)
