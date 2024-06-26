subject_scores_premise = [50, 60, 70, 80, 80]
subject_scores_hypothesis = [40, 60, 70, 80, 80]

# the hypothesis talks about the scores Reeya obtained in different subjects, referenced also in the premise
if subject_scores_hypothesis[0] >= subject_scores_premise[0]:
    # check if the first subject score in the hypothesis contradicts the estimate of less than'subject_scores_premise[0]'
    label = "contradiction"
elif subject_scores_hypothesis[1:]!= subject_scores_premise[1:]:
    # check if the remaining subject scores in the hypothesis contradicts the remaining subject scores reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the first subject score
    # any first subject score less than'subject_scores_premise[0]' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
