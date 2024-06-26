exam_score_premise = [60, 65, 45]
exam_score_hypothesis = [60, 65, 60]

# the hypothesis talks about the scores of three students in an exam, referenced also in the premise
if exam_score_hypothesis[0] <= exam_score_premise[0]:
    # check if the hypothesis value contradicts the estimate of Bright's score in the premise
    label = "contradiction"
elif exam_score_hypothesis[1]!= exam_score_premise[1]:
    # check if the number of scored percentages in the hypothesis contradicts the number of scored percentages reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
