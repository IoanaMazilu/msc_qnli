exam_score_premise = [40, 65, 45]
exam_score_hypothesis = [60, 65, 45]

# the hypothesis talks about the exam scores of Bright, Bivi, and Lisa
if exam_score_premise <= exam_score_hypothesis:
    # check if the estimate of 'exam_score_hypothesis' contradicts the scores reported in the premise
    label = "contradiction"
elif exam_score_hypothesis[0]!= exam_score_premise[0] or exam_score_hypothesis[1]!= exam_score_premise[1] or exam_score_hypothesis[2]!= exam_score_premise[2]:
    # check if any of the scores in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
