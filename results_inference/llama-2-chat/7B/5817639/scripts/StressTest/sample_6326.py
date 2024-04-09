exam_scores_premise = [38, 56, 66, 75]
exam_scores_hypothesis = [88, 56, 66, 75]

# the hypothesis refers to the scores of the students in the premise
if any(score1 > score2 for score1, score2 in exam_scores_premise):
    # check if any of the scores in the hypothesis contradict the scores in the premise
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)
