subject_scores_premise = [45, 67, 76, 82, 85]
subject_scores_hypothesis = [55, 67, 76, 82, 85]

# the hypothesis refers to the scores obtained by Reeya in different subjects, as mentioned in the premise
if set(subject_scores_hypothesis)!= set(subject_scores_premise):
    # check if the scores in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the scores
    # any score greater than'subject_scores_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
