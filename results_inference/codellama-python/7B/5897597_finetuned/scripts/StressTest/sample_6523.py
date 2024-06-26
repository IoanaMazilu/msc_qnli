subject_scores_premise = [45, 67, 76, 82, 85]
subject_scores_hypothesis = [55, 67, 76, 82, 85]

# the hypothesis talks about the scores Reeya obtained in different subjects, referenced also in the premise
if any(score_hypothesis <= score_premise for score_hypothesis, score_premise in zip(subject_scores_hypothesis, subject_scores_premise)):
    # check if the hypothesis value contradicts the estimate of more than'score_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the scores
    # any score greater than'score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
