subject_scores_premise = [45, 67, 76, 82, 85]
subject_scores_hypothesis = [55, 67, 76, 82, 85]

# the hypothesis talks about the scores of Reeya in different subjects, referenced also in the premise
if subject_scores_hypothesis[0] <= subject_scores_premise[0]:
    # check if the first score in the hypothesis contradicts the estimate of more than'subject_scores_premise[0]'
    label = "contradiction"
elif subject_scores_hypothesis[1:]!= subject_scores_premise[1:]:
    # check if the remaining scores in the hypothesis contradict the remaining scores in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the scores
    # any scores greater than'subject_scores_premise[0]' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
