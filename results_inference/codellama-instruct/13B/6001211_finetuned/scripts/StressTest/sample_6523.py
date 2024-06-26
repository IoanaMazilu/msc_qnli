subject_scores_premise = [45, 67, 76, 82, 85]
subject_scores_hypothesis = [55, 67, 76, 82, 85]

# the hypothesis talks about the scores Reeya obtained in different subjects, referenced also in the premise
if min(subject_scores_hypothesis) <= min(subject_scores_premise):
    # check if the lowest score in the hypothesis contradicts the estimate of more than'subject_scores_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the lowest score
    # any score greater than'subject_scores_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
