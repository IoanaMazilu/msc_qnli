subject_scores_premise = [50, 60, 70, 80, 80]
subject_scores_hypothesis = [40, 60, 70, 80, 80]

# the hypothesis talks about the scores Reeya obtained in different subjects, referenced also in the premise
for score_p, score_h in zip(subject_scores_premise, subject_scores_hypothesis):
    if score_h >= score_p:
        # check if the hypothesis value contradicts the estimate of less than'score_p'
        label = "contradiction"
        break
else:
    # the premise gives only an estimate for the scores
    # any score less than'score_p' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
