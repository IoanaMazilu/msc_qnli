subject_scores_premise = [50, 60, 70, 80, 80]
subject_scores_hypothesis = [40, 60, 70, 80, 80]

# the hypothesis refers to the scores obtained by Reeya in different subjects, which is also mentioned in the premise
if any(subject_scores_hypothesis >= score for score in subject_scores_premise):
    # check if any of the scores in the hypothesis contradicts the estimate of less than'score' in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the scores
    # any score less than'subject_scores_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
