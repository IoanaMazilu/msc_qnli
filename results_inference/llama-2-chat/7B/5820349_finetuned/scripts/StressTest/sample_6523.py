subject_scores_premise = [45, 67, 76, 82, 85]
subject_scores_hypothesis = [55, 67, 76, 82, 85]

# the hypothesis refers to the scores obtained by Reeya in different subjects, mentioned also in the premise
if subject_scores_hypothesis[0] <= subject_scores_premise[0]:
    # check if the first score in the hypothesis contradicts the estimate of more than'subject_scores_premise[0]'
    label = "contradiction"
elif any(score > score_premise for score, score_premise in subject_scores_premise):
    # check if any of the scores in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the first score
    # any score greater than'subject_scores_premise[0]' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
