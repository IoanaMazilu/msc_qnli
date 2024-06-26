average_score_premise = 85
average_score_hypothesis = 85

# the hypothesis refers to the average score of the first eight quizzes mentioned in the premise
if average_score_premise > average_score_hypothesis:
    # check if the 'average_score_premise' contradicts the hypothesis stating that the average score is more than 'average_score_hypothesis'
    label = "contradiction"
elif average_score_premise < average_score_hypothesis:
    # check if the 'average_score_premise' contradicts the hypothesis stating that the average score is more than 'average_score_hypothesis'
    label = "contradiction"
else:
    # if the average score in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
