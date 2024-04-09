exam_scores_premise = [25, 38, 23]
exam_scores_hypothesis = [35, 38, 23]

# the hypothesis refers to the scores of three students in an exam, mentioned in the premise
if exam_scores_premise[0] <= exam_scores_hypothesis[0]:
    # check if the estimate of 'exam_scores_hypothesis[0]' contradicts the score of 'Dibi' in the premise
    label = "contradiction"
elif exam_scores_hypothesis[1]!= exam_scores_premise[1]:
    # check if the score of 'Balan' in the hypothesis contradicts the score of 'Balan' in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
