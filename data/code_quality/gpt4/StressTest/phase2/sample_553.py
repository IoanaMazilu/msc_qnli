subjects_scores_premise = [45, 67, 76, 82, 85]
subjects_scores_hypothesis = [65, 67, 76, 82, 85]

# the hypothesis talks about the scores Reeya obtained in different subjects, also referenced in the premise
if subjects_scores_hypothesis[0] <= subjects_scores_premise[0]:
    # check if the first subject score in the hypothesis contradicts the estimate of more than 45 in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the first subject score
    # any first subject score greater than 45 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
